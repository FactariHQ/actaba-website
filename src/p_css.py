CSS = r"""
:root{
  --paper:#FFF9EF; --surface:#FFFFFF; --surface-2:#FFFDF8;
  --band-sky:#E4F3FB; --band-meadow:#E8F5E6; --band-sun:#FFF1CC; --coral-soft:#FFE6DC; --lilac-soft:#EEEAFB;
  --hero-sky:#DDF0FA; --hero-sky-2:#F2FAFE;
  --ink:#2A2B4A; --ink-2:#5A5B78; --ink-3:#6D6D88; --on-sun:#2A2B4A;
  --line:#EADFCB; --line-2:#D9CBB2;
  --sun:#FFC845; --sun-deep:#E9A824; --sky:#8ECDF0; --sky-ink:#1D6A96;
  --meadow:#7CC68A; --meadow-ink:#1E7247; --coral:#FF8A65; --coral-ink:#B53F24;
  --hill-1:#BFE0EC; --hill-2:#A9DBAE; --hill-3:#7CC68A; --hill-4:#4FA86A; --hill-5:#2F8A57;
  --trunk:#9B6B43; --trail:#FFF6DF; --cloud:#FFFFFF; --stars:0; --sunrays:1;
  --shadow-ink:rgba(42,43,74,.16);
  --ftr-bg:#2C7A51; --ftr-ink:#F4FBF3; --ftr-link:#FFE7A3; --ftr-line:rgba(255,255,255,.22);
  --ring:rgba(255,200,69,.55);
  --pro-bg:#FFFFFF; --pro-head:#2A2B4A; --pro-head-ink:#F5F0E6; --pro-head-2:#C4C2DA; --pro-band:#F3F3F8; --pro-line:#E1E1EA; --pro-line-2:#C8C8D6; --pro-ring:rgba(29,106,150,.28);
  --f-display:"Baloo 2","Trebuchet MS","Arial Rounded MT Bold",system-ui,sans-serif;
  --f-body:"Lexend","Segoe UI","Helvetica Neue",Arial,sans-serif;
  --f-hand:"Patrick Hand","Comic Neue","Segoe Print","Bradley Hand",cursive;
  --wrap:1180px; --measure:64ch;
  --r-sm:10px; --r:16px; --r-lg:26px;
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --paper:#1C1E37; --surface:#272A4B; --surface-2:#22254A;
    --band-sky:#212650; --band-meadow:#1E2C3D; --band-sun:#2F2B3A; --coral-soft:#3A2A3A; --lilac-soft:#2B2A55;
    --hero-sky:#232758; --hero-sky-2:#1C1E37;
    --ink:#F5F0E6; --ink-2:#C4C2DA; --ink-3:#A09EBB; --on-sun:#2A2B4A;
    --line:#363A62; --line-2:#454A78;
    --sun:#FFC845; --sun-deep:#C98F17; --sky:#6FB6E0; --sky-ink:#8FCDF2;
    --meadow:#5DB177; --meadow-ink:#86D9A2; --coral:#F07E5B; --coral-ink:#FF9C7F;
    --hill-1:#2E3767; --hill-2:#2B4B5E; --hill-3:#2C5F50; --hill-4:#276B4A; --hill-5:#1D5139;
    --trunk:#6E4E36; --trail:#E9E2CF; --cloud:#3A3F6E; --stars:1; --sunrays:0;
    --shadow-ink:rgba(0,0,0,.4);
    --ftr-bg:#15172C; --ftr-ink:#E9E6F2; --ftr-link:#FFD66E; --ftr-line:rgba(255,255,255,.12);
    --ring:rgba(255,200,69,.5);
    --pro-bg:#1C1E37; --pro-head:#15172C; --pro-head-ink:#F5F0E6; --pro-head-2:#C4C2DA; --pro-band:#23264A; --pro-line:#363A62; --pro-line-2:#4A4F7E; --pro-ring:rgba(143,205,242,.3);
  }
}
:root[data-theme="dark"]{
  --paper:#1C1E37; --surface:#272A4B; --surface-2:#22254A;
  --band-sky:#212650; --band-meadow:#1E2C3D; --band-sun:#2F2B3A; --coral-soft:#3A2A3A; --lilac-soft:#2B2A55;
  --hero-sky:#232758; --hero-sky-2:#1C1E37;
  --ink:#F5F0E6; --ink-2:#C4C2DA; --ink-3:#A09EBB; --on-sun:#2A2B4A;
  --line:#363A62; --line-2:#454A78;
  --sun:#FFC845; --sun-deep:#C98F17; --sky:#6FB6E0; --sky-ink:#8FCDF2;
  --meadow:#5DB177; --meadow-ink:#86D9A2; --coral:#F07E5B; --coral-ink:#FF9C7F;
  --hill-1:#2E3767; --hill-2:#2B4B5E; --hill-3:#2C5F50; --hill-4:#276B4A; --hill-5:#1D5139;
  --trunk:#6E4E36; --trail:#E9E2CF; --cloud:#3A3F6E; --stars:1; --sunrays:0;
  --shadow-ink:rgba(0,0,0,.4);
  --ftr-bg:#15172C; --ftr-ink:#E9E6F2; --ftr-link:#FFD66E; --ftr-line:rgba(255,255,255,.12);
  --ring:rgba(255,200,69,.5);
  --pro-bg:#1C1E37; --pro-head:#15172C; --pro-head-ink:#F5F0E6; --pro-head-2:#C4C2DA; --pro-band:#23264A; --pro-line:#363A62; --pro-line-2:#4A4F7E; --pro-ring:rgba(143,205,242,.3);
}

*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;scroll-padding-top:90px}
body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--f-body);font-size:17px;line-height:1.68;font-weight:350;
  -webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility;overflow-x:hidden;display:flex;flex-direction:column;min-height:100vh}
main{flex:1}
img,svg{max-width:100%}
h1,h2,h3,h4{font-family:var(--f-display);margin:0;text-wrap:balance;color:var(--ink)}
h1{font-size:clamp(2.5rem,6.2vw,4.5rem);line-height:1.02;font-weight:800;letter-spacing:-.015em}
h2{font-size:clamp(1.95rem,3.9vw,2.95rem);line-height:1.08;font-weight:700;letter-spacing:-.01em}
h3{font-size:1.42rem;line-height:1.2;font-weight:700}
h4{font-size:1.18rem;line-height:1.25;font-weight:700}
p{margin:0}
strong{font-weight:600;color:var(--ink)}
a{color:var(--meadow-ink);font-weight:500;text-decoration:underline;text-decoration-thickness:2px;text-underline-offset:3px;text-decoration-color:color-mix(in srgb,var(--meadow-ink) 35%,transparent)}
a:hover{text-decoration-color:currentColor}
ul,ol{margin:0;padding-left:1.15em}
button{font:inherit;color:inherit;background:none;border:0;cursor:pointer}
:focus-visible{outline:3px solid var(--sun-deep);outline-offset:3px;border-radius:8px}
.tnum{font-variant-numeric:tabular-nums}
.skip{position:absolute;left:-9999px;top:0;background:var(--surface);color:var(--ink);padding:12px 18px;z-index:200;border-radius:0 0 var(--r) 0}
.skip:focus{left:0}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}

/* layout */
.wrap{width:min(100% - 40px,var(--wrap));margin-inline:auto}
.sec{padding-block:clamp(56px,7.5vw,104px)}
.sec.tight{padding-block:clamp(36px,5vw,60px)}
.stack{display:flex;flex-direction:column}
.g6{gap:6px}.g10{gap:10px}.g14{gap:14px}.g20{gap:20px}.g28{gap:28px}.g40{gap:40px}
.grid{display:grid;gap:22px}
.c2{grid-template-columns:repeat(2,minmax(0,1fr))}
.c3{grid-template-columns:repeat(3,minmax(0,1fr))}
.c4{grid-template-columns:repeat(4,minmax(0,1fr))}
.split{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(28px,5vw,72px);align-items:start}
@media (max-width:1040px){.c4{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:880px){.c2,.c3,.c4,.split{grid-template-columns:minmax(0,1fr)}}
.measure{max-width:var(--measure)}
.lede{font-size:clamp(1.08rem,1.6vw,1.24rem);line-height:1.6;color:var(--ink-2)}
.muted{color:var(--ink-2)}
.small{font-size:.95rem}
.tiny{font-size:.86rem;color:var(--ink-3)}
.center{text-align:center;align-items:center}

/* handwritten eyebrow */
.hand{font-family:var(--f-hand);font-size:1.32rem;line-height:1.1;color:var(--coral-ink);letter-spacing:.01em;font-weight:400}
.hand.sky{color:var(--sky-ink)} .hand.meadow{color:var(--meadow-ink)}

/* bands with soft wavy paper edges */
.band{position:relative;background:var(--bandc)}
.band::before,.band::after{content:"";position:absolute;left:0;right:0;height:22px;background:var(--bandc);pointer-events:none;
  -webkit-mask:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 160 22' preserveAspectRatio='none'%3E%3Cpath d='M0 12C27 2 53 2 80 12S133 22 160 12V22H0Z'/%3E%3C/svg%3E") repeat-x left bottom/220px 22px;
          mask:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 160 22' preserveAspectRatio='none'%3E%3Cpath d='M0 12C27 2 53 2 80 12S133 22 160 12V22H0Z'/%3E%3C/svg%3E") repeat-x left bottom/220px 22px}
.band::before{top:-21px}
.band::after{bottom:-21px;transform:scaleY(-1)}
.band.flat-top::before,.band.flat-bottom::after{display:none}
.b-sky{--bandc:var(--band-sky)} .b-meadow{--bandc:var(--band-meadow)} .b-sun{--bandc:var(--band-sun)}

/* top strip + header */
.topstrip{background:var(--sun);color:var(--on-sun);font-size:.9rem;padding:8px 0;font-weight:450}
.topstrip .wrap{display:flex;gap:4px 14px;flex-wrap:wrap;justify-content:center;text-align:center}
.topstrip a{color:var(--on-sun);font-weight:600;text-decoration-color:rgba(42,43,74,.4)}
.hdr{position:sticky;top:0;z-index:100;background:color-mix(in srgb,var(--paper) 90%,transparent);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border-bottom:2px solid var(--line)}
.hdr-in{display:flex;align-items:center;gap:14px;padding-block:10px}
.brand{display:flex;align-items:center;gap:11px;color:var(--ink);text-decoration:none;flex:none}
.brand .b1{white-space:nowrap}
.brand svg{flex:none}
@media (max-width:480px){.brand{flex:0 1 auto;min-width:0}.brand .b1{font-size:1.02rem}.brand .b2{font-size:.95rem}.hdr-in{gap:10px}.menu-btn{padding:7px 13px}}
.brand .bn{display:flex;flex-direction:column;line-height:1}
.brand .b1{font-family:var(--f-display);font-size:1.22rem;font-weight:800;letter-spacing:-.01em}
.brand .b2{font-family:var(--f-hand);font-size:1.02rem;color:var(--coral-ink);margin-top:2px}
.nav{display:flex;align-items:center;gap:2px;margin-left:auto}
.nav a{color:var(--ink-2);padding:7px 11px;border-radius:999px;font-size:.92rem;font-weight:450;white-space:nowrap;text-decoration:none}
.nav a:hover{background:var(--band-sun);color:var(--ink)}
.nav a[aria-current="page"]{color:var(--on-sun);background:var(--sun)}
.hdr-cta{flex:none}
.menu-btn{display:none;margin-left:auto;border:2px solid var(--line-2);border-radius:999px;padding:8px 16px;font-weight:500;font-size:.92rem;background:var(--surface)}
@media (max-width:1240px){
  .nav{position:absolute;top:100%;left:0;right:0;background:var(--surface);border-bottom:2px solid var(--line);flex-direction:column;align-items:stretch;gap:4px;padding:10px 20px 20px;max-height:min(74dvh,640px);overflow:auto;box-shadow:0 20px 40px -24px var(--shadow-ink);transform:translateY(-8px);opacity:0;pointer-events:none;transition:opacity .18s ease,transform .18s ease;margin-left:0}
  .nav.open{opacity:1;transform:none;pointer-events:auto}
  .nav a{padding:11px 14px;font-size:1.02rem}
  .menu-btn{display:block}
  .hdr-cta{display:none}
}

/* buttons: paper tabs with a stacked edge */
.btn{display:inline-flex;align-items:center;justify-content:center;gap:9px;padding:13px 24px;border-radius:999px;font-family:var(--f-display);font-weight:700;font-size:1.1rem;line-height:1.1;text-decoration:none;border:2px solid transparent;transition:transform .14s ease,box-shadow .14s ease,background .16s ease}
.btn:hover{transform:translateY(-2px)}
.btn:active{transform:translateY(2px)}
.btn-primary{background:var(--sun);color:var(--on-sun);box-shadow:0 4px 0 var(--sun-deep)}
.btn-primary:hover{box-shadow:0 6px 0 var(--sun-deep)}
.btn-primary:active{box-shadow:0 1px 0 var(--sun-deep)}
.btn-secondary{background:var(--surface);color:var(--ink);border-color:var(--line-2);box-shadow:0 4px 0 var(--line-2)}
.btn-secondary:hover{box-shadow:0 6px 0 var(--line-2)}
.btn-secondary:active{box-shadow:0 1px 0 var(--line-2)}
.btn-sm{padding:9px 18px;font-size:1rem}
.go{display:inline-flex;align-items:center;gap:7px;font-weight:600;color:var(--meadow-ink);text-decoration:none}
.go:hover{text-decoration:underline}
.arrow{display:inline-block;transition:transform .18s ease}
.btn:hover .arrow,.go:hover .arrow,.card:hover .arrow{transform:translateX(4px)}
.cta-row{display:flex;gap:14px;flex-wrap:wrap;align-items:center}

/* hero */
.hero{position:relative;overflow:hidden;background:linear-gradient(180deg,var(--hero-sky) 0%,var(--hero-sky-2) 88%)}
.hero-sky{position:absolute;inset:0;pointer-events:none}
.sun{position:absolute;right:clamp(-40px,6vw,120px);top:clamp(24px,5vw,60px);width:clamp(120px,15vw,210px)}
.kite{position:absolute;right:clamp(8px,19vw,300px);top:clamp(150px,20vw,250px);width:clamp(70px,8vw,112px);transform-origin:50% 20%}
.cloud{position:absolute;width:clamp(120px,14vw,200px)}
.cloud.a{left:-30px;top:40px} .cloud.b{right:36%;top:22px;width:clamp(90px,9vw,140px)}
.stars{position:absolute;inset:0;opacity:var(--stars)}
.hero-copy{position:relative;z-index:2;padding-top:clamp(44px,7vw,96px);display:flex;flex-direction:column;gap:20px}
.hero-copy > *{max-width:780px}
.hero h1 .hl{position:relative;white-space:nowrap;display:inline-block}
.hero h1 .hl::after{content:"";position:absolute;left:-4px;right:-6px;bottom:.06em;height:.3em;background:var(--sun);border-radius:40% 60% 50% 45%/60% 40% 60% 40%;z-index:-1;transform:rotate(-1.2deg)}
.hero h1{position:relative;z-index:0}
.chips{display:flex;flex-wrap:wrap;gap:10px;padding-top:4px}
.chip{display:inline-flex;align-items:center;gap:8px;background:var(--surface);border:2px solid var(--line);border-radius:999px;padding:6px 14px 6px 8px;font-size:.92rem;color:var(--ink);line-height:1.3}
.chip i{width:22px;height:22px;border-radius:50%;flex:none;display:grid;place-items:center;font-style:normal}
.chip svg{width:14px;height:14px}
.hills{position:relative;z-index:1;display:block;width:100%;height:clamp(180px,27vw,390px);margin-top:clamp(-70px,-3vw,-20px);margin-bottom:-2px}
.anim-rise{animation:rise 1s cubic-bezier(.2,.8,.25,1) both}
.anim-rise.l2{animation-delay:.08s}.anim-rise.l3{animation-delay:.16s}.anim-rise.l4{animation-delay:.24s}
@keyframes rise{from{transform:translateY(40px)}to{transform:none}}
.kite{animation:sway 6s ease-in-out infinite}
@keyframes sway{0%,100%{transform:rotate(-5deg) translateY(0)}50%{transform:rotate(6deg) translateY(-8px)}}
.cloud{animation:drift 22s ease-in-out infinite alternate}
.cloud.b{animation-duration:28s}
@keyframes drift{from{transform:translateX(0)}to{transform:translateX(46px)}}
@media (max-width:760px){.kite{display:none}.cloud.b{display:none}.sun{right:-38px;top:12px;width:120px}}

/* page heads (inner pages) */
.phead{position:relative;background:var(--hero-sky);padding-top:clamp(40px,6vw,80px)}
.phead .wrap{position:relative;z-index:2;padding-bottom:10px}
.phead h1{font-size:clamp(2.2rem,5vw,3.6rem);max-width:18ch}
.phead .strip{position:relative;display:block;width:100%;height:clamp(64px,8vw,110px);margin-top:clamp(18px,3vw,36px);margin-bottom:-2px}
.phead .sun{width:clamp(90px,10vw,150px);top:clamp(20px,4vw,44px);right:clamp(-30px,4vw,80px)}
.anchors{display:flex;flex-wrap:wrap;gap:8px}
.anchors a{font-size:.9rem;border:2px solid var(--line);border-radius:999px;padding:5px 14px;color:var(--ink);background:var(--surface);text-decoration:none;font-weight:450}
.anchors a:hover{border-color:var(--sun-deep);background:var(--band-sun)}

/* cards */
.card{background:var(--surface);border:2px solid var(--line);border-radius:var(--r-lg);padding:26px;display:flex;flex-direction:column;gap:12px;box-shadow:0 6px 0 var(--line);color:inherit}
a.card{text-decoration:none;font-weight:inherit;transition:transform .18s ease,box-shadow .18s ease}
a.card:hover{transform:translateY(-3px);box-shadow:0 9px 0 var(--line)}
.card.soft{box-shadow:none}
.tint-sun{background:var(--band-sun);border-color:transparent;box-shadow:0 6px 0 color-mix(in srgb,var(--sun-deep) 35%,transparent)}
.tint-sky{background:var(--band-sky);border-color:transparent;box-shadow:0 6px 0 color-mix(in srgb,var(--sky) 45%,transparent)}
.tint-meadow{background:var(--band-meadow);border-color:transparent;box-shadow:0 6px 0 color-mix(in srgb,var(--meadow) 40%,transparent)}
.tint-coral{background:var(--coral-soft);border-color:transparent;box-shadow:0 6px 0 color-mix(in srgb,var(--coral) 35%,transparent)}
.tint-lilac{background:var(--lilac-soft);border-color:transparent;box-shadow:0 6px 0 color-mix(in srgb,#9C8FE0 35%,transparent)}
.band .card:not([class*="tint-"]){border-color:transparent}
.k{font-family:var(--f-hand);font-size:1.18rem;line-height:1.1;color:var(--coral-ink)}
.ico{width:54px;height:54px;flex:none}
.ico.lg{width:66px;height:66px}
.panel{background:var(--surface);border-radius:32px;padding:clamp(24px,4vw,48px);border:2px solid var(--line);box-shadow:0 8px 0 var(--line)}
.callout{background:var(--coral-soft);border-radius:var(--r);padding:16px 20px;color:var(--ink-2)}
.note{background:var(--band-meadow);border-radius:var(--r);padding:18px 22px;color:var(--ink-2)}
.band.b-meadow .note{background:var(--surface)}
.pill{display:inline-flex;align-items:center;border-radius:999px;padding:4px 13px;font-size:.88rem;color:var(--ink);background:var(--band-sky)}
.band .pill{background:var(--surface)}
.pill.zip{font-variant-numeric:tabular-nums;letter-spacing:.03em;background:var(--band-sun)}
.pills{display:flex;flex-wrap:wrap;gap:8px}
.ticks{list-style:none;padding:0;display:flex;flex-direction:column;gap:10px}
.ticks li{display:grid;grid-template-columns:22px minmax(0,1fr);gap:10px;align-items:start;color:var(--ink-2)}
.ticks li::before{content:"";width:18px;height:18px;margin-top:4px;border-radius:50%;background:var(--meadow) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 18 18'%3E%3Cpath d='M5 9.4l2.6 2.6L13 6.4' fill='none' stroke='%23fff' stroke-width='2.2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/18px no-repeat}
.ticks.x li::before{background:var(--coral) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 18 18'%3E%3Cpath d='M6 6l6 6M12 6l-6 6' fill='none' stroke='%23fff' stroke-width='2.2' stroke-linecap='round'/%3E%3C/svg%3E") center/18px no-repeat}

/* trail of steps */
.trail{max-width:920px;position:relative;display:flex;flex-direction:column;gap:clamp(18px,3vw,30px);padding-left:0;list-style:none;margin:0}
.trail::before{content:"";position:absolute;left:31px;top:30px;bottom:30px;border-left:4px dotted var(--line-2)}
.stop{position:relative;display:grid;grid-template-columns:66px minmax(0,1fr);gap:clamp(16px,2.6vw,28px);align-items:start}
.marker{position:relative;z-index:1;width:66px;height:66px;display:grid;place-items:center}
.marker svg{position:absolute;inset:0;width:66px;height:66px}
.marker b{position:relative;font-family:var(--f-display);font-weight:800;font-size:1.6rem;color:var(--on-sun);line-height:1;margin-top:4px}
.stop-body{background:var(--surface);border:2px solid var(--line);border-radius:var(--r-lg);padding:22px 26px;display:flex;flex-direction:column;gap:8px;box-shadow:0 6px 0 var(--line)}
.band .stop-body{border-color:transparent}
.when{display:inline-block;align-self:flex-start;font-size:.8rem;font-weight:500;letter-spacing:.04em;text-transform:uppercase;color:var(--sky-ink);background:var(--band-sky);border-radius:999px;padding:2px 11px}
.band.b-sky .when{background:var(--band-sun);color:var(--ink)}
.stop .tip{display:flex;gap:10px;align-items:flex-start;color:var(--meadow-ink);font-weight:500;font-size:.96rem;padding-top:4px}
.stop .tip svg{flex:none;width:20px;height:20px;margin-top:3px}
.hand-note{position:absolute;right:-6px;top:-34px;transform:rotate(-3deg);display:flex;align-items:center;gap:6px;color:var(--coral-ink)}
.hand-note svg{width:48px;height:30px}
@media (max-width:640px){.stop{grid-template-columns:48px minmax(0,1fr)}.marker,.marker svg{width:48px;height:48px}.marker b{font-size:1.2rem}.trail::before{left:22px}.stop-body{padding:18px}.hand-note{position:static;transform:none;margin-bottom:-4px}}

/* services */
.svc{display:grid;grid-template-columns:minmax(0,.85fr) minmax(0,1.3fr);gap:clamp(18px,4vw,56px);align-items:start;padding-block:clamp(26px,3.6vw,40px);border-top:2px dashed var(--line)}
.svc:first-child{border-top:0}
.svc-head{display:grid;grid-template-columns:auto minmax(0,1fr);gap:16px;align-items:start}
.svc-head p{font-family:var(--f-hand);font-size:1.28rem;line-height:1.2;color:var(--coral-ink);margin-top:4px}
@media (max-width:820px){.svc{grid-template-columns:minmax(0,1fr);gap:14px}}
.tile{display:grid;grid-template-columns:auto minmax(0,1fr);gap:14px;align-items:start;padding:18px 20px}
.tile h4{margin-bottom:2px}

/* faq */
.faqs{display:flex;flex-direction:column;gap:12px}
details.faq{background:var(--surface);border-radius:var(--r);border:2px solid var(--line)}
.band details.faq{border-color:transparent}
details.faq summary{list-style:none;cursor:pointer;padding:16px 56px 16px 22px;position:relative;font-family:var(--f-display);font-weight:700;font-size:1.16rem;line-height:1.3}
details.faq summary::-webkit-details-marker{display:none}
details.faq summary::after{content:"+";position:absolute;right:16px;top:50%;width:28px;height:28px;margin-top:-14px;border-radius:50%;background:var(--sun);color:var(--on-sun);display:grid;place-items:center;font-size:1.3rem;line-height:1;font-weight:700;transition:transform .2s ease}
details.faq[open] summary::after{transform:rotate(45deg)}
details.faq .a{padding:0 24px 20px 22px;color:var(--ink-2);max-width:var(--measure)}

/* progress chart */
.chart-card{padding:22px 22px 16px}
.chart-card svg{width:100%;height:auto;display:block}

/* locations */
.loc{padding:0;overflow:hidden;gap:0}
.loc .mini{display:block;width:100%;height:auto;aspect-ratio:200/96;background:var(--band-sky)}
.loc-body{padding:18px 22px 22px;display:flex;flex-direction:column;gap:8px;flex:1}
.loc-body .go{margin-top:auto;padding-top:6px}
.addr{font-size:.93rem;line-height:1.55;color:var(--ink-2);font-style:normal}
.locrow{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(24px,5vw,64px);align-items:start;scroll-margin-top:100px}
@media (max-width:880px){.locrow{grid-template-columns:minmax(0,1fr)}}

/* forms */
form.act{display:flex;flex-direction:column;gap:18px}
.field{display:flex;flex-direction:column;gap:7px}
.field label{font-weight:500;font-size:.95rem}
.field .hint{font-size:.85rem;color:var(--ink-3)}
.field input,.field select,.field textarea{font:inherit;font-size:1rem;color:var(--ink);background:var(--paper);border:2px solid var(--line-2);border-radius:14px;padding:12px 14px;width:100%;transition:border-color .16s ease,box-shadow .16s ease}
.field textarea{min-height:110px;resize:vertical}
.field input:focus,.field select:focus,.field textarea:focus{outline:none;border-color:var(--sun-deep);box-shadow:0 0 0 4px var(--ring)}
.field [aria-invalid="true"]{border-color:var(--coral-ink)}
.err{color:var(--coral-ink);font-size:.87rem;font-weight:500;display:none}
.err.show{display:block}
.req{color:var(--coral-ink)}
.f2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px}
@media (max-width:640px){.f2{grid-template-columns:minmax(0,1fr)}}
.checkrow{display:flex;gap:11px;align-items:flex-start}
.checkrow input{width:20px;height:20px;margin-top:3px;flex:none;accent-color:var(--meadow)}
.checkrow label{font-size:.93rem;color:var(--ink-2)}
.hp{position:absolute;left:-9999px;width:1px;height:1px;overflow:hidden}
.form-status{border-radius:var(--r);padding:16px 18px;display:none;font-size:.96rem}
.form-status.show{display:block}
.form-status.ok{background:var(--band-meadow);color:var(--ink)}
.form-status.warn{background:var(--band-sun);color:var(--ink)}
.intake-card{border-style:dashed;box-shadow:none;align-items:flex-start;background:var(--paper)}

/* jobs */
.job{background:var(--surface);border:2px solid var(--line);border-radius:var(--r-lg);overflow:hidden}
.job summary{list-style:none;cursor:pointer;padding:20px 24px;display:grid;grid-template-columns:minmax(0,1fr) auto;gap:14px;align-items:center}
.job summary::-webkit-details-marker{display:none}
.jt{display:block;font-family:var(--f-display);font-size:1.3rem;font-weight:700;line-height:1.2}
.jm{display:block;font-size:.9rem;color:var(--ink-2);margin-top:3px}
.job .plus{width:32px;height:32px;border-radius:50%;background:var(--sun);color:var(--on-sun);display:grid;place-items:center;font-weight:700;font-size:1.35rem;line-height:1;transition:transform .2s ease}
.job[open] .plus{transform:rotate(45deg)}
.job-body{padding:4px 24px 24px;display:flex;flex-direction:column;gap:14px}
.pay{background:var(--band-sun);border-radius:var(--r);padding:12px 16px;color:var(--ink);font-size:.95rem}

/* CTA with kite */
.cta{position:relative;overflow:hidden;background:var(--band-sun);border-radius:36px;padding:clamp(30px,5vw,60px);display:grid;grid-template-columns:minmax(0,1.4fr) minmax(0,.6fr);gap:24px;align-items:center}
.cta .kite-art{width:100%;max-width:220px;justify-self:center}
@media (max-width:760px){.cta{grid-template-columns:minmax(0,1fr)}.cta .kite-art{max-width:130px;order:-1;justify-self:start}}

/* footer */
.ftr{background:var(--ftr-bg);color:var(--ftr-ink);position:relative;margin-top:clamp(60px,8vw,110px)}
.ftr-hills{position:absolute;left:0;right:0;bottom:calc(100% - 2px);height:clamp(50px,6vw,84px);width:100%;display:block}
.ftr .wrap{padding-block:48px 30px}
.ftr-grid{display:grid;grid-template-columns:1.5fr repeat(3,1fr);gap:34px}
@media (max-width:900px){.ftr-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:560px){.ftr-grid{grid-template-columns:minmax(0,1fr)}}
.ftr h4{font-family:var(--f-hand);font-weight:400;font-size:1.3rem;color:var(--ftr-link)}
.ftr ul{list-style:none;padding:0;display:flex;flex-direction:column;gap:8px}
.ftr a{color:var(--ftr-ink);text-decoration-color:var(--ftr-line);font-weight:400}
.ftr a:hover{color:var(--ftr-link)}
.ftr .brand{color:var(--ftr-ink)} .ftr .brand .b2{color:var(--ftr-link)}
.ftr p{color:var(--ftr-ink);opacity:.9}
.ftr-btm{display:flex;flex-wrap:wrap;gap:12px 26px;justify-content:space-between;border-top:2px solid var(--ftr-line);margin-top:36px;padding-top:20px;font-size:.88rem}

/* ---------- professional register: Providers & Careers ---------- */
.pro{--line:var(--pro-line);--line-2:var(--pro-line-2);background:var(--pro-bg)}
.pro .hand,.pro .k{font-family:var(--f-body);font-size:.76rem;font-weight:600;letter-spacing:.13em;text-transform:uppercase;line-height:1.3;color:var(--meadow-ink)}
.pro h1,.pro h2,.pro h3,.pro h4,.pro .jt{font-family:var(--f-body);font-weight:600;letter-spacing:-.022em}
.pro h1{font-size:clamp(2rem,4.3vw,3.05rem);line-height:1.1;max-width:22ch}
.pro h2{font-size:clamp(1.55rem,2.8vw,2.1rem);line-height:1.18}
.pro h3{font-size:1.14rem;line-height:1.3;letter-spacing:-.012em}
.pro h4{font-size:1.02rem;letter-spacing:-.01em}
.pro .card{border:1px solid var(--line);box-shadow:none;border-radius:14px;padding:24px;background:var(--surface)}
.pro .band .card:not([class*="tint-"]){border-color:var(--line)}
.pro .band{--bandc:var(--pro-band)}
.pro .band::before,.pro .band::after{display:none}
.pro .btn{border-radius:10px;font-family:var(--f-body);font-weight:600;font-size:.98rem;letter-spacing:-.005em;box-shadow:none;border-width:1px}
.pro .btn:hover,.pro .btn:active{transform:none;box-shadow:none}
.pro .btn-primary{background:var(--ink);color:var(--paper)}
.pro .btn-primary:hover{background:var(--ink-2)}
.pro .btn-secondary{background:var(--surface);border-color:var(--line-2)}
.pro .btn-secondary:hover{border-color:var(--ink-2)}
.pro .btn-sm{padding:9px 16px;font-size:.93rem}
.pro .panel{border-radius:16px;box-shadow:none;border:1px solid var(--line)}
.pro .pill{background:var(--pro-band);border-radius:6px;font-size:.85rem}
.pro .ticks{gap:9px}
.pro .ticks li{grid-template-columns:18px minmax(0,1fr)}
.pro .ticks li::before{width:16px;height:16px;margin-top:5px;border-radius:0;background:var(--meadow-ink);
  -webkit-mask:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Cpath d='M3 8.4l3.2 3.2L13 4.6' fill='none' stroke='%23000' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/16px no-repeat;
          mask:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Cpath d='M3 8.4l3.2 3.2L13 4.6' fill='none' stroke='%23000' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/16px no-repeat}
.pro .ticks.neg li::before{background:var(--ink-3);
  -webkit-mask:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Cpath d='M4 8h8' fill='none' stroke='%23000' stroke-width='2' stroke-linecap='round'/%3E%3C/svg%3E") center/16px no-repeat;
          mask:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Cpath d='M4 8h8' fill='none' stroke='%23000' stroke-width='2' stroke-linecap='round'/%3E%3C/svg%3E") center/16px no-repeat}
.pro .callout{background:var(--surface);border:1px solid var(--line-2);border-radius:12px;padding:18px 22px;display:grid;grid-template-columns:auto minmax(0,1fr);gap:14px;align-items:start}
.pro .callout .tag{font-size:.72rem;font-weight:600;letter-spacing:.12em;text-transform:uppercase;background:var(--ink);color:var(--paper);border-radius:6px;padding:4px 8px;margin-top:2px;white-space:nowrap}
@media (max-width:560px){.pro .callout{grid-template-columns:minmax(0,1fr)}.pro .callout .tag{justify-self:start}}
.pro .job{border-width:1px;border-radius:12px}
.pro .jt{font-size:1.1rem}
.pro .jm{font-size:.86rem;color:var(--ink-3)}
.pro .job .plus{background:none;border:1px solid var(--line-2);color:var(--ink-2);font-weight:400;width:30px;height:30px;font-size:1.2rem}
.pro .job-body{border-top:1px solid var(--line);padding-top:18px;margin-inline:24px;padding-inline:0}
.pro .pay{background:var(--pro-band);border-radius:8px;font-size:.93rem}
.pro .field label{font-size:.9rem}
.pro .field input,.pro .field select,.pro .field textarea{border-width:1px;border-radius:10px;background:var(--surface)}
.pro .field input:focus,.pro .field select:focus,.pro .field textarea:focus{border-color:var(--sky-ink);box-shadow:0 0 0 3px var(--pro-ring)}
.pro .checkrow input{accent-color:var(--ink)}
.pro .form-status.ok{background:var(--pro-band)}
.pro .sec{padding-block:clamp(48px,6vw,84px)}
.pro .sec.tight{padding-block:clamp(28px,4vw,48px)}
.pro .measure{max-width:68ch}
.pro .tnum{font-variant-numeric:tabular-nums}
.pro .lead-list{display:grid;gap:0;border-top:1px solid var(--line)}
.pro .lead-list > div{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,2fr);gap:20px;padding-block:18px;border-bottom:1px solid var(--line)}
@media (max-width:700px){.pro .lead-list > div{grid-template-columns:minmax(0,1fr);gap:6px}}
.pro .sec-head{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.2fr);gap:clamp(20px,4vw,56px);align-items:end}
@media (max-width:880px){.pro .sec-head{grid-template-columns:minmax(0,1fr)}}

.phead-pro{background:var(--pro-head);color:var(--pro-head-ink);padding-block:clamp(44px,6vw,80px)}
.phead-pro .wrap{display:grid;grid-template-columns:minmax(0,1.35fr) minmax(0,.85fr);gap:clamp(28px,5vw,64px);align-items:end}
@media (max-width:900px){.phead-pro .wrap{grid-template-columns:minmax(0,1fr)}}
.pro .phead-pro h1{color:var(--pro-head-ink)}
.pro .phead-pro .hand{color:var(--sun)}
.phead-pro .lede{color:var(--pro-head-2)}
.phead-pro .anchors{padding-top:6px}
.phead-pro .anchors a{background:transparent;border:1px solid rgba(255,255,255,.22);color:var(--pro-head-ink);border-radius:8px;font-size:.86rem}
.phead-pro .anchors a:hover{background:rgba(255,255,255,.08);border-color:rgba(255,255,255,.45)}
.glance{margin:0;border:1px solid rgba(255,255,255,.18);border-radius:14px;padding:6px 22px;display:grid}
.glance > div{display:grid;grid-template-columns:minmax(0,.8fr) minmax(0,1.4fr);gap:14px;padding-block:13px;border-bottom:1px solid rgba(255,255,255,.12)}
.glance > div:last-child{border-bottom:0}
.glance dt{font-size:.72rem;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--pro-head-2);padding-top:3px}
.glance dd{margin:0;color:var(--pro-head-ink);font-size:.95rem;font-weight:450;line-height:1.45}
.glance a{color:var(--pro-head-ink);text-decoration-color:rgba(255,255,255,.35)}
body.is-pro .ftr-hills{display:none}
body.is-pro .ftr{margin-top:0}

[data-route][hidden]{display:none !important}
@media (prefers-reduced-motion:reduce){*,*::before,*::after{animation:none !important;transition:none !important;scroll-behavior:auto !important}}
@media print{.hdr,.nav,.topstrip,.ftr,.hero-sky,.hills{display:none}body{background:#fff;color:#000}}
"""
