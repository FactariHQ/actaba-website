import re, os, json, shutil, datetime
import p_shared, p_pages, p_pro
from p_css import CSS
from p_art import DEFS, LOGO
from p_shared import CO_TEL, OK_TEL, ARROW

SITE = "https://actaba.com"
OUT = "dist"
TODAY = datetime.date(2026, 9, 10).isoformat()
FONTS = "https://fonts.googleapis.com/css2?family=Baloo+2:wght@500;600;700;800&family=Lexend:wght@300;350;400;450;500;600&family=Patrick+Hand&display=swap"

# ---- live intake embed replaces the review-preview card ----
def intake_live(title, lede):
    return f'''<div class="panel stack g20">
  <div class="stack g10"><span class="hand">Step one</span><h2>{title}</h2><p class="muted measure">{lede}</p></div>
  <div class="intake-embed">
    <iframe id="JotFormIFrame-231875318826061" title="ACT ABA Intake form" allow="geolocation; microphone; camera; fullscreen" src="https://form.jotform.com/231875318826061" style="min-width:100%;max-width:100%;height:900px;border:none" loading="lazy"></iframe>
  </div>
  <p class="tiny">Rather talk to a person? Call Colorado {CO_TEL} or Oklahoma {OK_TEL}. Trouble loading the form? <a href="https://form.jotform.com/231875318826061" target="_blank" rel="noopener">Open it in a new tab</a>.</p>
</div>'''
p_pages.intake_live = intake_live
p_pages.intake_block = intake_live

PAGES = [
  # key, path, fn, title, description, nav key
  ("home", "/", p_pages.home, "Adventure Child Therapy | ABA therapy for kids in Colorado & Oklahoma",
   "Small, clinician-led ABA therapy for kids and families — in-home across the Denver metro, Grand Junction and Pueblo, and at our Tulsa center. No autism diagnosis needed to start in Colorado.", "home"),
  ("families", "/families/", p_pages.families, "Getting started with ABA | Adventure Child Therapy",
   "What happens between your first call and your first session: state requirements, insurance and cost, what we ask of families, and the ACT intake form.", "families"),
  ("services", "/services/", p_pages.services, "ABA services | Adventure Child Therapy",
   "Assessment, 1:1 ABA therapy, family guidance, toilet training, feeding, social and communication skills, daily living skills, and school and daycare support.", "services"),
  ("what-is-aba", "/what-is-aba/", p_pages.aba, "What is ABA? | Adventure Child Therapy",
   "Applied behavior analysis explained in plain language — what the science is, what a session looks like, and what we think is honest to promise.", "aba"),
  ("locations", "/locations/", p_pages.locations, "Locations | Adventure Child Therapy",
   "In-home ABA across the Denver metro, Grand Junction and Pueblo, Colorado, and center-based and in-home ABA in Tulsa, Oklahoma.", "locations"),
  ("providers", "/providers/", p_pro.providers, "Referral information for providers | Adventure Child Therapy",
   "For pediatricians, diagnosticians, school teams and case managers: documentation requirements by state, coverage, secure records, and the referral form.", "providers"),
  ("careers", "/careers/", p_pro.careers, "Careers | Adventure Child Therapy",
   "Behavior technician, RBT and BCBA positions in Colorado and Oklahoma. Colorado in-home technicians are salaried full-time; Tulsa center technicians are hourly on set shifts.", "careers"),
  ("about", "/about/", p_pages.about, "About us | Adventure Child Therapy",
   "A small, clinician-led ABA practice founded in 2021 — our clinical values, how we measure ourselves, and how we keep care safe and organized.", "about"),
  ("contact", "/contact/", p_pages.contact, "Contact | Adventure Child Therapy",
   "Call Colorado (720) 432-8989 or Oklahoma (918) 764-8544, email info@actaba.com, or start intake online.", "contact"),
]
NAV = [("/","home","Home"),("/families/","families","Families"),("/services/","services","Services"),("/what-is-aba/","aba","What is ABA"),("/locations/","locations","Locations"),("/providers/","providers","Providers"),("/careers/","careers","Careers"),("/about/","about","About"),("/contact/","contact","Contact")]

def fix_links(html):
    def rep(m):
        path, anchor = m.group(1), m.group(2) or ""
        return f'href="/{path + "/" if path else ""}{anchor}"'
    return re.sub(r'href="#/([a-z-]*)(#[a-z0-9-]+)?"', rep, html)

