from p_art import ico, mini, HERO_SKY, HILLS, strip
from p_shared import *

def phead(eyebrow, title, lede, anchors=None, extra=""):
    a = ''
    if anchors:
        a = '<nav class="anchors" aria-label="On this page">' + "".join(f'<a href="{h}">{t}</a>' for h, t in anchors) + '</nav>'
    return f'''<section class="phead">
  <div class="hero-sky" aria-hidden="true"><svg class="sun" viewBox="0 0 200 200" focusable="false"><use href="#sunsym"/></svg></div>
  <div class="wrap stack g14"><span class="hand">{eyebrow}</span><h1>{title}</h1><p class="lede measure">{lede}</p>{extra}{a}</div>
  {strip()}
</section>'''

CHECK = '<svg viewBox="0 0 14 14"><path d="M3 7.4l2.4 2.4L11 4.4" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def chart():
    import math
    pts = [189.7,180.6,186.7,171.5,159.4,162.5,144.3,132.1,135.2,113.9,98.8,89.7,71.5,56.3,59.4,38.1]
    xs = [40 + i*26.4 for i in range(16)]
    d = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in zip(xs, pts))
    area = d + f" L {xs[-1]:.1f} 214 L 40 214 Z"
    grid = "".join(f'<line x1="40" x2="436" y1="{y}" y2="{y}" stroke="var(--line)" stroke-width="1.5" stroke-dasharray="2 6" stroke-linecap="round"/>' for y in (38, 96, 155, 214))
    dots = "".join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="var(--surface)" stroke="var(--meadow-ink)" stroke-width="2.2"/>' for x, y in zip(xs[:-1], pts[:-1]))
    star = lambda cx, cy, r: "M" + " L".join(f"{cx + (r if i%2==0 else r*.45)*math.sin(i*math.pi/5):.1f} {cy - (r if i%2==0 else r*.45)*math.cos(i*math.pi/5):.1f}" for i in range(10)) + "Z"
    return f'''<div class="card chart-card stack g10">
  <div class="stack g6"><span class="k">A program that’s working</span><p class="small muted">Skills mastered, session by session</p></div>
  <svg viewBox="0 0 460 250" role="img" aria-label="Illustration: a line of skills mastered climbing steadily from session 1 to session 16, with small dips along the way" focusable="false">
    {grid}
    <path d="{area}" fill="var(--meadow)" opacity=".22"/>
    <path d="{d}" fill="none" stroke="var(--meadow-ink)" stroke-width="3.2" stroke-linejoin="round" stroke-linecap="round"/>
    {dots}
    <path d="{star(xs[-1], pts[-1], 13)}" fill="var(--sun)" stroke="var(--sun-deep)" stroke-width="1.6" stroke-linejoin="round"/>
    <text x="{xs[7]:.0f}" y="118" font-family="Patrick Hand, cursive" font-size="17" fill="var(--coral-ink)" text-anchor="end">a wobbly week — totally normal</text>
    <path d="M{xs[7]+4:.0f} 122 C{xs[8]-6:.0f} 128 {xs[8]:.0f} 132 {xs[8]:.0f} 140" fill="none" stroke="var(--coral-ink)" stroke-width="1.6" stroke-linecap="round"/>
    <text x="40" y="240" font-family="Lexend, sans-serif" font-size="12" fill="var(--ink-3)">Session 1</text>
    <text x="436" y="240" text-anchor="end" font-family="Lexend, sans-serif" font-size="12" fill="var(--ink-3)">Session 16</text>
  </svg>
  <p class="tiny">Illustration of how progress data looks — not a real child’s chart.</p>
</div>'''

