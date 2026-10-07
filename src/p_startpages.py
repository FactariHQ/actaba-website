"""/start/ — the new-hire "Before Day One" modules (hub + six module pages).

Unlisted: noindex, kept out of the sitemap and the site nav. Links arrive by text and email from the
ACT New Hire Drip engine with a per-hire token (?h=...). When a token is present, the page pings the
engine so the team can see who has opened and finished which module. Pages work fine without it.
"""
import json
from p_start import MODULES, module, ADMIN_ALL

# The drip engine's web app URL (Apps Script). Opens and quiz results are sent here when ?h= is present.
BEACON = "https://script.google.com/macros/s/AKfycbxVd8RE22HYoLXoHligkiznEt_7RE7qLJAZ_E_DXJI3KLfek6JC9pBHnR30Vp8XAVBr/exec"

START_CSS = """
/* ---- new-hire Before Day One modules ---- */
.mhead{padding:clamp(36px,6vw,72px) 0 clamp(20px,3vw,32px);background:var(--pro-band)}
.mhead .meta{display:flex;flex-wrap:wrap;gap:8px 16px;font-size:.9rem;color:var(--ink-3)}
.mprog{display:flex;gap:6px;margin-top:6px}
.mprog a{flex:1;height:6px;border-radius:3px;background:var(--line-2)}
.mprog a.on{background:var(--meadow-ink)}
.mprog a.done{background:var(--meadow)}
.mbody{display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:clamp(28px,5vw,64px);align-items:start}
.mbody article{display:flex;flex-direction:column;gap:34px;max-width:68ch}
.mbody article section{display:flex;flex-direction:column;gap:12px}
.mbody article p,.mbody article li{color:var(--ink-2)}
.mside{position:sticky;top:96px;display:flex;flex-direction:column;gap:16px}
.mlist{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:6px}
.mlist a{display:grid;grid-template-columns:28px minmax(0,1fr);gap:10px;align-items:center;text-decoration:none;color:inherit;padding:8px 10px;border-radius:10px;border:1px solid transparent}
.mlist a[aria-current]{background:var(--surface);border-color:var(--line-2)}
.mlist .num{width:26px;height:26px;border-radius:50%;display:grid;place-items:center;font-size:.8rem;font-weight:600;border:1px solid var(--line-2);background:var(--surface)}
.mlist a.done .num{background:var(--meadow-ink);border-color:var(--meadow-ink);color:var(--paper)}
.mlist b{font-weight:600;font-size:.95rem;line-height:1.25}
.vals,.steps{margin:0;padding-left:1.3em;display:flex;flex-direction:column;gap:10px}
.abc{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}
.abc>div{border:1px solid var(--line-2);border-radius:12px;padding:14px;background:var(--surface);display:flex;flex-direction:column;gap:2px}
.abc b{font-size:1.6rem;line-height:1;color:var(--meadow-ink)}
.abc span{font-weight:600}
.abc p{margin:0;font-size:.9rem;color:var(--ink-3)}
.ladder{display:flex;flex-wrap:wrap;gap:6px;align-items:center}
.ladder span{border:1px solid var(--line-2);border-radius:999px;padding:5px 12px;font-size:.88rem;background:var(--surface)}
.ladder span:not(:last-child)::after{content:"\\2192";margin-left:10px;color:var(--ink-3)}
.ladder span:last-child{background:var(--meadow-ink);color:var(--paper);border-color:var(--meadow-ink)}
.grid.c2{grid-template-columns:repeat(2,minmax(0,1fr))}
.doit{border-left:4px solid var(--sun-deep);background:var(--surface);border-radius:12px;padding:18px 20px;display:flex;flex-direction:column;gap:6px}
.quiz{display:flex;flex-direction:column;gap:22px}
.quiz fieldset{border:1px solid var(--line);border-radius:14px;padding:18px 20px;margin:0;display:flex;flex-direction:column;gap:8px;background:var(--surface)}
.quiz legend{font-weight:600;padding:0 6px;margin-left:-6px;color:var(--ink)}
.quiz label{display:grid;grid-template-columns:22px minmax(0,1fr);gap:10px;align-items:start;padding:8px 10px;border-radius:10px;border:1px solid transparent;cursor:pointer;color:var(--ink-2)}
.quiz label:hover{background:var(--pro-band)}
.quiz input{margin-top:4px;accent-color:var(--meadow-ink)}
.quiz label.right{border-color:var(--meadow-ink);background:color-mix(in srgb,var(--meadow) 18%,transparent)}
.quiz label.wrong{border-color:var(--coral);background:color-mix(in srgb,var(--coral) 12%,transparent)}
.quiz .why{display:none;font-size:.93rem;color:var(--ink-2);margin:4px 0 0}
.quiz.checked .why{display:block}
.qres{font-weight:600}
.mnext{text-decoration:none;color:inherit}
@media (max-width:900px){.mbody{grid-template-columns:minmax(0,1fr)}.mside{position:static}}
@media (max-width:560px){.abc,.grid.c2{grid-template-columns:minmax(0,1fr)}}
"""

