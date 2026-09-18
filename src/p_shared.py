from p_art import ico, mini

CO_TEL = '<a href="tel:+17204328989">(720) 432-8989</a>'
NC_TEL = CO_TEL  # North Carolina families call the main line
OK_TEL = '<a href="tel:+19187648544">(918) 764-8544</a>'
ARROW = '<span class="arrow" aria-hidden="true">&rarr;</span>'
TIP = '<svg aria-hidden="true" focusable="false"><use href="#leaf"/></svg>'

def btn(href, label, kind="primary", extra="", arrow=True):
    return f'<a class="btn btn-{kind}{(" "+extra) if extra else ""}" href="{href}">{label}{(" "+ARROW) if arrow else ""}</a>'

def go(href, label, cls=""):
    return f'<a class="go {cls}" href="{href}">{label} {ARROW}</a>'

def ticks(items, cls="ticks"):
    return f'<ul class="{cls}">' + "".join(f"<li><span>{i}</span></li>" for i in items) + "</ul>"

def head(label, title, lede=None, hand_cls="", tag="h2", lede_cls="lede measure"):
    out = f'<div class="stack g14"><span class="hand {hand_cls}">{label}</span><{tag}>{title}</{tag}>'
    if lede: out += f'<p class="{lede_cls}">{lede}</p>'
    return out + "</div>"

STEPS = [
  ("About 10 minutes", "Tell us about your child",
   "One call or one form. We’ll ask for your child’s name and date of birth, a good callback number, your insurance carrier and member ID, whether there’s a diagnosis and who made it, how you heard about us, and the days and times that realistically work for sessions.",
   "We won’t guess at a start date on that first call. As soon as we know, you’ll know.", "pin"),
  ("Depends on your state", "Gather what we need on file",
   "In Colorado, your child doesn’t need an autism diagnosis to begin — a letter from your child’s physician recommending ABA is enough, and we’ll tell you exactly what it should say. In Oklahoma and North Carolina, a diagnostic evaluation needs to be on file before ABA can start. Don’t have the paperwork yet? We’ll share our referral list and hold on to your information, so you never have to start over.",
   "No diagnosis yet isn’t a dead end anywhere — and in Colorado, you may not need one at all.", "pin-sky"),
  ("Days to weeks", "Benefits and authorization",
   "We check your coverage and request authorization for you. With Health First Colorado, SoonerCare or NC Medicaid, authorized services cost your family nothing. With a commercial plan, we’ll share exactly what we verified and on what date — we’ll never make up a number just to fill a silence.",
   "Coordination of benefits is needed when care starts, once a year, and any time your insurance changes.", "pin-meadow"),
  ("Usually 2–4 sessions", "Assessment",
   "A BCBA spends time with your child and with you, completes a skills assessment, and writes the treatment plan and hours request. You’ll read the goals before anything is final.",
   None, "pin-coral"),
  ("Ongoing", "Sessions begin!",
   "We match your technician on availability, location and continuity — the same friendly face at the same times, whenever we can make it happen. Family guidance goes on the calendar from day one, not as an afterthought.",
   "Two hours of family guidance each month is the minimum, and your insurer requires it.", "flag"),
]

def trail(note=True):
    out = ['<ol class="trail">']
    for i, (when, title, body, tip, pin) in enumerate(STEPS, 1):
        mark = f'<b class="tnum">{i}</b>' if pin != "flag" else '<span class="sr">5</span>'
        n = ''
        if i == 1 and note:
            n = '<span class="hand-note hand" aria-hidden="true">Most families start right here! <svg style="transform:scaleX(-1) rotate(20deg)"><use href="#squiggle"/></svg></span>'
        tip_html = f'<p class="tip">{TIP}<span>{tip}</span></p>' if tip else ''
        out.append(f'''<li class="stop"><span class="marker"><svg aria-hidden="true" focusable="false"><use href="#{pin}"/></svg>{mark}</span>
  <div class="stop-body" style="position:relative">{n}<span class="when">{when}</span><h3>{title}</h3><p class="muted measure">{body}</p>{tip_html}</div></li>''')
    out.append('</ol>')
    return "\n".join(out)