def home():
    doors = [
      ("#/families", "i-home", "tint-sun", "For families", "My child needs a little help", "It starts with one call and a short form. Not having a diagnosis yet is a perfectly normal place to begin.", "Getting started"),
      ("#/providers", "i-letter", "tint-sky", "For providers", "I’d like to refer a family", "What to send, what we do with it, and how we’ll keep you in the loop — even if we can’t serve the family.", "Referral info"),
      ("#/careers", "i-seed", "tint-meadow", "Careers", "I want to work with kids", "Salaried RBT roles, part-time technician work, and BCBA positions across Colorado and Tulsa.", "Open roles"),
    ]
    door_html = "".join(f'<a class="card {t}" href="{h}">{ico(i,"ico lg")}<span class="k">{k}</span><h3>{ti}</h3><p class="small muted" style="flex:1">{p}</p><span class="go">{g} {ARROW}</span></a>' for h, i, t, k, ti, p, g in doors)
    tiles = "".join(f'<a class="card tile" href="#/services#{sid}">{ico(ic)}<div class="stack g6"><h4>{name}</h4><span class="small muted">{short}</span></div></a>' for sid, ic, name, short, *_ in SERVICES[:6])
    values = "".join(f'<div class="card {tint}">{ico(ic)}<h3>{t}</h3><p class="muted" style="font-family:var(--f-display);font-size:1.12rem;line-height:1.35;font-weight:500">{q}</p></div>' for t, q, tint, ic in VALUES)
    def loccard(lid, m, st, name, kind, addr, alt):
        a = ('<span class="addr">' + addr + '</span>') if addr else ''
        return f'<a class="card loc" href="#/locations#{lid}">{mini(m, alt)}<div class="loc-body"><span class="k">{st}</span><h3>{name}</h3><span class="small muted">{kind}</span>{a}<span class="go">Details {ARROW}</span></div></a>'
    locs = "".join(loccard(*l) for l in LOCS)
    ben = "".join(f'<div class="card" style="padding:18px 22px;gap:4px"><h4>{t}</h4><p class="small muted">{d}</p></div>' for t, d in BENEFITS[:4])
    return f'''<div data-route="" data-title="Adventure Child Therapy">
<section class="hero">
  {HERO_SKY}
  <div class="wrap hero-copy">
    <span class="hand">Kids’ ABA therapy in Colorado &amp; Oklahoma · since 2021</span>
    <h1>Every big adventure starts <span class="hl">close to home.</span></h1>
    <p class="lede measure">Adventure Child Therapy is a small, clinician-led ABA practice. We meet kids where life happens — living rooms across the Denver metro, Grand Junction, Pueblo and Ada, and the playroom floor of our Tulsa center — with one technician for one child, and a BCBA who looks at your child’s progress every week.</p>
    <div class="cta-row">{btn("#/families#start", "Start intake")}{btn("#/what-is-aba", "What is ABA?", "secondary", arrow=False)}</div>
    <div class="chips">
      <span class="chip"><i style="background:var(--meadow)">{CHECK}</i>One-on-one at the heart</span>
      <span class="chip"><i style="background:var(--sky)">{CHECK}</i>No autism diagnosis needed to start in Colorado</span>
      <span class="chip"><i style="background:var(--coral)">{CHECK}</i>$0 for authorized care on Medicaid</span>
      <span class="chip"><i style="background:var(--sun-deep)">{CHECK}</i>Parent coaching built in</span>
    </div>
  </div>
  {HILLS}
</section>

<section class="sec tight"><div class="wrap stack g28">
  {head("Where would you like to start?", "How can we help?")}
  <div class="grid c3">{door_html}</div>
</div></section>

<section class="sec band b-sky"><div class="wrap split" style="align-items:center">
  <div class="stack g14">
    <span class="hand">What we do</span>
    <h2>Therapy that happens where your child’s day happens</h2>
    <p class="muted">In Colorado, that’s usually your home — plus daycare, school and community outings when your child’s plan calls for it. In Tulsa, it’s our center, with a whole team on site, and nearby homes too. Around Ada, it’s your home. We pick the setting because it’s where the skill needs to work, not because it’s convenient for us.</p>
    <p class="muted">Behind every child: an assessment you can actually read, a technician who stays with your family, a BCBA who truly supervises, and an admin team whose whole job is keeping authorizations, schedules and claims off your plate.</p>
    <div>{go("#/services", "See all eight services")}</div>
  </div>
  <div class="grid c2" style="gap:14px">{tiles}</div>
</div></section>

<section class="sec"><div class="wrap stack g40">
  {head("The path to your first session", "Five steps, and we’ll walk every one with you", "Most families find us somewhere in the middle of this path. Wherever you are, the next step is the same: give us a call or send the form.")}
  {trail()}
  <div class="cta-row">{btn("#/families#start", "Start intake")}<span class="muted small">or call Colorado {CO_TEL} · Oklahoma {OK_TEL}</span></div>
</div></section>

<section class="sec band b-meadow"><div class="wrap split" style="align-items:center">
  <div class="stack g20">
    {head("How you’ll know it’s working", "We watch the little wins add up", "Your technician records data during every session, and your BCBA reviews it every week. When a program isn’t moving, we change it within weeks — not at the next six-month review. Ask to see the graphs anytime. We love that question.", hand_cls="meadow")}
    <div class="card soft stack g10" style="border-color:transparent">
      <h3>Why you won’t find parent reviews here</h3>
      <p class="small muted">Your child’s progress is private, and it belongs to your family — not our marketing. Instead, we’ll introduce you to the BCBA who would supervise your child, walk you through how progress is tracked, and give you a straight answer about whether we can staff your ZIP code.</p>
      <p class="small muted">Want to talk with another family? Just ask. We’ll reach out to them, with their permission and on their terms.</p>
    </div>
  </div>
  {chart()}
</div></section>

<section class="sec"><div class="wrap stack g28">
  {head("What we believe", "Five questions we keep asking ourselves", "These aren’t posters on a wall. They’re the questions our supervisors ask about every child — and ones you’re always welcome to ask us, too.")}
  <div class="grid c3">{values}
    <div class="card" style="border-style:dashed;box-shadow:none;background:transparent">
      <span class="k">And when the answer is no?</span>
      <p class="muted">Something changes — the program, the schedule, the technician, or the way we’re communicating with you. That’s what makes a value real.</p>
      <div style="margin-top:auto">{go("#/about", "How we work")}</div>
    </div>
  </div>
</div></section>

<section class="sec band b-sky"><div class="wrap stack g28">
  {head("Where we work", "Five communities, two states, one standard of care")}
  <div class="grid c5">{locs}</div>
  <div class="note" style="display:grid;grid-template-columns:auto minmax(0,1fr);gap:16px;align-items:start">{ico("i-seed")}<p><strong>Coming next: North Carolina.</strong> We’re working on opening in more states, starting with North Carolina, and we choose new places based on where families struggle to find care — not where it’s easiest for us. If you can’t find an ABA provider where you live, or you’re a clinician who’d love to build a team somewhere new, we’d really like to hear from you.</p></div>
</div></section>

<section class="sec"><div class="wrap split">
  <div class="stack g14">
    <span class="hand meadow">Working here</span>
    <h2>A job where you’re supported, too</h2>
    <p class="muted">In Colorado, our full-time in-home technicians are salaried, not hourly — so a family’s cancellation doesn’t shrink your paycheck, and billable hours above your base are paid on top. We group cases by ZIP code, reimburse mileage, and tell you on the very first call that drive time isn’t paid hourly, because you deserve to know that before an offer, not after. At our Tulsa center, technicians are hourly and work set shifts alongside the team on site.</p>
    <div class="pills"><span class="pill">Denver metro</span><span class="pill">Grand Junction</span><span class="pill">Tulsa</span><span class="pill">BCBA roles</span></div>
    <div>{btn("#/careers", "See open roles", "secondary")}</div>
  </div>
  <div class="grid" style="gap:14px">{ben}</div>
</div></section>

<section class="sec band b-meadow"><div class="wrap stack g28">
  {head("Questions parents ask", "Good questions, honest answers", hand_cls="meadow")}
  {faqs(FAQ_CORE)}
  <div>{go("#/families#faq", "More questions")}</div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="cta">
    <div class="stack g20">
      <span class="hand">One call is all it takes</span>
      <h2 style="max-width:20ch">Tell us about your child. We’ll be honest about what comes next.</h2>
      <div class="cta-row">{btn("#/families#start", "Start intake")}{btn("tel:+17204328989", "Colorado (720) 432-8989", "secondary", arrow=False)}{btn("tel:+19187648544", "Oklahoma (918) 764-8544", "secondary", arrow=False)}</div>
    </div>
    <svg class="kite-art" viewBox="0 0 120 220" aria-hidden="true" focusable="false"><use href="#kitesym"/></svg>
  </div>
</div></section>
</div>'''