def strip_route(html):
    html = re.sub(r'<div data-route="[^"]*"( class="pro")? data-title="[^"]*" hidden>', lambda m: '<div' + (m.group(1) or '') + '>', html, count=1)
    html = re.sub(r'<div data-route="" data-title="[^"]*">', '<div>', html, count=1)
    return html

JSONLD = {
  "@context": "https://schema.org",
  "@graph": [
    {"@type": "MedicalOrganization", "@id": SITE + "/#org", "name": "Adventure Child Therapy", "alternateName": "ACT ABA",
     "url": SITE + "/", "logo": SITE + "/favicon.svg", "email": "info@actaba.com", "foundingDate": "2021",
     "medicalSpecialty": "Applied Behavior Analysis",
     "areaServed": ["Denver metro, CO", "Grand Junction, CO", "Pueblo, CO", "Tulsa, OK"],
     "contactPoint": [
        {"@type": "ContactPoint", "telephone": "+1-720-432-8989", "contactType": "customer service", "areaServed": "US-CO"},
        {"@type": "ContactPoint", "telephone": "+1-918-764-8544", "contactType": "customer service", "areaServed": "US-OK"}]},
    {"@type": "MedicalClinic", "@id": SITE + "/locations/#tulsa", "name": "Adventure Child Therapy — Tulsa Center",
     "parentOrganization": {"@id": SITE + "/#org"}, "telephone": "+1-918-764-8544", "email": "tulsa@actaba.com",
     "address": {"@type": "PostalAddress", "streetAddress": "1217 East 48th Street, Suite 101", "addressLocality": "Tulsa", "addressRegion": "OK", "postalCode": "74105", "addressCountry": "US"},
     "url": SITE + "/locations/#tulsa"}
  ]
}

