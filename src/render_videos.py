"""Render the /learn/ micro-course videos: AI narration + burned-in captions, 720x1280 MP4.

Pipeline per lesson (p_learn.LESSONS):
  1. Narration: Kokoro TTS (kokoro-onnx, voice af_heart), one clip per beat, joined with short pauses.
  2. Timeline: each beat lasts as long as its narration; captions are split into short chunks and
     timed in proportion to their length inside the beat.
  3. Frames: one self-contained HTML page per lesson draws every frame from a time `t`
     (window.frame(t)), so rendering is deterministic. Playwright screenshots each frame and
     pipes it into ffmpeg, which muxes the narration.
Outputs into dist/learn/media/: lesson-<n>.mp4, lesson-<n>.jpg (poster), lesson-<n>.vtt (captions)
and lessons.json (durations), consumed by the /learn/ pages.

Needs: kokoro-onnx + soundfile + numpy, the model files in TTS_DIR (kokoro-v1.0.onnx, voices-v1.0.bin),
Playwright Chromium, ffmpeg, and the Fontsource packages (same as render_images.py).
Run:  python render_videos.py [lesson numbers...]
"""
import asyncio, json, os, pathlib, re, shutil, subprocess, sys, tempfile, time, wave
try:
    import numpy as np
except ImportError:  # CI runner: install on first use
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "numpy"])
    import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
DIST = HERE / "dist"
OUT = (HERE / os.environ["MEDIA_DIR"]) if os.environ.get("MEDIA_DIR") else DIST / "learn" / "media"
TTS_DIR = pathlib.Path(os.environ.get("TTS_DIR", HERE.parent / "tts")).resolve()
VOICE = os.environ.get("TTS_VOICE", "af_heart")
SPEED = float(os.environ.get("TTS_SPEED", "0.96"))
FPS = int(os.environ.get("VIDEO_FPS", "24"))
W, H, DPR = 540, 960, 4 / 3      # CSS px; output is 720x1280
LEAD, GAP, TAIL = 0.7, 0.45, 1.6  # seconds of silence: before first beat, between beats, after last
SR = 24000

import p_learn
from p_css import CSS
from p_art import DEFS, HILLS, LOGO
from render_images import FACES

# ------------------------------------------------------------------ narration
def tts_beats(lesson):
    from kokoro_onnx import Kokoro
    k = Kokoro(str(TTS_DIR / "kokoro-v1.0.onnx"), str(TTS_DIR / "voices-v1.0.bin"))
    clips = []
    for b in lesson["beats"]:
        s, sr = k.create(b["say"], voice=VOICE, speed=SPEED, lang="en-us")
        assert sr == SR, sr
        s = np.asarray(s, dtype=np.float32)
        # trim leading/trailing near-silence so beat timing is tight
        idx = np.where(np.abs(s) > 0.01)[0]
        if len(idx): s = s[max(0, idx[0] - 600): idx[-1] + 1200]
        clips.append(s)
    return clips

def build_audio(clips, path):
    parts, beats, t = [np.zeros(int(LEAD * SR), np.float32)], [], LEAD
    for i, c in enumerate(clips):
        d = len(c) / SR
        beats.append((t, t + d))
        parts.append(c); t += d
        gap = GAP if i < len(clips) - 1 else TAIL
        parts.append(np.zeros(int(gap * SR), np.float32)); t += gap
    audio = np.concatenate(parts)
    peak = float(np.max(np.abs(audio))) or 1.0
    audio = np.clip(audio / peak * 0.89, -1, 1)
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((audio * 32767).astype("<i2").tobytes())
    return beats, len(audio) / SR

# ------------------------------------------------------------------ captions
def chunks(text, limit=31):
    words, out, cur = text.split(), [], ""
    for w in words:
        if cur and (len(cur) + 1 + len(w) > limit):
            out.append(cur); cur = w
        else:
            cur = (cur + " " + w).strip()
        if re.search(r"[.!?:]$", w) and len(cur) > 18:
            out.append(cur); cur = ""
    if cur: out.append(cur)
    # pair into two-line captions
    caps, i = [], 0
    while i < len(out):
        if i + 1 < len(out) and len(out[i + 1]) <= 31 and not re.search(r"[.!?]$", out[i]):
            caps.append(out[i] + "\n" + out[i + 1]); i += 2
        else:
            caps.append(out[i]); i += 1
    return caps