def families():
    return f'''<div data-route="families" data-title="Getting started | Adventure Child Therapy" hidden>
{phead("For families", "Getting started", "Every family finds us from a different place — a new diagnosis, a school that’s run out of ideas, a waitlist somewhere else that never moved. Wherever you’re coming from, you’re in the right place. Here’s exactly what happens between your first call and your first session.",
  [("#/families#route","The five steps"),("#/families#requirements","What you need to start"),("#/families#insurance","Insurance &amp; cost"),("#/families#expect","Teamwork"),("#/families#faq","Questions"),("#/families#start","Start intake")])}

<section class="sec" id="route"><div class="wrap">{trail()}</div></section>

<section class="sec band b-sky" id="requirements"><div class="wrap stack g28">
  {head("Before therapy starts", "What’s needed on file depends on your state", "This is the part families most often get mixed messages about, so here it is, simply.")}
  <div class="grid c2">
    <div class="card">{mini("m-denver","Colorado mountains")}<span class="k">Colorado</span><h3>No autism diagnosis required</h3><p class="small muted">A letter from your child’s physician recommending ABA is enough to begin. If your child does have a diagnosis, please bring the report — it helps the assessment — but it isn’t a requirement.</p>{ticks(["A physician’s letter recommending ABA","Your insurance information","A caregiver who can be present for sessions and family guidance"])}</div>
    <div class="card">{mini("m-tulsa","Oklahoma prairie")}<span class="k">Oklahoma</span><h3>Diagnostic evaluation required</h3><p class="small muted">SoonerCare requires a diagnostic evaluation on file before ABA can begin. If you don’t have one yet, that’s a very normal place to start — we’ll share our referral list for evaluations and pick right back up when you have the report.</p>{ticks(["The diagnostic evaluation report","Your insurance information","Any prescription or order your plan requires"])}</div>
  </div>
  <p class="tiny">When we open in North Carolina, it will follow the Oklahoma pattern: a diagnostic evaluation on file first.</p>
</div></section>

<section class="sec" id="insurance"><div class="wrap stack g28">
  {head("Insurance and cost", "What this costs your family", "If your child is enrolled in Medicaid and services are authorized, ABA costs you nothing. With a commercial plan, we verify your benefits and tell you exactly what the plan said and when — no made-up estimates.")}
  <div class="grid c2">
    <div class="card"><span class="k">Colorado</span>{ticks(["Health First Colorado (Colorado Medicaid)","Commercial plans — benefits verified before we start"])}</div>
    <div class="card"><span class="k">Oklahoma</span>{ticks(["SoonerCare (Oklahoma Medicaid)","SoonerSelect plans: Aetna Better Health of Oklahoma, Blue Cross and Blue Shield of Oklahoma, Oklahoma Complete Health, Humana Healthy Horizons","Commercial plans — benefits verified before we start"])}</div>
  </div>
  <div class="callout"><strong>Coordination of benefits is required</strong> when care starts, once a year, and any time your insurance changes. Please let us know the day it changes — a lapsed authorization is the most common reason therapy pauses, and it’s completely preventable.</div>
  <p class="small muted measure">If ABA isn’t covered, or you’d rather not use insurance, services are private-pay and invoiced. We’ll always tell you before we begin, never after.</p>
</div></section>

<section class="sec band b-meadow" id="expect"><div class="wrap split">
  <div class="stack g14">
    <span class="hand meadow">Teamwork</span>
    <h2>How you can help it work</h2>
    <p class="muted">ABA works best when new skills keep going in the hours we’re not at your house. That takes teamwork, and we’d rather talk about it openly now so we’re all on the same page.</p>
  </div>
  <div class="card">{ticks([
    "<strong>At least two hours a month of family guidance.</strong> It’s a required part of ABA and your insurer expects it. It’s also where a lot of the lasting change comes from.",
    "<strong>Access and consistency.</strong> Sessions happen in your home on the schedule we build together. Frequent cancellations can quietly undo months of progress.",
    "<strong>A heads-up when plans change.</strong> Two weeks’ notice for planned vacations; same-day cancellations by 6:00 a.m., by call or text.",
    "<strong>Tell us when something isn’t working.</strong> A technician who isn’t the right fit, a goal that doesn’t matter to you, a time slot that’s become impossible — just say so. We’ll change it."])}</div>
</div></section>

<section class="sec" id="faq"><div class="wrap stack g28">
  {head("Questions", "The things families actually ask")}
  {faqs(FAQ_CORE + FAQ_MORE)}
</div></section>

<section class="sec tight" id="start"><div class="wrap">
  {intake_block("Start intake", f"This is the same information we’d collect on the phone. Someone from our team will call you back — forms never just sit in an inbox here. If you’d rather talk to a person right now, call Colorado {CO_TEL} or Oklahoma {OK_TEL}.")}
</div></section>
</div>'''