FAQ_CORE = [
  ("Do we need an autism diagnosis before we call?",
   "Not in Colorado. A letter from your child’s physician recommending ABA is enough to begin — no autism diagnosis required. In Oklahoma and North Carolina, a diagnostic evaluation does need to be on file before ABA can start. Either way, please call: if you need an evaluation or a physician letter, we’ll tell you exactly what to ask for and share our referral list."),
  ("What will this cost us?",
   "If your child is enrolled in Health First Colorado, SoonerCare or NC Medicaid, there’s no cost to you for authorized services. If you have a commercial plan, we verify your benefits and tell you exactly what the plan said and when we checked. We won’t guess at a number just to have one to say."),
  ("Where do sessions happen?",
   "In Colorado, almost always in your home — and in daycare, school or community settings when your child’s plan calls for it. In Tulsa, we have a center at 1217 East 48th Street, and we also see families in their homes. Around Ada, sessions happen in your home. In North Carolina, around Charlotte and Thomasville, sessions happen in your home and community."),
  ("How many hours will my child get?",
   "That comes from the assessment and the authorization, not from a phone call. Hours are recommended by the BCBA who assessed your child and approved by your plan."),
  ("How long is the wait?",
   "It depends on your area, your availability, and staffing in your ZIP code. We don’t hand out a position number or a start date we can’t stand behind — when we have a real answer, we’ll call you with it."),
]
FAQ_MORE = [
  ("Do you offer services in Spanish?",
   "Yes. Our caregiver handbook and intake paperwork are available in Spanish, and we staff Spanish-speaking team members wherever we can. Just let us know at intake so we can plan for it."),
  ("What’s expected of us as parents?",
   "At least two hours a month of family guidance, access to your home for sessions, and honesty with us when something isn’t working. Consistency across people and places is what helps new skills stick."),
  ("What if we need to cancel a session?",
   "Life happens! Give us as much notice as you can, and at least two weeks for planned vacations. Same-day cancellations should reach us by 6:00 a.m. by call or text, so we can rework your technician’s day."),
  ("Who actually works with my child?",
   "A behavior technician or RBT runs the sessions, supervised by the BCBA who wrote the plan. Our technicians are trained in Safety-Care (QBS) crisis procedures and are certified or actively working toward certification."),
  ("Why don’t you post parent reviews?",
   "Because your child’s progress is private, and it belongs to your family — not our marketing page. Instead, ask us to walk you through the data on a program. We’re always happy to show you."),
]

def faqs(items):
    return '<div class="faqs">' + "".join(f'<details class="faq"><summary>{q}</summary><div class="a">{a}</div></details>' for q, a in items) + '</div>'