START_JS = r"""
(function(){
  "use strict";
  var B = window.ACT_START || {}; if (!B.n && B.n !== 0) return;
  var store = { get:function(k){ try { return localStorage.getItem(k); } catch(e){ return null; } },
                set:function(k,v){ try { localStorage.setItem(k,v); } catch(e){} } };
  var qs = new URLSearchParams(location.search), h = qs.get('h');
  if (h) store.set('act_start_h', h); else h = store.get('act_start_h');
  function ping(a, extra){
    if (!h || !B.beacon || B.beacon.indexOf('PLACEHOLDER') > -1) return;
    var u = B.beacon + '?a=' + a + '&h=' + encodeURIComponent(h) + '&m=' + B.n + (extra || '');
    try { fetch(u, { mode:'no-cors', keepalive:true }); } catch(e) { (new Image()).src = u; }
  }
  function markDone(n){ var d = (store.get('act_start_done') || '').split(',').filter(Boolean); if (d.indexOf(String(n)) < 0) d.push(String(n)); store.set('act_start_done', d.join(',')); paint(); }
  function paint(){
    var d = (store.get('act_start_done') || '').split(',');
    document.querySelectorAll('[data-mod]').forEach(function(el){ if (d.indexOf(el.getAttribute('data-mod')) > -1) el.classList.add('done'); });
  }
  paint();
  if (B.n > 0) ping('open');
  // keep the token on every module link so moving around the site still counts
  if (h) document.querySelectorAll('a[href^="/start/"]').forEach(function(a){ if (a.href.indexOf('h=') < 0) a.href += (a.href.indexOf('?') > -1 ? '&' : '?') + 'h=' + encodeURIComponent(h); });
  var form = document.querySelector('form.quiz'); if (!form) return;
  form.addEventListener('submit', function(e){
    e.preventDefault();
    var sets = form.querySelectorAll('fieldset'), right = 0, answered = 0;
    sets.forEach(function(fs){
      var ok = fs.getAttribute('data-ok'), picked = fs.querySelector('input:checked');
      fs.querySelectorAll('label').forEach(function(l){ l.classList.remove('right','wrong'); });
      if (picked) { answered++; }
      fs.querySelectorAll('input').forEach(function(i){
        if (i.value === ok) i.closest('label').classList.add('right');
        else if (i.checked) i.closest('label').classList.add('wrong');
      });
      if (picked && picked.value === ok) right++;
    });
    var res = form.querySelector('.qres');
    if (answered < sets.length) { res.textContent = 'Pick an answer for each question, then check again.'; return; }
    form.classList.add('checked');
    res.textContent = right === sets.length ? 'All ' + right + ' right. Nice work! This module is done.' : right + ' of ' + sets.length + ' right. Read the notes under each question, then move on whenever you are ready. This module is done.';
    markDone(B.n);
    ping('quiz', '&s=' + right + '&t=' + sets.length);
  });
})();
"""

def _mlist(cur):
    CUR = ' aria-current="page"'
    return '<ol class="mlist">' + "".join(
        f'<li><a href="/start/{m["n"]}/" data-mod="{m["n"]}"{CUR if m["n"] == cur else ""}><span class="num">{m["n"]}</span><b>{m["title"]}</b></a></li>'
        for m in MODULES) + '</ol>'