def services():
    anchors = [(f"#/services#{s[0]}", s[2]) for s in SERVICES]
    rows = "".join(f'''<article class="svc" id="{sid}" style="scroll-margin-top:100px">
    <div class="svc-head">{ico(ic,"ico lg")}<div><h2 style="font-size:clamp(1.6rem,2.8vw,2.15rem)">{name}</h2><p>{tag}</p></div></div>
    <div class="stack g14"><p class="muted measure">{body}</p>{ticks(items)}</div>
  </article>''' for sid, ic, name, short, tag, body, items in SERVICES)
    return f'''<div data-route="services" data-title="Services | Adventure Child Therapy" hidden>
{phead("Services", "How we help kids grow", "Eight ways we can help, one approach: get to know your child first, deliver one-on-one hours with a technician who stays with your family, and have a BCBA guide it all using real progress data instead of guesswork.", anchors)}
<section class="sec"><div class="wrap">{rows}</div></section>
<section class="sec tight"><div class="wrap">
  <div class="cta">
    <div class="stack g14">
      <span class="hand">Not sure what your child needs?</span>
      <h2 style="max-width:22ch">Most families aren’t — and that’s okay.</h2>
      <p class="muted measure">That’s what the assessment is for. You tell us what your days actually look like, the BCBA suggests goals, and you read them before anything is final.</p>
      <div>{btn("#/families#start", "Start intake")}</div>
    </div>
    <svg class="kite-art" viewBox="0 0 120 220" aria-hidden="true" focusable="false"><use href="#kitesym"/></svg>
  </div>
</div></section>
</div>'''