SERVICES = [
  ("assessment", "i-assess", "Assessment", "Getting to know your child as a whole person, not a score.",
   "Getting to know your child — not a score.",
   "A BCBA spends time with your child and with you: watching play and routines, completing a structured skills assessment, and having a real conversation about what a hard day looks like at your house. What comes out is a treatment plan with goals you recognize, written in words you can actually read, plus the hours request we send to your insurer.",
   ["Observation in the place where therapy will happen", "Skills assessment across communication, play, self-help and social skills", "A function-based look at challenging behavior", "A caregiver interview about your priorities, routines and the goals that matter to you", "A written plan and an authorization request to your plan"]),
  ("therapy", "i-blocks", "1:1 therapy", "Playful, focused one-on-one time where the learning happens.",
   "The playful, one-on-one hours where learning happens.",
   "One technician, one child, and a plan written by the BCBA who assessed them. Sessions happen where the skill needs to work — your living room, the daycare classroom, the playroom floor in Tulsa. Data is collected every session and reviewed by the supervising BCBA, so a program that isn’t moving gets changed in weeks, not months.",
   ["An RBT or behavior technician working 1:1 with your child", "Ongoing BCBA supervision and program updates", "Session-by-session progress you can see", "Learning through play and everyday moments, alongside structured practice"]),
  ("family-guidance", "i-home", "Family guidance", "At least two hours a month of coaching for the grown-ups — often the most helpful time of all.",
   "Coaching for the grown-ups — two hours a month, minimum.",
   "Caregiver training is a required part of ABA, and insurers ask for at least two hours a month for a good reason: strategies only stick when they work in the hours we’re not there. Your BCBA helps with the specific moments that tend to go sideways — bath time, the car seat, the grocery store — and practices them with you, instead of handing you a worksheet.",
   ["Scheduled time with your BCBA, not a quick chat at the door", "Practice during your real routines", "Written summaries of what to try and what to expect", "Progress reviewed together, in plain language"]),
  ("toilet-training", "i-star", "Toilet training", "A step-by-step plan, a plan for setbacks, and someone to call.",
   "A step-by-step plan — and someone to call.",
   "Potty training is the goal families ask us about most, and it’s where generic advice falls short fastest. We build a plan around your child’s current skills, schedule the intensive stretch thoughtfully, and prepare you for the tricky week that often comes right before it clicks.",
   ["A readiness check before we start", "A written plan every adult in the house can follow", "Daycare and school coordination, so the plan doesn’t stop at the front door", "A plan for setbacks, written before they happen"]),
  ("feeding", "i-bowl", "Feeding and mealtimes", "For families whose child sticks to a very short list of foods.",
   "For kids who stick to a very short list of foods.",
   "Gentle, gradual work on trying new foods, mealtime routines, and the big feelings that can make dinner the hardest hour of the day. We coordinate with your child’s medical team and stay in our lane — behavioral feeding support, not medical or swallowing treatment.",
   ["A look at the foods your child accepts today and your mealtime patterns", "Gradual, consent-respecting steps toward new foods", "Mealtime routines the whole family can keep", "Referral and coordination when a medical or feeding-therapy evaluation should come first"]),
  ("social", "i-talk", "Social and communication skills", "Being understood, and getting to be a kid with other kids.",
   "Being understood — and getting to be a kid with other kids.",
   "Communication comes first: a reliable way for your child to ask, say no, and be understood — whether that’s words, a device, or signs. Then the fun, harder social stuff: joining play, taking turns, and handling the moment a friend says no.",
   ["Functional communication training", "Play and friendship skills in real settings", "Support for AAC use alongside your child’s speech-language provider", "Sibling and peer coaching where it helps", "Small social groups when your child is ready to practice with peers"]),
  ("daily-living", "i-shirt", "Daily living skills", "Getting dressed, brushing teeth, bedtime — independence, one routine at a time.",
   "Independence, one routine at a time.",
   "Getting dressed, brushing teeth, bedtime routines, staying safe, waiting, and moving from one activity to the next. The everyday list that decides whether a Saturday outing feels possible.",
   ["Step-by-step routines built for your household", "Safety skills — wandering, roads, water — prioritized when they matter", "Practice with transitions and waiting", "Skills handed over to caregivers on purpose, not left with the technician"]),
  ("school", "i-pack", "School and daycare support", "We show up where your child already spends the day.",
   "We show up where your child already spends the day.",
   "With the school’s agreement and the right clearances, our technicians work alongside teachers and daycare staff. We’ll join IEP meetings when you want us there, and we bring the data, not just opinions.",
   ["Daycare and community sessions when the plan calls for it", "District clearance and background checks completed before a technician steps into a building", "Teamwork with teachers and special-education staff", "Good to know: Medicaid doesn’t reimburse ABA in a school setting except for a limited time during a transition — we’ll always tell you plainly what is and isn’t covered"]),
]

VALUES = [
  ("Exceptional Clinical Care", "Are we doing excellent behavior analysis?", "tint-sun", "i-star"),
  ("Understand, Don’t Judge", "Are we approaching people behaviorally, compassionately, and with dignity?", "tint-coral", "i-heart"),
  ("Build Bigger Lives", "Are we improving what actually matters in the child’s life?", "tint-meadow", "i-seed"),
  ("Make It Work in the Real World", "Does treatment actually work across the environments where the child’s life occurs?", "tint-sky", "i-home"),
  ("Collaborate & Be Transparent", "Are we working openly and effectively with families, schools/daycares, external partners, and one another?", "tint-lilac", "i-talk"),
]

PILLARS = [
  ("Client Outcomes", "Meaningful, data-driven progress through evidence-based care.", "i-seed"),
  ("Behavior Technician Support", "Technicians feel trained, supported, and confident.", "i-shield"),
  ("Parent Access", "Families experience collaboration, responsiveness, and trust with experts.", "i-home"),
  ("Clinician Satisfaction", "Work is sustainable, rewarding, and aligned with your expertise.", "i-heart"),
]
def pillars():
    return '<div class="grid c4">' + "".join(f'<div class="card">{ico(ic)}<h3>{t}</h3><p class="small muted">{d}</p></div>' for t, d, ic in PILLARS) + '</div>'