def caption_track(lesson, beats):
    track = []
    for b, (s, e) in zip(lesson["beats"], beats):
        cs = chunks(b.get("cap", b["say"]))
        total = sum(len(c) for c in cs)
        t = s
        for c in cs:
            d = (e - s) * len(c) / total
            track.append({"s": round(t, 3), "e": round(t + d, 3), "text": c})
            t += d
    return track

def vtt(track):
    f = lambda x: f"{int(x // 3600):02d}:{int(x % 3600 // 60):02d}:{x % 60:06.3f}"
    return "WEBVTT\n\n" + "\n\n".join(f"{i}\n{f(c['s'])} --> {f(c['e'])}\n{c['text']}" for i, c in enumerate(track, 1)) + "\n"

# ------------------------------------------------------------------ frame page
PAGE_CSS = """
*{animation:none !important;transition:none !important}
html,body{margin:0;width:540px;height:960px;overflow:hidden;background:#DDF0FA}
.stage{position:relative;width:540px;height:960px;overflow:hidden;background:linear-gradient(180deg,#CFEAF8 0%,#EAF6FC 52%,#FFF9EF 100%);font-family:var(--f-body);color:var(--ink)}
.stage .sun{position:absolute;right:-34px;top:70px;width:150px}
.stage .cloud{position:absolute;width:150px;opacity:.95}
.stage .hills{position:absolute;left:0;right:0;bottom:0;height:190px;width:540px;margin:0}
.top{position:absolute;left:28px;right:28px;top:26px;display:flex;align-items:center;gap:10px;z-index:3}
.top svg{width:38px;height:38px}
.top .bn{display:flex;flex-direction:column;line-height:1.05}
.top .b1{font-family:var(--f-display);font-weight:800;font-size:17px}
.top .b2{font-family:var(--f-hand);font-size:15px;color:var(--coral-ink)}
.prog{position:absolute;left:28px;right:28px;top:78px;display:flex;gap:6px;z-index:3}
.prog i{flex:1;height:6px;border-radius:6px;background:rgba(42,43,74,.14);overflow:hidden;position:relative}
.prog i b{position:absolute;inset:0;width:0;background:var(--sun-deep);border-radius:6px}
.beat{position:absolute;left:28px;right:28px;top:118px;height:470px;opacity:0;z-index:2}
.card{background:#fff;border-radius:30px;padding:26px 26px 24px;box-shadow:0 8px 0 rgba(42,43,74,.08),0 18px 40px rgba(29,106,150,.10);border:2px solid #F1EBDD}
.kick{font-family:var(--f-hand);font-size:22px;color:var(--coral-ink);line-height:1.1}
.ttl{font-family:var(--f-display);font-weight:800;font-size:38px;line-height:1.02;margin-top:6px;letter-spacing:-.01em;text-wrap:balance}
.items{display:flex;flex-direction:column;gap:12px;margin-top:20px}
.chip{display:flex;align-items:center;gap:12px;background:var(--band-sun);border-radius:18px;padding:13px 16px;font-size:19px;font-weight:500;line-height:1.25;opacity:0}
.chip:nth-child(3n+2){background:var(--band-sky)} .chip:nth-child(3n+3){background:var(--band-meadow)}
.dot{flex:none;width:26px;height:26px;border-radius:50%;background:var(--meadow);display:grid;place-items:center}
.dot svg{width:16px;height:16px}
.step{display:flex;align-items:center;gap:12px;padding:9px 12px;border-radius:16px;font-size:18px;font-weight:500;opacity:0;line-height:1.2}
.step .n{flex:none;width:32px;height:32px;border-radius:50%;background:#EFEAE0;color:var(--ink);font-family:var(--f-display);font-weight:800;font-size:17px;display:grid;place-items:center}
.step.done .n{background:var(--meadow);color:#fff}
.step.focus{background:var(--band-sun);box-shadow:inset 0 0 0 2px var(--sun-deep)}
.step.focus .n{background:var(--sun);color:var(--on-sun)}
.flow{display:flex;flex-direction:column;align-items:stretch;gap:0;margin-top:22px}
.fbox{border-radius:20px;padding:16px 18px;font-family:var(--f-display);font-weight:800;font-size:26px;text-align:center;opacity:0}
.fbox.f1{background:var(--band-sky)} .fbox.f2{background:var(--band-sun)} .fbox.f3{background:var(--band-meadow)}
.farrow{height:30px;display:grid;place-items:center;opacity:0;color:var(--ink-3);font-size:24px;line-height:1}
.swap{margin-top:22px;display:flex;flex-direction:column;gap:16px}
.old,.new{border-radius:20px;padding:18px;font-size:22px;font-weight:600;line-height:1.25;position:relative}
.old{background:var(--coral-soft);opacity:0}
.old s{position:absolute;left:14px;right:14px;top:50%;height:4px;border-radius:4px;background:var(--coral-ink);transform-origin:left;transform:scaleX(0)}
.new{background:var(--band-meadow);opacity:0}
.chart{margin-top:16px}
.chart svg{width:100%;height:auto;display:block}
.team{display:grid;grid-template-columns:1fr;gap:12px;margin-top:20px}
.person{display:flex;gap:14px;align-items:center;border-radius:20px;padding:14px 16px;background:var(--band-sky);opacity:0}
.person:nth-child(2){background:var(--band-sun)} .person:nth-child(3){background:var(--band-meadow)}
.person .av{flex:none;width:50px;height:50px;border-radius:50%;background:#fff;display:grid;place-items:center;font-family:var(--f-display);font-weight:800;font-size:15px;color:var(--ink)}
.person b{display:block;font-family:var(--f-display);font-weight:800;font-size:22px;line-height:1.1}
.person span{font-size:16px;color:var(--ink-2)}
.big-ico{width:120px;height:120px;margin:4px auto 6px;display:block}
.title-card{text-align:center;padding-top:34px;padding-bottom:34px}
.title-card .ttl{font-size:52px}
.url{display:inline-block;margin-top:18px;font-family:var(--f-display);font-weight:800;font-size:22px;color:var(--meadow-ink);background:var(--band-meadow);border-radius:999px;padding:8px 18px}
.phonebtn{display:block;margin-top:22px;background:var(--sun);color:var(--on-sun);border-radius:999px;padding:16px 20px;text-align:center;font-family:var(--f-display);font-weight:800;font-size:30px;box-shadow:0 5px 0 var(--sun-deep)}
.cap{position:absolute;left:24px;right:24px;top:612px;min-height:96px;display:flex;align-items:center;justify-content:center;z-index:4}
.cap div{background:rgba(42,43,74,.90);color:#fff;border-radius:22px;padding:14px 20px;font-size:25px;line-height:1.3;font-weight:500;text-align:center;white-space:pre;box-shadow:0 6px 18px rgba(42,43,74,.25)}
"""