def aba():
    targets = ["Attending and engagement","Imitation","Fine and gross motor","Language and communication","Conversation","Functional play","Self-help and functional skills","Social skills","Perspective-taking","Toileting","Challenging behavior"]
    return f'''<div data-route="what-is-aba" data-title="What is ABA | Adventure Child Therapy" hidden>
{phead("What is ABA?", "ABA, explained simply", "No jargon and no sales pitch — just what the science is, what a session looks like, and what we think is honest to promise.")}
<section class="sec"><div class="wrap split">
  <div class="stack g20">
    <p class="lede" style="color:var(--ink)">ABA (applied behavior analysis) is the study of how behavior and the environment affect each other — what happens right before a behavior, what happens right after, and how changing those things can change what happens next.</p>
    <p class="muted">In practice, it looks like this: bigger skills are broken into small steps, taught in order, supported with just the right amount of help, and celebrated when they happen. We record data on every step, so progress is something you can see for yourself, not just something we tell you. When progress stalls, the program changes.</p>
    <p class="muted">The research is strongest for autism, and the same principles help children with other developmental disabilities too. ABA is a set of principles, not one fixed curriculum — anyone who tells you their program <em>is</em> ABA has it backwards.</p>
    <h3 style="margin-top:6px">What a program can work on</h3>
    <div class="pills">{"".join(f'<span class="pill">{t}</span>' for t in targets)}</div>
  </div>
  <div class="stack g20">
    <div class="card tint-sun stack g10">
      <span class="k">A session, step by step</span>
      {ticks(["A technician arrives at your home, daycare or our Tulsa center at the scheduled time.","They run the programs your BCBA wrote — mostly through play, motivation and everyday opportunities.","They take data as they go: what needed help, what your child did on their own, and what happened around any challenging behavior.","They tell you how it went before they leave.","Your BCBA reviews the data between sessions and adjusts the plan."])}
    </div>
    <div class="card tint-coral stack g10">
      <span class="k">Things we’ll never tell you</span>
      {ticks(["That ABA cures autism. It doesn’t, and that isn’t the goal.","That more hours are automatically better. Hours come from the assessment and the authorization.","That compliance is the point. A child who can ask, say no, and be understood is the point.","That progress is a straight line. It isn’t, and we’ll show you the wobbly weeks too."], "ticks x")}
    </div>
  </div>
</div></section>
<section class="sec band b-sky"><div class="wrap split">
  <div class="stack g14">
    <span class="hand sky">Ethics and oversight</span>
    <h2>Who is responsible for your child’s program</h2>
    <p class="muted">Programs are designed and supervised by a Board Certified Behavior Analyst (BCBA) practicing under the BACB’s ethics code, alongside the standards of ABAI and APBA. Technicians are certified — or actively working toward the RBT credential with our support — and every clinical team member is trained in Safety-Care (QBS) crisis procedures before working with a child.</p>
    <p class="muted">You can ask at any time who supervises your child’s program, when they last observed a session, and what the data says. Those aren’t special requests — they’re just good questions.</p>
  </div>
  <div class="stack g14">
    <div class="card stack g10">{ico("i-home")}<h3>Caregivers are part of the team</h3><p class="small muted">Your BCBA coaches you on building skills and on responding to challenging behavior, because consistency across people and places is what helps a skill stick. Insurance requires a minimum of two hours a month.</p></div>
    <div class="card stack g10">
      <span class="k">Where the data goes</span>
      {ticks(["<strong>Session data, captured live.</strong> Data is recorded during the session, not pieced together from memory afterward, and your BCBA reviews it between sessions.","<strong>Documentation and oversight.</strong> Notes, treatment plans and supervision records live in HIPAA-compliant clinical software, not in someone’s inbox.","<strong>Scheduling, authorizations and billing.</strong> Coverage, prior authorizations and claims run through secure systems our admin team watches closely, so lapses get caught before they interrupt therapy."])}
      <p class="tiny">All HIPAA-compliant. Ask us anything about how your child’s information is stored and who can see it.</p>
    </div>
  </div>
</div></section>
</div>'''

