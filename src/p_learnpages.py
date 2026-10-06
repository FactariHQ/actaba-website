"""/learn/ watch pages for the family micro-courses (kept apart from p_learn.py so page edits don't force a video re-render)."""
from p_learn import LESSONS, lesson

# ------------------------------------------------------------------ /learn/ watch pages
def _pages():
    from p_art import ico, strip
    from p_shared import CO_TEL, ARROW, btn
    return ico, strip, CO_TEL, ARROW, btn

LEARN_CSS = """
/* ---- micro-course watch pages ---- */
.lwrap{display:grid;grid-template-columns:minmax(0,380px) minmax(0,1fr);gap:clamp(24px,5vw,64px);align-items:start}
.lvid{position:relative;border-radius:28px;overflow:hidden;background:#DDF0FA;box-shadow:0 10px 0 var(--line),0 24px 50px rgba(29,106,150,.14);aspect-ratio:9/16}
.lvid video{display:block;width:100%;height:100%;object-fit:cover;background:#DDF0FA}
.lnext{background:var(--band-sun);border-color:transparent}
.llist{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:10px}
.llist a{display:grid;grid-template-columns:64px minmax(0,1fr);gap:14px;align-items:center;text-decoration:none;color:inherit;background:var(--surface);border:2px solid var(--line);border-radius:18px;padding:8px 14px 8px 8px}
.llist a[aria-current]{border-color:var(--sun-deep);background:var(--band-sun)}
.llist img{width:64px;height:86px;object-fit:cover;border-radius:12px;background:#DDF0FA}
.llist b{display:block;font-family:var(--f-display);font-weight:800;font-size:1.08rem;line-height:1.15}
.llist span{font-size:.9rem;color:var(--ink-3)}
.lgrid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:22px;max-width:980px}
.lcard{text-decoration:none;color:inherit;display:flex;flex-direction:column;gap:10px}
.lcard img{width:100%;aspect-ratio:9/16;object-fit:cover;border-radius:20px;background:#DDF0FA;box-shadow:0 6px 0 var(--line)}
.lcard b{font-family:var(--f-display);font-weight:800;font-size:1.12rem;line-height:1.15}
@media (max-width:980px){.lgrid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:760px){.lwrap{grid-template-columns:minmax(0,1fr)}.lvid{max-width:420px;margin-inline:auto;width:100%}}
"""

def watch_page(n):
    ico, strip, CO_TEL, ARROW, btn = _pages()
    L = lesson(n)
    nxt = lesson(n + 1) if n < len(LESSONS) else None
    items = "".join(f'''<li><a href="/learn/{x["n"]}/"{' aria-current="page"' if x["n"] == n else ""}><img src="/learn/media/lesson-{x["n"]}.jpg" alt="" loading="lazy"><div><b>{x["n"]}. {x["title"]}</b><span>About a minute</span></div></a></li>''' for x in LESSONS)
    nxt_html = (f'<a class="card lnext" href="/learn/{nxt["n"]}/" style="text-decoration:none;color:inherit;gap:6px"><span class="k">Up next · Lesson {nxt["n"]} of {len(LESSONS)}</span><h3>{nxt["title"]}</h3><p class="small muted">{nxt["blurb"]}</p><span class="go">Watch lesson {nxt["n"]} {ARROW}</span></a>'
                if nxt else f'<div class="card lnext stack g10"><span class="k">You finished all {len(LESSONS)}!</span><h3>Questions? We’re one call away.</h3><p class="small muted">Colorado {CO_TEL} · <a href="mailto:info@actaba.com">info@actaba.com</a></p></div>')
    return f'''<section class="sec tight"><div class="wrap lwrap">
  <div class="lvid"><video controls playsinline preload="metadata" poster="/learn/media/lesson-{n}.jpg" src="/learn/media/lesson-{n}.mp4">
    <track kind="captions" srclang="en" label="English" src="/learn/media/lesson-{n}.vtt">
    Your browser can’t play this video. <a href="/learn/media/lesson-{n}.mp4">Download it here</a>.</video></div>
  <div class="stack g20">
    <div class="stack g10"><span class="hand">Family micro-course · Lesson {n} of {len(LESSONS)}</span><h1 style="font-size:clamp(2.1rem,4vw,3rem)">{L["title"]}</h1><p class="lede measure">{L["blurb"]}</p>
      <p class="small muted">About a minute, with captions. Prefer to read? <a href="{L["guide"]}">Read the full guide</a>.</p></div>
    {nxt_html}
    <div class="stack g10"><span class="k">All {len(LESSONS)} lessons</span><ol class="llist">{items}</ol></div>
  </div>
</div></section>'''

def learn_hub():
    ico, strip, CO_TEL, ARROW, btn = _pages()
    cards = "".join(f'<a class="lcard" href="/learn/{L["n"]}/"><img src="/learn/media/lesson-{L["n"]}.jpg" alt="" loading="lazy"><span class="k">Lesson {L["n"]}</span><b>{L["title"]}</b><span class="small muted">{L["blurb"]}</span></a>' for L in LESSONS)
    return f'''<section class="phead">
  <div class="hero-sky" aria-hidden="true"><svg class="sun" viewBox="0 0 200 200" focusable="false"><use href="#sunsym"/></svg></div>
  <div class="wrap stack g14"><span class="hand">Family micro-course</span><h1>Getting ready for ABA, one minute at a time</h1>
  <p class="lede measure">Six short videos for families starting with Adventure Child Therapy. Each one takes about a minute and has captions, so you can watch with the sound off.</p>
  <div class="cta-row">{btn("/learn/1/", "Start with lesson 1")}<a class="go" href="/guide/">Prefer to read? The family guide {ARROW}</a></div></div>
  {strip()}
</section>
<section class="sec"><div class="wrap"><div class="lgrid">{cards}</div></div></section>'''