CHECK = '<svg viewBox="0 0 16 16"><path d="M4 8.4l2.6 2.6L12.4 5" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def chart_svg():
    pts = [176, 168, 172, 150, 140, 144, 122, 110, 114, 92, 80, 70, 56, 46]
    xs = [20 + i * 33 for i in range(len(pts))]
    d = "M " + " L ".join(f"{x} {y}" for x, y in zip(xs, pts))
    grid = "".join(f'<line x1="20" x2="449" y1="{y}" y2="{y}" stroke="#E8E2D6" stroke-width="2" stroke-dasharray="2 8" stroke-linecap="round"/>' for y in (46, 100, 154, 200))
    dots = "".join(f'<circle class="cd" data-i="{i}" cx="{x}" cy="{y}" r="6" fill="#fff" stroke="var(--meadow-ink)" stroke-width="3" opacity="0"/>' for i, (x, y) in enumerate(zip(xs, pts)))
    return f'''<svg viewBox="0 0 470 230">{grid}<path class="cl" d="{d}" fill="none" stroke="var(--meadow-ink)" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>{dots}
<text x="20" y="226" font-family="Lexend" font-size="15" fill="var(--ink-3)">Session 1</text><text x="449" y="226" text-anchor="end" font-family="Lexend" font-size="15" fill="var(--ink-3)">Session 14</text></svg>'''