def locations():
    def row(lid, m, alt, st, name, intro, kind, contact, areas, zips=None, extra=""):
        zp = "".join('<span class="pill zip">' + x + '</span>' for x in (zips or []))
        z = f'<div class="stack g6"><span class="tiny">Primary ZIP coverage</span><div class="pills">{zp}</div></div>' if zips else ''
        ap = "".join('<span class="pill">' + a + '</span>' for a in areas)
        return f'''<article class="locrow" id="{lid}">
    <div class="stack g14"><span class="hand">{st}</span><h2>{name}</h2><p class="muted measure">{intro}</p>{extra}</div>
    <div class="card loc">{mini(m, alt)}<div class="loc-body" style="gap:12px"><span class="k">{kind}</span>{contact}
      <div class="stack g6"><span class="tiny">Areas served</span><div class="pills">{ap}</div></div>{z}
      <div>{btn("#/families#start", "Start intake here", extra="btn-sm", arrow=False)}</div></div></div>
  </article>'''
    co = f'<p class="addr">{CO_TEL}<br><a href="mailto:info@actaba.com">info@actaba.com</a></p>'
    rows = "".join([
      row("denver","m-denver","Mountains behind the Denver metro","Colorado","Denver metro","Our Denver care happens where your family lives. We group cases by ZIP code on purpose, so your technician spends the afternoon on your floor instead of on I-25 — and so the person who knows your child can keep working with them when schedules shift.","In-home, daycare, school and community",co,["Aurora","Westminster / Northglenn","Englewood","Castle Rock","Parker","SE Denver","Denver East"],["80011","80017","80108","80110","80138","80231","80234","80247"]),
      row("grand-junction","m-gj","Mesas of the Western Slope","Colorado","Grand Junction","On the Western Slope, ABA gets hard to find once you leave the Front Range. We staff Grand Junction as a real service area, with local technicians and BCBA supervision, and we hold the district clearances needed to work inside Mesa County Valley School District 51 and Caprock Academy.","In-home, daycare, school and community",co,["Grand Junction","Mesa County","Western Slope"]),
      row("pueblo","m-pueblo","A river valley in southern Colorado","Colorado","Pueblo","In-home care for families in and around Pueblo, with the same supervision model we use in Denver and Grand Junction.","In-home and community",co,["Pueblo","Southern Colorado"]),
      row("tulsa","m-tulsa","Our Tulsa center on the prairie","Oklahoma","Tulsa Center","Our Tulsa center is a purpose-built space for kids — room to move, a kitchen for feeding and mealtime work, and a whole team on site. Families send a lunch, a change of clothes and a water bottle; we take care of the rest. We also see Tulsa-area families in their homes.","Center-based and in-home",
          '<p class="addr">1217 East 48th Street, Suite 101<br>Tulsa, OK 74105</p><p class="addr"><a href="tel:+19187648544">(918) 764-8544</a><br><a href="mailto:tulsa@actaba.com">tulsa@actaba.com</a></p>',["Tulsa","Tulsa County"], extra='<div class="callout small">Same-day cancellations: call or text (918) 764-8544 by 6:00 a.m.</div>'),
      row("ada","m-ada","Rolling hills and oak trees around Ada, Oklahoma","Oklahoma","Ada","In-home ABA for families in and around Ada, with the same BCBA supervision and SoonerCare billing we use in Tulsa. Sessions happen in your home, where the skills need to work.","In-home",
          f'<p class="addr">{OK_TEL}<br><a href="mailto:info@actaba.com">info@actaba.com</a></p>',["Ada","Nearby communities"], extra='<div class="callout small">Same-day cancellations: call or text (918) 764-8544 by 6:00 a.m.</div>'),
    ])
    note = '<div class="note" style="max-width:62ch">In <strong>Colorado</strong>, ABA can begin with a letter from your child’s physician recommending it — no autism diagnosis required. In <strong>Oklahoma</strong>, a diagnostic evaluation needs to be on file first.</div>'
    return f'''<div data-route="locations" data-title="Locations | Adventure Child Therapy" hidden>
{phead("Locations", "Where we work", "In-home and community care across Colorado, a center in Tulsa, in-home care around Ada, and an honest answer about the places we can’t reach yet.", extra=note)}
<section class="sec"><div class="wrap stack" style="gap:clamp(48px,7vw,84px)">{rows}</div></section>
<section class="sec band b-meadow" id="expanding"><div class="wrap split">
  <div class="stack g14">
    <span class="hand meadow">Growing</span>
    <h2>Where we’re headed</h2>
    <p class="muted measure">We’re working on opening in more states, starting with North Carolina, and we choose new places based on where families struggle to find care — not where it’s easiest for us. If you can’t find an ABA provider where you live, or you’re a clinician who’d love to build a team somewhere new, we’d really like to hear from you.</p>
    <div class="pills"><span class="pill">North Carolina</span><span class="pill">More Colorado and Oklahoma communities</span></div>
  </div>
  <div class="card stack g14">
    <h3>Not in one of our areas?</h3>
    <p class="muted small">Please send the form anyway. We keep a list of families in places we don’t staff yet, and it helps decide where we go next. If we can’t help you right now, we’ll tell you kindly and clearly, rather than leaving you on a waitlist that goes nowhere.</p>
    <div>{btn("#/families#start", "Tell us where you are", "secondary", "btn-sm", arrow=False)}</div>
  </div>
</div></section>
</div>'''