JS = r"""
(function(){
  "use strict";
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.querySelectorAll('[data-year]').forEach(function(e){ e.textContent = new Date().getFullYear(); });

  var btn = document.querySelector('.menu-btn'), navEl = document.getElementById('sitenav');
  if (btn && navEl) {
    btn.addEventListener('click', function(){
      var open = navEl.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      btn.textContent = open ? 'Close' : 'Menu';
    });
    document.addEventListener('keydown', function(e){ if (e.key === 'Escape' && navEl.classList.contains('open')) { btn.click(); btn.focus(); } });
  }

  /* Jotform intake: resize the iframe to its content */
  if (window.jotformEmbedHandler) {
    document.querySelectorAll("iframe[id^='JotFormIFrame-']").forEach(function(f){
      window.jotformEmbedHandler("iframe[id='" + f.id + "']", "https://form.jotform.com/");
    });
  }

  /* ---- referral + careers forms post into Jotform ---- */
  var CONSENT = "I understand this form isn't a secure medical record, so I won't include clinical details or documents here.";
  var JOTFORM = {
    referral: { id: "262524494233053", map: {
      ref_name: "q2_q2_textbox0", ref_org: "q3_q3_textbox1", ref_email: "q4_q4_email2", ref_phone: "q5_q5_phone3[full]",
      ref_role: "q6_q6_dropdown4", ref_region: "q7_q7_dropdown5", ref_dx: "q8_q8_dropdown6", ref_payer: "q9_q9_dropdown7",
      ref_notes: "q10_q10_textarea8" }, consent: "q11_q11_checkbox9[]", page: "q12_q12_textbox10" },
    careers: { id: "262524661979066", map: {
      app_email: "q3_q3_email1", app_phone: "q4_q4_phone2[full]", app_role: "q5_q5_dropdown3", app_cert: "q6_q6_dropdown4",
      app_zip: "q7_q7_textbox5", app_avail: "q8_q8_textarea6", app_notes: "q9_q9_textarea7" },
      name: ["q2_q2_fullname0[first]", "q2_q2_fullname0[last]"], consent: "q10_q10_checkbox8[]", page: "q11_q11_textbox9" }
  };

  function setErr(el, msg){
    var err = document.getElementById(el.id + '-err');
    if (msg) { el.setAttribute('aria-invalid','true'); if (err) { err.textContent = msg; err.classList.add('show'); } }
    else { el.removeAttribute('aria-invalid'); if (err) { err.textContent=''; err.classList.remove('show'); } }
  }
  function labelFor(el){
    var l = el.closest('.field') ? el.closest('.field').querySelector('label') : null;
    return l ? l.textContent.replace('*','').trim() : el.name;
  }
  function validate(f){
    var ok = true, first = null;
    f.querySelectorAll('input,select,textarea').forEach(function(el){
      if (el.type === 'hidden' || el.name === 'company') return;
      if (el.type === 'checkbox') {
        var box = document.getElementById(el.id + '-err');
        if (el.required && !el.checked) { ok = false; if (box) { box.textContent = 'Please tick this box before sending.'; box.classList.add('show'); } if(!first) first = el; }
        else if (box) { box.textContent=''; box.classList.remove('show'); }
        return;
      }
      var v = (el.value||'').trim();
      if (el.required && !v) { setErr(el, 'Please add your ' + labelFor(el).toLowerCase() + '.'); ok = false; if(!first) first = el; return; }
      if (el.type === 'email' && v && !/^[^@\s]+@[^@\s]+\.[^@\s]{2,}$/.test(v)) { setErr(el, 'That email address doesn’t look quite right — check for a typo.'); ok = false; if(!first) first = el; return; }
      if (el.type === 'tel' && v && v.replace(/\D/g,'').length < 10) { setErr(el, 'Please include all 10 digits, with the area code.'); ok = false; if(!first) first = el; return; }
      setErr(el, '');
    });
    if (first) { first.focus(); first.scrollIntoView({ block:'center', behavior: reduce ? 'auto':'smooth' }); }
    return ok;
  }
  function payload(kind, f){
    var cfg = JOTFORM[kind], d = new URLSearchParams(), now = Date.now();
    d.append('formID', cfg.id);
    d.append('website', '');
    d.append('submitSource', 'form');
    d.append('buildDate', String(now));
    d.append('jsExecutionTracker', 'build-date-' + now + '=>init-started:' + now + '=>validator-called:' + now + '=>validator-mounted-false:' + now + '=>init-complete:' + now + '=>onsubmit-fired:' + (now + 1) + '=>submit-validation-passed:' + (now + 2));
    Object.keys(cfg.map).forEach(function(k){ var el = f.elements[k]; if (el && el.value.trim()) d.append(cfg.map[k], el.value.trim()); });
    if (cfg.name) {
      var full = (f.elements.app_name.value || '').trim(), i = full.indexOf(' ');
      d.append(cfg.name[0], i > 0 ? full.slice(0, i) : full);
      d.append(cfg.name[1], i > 0 ? full.slice(i + 1) : '');
    }
    if (f.elements.consent && f.elements.consent.checked) d.append(cfg.consent, CONSENT);
    d.append(cfg.page, location.href);
    return d;
  }
  document.querySelectorAll('form[data-form]').forEach(function(f){
    var status = f.querySelector('[data-status]');
    f.addEventListener('submit', function(e){
      e.preventDefault();
      var hp = f.querySelector('[name="company"]'); if (hp && hp.value) return;
      if (!validate(f)) { status.className = 'form-status warn show'; status.textContent = 'Almost there — a few fields above still need a little something.'; return; }
      var kind = f.dataset.form, btnEl = f.querySelector('button[type="submit"]');
      btnEl.disabled = true; btnEl.style.opacity = '.6';
      fetch('https://submit.jotform.com/submit/' + JOTFORM[kind].id, { method: 'POST', body: payload(kind, f), mode: 'no-cors' }).then(function(){
        f.reset();
        status.className = 'form-status ok show';
        status.innerHTML = kind === 'careers'
          ? '<strong>Application received — thank you.</strong> A member of our team reviews every application, and every applicant receives a response.'
          : '<strong>Referral received — thank you.</strong> We will contact the family and confirm the outcome with you. For anything urgent, call Colorado <a href="tel:+17204328989">(720) 432-8989</a> or Oklahoma <a href="tel:+19187648544">(918) 764-8544</a>.';
        status.scrollIntoView({ block:'center', behavior: reduce ? 'auto':'smooth' });
      }).catch(function(){
        status.className = 'form-status warn show';
        status.innerHTML = '<strong>That didn’t go through.</strong> Please call Colorado <a href="tel:+17204328989">(720) 432-8989</a> or Oklahoma <a href="tel:+19187648544">(918) 764-8544</a>, or email <a href="mailto:info@actaba.com">info@actaba.com</a>.';
      }).then(function(){ btnEl.disabled = false; btnEl.style.opacity = ''; });
    });
    f.querySelectorAll('input,select,textarea').forEach(function(el){
      el.addEventListener('input', function(){ if (el.getAttribute('aria-invalid')) setErr(el, ''); });
      el.addEventListener('change', function(){ if (el.getAttribute('aria-invalid')) setErr(el, ''); });
    });
  });
})();
"""