def beat_html(v, n_lessons=5):
    k = v["kind"]
    head = f'<div class="kick">{esc(v["kicker"])}</div><div class="ttl">{esc(v["title"])}</div>'
    if k == "title":
        return f'<div class="card title-card"><svg class="big-ico anim-i" viewBox="0 0 48 48"><use href="#{v["icon"]}"/></svg>{head}<div class="url">actaba.com/learn</div></div>'
    if k == "chips":
        items = "".join(f'<div class="chip anim-i"><span class="dot">{CHECK}</span><span>{esc(t)}</span></div>' for t in v["items"])
        return f'<div class="card">{head}<div class="items">{items}</div></div>'
    if k == "steps":
        done, focus = v.get("done", 0), v.get("focus", 0)
        items = "".join(f'<div class="step anim-i{" done" if i <= done else ""}{" focus" if i == focus else ""}"><span class="n">{CHECK if i <= done else i}</span><span>{esc(t)}</span></div>' for i, t in enumerate(v["items"], 1))
        return f'<div class="card">{head}<div class="items" style="gap:6px">{items}</div></div>'
    if k == "flow":
        a, b, c = v["items"]
        return f'<div class="card">{head}<div class="flow"><div class="fbox f1 anim-i">{a}</div><div class="farrow anim-i">&#8595;</div><div class="fbox f2 anim-i">{b}</div><div class="farrow anim-i">&#8595;</div><div class="fbox f3 anim-i">{c}</div></div></div>'
    if k == "swap":
        return f'<div class="card">{head}<div class="swap"><div class="old">{esc(v["old"])}<s></s></div><div class="new">{esc(v["new"])}</div></div></div>'
    if k == "chart":
        return f'<div class="card">{head}<div class="chart">{chart_svg()}</div></div>'
    if k == "team":
        items = "".join(f'<div class="person anim-i"><span class="av">{esc(a[:4])}</span><div><b>{esc(a)}</b><span>{esc(b)}</span></div></div>' for a, b in v["items"])
        return f'<div class="card">{head}<div class="team">{items}</div></div>'
    if k == "next":
        return f'<div class="card title-card">{head}<div class="url">actaba.com/learn</div></div>'
    if k == "phone":
        return f'<div class="card title-card"><svg class="big-ico anim-i" viewBox="0 0 48 48"><use href="#i-talk"/></svg>{head}<div class="phonebtn anim-i">{p_learn.PHONE_CO}</div><div class="url">actaba.com/learn</div></div>'
    raise ValueError(k)

FRAME_JS = r"""
const D = __DATA__;
const beats = [...document.querySelectorAll('.beat')];
const bars = [...document.querySelectorAll('.prog i b')];
const capEl = document.querySelector('.cap div'), capBox = document.querySelector('.cap');
const clouds = [...document.querySelectorAll('.stage .cloud')];
const ease = x => 1 - Math.pow(1 - Math.min(Math.max(x, 0), 1), 3);
const back = x => { x = Math.min(Math.max(x, 0), 1); const c = 1.6; return 1 + (c + 1) * Math.pow(x - 1, 3) + c * Math.pow(x - 1, 2); };
window.frame = function(t){
  clouds.forEach((c, i) => c.style.transform = `translateX(${Math.sin(t / (9 + i * 4)) * 26}px)`);
  D.beats.forEach((b, i) => {
    const el = beats[i], s = b.s, e = (i < D.beats.length - 1) ? D.beats[i + 1].s : D.total;
    const fin = ease((t - s + 0.25) / 0.45), fout = (i < D.beats.length - 1) ? 1 - ease((t - e + 0.3) / 0.3) : 1;
    const o = Math.min(fin, fout);
    el.style.opacity = o;
    el.style.transform = `translateY(${(1 - fin) * 40}px) scale(${0.97 + 0.03 * fin})`;
    if (o <= 0) return;
    const dur = Math.max(b.e - s, 1);
    const items = [...el.querySelectorAll('.anim-i')];
    const span = Math.min(dur * 0.62, Math.max(items.length * 0.9, 1.2));
    items.forEach((it, j) => {
      const at = s + 0.35 + (items.length > 1 ? span * j / (items.length - 1) : 0);
      const p = back((t - at) / 0.45);
      it.style.opacity = Math.min(1, Math.max(0, (t - at) / 0.25));
      it.style.transform = `translateY(${(1 - p) * 18}px) scale(${0.9 + 0.1 * p})`;
    });
    const old = el.querySelector('.old'), nw = el.querySelector('.new');
    if (old) {
      old.style.opacity = Math.min(1, Math.max(0, (t - s - 0.3) / 0.3));
      const k = ease((t - s - dur * 0.42) / 0.5);
      old.querySelector('s').style.transform = `scaleX(${k})`;
      old.style.filter = `saturate(${1 - 0.6 * k})`; old.style.opacity *= (1 - 0.45 * k);
      const p = back((t - s - dur * 0.5) / 0.5);
      nw.style.opacity = Math.min(1, Math.max(0, (t - s - dur * 0.5) / 0.3));
      nw.style.transform = `scale(${0.85 + 0.15 * p})`;
    }
    const cl = el.querySelector('.cl');
    if (cl) {
      const k = ease((t - s - 0.4) / Math.min(dur * 0.7, 4));
      cl.style.strokeDashoffset = 1 - k;
      el.querySelectorAll('.cd').forEach(d => d.setAttribute('opacity', (+d.dataset.i / 13) <= k ? 1 : 0));
    }
  });
  D.beats.forEach((b, i) => {
    const e = (i < D.beats.length - 1) ? D.beats[i + 1].s : D.total;
    bars[i].style.width = (Math.min(1, Math.max(0, (t - b.s) / (e - b.s))) * 100) + '%';
  });
  let c = null;
  for (const x of D.caps) if (t >= x.s - 0.05 && t < x.e + 0.12) { c = x; }
  if (c) {
    if (capEl.textContent !== c.text) capEl.textContent = c.text;
    const a = Math.min(1, (t - c.s + 0.05) / 0.12);
    capBox.style.opacity = a; capEl.style.display = '';
  } else { capBox.style.opacity = 0; }
};
"""