def _boot(n):
    return f'<script>window.ACT_START={json.dumps({"n": n, "beacon": BEACON})};</script>'

def module_page(n):
    from p_shared import ARROW
    M = module(n)
    nxt = module(n + 1) if n < len(MODULES) else None
    prog = '<div class="mprog" aria-hidden="true">' + "".join(
        f'<a href="/start/{m["n"]}/" data-mod="{m["n"]}" class="{"on" if m["n"] == n else ""}" tabindex="-1"></a>' for m in MODULES) + '</div>'
    secs = "".join(f'<section><h2 style="font-size:1.35rem">{h}</h2>{body}</section>' for h, body in M["sections"])
    quiz = "".join(
        f'''<fieldset data-ok="{ok}"><legend>{i}. {q}</legend>''' +
        "".join(f'<label><input type="radio" name="q{i}" value="{j}"><span>{opt}</span></label>' for j, opt in enumerate(opts)) +
        f'<p class="why">{why}</p></fieldset>'
        for i, (q, opts, ok, why) in enumerate(M["quiz"], 1))
    nxt_html = (f'<a class="card mnext" href="/start/{nxt["n"]}/"><span class="k">Up next · Module {nxt["n"]} of 6</span><h3>{nxt["title"]}</h3><p class="small muted">{nxt["blurb"]}</p><span class="go">Start module {nxt["n"]} {ARROW}</span></a>'
                if nxt else f'<div class="card"><span class="k">That’s all six</span><h3>You’re ready for day one.</h3><p class="small muted">Your welcome email arrives by end of day the Friday before your start date. Questions before then? Text or call the admin line: {ADMIN_ALL}.</p></div>')
    return f'''<div class="pro">
<section class="mhead"><div class="wrap stack g14">
  <span class="hand">Before Day One · Module {n} of 6</span>
  <h1 style="max-width:26ch">{M["title"]}</h1>
  <p class="lede measure">{M["blurb"]}</p>
  <div class="meta"><span>About {M["minutes"]} minutes</span><span>3-question check at the end</span></div>
  {prog}
</div></section>
<section class="sec"><div class="wrap mbody">
  <article>
    {secs}
    <div class="doit"><span class="k">Do this before the next module</span><p style="margin:0">{M["action"]}</p></div>
    <section id="check"><h2 style="font-size:1.35rem">Quick check</h2>
      <p class="small muted">Three questions, not graded. It’s here to help the ideas stick.</p>
      <form class="quiz" novalidate>{quiz}
        <div class="stack g10"><div><button class="btn btn-primary" type="submit">Check my answers</button></div><p class="qres" role="status" aria-live="polite"></p></div>
      </form>
    </section>
    {nxt_html}
  </article>
  <aside class="mside">
    <div class="card stack g10"><span class="k">All six modules</span>{_mlist(n)}</div>
    <div class="card stack g10"><span class="k">Questions?</span><p class="small muted">Text or call the ACT admin line. {ADMIN_ALL}.</p></div>
  </aside>
</div></section>
</div>
{_boot(n)}'''

def start_hub():
    from p_shared import ARROW, btn
    cards = "".join(
        f'<a class="card mnext" href="/start/{m["n"]}/" data-mod="{m["n"]}"><span class="k">Module {m["n"]} · About {m["minutes"]} min</span><h3>{m["title"]}</h3><p class="small muted">{m["blurb"]}</p></a>'
        for m in MODULES)
    return f'''<div class="pro">
<section class="mhead"><div class="wrap stack g14">
  <span class="hand">Before Day One</span>
  <h1 style="max-width:24ch">Welcome to Adventure Child Therapy</h1>
  <p class="lede measure">Six short modules for new behavior technicians, to read on your phone before your first day. Each takes about five minutes and ends with a three-question check. We’ll send you each one by email and text as your start date gets closer, or you can go at your own pace.</p>
  <div class="cta-row">{btn("/start/1/", "Start with module 1")}</div>
</div></section>
<section class="sec"><div class="wrap stack g28">
  <div class="grid c3">{cards}</div>
  <p class="small muted measure">Questions before your first day? Text or call the ACT admin line. {ADMIN_ALL}.</p>
</div></section>
</div>
{_boot(0)}'''