EXTRA_CSS = """
.intake-embed{border-radius:18px;overflow:hidden;background:#fff;border:2px solid var(--line)}
.intake-embed iframe{display:block;width:100%}
.skip{position:absolute}
.nf{min-height:50vh}
"""

def header(active):
    CUR = ' aria-current="page"'
    nav = "".join(f'<a href="{h}"{CUR if k==active else ""}>{t}</a>' for h,k,t in NAV)
    return f'''<a class="skip" href="#main">Skip to content</a>
{DEFS}
<div class="topstrip"><div class="wrap"><span>New here? One friendly call is all it takes to get started.</span><span>Colorado {CO_TEL} · Oklahoma {OK_TEL}</span></div></div>
<header class="hdr">
  <div class="wrap hdr-in">
    <a class="brand" href="/" aria-label="Adventure Child Therapy home">{LOGO}<span class="bn"><span class="b1">Adventure Child Therapy</span><span class="b2">ABA your way</span></span></a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="sitenav">Menu</button>
    <nav class="nav" id="sitenav" aria-label="Main">{nav}</nav>
    <div class="hdr-cta"><a class="btn btn-primary btn-sm" href="/families/#start">Start intake</a></div>
  </div>
</header>'''

FOOTER = f'''<footer class="ftr">
  <svg class="ftr-hills" aria-hidden="true" focusable="false"><use href="#ftrhills"/></svg>
  <div class="wrap stack g28">
    <div class="ftr-grid">
      <div class="stack g14">
        <div class="brand">{LOGO}<span class="bn"><span class="b1">Adventure Child Therapy</span><span class="b2">ABA your way</span></span></div>
        <p class="small" style="max-width:36ch">Small, clinician-led ABA for kids and families in Colorado and Oklahoma. Growing with families since 2021.</p>
      </div>
      <div class="stack g10"><h4>Families</h4><ul><li><a href="/families/">Getting started</a></li><li><a href="/services/">Services</a></li><li><a href="/what-is-aba/">What is ABA</a></li><li><a href="/families/#insurance">Insurance &amp; cost</a></li><li><a href="/families/#faq">Questions</a></li></ul></div>
      <div class="stack g10"><h4>Locations</h4><ul><li><a href="/locations/#denver">Denver metro</a></li><li><a href="/locations/#grand-junction">Grand Junction</a></li><li><a href="/locations/#pueblo">Pueblo</a></li><li><a href="/locations/#tulsa">Tulsa Center</a></li><li><a href="/locations/#expanding">Where we’re headed</a></li></ul></div>
      <div class="stack g10"><h4>Work &amp; referrals</h4><ul><li><a href="/careers/">Open roles</a></li><li><a href="/providers/">Refer a family</a></li><li><a href="/about/">About us</a></li><li><a href="/contact/">Contact</a></li></ul></div>
    </div>
    <div class="ftr-btm">
      <span>&copy; <span data-year>2026</span> Adventure Child Therapy, LLC. All rights reserved.</span>
      <span>Colorado {CO_TEL} · Oklahoma {OK_TEL} · <a href="mailto:info@actaba.com">info@actaba.com</a></span>
    </div>
  </div>
</footer>'''