def page(lesson, timeline):
    beats = "".join(f'<div class="beat">{beat_html(b["v"])}</div>' for b in lesson["beats"])
    bars = "".join("<i><b></b></i>" for _ in lesson["beats"])
    js = FRAME_JS.replace("__DATA__", json.dumps(timeline))
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{FACES}{CSS}{PAGE_CSS}</style></head>
<body>{DEFS}<div class="stage">
<svg class="sun" viewBox="0 0 200 200"><use href="#sunsym"/></svg>
<svg class="cloud" style="left:-30px;top:120px" viewBox="0 0 200 90"><use href="#cloudsym"/></svg>
<svg class="cloud" style="left:290px;top:560px;width:110px;opacity:.7" viewBox="0 0 200 90"><use href="#cloudsym"/></svg>
<div class="top">{LOGO.replace('width="42" height="42"', '')}<span class="bn"><span class="b1">Adventure Child Therapy</span><span class="b2">Family micro-course · {lesson["n"]} of 5</span></span></div>
<div class="prog">{bars}</div>
{beats}
<div class="cap"><div></div></div>
{HILLS}
</div><script>{js}</script></body></html>"""

# ------------------------------------------------------------------ render
def ffmpeg_bin():
    """System ffmpeg if present, otherwise a static build from the imageio-ffmpeg wheel (no sudo needed)."""
    if shutil.which("ffmpeg"):
        return "ffmpeg"
    try:
        import imageio_ffmpeg
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "imageio-ffmpeg"])
        import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()

async def render_frames(html_path, total, mp4, wav, poster_t, poster):
    from playwright.async_api import async_playwright
    n = int(total * FPS) + 1
    ff = subprocess.Popen([ffmpeg_bin(), "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS), "-c:v", "mjpeg", "-i", "-",
                           "-i", str(wav), "-c:v", "libx264", "-preset", "medium", "-crf", "24", "-pix_fmt", "yuv420p",
                           "-profile:v", "high", "-c:a", "aac", "-b:a", "96k", "-movflags", "+faststart", "-shortest", str(mp4)],
                          stdin=subprocess.PIPE)
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": W, "height": H}, device_scale_factor=DPR, color_scheme="light")
        await pg.goto(html_path.as_uri())
        await pg.evaluate("document.fonts.ready")
        if not await pg.evaluate("document.fonts.check('800 40px \"Baloo 2\"')"):
            raise SystemExit("Baloo 2 did not load for the videos")
        await pg.evaluate(f"frame({poster_t})")
        await pg.screenshot(path=str(poster), type="jpeg", quality=88)
        for i in range(n):
            await pg.evaluate(f"frame({i / FPS})")
            ff.stdin.write(await pg.screenshot(type="jpeg", quality=90))
        await b.close()
    ff.stdin.close()
    if ff.wait() != 0:
        raise SystemExit(f"ffmpeg failed for {mp4}")

async def render_lesson(lesson, meta):
    n = lesson["n"]
    t0 = time.time()
    with tempfile.TemporaryDirectory() as tmp:
        tmp = pathlib.Path(tmp)
        clips = tts_beats(lesson)
        wav = tmp / "narration.wav"
        beats, total = build_audio(clips, wav)
        track = caption_track(lesson, beats)
        timeline = {"beats": [{"s": round(s, 3), "e": round(e, 3)} for s, e in beats], "total": round(total, 3), "caps": track}
        html = tmp / "frame.html"; html.write_text(page(lesson, timeline))
        mp4, poster = OUT / f"lesson-{n}.mp4", OUT / f"lesson-{n}.jpg"
        await render_frames(html, total, mp4, wav, poster_t=beats[0][0] + 1.6, poster=poster)
        (OUT / f"lesson-{n}.vtt").write_text(vtt(track))
    meta[str(n)] = {"duration": round(total, 1), "bytes": mp4.stat().st_size}
    print(f"lesson {n}: {total:.1f}s, {mp4.stat().st_size / 1e6:.1f} MB, rendered in {time.time() - t0:.0f}s")

SITE = "https://actaba.com"
MODEL_URL = "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/"
INPUTS = ["p_learn.py", "render_videos.py", "p_art.py", "p_css.py"]

def inputs_hash():
    import hashlib
    h = hashlib.sha256(f"{VOICE}|{SPEED}|{FPS}|{W}x{H}@{DPR}".encode())
    for f in INPUTS: h.update((HERE / f).read_bytes())
    return h.hexdigest()[:16]

def reuse_live(want):
    """If the live site already serves videos built from these exact inputs, download them instead of re-rendering."""
    import urllib.request
    try:
        live = json.loads(urllib.request.urlopen(f"{SITE}/learn/media/lessons.json", timeout=20).read())
    except Exception as e:
        print("no live media manifest:", e); return False
    if live.get("hash") != want:
        print("live media built from different inputs; re-rendering"); return False
    OUT.mkdir(parents=True, exist_ok=True)
    for l in p_learn.LESSONS:
        for ext in ("mp4", "jpg", "vtt"):
            name = f"lesson-{l['n']}.{ext}"
            (OUT / name).write_bytes(urllib.request.urlopen(f"{SITE}/learn/media/{name}", timeout=60).read())
    (OUT / "lessons.json").write_text(json.dumps(live, indent=1))
    print("reused", len(p_learn.LESSONS), "videos from the live site (inputs unchanged)")
    return True

def ensure_tts():
    """Install the TTS runtime and fetch the model files when they are missing (CI)."""
    try:
        import kokoro_onnx, soundfile  # noqa: F401
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "kokoro-onnx==0.6.1", "soundfile", "numpy"])
    TTS_DIR.mkdir(parents=True, exist_ok=True)
    import urllib.request
    for f in ("kokoro-v1.0.onnx", "voices-v1.0.bin"):
        if not (TTS_DIR / f).exists() or (TTS_DIR / f).stat().st_size < 1_000_000:
            print("downloading", f)
            urllib.request.urlretrieve(MODEL_URL + f, TTS_DIR / f)

async def main(which, force=False):
    want = inputs_hash()
    if not which and not force and reuse_live(want):
        return
    ensure_tts()
    OUT.mkdir(parents=True, exist_ok=True)
    meta_path = OUT / "lessons.json"
    meta = json.loads(meta_path.read_text()) if meta_path.exists() else {}
    meta.setdefault("lessons", {})
    for l in p_learn.LESSONS:
        if not which or l["n"] in which:
            await render_lesson(l, meta["lessons"])
    meta["hash"] = want if not which else meta.get("hash", "partial")
    meta_path.write_text(json.dumps(meta, indent=1))

def build_media():
    """Entry point used by render_images.py during the site build."""
    asyncio.run(main([]))

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--force"]
    asyncio.run(main([int(a) for a in args], force="--force" in sys.argv))