def about():
    vals = "".join(f'<div class="stack g6" style="display:grid;grid-template-columns:auto minmax(0,1fr);gap:14px;align-items:start">{ico(ic)}<div class="stack g6"><h4>{t}</h4><p class="small muted" style="font-family:var(--f-display);font-size:1.06rem;line-height:1.35">{q}</p></div></div>' for t, q, tint, ic in VALUES)
    treat = [("Show up authentically","Real people, real conversations. We’d rather tell you what we don’t know yet than pretend to be certain."),
             ("Put humanities first","Your child is a person before they’re a case. So are you, and so is the technician sitting on your floor."),
             ("Provide holistic care","We work on the skills that change a family’s day — sleeping, eating, toileting, playing, asking for help — not just the ones that look good on a graph."),
             ("Grow a culture of inclusion and support","The care a child receives can only be as good as the way we treat the people giving it.")]
    treat_html = "".join(f'<div class="stack g6"><h4>{t}</h4><p class="small muted">{d}</p></div>' for t, d in treat)
    return f'''<div data-route="about" data-title="About | Adventure Child Therapy" hidden>
{phead("About us", "Nice to meet you", "Adventure Child Therapy was founded in 2021 with a simple idea: families should be able to reach the person responsible for their child’s program — and that person should be happy to show their work.")}
<section class="sec"><div class="wrap split">
  <div class="stack g14">
    <h2>Why “Adventure”?</h2>
    <p class="muted">Because that’s what this is. Growing through behavioral challenges comes with highs, lows and unexpected turns, and families rarely get to choose when the journey starts. Our job is to be the guide who’s walked this trail before — cheering for the wins that might look small from the outside, and staying right beside you when a month is hard.</p>
    <p class="muted">Staying small is a choice, not a phase we’re trying to outgrow. It’s what lets the clinician who assessed your child still know their name, and their favorite toy, a year later.</p>
    <h2 style="margin-top:18px">What makes us different</h2>
    {ticks(["<strong>Clinician-led.</strong> Clinical decisions are made by the BCBA on your child’s case, not by a scheduling target.","<strong>Progress you can see.</strong> Data from every session is recorded as it happens and reviewed by the supervising BCBA between sessions.","<strong>An admin team that handles the paperwork.</strong> Authorizations, scheduling and claims are our job, not yours.","<strong>Fun is part of the plan.</strong> Kids learn best when they want to be there, so we build sessions your child looks forward to.","<strong>Spanish-language materials and staff.</strong> Our caregiver handbook and intake paperwork are available in Spanish."])}
  </div>
  <div class="stack g20">
    <div class="card tint-sun stack g14"><span class="k">Our clinical values</span>{vals}</div>
    <div class="card stack g14"><span class="k">How we treat each other</span>{treat_html}</div>
    <div class="card stack g10">{ico("i-shield")}<h4>Training and safety</h4><p class="small muted">Clinical staff complete Safety-Care (QBS) training before working with a child, and recertify on schedule. Physical management is a last resort with three conditions — imminent risk of serious harm, greater risk in not acting, and no other practical way to prevent it — and it’s documented every time.</p></div>
  </div>
</div></section>
<section class="sec band b-sky"><div class="wrap stack g28">
  {head("How we measure ourselves", "Four pillars — and none of them is billable hours", "Clinician success at ACT is defined across four pillars. A clinic that only counts hours ends up losing sight of all of them.", hand_cls="sky")}
  {pillars()}
</div></section>
<section class="sec"><div class="wrap stack g28">
  {head("Behind the scenes", "The systems that make sure nothing gets lost")}
  <div class="grid c3">
    <div class="card">{ico("i-star")}<h4>Session data, captured live</h4><p class="small muted">Data is recorded during the session, not pieced together from memory afterward, and your BCBA reviews it between sessions.</p></div>
    <div class="card">{ico("i-letter")}<h4>Documentation and oversight</h4><p class="small muted">Notes, treatment plans and supervision records live in HIPAA-compliant clinical software, not in someone’s inbox.</p></div>
    <div class="card">{ico("i-shield")}<h4>Scheduling, authorizations and billing</h4><p class="small muted">Coverage, prior authorizations and claims run through secure systems our admin team watches closely, so lapses get caught before they interrupt therapy.</p></div>
  </div>
  <p class="small muted measure">Everything we use is HIPAA-compliant. If you’d like to know how your child’s information is stored, who can see it, or how to get a copy, just ask — we’ll answer specifically, and in writing if you prefer.</p>
</div></section>
<section class="sec tight"><div class="wrap">
  <div class="cta">
    <div class="stack g20"><span class="hand">Two ways to join the adventure</span><h2 style="max-width:20ch">Bring us your child, or come build this with us.</h2>
    <div class="cta-row">{btn("#/families#start","Start intake")}{btn("#/careers","Open roles","secondary",arrow=False)}</div></div>
    <svg class="kite-art" viewBox="0 0 120 220" aria-hidden="true" focusable="false"><use href="#kitesym"/></svg>
  </div>
</div></section>
</div>'''