BENEFITS = [
  ("Paid time off and paid sick time", "Accrued, and actually usable."),
  ("Paid training", "Including Safety-Care (QBS) crisis-procedure certification."),
  ("Certification reimbursement", "We reimburse RBT, BCaBA and BCBA exam costs."),
  ("Mileage reimbursement", "For Colorado in-home roles. Drive time isn’t paid hourly, and we tell you that on the first screening call rather than at the offer."),
  ("Professional development", "CEU support and a clear path from BT to RBT to Lead RBT to full-time and beyond."),
  ("Schedules that fit the setting", "In Colorado, we build in-home schedules from your availability, with a target commute of 30 minutes or less. At our Tulsa center, you work set shifts with the team on site."),
]

LOCS = [
  ("denver", "m-denver", "Colorado", "Denver metro", "In-home, daycare, school and community", None, "Mountains behind the Denver metro"),
  ("grand-junction", "m-gj", "Colorado", "Grand Junction", "In-home, daycare, school and community", None, "Mesas of the Western Slope"),
  ("pueblo", "m-pueblo", "Colorado", "Pueblo", "In-home and community", None, "A river valley in southern Colorado"),
  ("tulsa", "m-tulsa", "Oklahoma", "Tulsa Center", "Center-based and in-home", "1217 East 48th Street, Suite 101<br>Tulsa, OK 74105", "Our Tulsa center on the prairie"),
  ("ada", "m-ada", "Oklahoma", "Ada", "In-home", None, "Rolling hills and oak trees around Ada, Oklahoma"),
  ("charlotte", "m-charlotte", "North Carolina", "Charlotte", "In-home and community", None, "The Charlotte skyline above leafy Piedmont hills"),
  ("thomasville", "m-thomasville", "North Carolina", "Thomasville", "In-home and community", None, "Thomasville’s Big Chair among rolling North Carolina hills"),
]

def field(inst, name, label, kind="input", typ="text", required=False, auto=None, options=None, placeholder="", hint=None, rows=4):
    fid = f"{inst}__{name}"
    req = ' <span class="req" aria-hidden="true">*</span>' if required else ''
    ra = ' required aria-required="true"' if required else ''
    ac = f' autocomplete="{auto}"' if auto else ''
    h = f'<span class="hint" id="{fid}-hint">{hint}</span>' if hint else ''
    db = f' aria-describedby="{fid}-hint"' if hint else ''
    if kind == "select":
        opts = '<option value="">Choose one</option>' + "".join(f'<option value="{o}">{o}</option>' for o in options)
        ctl = f'<select id="{fid}" name="{name}"{ra}{db}>{opts}</select>'
    elif kind == "textarea":
        ctl = f'<textarea id="{fid}" name="{name}" rows="{rows}"{ra}{db} placeholder="{placeholder}"></textarea>'
    else:
        ctl = f'<input id="{fid}" name="{name}" type="{typ}"{ra}{ac}{db} placeholder="{placeholder}">'
    return f'<div class="field"><label for="{fid}">{label}{req}</label>{h}{ctl}<span class="err" id="{fid}-err"></span></div>'

def consent(inst):
    return f'''<div class="hp" aria-hidden="true"><label>Leave this empty<input type="text" name="company" tabindex="-1" autocomplete="off"></label></div>
      <div class="checkrow"><input type="checkbox" id="{inst}-consent" name="consent" required><label for="{inst}-consent">I understand this form isn’t a secure medical record, so I won’t include clinical details or documents here. Someone from ACT will reach out to collect anything sensitive securely. <span class="req" aria-hidden="true">*</span></label></div>
      <span class="err" id="{inst}-consent-err"></span>'''

def intake_block(title, lede):
    return f'''<div class="panel stack g20">
  <div class="stack g10"><span class="hand">Step one</span><h2>{title}</h2><p class="muted measure">{lede}</p></div>
  <div class="card intake-card stack g14">
    <span class="k">Preview only</span>
    <p class="muted measure">On the live site, the ACT ABA intake form sits right here. This review preview blocks third-party forms from loading, so it opens in a new tab instead.</p>
    {btn("https://form.jotform.com/231875318826061", "Open the intake form").replace('href=', 'target="_blank" rel="noopener" href=')}
  </div>
  <p class="tiny">Rather talk to a person? Call Colorado &amp; North Carolina {CO_TEL} or Oklahoma {OK_TEL}.</p>
</div>'''