def doc(path, title, desc, body_html, active, pro=False, jsonld=None, jotform=False, noindex=False, extra_head=""):
    url = SITE + path
    ld = f'<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False)}</script>' if jsonld else ''
    jf = '<script src="https://cdn.jotfor.ms/s/umd/latest/for-form-embed-handler.js"></script>' if jotform else ''
    robots = '<meta name="robots" content="noindex">' if noindex else ''
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
{robots}<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Adventure Child Therapy">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#FFC845">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="/assets/site.css">
{extra_head}{ld}
</head>
<body{' class="is-pro"' if pro else ''}>
{header(active)}
<main id="main">
{body_html}
</main>
{FOOTER}
{jf}
<script src="/assets/site.js" defer></script>
</body>
</html>
'''

def build():
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT + "/assets")
    open(OUT + "/assets/site.css", "w").write(CSS + EXTRA_CSS)
    open(OUT + "/assets/site.js", "w").write(JS)
    for key, path, fn, title, desc, active in PAGES:
        body = fix_links(strip_route(fn()))
        assert 'data-route' not in body and ' hidden>' not in body, key
        d = OUT + path
        os.makedirs(d, exist_ok=True)
        html = doc(path, title, desc, body, active, pro=(key in ("providers", "careers")),
                   jsonld=JSONLD if key == "home" else None, jotform=(key in ("families", "contact")))
        open(d + "index.html", "w").write(html)
    # 404
    nf = f'''<section class="phead"><div class="hero-sky" aria-hidden="true"><svg class="sun" viewBox="0 0 200 200" focusable="false"><use href="#sunsym"/></svg></div>
  <div class="wrap stack g14 nf"><span class="hand">Page not found</span><h1>This page wandered off the trail.</h1>
  <p class="lede measure">The page you were looking for isn’t here — it may have moved when we updated our website. These will get you back on track:</p>
  <div class="cta-row"><a class="btn btn-primary" href="/">Go to the home page {ARROW}</a><a class="btn btn-secondary" href="/families/">Getting started</a><a class="btn btn-secondary" href="/contact/">Contact us</a></div></div>
  {p_pages.strip()}</section>'''
    open(OUT + "/404.html", "w").write(doc("/404.html", "Page not found | Adventure Child Therapy", "This page could not be found.", nf, "", noindex=True).replace('href="/families/"', 'href="/families/"'))
    # legacy WordPress URLs -> new pages
    legacy = {"about-us": "/about/", "contact-us": "/contact/", "book-an-appointment": "/families/#start",
              "assessment": "/services/#assessment", "on-going-treatment": "/services/#therapy", "toilet-training": "/services/#toilet-training",
              "feeding-issues": "/services/#feeding", "social-skills": "/services/#social", "academic-support": "/services/#school"}
    for old, new in legacy.items():
        os.makedirs(f"{OUT}/{old}", exist_ok=True)
        open(f"{OUT}/{old}/index.html", "w").write(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Adventure Child Therapy</title>
<meta name="robots" content="noindex"><link rel="canonical" href="{SITE}{new.split('#')[0]}">
<meta http-equiv="refresh" content="0; url={new}"><script>location.replace("{new}")</script></head>
<body><p>This page has moved. <a href="{new}">Continue to the new page</a>.</p></body></html>''')
    # sitemap, robots, CNAME, nojekyll
    urls = "".join(f"<url><loc>{SITE}{p}</loc><lastmod>{TODAY}</lastmod><changefreq>monthly</changefreq><priority>{'1.0' if p=='/' else '0.8'}</priority></url>" for _, p, *_ in PAGES)
    open(OUT + "/sitemap.xml", "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    open(OUT + "/robots.txt", "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    open(OUT + "/CNAME", "w").write("actaba.com\n")
    open(OUT + "/.nojekyll", "w").write("")
    # favicon (fixed colors — no CSS variables outside the page)
    open(OUT + "/favicon.svg", "w").write('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44 44"><rect x="1" y="1" width="42" height="42" rx="14" fill="#DDF0FA"/><circle cx="31" cy="13" r="5.2" fill="#FFC845"/><path d="M1 30 C9 21 15 20 22 25 C28 29 34 22 43 24 V30 C43 37.7 36.7 43 29 43 H15 C7.3 43 1 37.7 1 30Z" fill="#7CC68A"/><path d="M1 35 C10 30 18 31 25 34 C31 36.5 37 34 43 33 V29 C43 36.7 36.7 43 29 43 H15 C7.3 43 1 37.7 1 35Z" fill="#2F8A57"/><path d="M9 40 C14 36 16 33 21 32 C26 31 27 27 31 26" fill="none" stroke="#FFF6DF" stroke-width="2" stroke-linecap="round" stroke-dasharray=".5 4"/></svg>''')
    print("built", sum(len(fs) for _, _, fs in os.walk(OUT)), "files")

if __name__ == "__main__":
    build()