def contact():
    return f'''<div data-route="contact" data-title="Contact | Adventure Child Therapy" hidden>
{phead("Contact", "Come say hello", "Our admin team answers the phones during business hours. If you reach voicemail, leave your name and number — we return calls the same business day.")}
<section class="sec tight"><div class="wrap stack g20">
  <div class="grid c3">
    <div class="card tint-sun">{ico("i-talk")}<span class="k">Colorado</span><h3><a href="tel:+17204328989">(720) 432-8989</a></h3><p class="small muted">New families, scheduling, authorizations and billing questions.</p></div>
    <div class="card tint-coral">{ico("i-talk")}<span class="k">Oklahoma</span><h3><a href="tel:+19187648544">(918) 764-8544</a></h3><p class="small muted">New families, scheduling, authorizations and billing questions.</p></div>
    <div class="card tint-sky">{ico("i-letter")}<span class="k">Email</span><h3><a href="mailto:info@actaba.com">info@actaba.com</a></h3><p class="small muted">General questions. Please don’t email clinical details or records — we’ll send you a secure link.</p></div>
  </div>
  <div class="grid c3">
    <div class="card"><span class="k">Tulsa center</span><p class="addr">1217 East 48th Street, Suite 101<br>Tulsa, OK 74105</p><p class="addr"><a href="tel:+19187648544">(918) 764-8544</a><br><a href="mailto:tulsa@actaba.com">tulsa@actaba.com</a></p></div>
    <div class="card"><span class="k">Fax</span><h3 class="tnum">888-910-5088</h3><p class="small muted">Referrals, records and authorization paperwork.</p></div>
    <div class="card"><span class="k">Need to cancel a session?</span><p class="small muted">Same-day cancellations should reach us by <strong>6:00 a.m.</strong> — call or text your location’s number. For planned time off, two weeks’ notice helps us protect your spot and your technician’s schedule.</p></div>
  </div>
</div></section>
<section class="sec"><div class="wrap">
  {intake_block("Or start intake here", "If you’re reaching out about starting services, this form saves you a phone call — it asks for the same information we would.")}
</div></section>
</div>'''
