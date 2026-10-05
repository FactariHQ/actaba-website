"""New-family guide: five short reads for families who have just reached out.

GUIDES is the single source of truth. render_page() turns a guide into a site page;
to_markdown() turns the same data into the editable team copy.

Block kinds inside a section:
  ("p", html)                     paragraph
  ("ticks", [html, ...])          check list
  ("x", [html, ...])              "never" list
  ("pills", [text, ...])          tag cloud
  ("cards", [(kicker, title, body_html, tint, icon), ...])
  ("steps", [(label, title, body_html), ...])   numbered walk-through
  ("faq", [(q, a_html), ...])
  ("note", html)                  green reassurance box
  ("callout", html)               coral heads-up box
  ("chart", None)                 the illustrative progress chart
"""
import re
from p_art import ico, strip
from p_shared import CO_TEL, OK_TEL, NC_TEL, ARROW, ticks, btn

PHONES = f"Colorado {CO_TEL} · Oklahoma {OK_TEL} · North Carolina {NC_TEL}"

GUIDES = [
# ---------------------------------------------------------------- 1
{"slug": "what-is-aba", "n": 1, "nav": "What is ABA?", "read": "3-minute read", "icon": "i-seed", "tint": "tint-meadow",
 "title": "What is ABA?",
 "card": "The science in plain words, what it can help with, and what good ABA should feel like for your child.",
 "lede": "You don’t need to know any of this before you start — your team will explain things as you go. But if you’re the kind of parent who likes to understand what you’re signing up for, this is for you.",
 "short": [
   "ABA (applied behavior analysis) is a way of teaching that looks closely at what helps your child learn — and what gets in the way.",
   "Big skills get broken into small, doable steps, practiced mostly through play and everyday routines.",
   "We measure progress every session, so you can see what’s working — and we change what isn’t.",
 ],
 "sections": [
  {"id": "idea", "hand": "The idea in one minute", "title": "Before, during, after",
   "intro": "ABA looks at three simple things: what happens right <em>before</em> a behavior, the behavior itself, and what happens right <em>after</em>. Small changes to the before and after can change what happens next time.",
   "blocks": [
     ("cards", [
       ("An example", "Snack time is hard", "Your child screams when they want crackers. Screaming works — eventually, the crackers arrive. So screaming keeps happening.", "tint-coral", "i-talk"),
       ("What we do", "Teach a faster, easier way", "We teach a quicker way to ask — a word, a sign, a picture or a device — and make sure it works <em>better</em> than screaming ever did.", "tint-sky", "i-blocks"),
       ("What changes", "Asking replaces screaming", "Over time, asking becomes the easy choice. Nobody had to punish anything; your child just learned something that works better.", "tint-meadow", "i-seed"),
     ]),
     ("p", "That’s ABA in a nutshell. The same idea is used to teach talking, playing, getting dressed, using the toilet, waiting, joining a game with other kids — and to make hard moments less frequent and less intense."),
   ]},
  {"id": "help", "hand": "What it can help with", "title": "The skills a program can work on", "band": "b-sky",
   "intro": "Every child’s plan is different. Goals come from the assessment and from what matters most to your family. Programs often include:",
   "blocks": [
     ("pills", ["Communication — asking, saying no, being understood", "Play and getting along with other kids", "Imitation and attention", "Getting dressed, brushing teeth, bedtime", "Toilet training", "Mealtimes and trying new foods", "Waiting and handling transitions", "Safety — wandering, roads, water", "Big feelings and challenging behavior", "Getting ready for daycare or school"]),
     ("p", "The research behind ABA is strongest for autism, and the same principles help children with other developmental differences too."),
   ]},
  {"id": "good", "hand": "What good ABA looks like", "title": "What you should see — and what you never should",
   "blocks": [
     ("cards", [
       ("You should see", "Play and motivation first", "Learning built around what your child loves. A lot of good ABA looks like play — that’s on purpose.", "tint-sun", "i-blocks"),
       ("You should see", "Communication over compliance", "A child who can ask, say no, and be understood is the point. Sitting still and following orders is not.", "tint-sky", "i-talk"),
       ("You should see", "Your priorities in the plan", "You read and agree to the goals before anything is final. If a goal doesn’t matter to your family, it comes out.", "tint-meadow", "i-home"),
       ("You should see", "Data you can actually read", "Progress you can see for yourself, in plain language — including the wobbly weeks.", "tint-lilac", "i-star"),
     ]),
     ("x", [
       "We’ll never tell you ABA cures autism. It doesn’t, and that isn’t the goal.",
       "We’ll never tell you more hours are automatically better. Hours come from the assessment and your child’s needs.",
       "We’ll never tell you progress is a straight line. It isn’t, and we’ll show you the hard weeks too.",
     ]),
   ]},
  {"id": "team", "hand": "Who’s who", "title": "The people on your child’s team", "band": "b-meadow",
   "blocks": [
     ("cards", [
       ("The planner", "BCBA", "A Board Certified Behavior Analyst assesses your child, writes the plan, trains the technician, checks the data and coaches you. This is your go-to person for questions.", "", "i-assess"),
       ("The day-to-day", "Behavior technician (RBT)", "Works one-on-one with your child during sessions, follows the BCBA’s plan, and records data as they go. Certified — or actively earning the RBT credential with our support.", "", "i-blocks"),
       ("The expert on your child", "You", "Nobody knows your child better. You help choose the goals, and you’re the one who helps new skills keep working when we’re not there.", "", "i-heart"),
     ]),
     ("p", "We’re also happy to coordinate with your child’s pediatrician, speech or occupational therapist, daycare or school team — with your permission."),
   ]},
  {"id": "worries", "hand": "Common worries", "title": "Questions parents ask us quietly",
   "blocks": [
     ("faq", [
       ("Will my child be made to sit at a table for hours?", "No. Some practice happens at a table, in short bursts, with plenty of breaks — but most learning happens through play and everyday routines, wherever the skill needs to work."),
       ("Will ABA change who my child is?", "It shouldn’t, and if it ever feels that way, please tell us. The goal is a bigger life for your child — more ways to communicate, play, and take part in things they enjoy — not a different child."),
       ("Is it okay that I have doubts about ABA?", "Completely. Ask us anything, including the hard questions. You can always ask what a goal is for, why we chose a strategy, and what the data says."),
       ("Is ABA only for autism?", "No. The research is strongest for autism, but the same principles help children with other developmental differences. In Colorado, your child doesn’t need an autism diagnosis to begin."),
     ]),
   ]},
 ]},
# ---------------------------------------------------------------- 2
{"slug": "how-it-works", "n": 2, "nav": "How it works", "read": "4-minute read", "icon": "i-letter", "tint": "tint-sky",
 "title": "How ABA works at ACT",
 "card": "The road from your first call to your first session — and what the months after that look like.",
 "lede": "There are a few steps between “we called” and “therapy started.” You don’t have to manage any of them alone — our team handles the paperwork with you and tells you what’s next at every stop.",
 "short": [
   "There are five stops: intake call, paperwork, insurance approval, assessment, and then sessions begin.",
   "Your BCBA reviews progress constantly and updates the plan — usually with a formal reassessment about every six months.",
   "The goal is for your family to need us <em>less</em> over time, not more.",
 ],
 "sections": [
  {"id": "road", "hand": "Getting started", "title": "Five stops to your first session",
   "blocks": [
     ("steps", [
       ("About 10 minutes", "Intake call or form", "We ask about your child, your insurance, and the days and times that realistically work. We won’t guess at a start date — as soon as we know, you’ll know."),
       ("Depends on your state", "Gather what’s needed on file", "<strong>Colorado:</strong> no autism diagnosis needed — a letter from your child’s physician recommending ABA is enough. <strong>Oklahoma and North Carolina:</strong> a diagnostic evaluation needs to be on file. No paperwork yet? We’ll share our referral list and hold on to your information so you never start over."),
       ("Days to weeks", "Insurance check and approval", "We verify your benefits and ask your insurer to approve the assessment. With Medicaid, authorized services cost your family nothing. With a commercial plan, we tell you exactly what the plan said — no made-up numbers."),
       ("Usually 2–4 visits", "Assessment", "A BCBA gets to know your child and you, then writes the treatment plan. You read the goals before anything is final. (Guide 4 walks through this.)"),
       ("Ongoing", "Sessions begin", "We match your technician on availability, location and continuity — the same friendly face at the same times whenever we can. Family guidance goes on the calendar from day one."),
     ]),
     ("note", "<strong>Waiting is the hardest part.</strong> Timelines depend on your insurer, your area and staffing near you. We won’t give you a date we can’t stand behind — but we will keep you updated, and you can always call to ask where things are."),
   ]},
  {"id": "hours", "hand": "How hours are decided", "title": "Where the number of hours comes from", "band": "b-sky",
   "intro": "The number of therapy hours isn’t picked on the phone. The BCBA who assessed your child recommends hours based on your child’s needs, goals and daily life — including school, daycare and family time — and your insurer approves them.",
   "blocks": [
     ("cards", [
       ("Often", "Focused programs", "Fewer hours a week, aimed at a handful of specific goals — like toilet training, mealtimes or a particular challenging behavior.", "", "i-star"),
       ("Sometimes", "Comprehensive programs", "More hours a week across many areas of development, usually for younger children who need support in lots of areas at once.", "", "i-blocks"),
     ]),
     ("p", "If the recommended hours don’t fit your family’s life, say so. The plan has to work in the real world — that’s one of our core values."),
   ]},
  {"id": "progress", "hand": "How progress is tracked", "title": "You’ll be able to see it, not just hear about it",
   "blocks": [
     ("split", [
       ("ticks", [
         "<strong>Every session:</strong> the technician records data as they go — what your child did independently, what needed help, and what happened around any hard moments.",
         "<strong>Between sessions:</strong> your BCBA reviews the data. If a program isn’t moving, it changes in weeks, not months.",
         "<strong>During family guidance:</strong> your BCBA walks you through progress in plain language. Ask to see the graphs any time.",
         "<strong>About every six months:</strong> a reassessment updates goals and the hours request, and your insurer reviews it again.",
       ]),
       ("chart", None),
     ]),
   ]},
  {"id": "later", "hand": "Down the road", "title": "Where this is all headed", "band": "b-meadow",
   "blocks": [
     ("p", "From the start, your child’s plan includes what “ready to step down” looks like. As skills grow, hours usually come down, more of the work shifts to you and the other people in your child’s life, and eventually your child graduates from ABA. We’ll plan that transition with you, not spring it on you."),
     ("ticks", [
       "Hours change as your child’s needs change — up or down.",
       "Goals get handed over to caregivers on purpose, so they keep working after we step back.",
       "Transitions — to preschool, kindergarten, a new classroom — get planned ahead.",
     ]),
   ]},
 ]},
# ---------------------------------------------------------------- 3
{"slug": "a-session", "n": 3, "nav": "A typical session", "read": "3-minute read", "icon": "i-blocks", "tint": "tint-sun",
 "title": "What a session looks like",
 "card": "The first few weeks, a sample session from hello to goodbye, and where you fit in.",
 "lede": "Most families are surprised by how much an ABA session looks like play. Here’s what to expect, so nothing on day one feels strange.",
 "short": [
   "The first few weeks are mostly about building trust between your child and their technician. That’s on purpose.",
   "Sessions mix play, short bursts of practice, breaks and everyday routines — wherever the skill needs to work.",
   "The technician collects data throughout the session and updates your child’s record. Your BCBA visits regularly to supervise and adjust.",
 ],
 "sections": [
  {"id": "first-weeks", "hand": "The first few weeks", "title": "First, we build trust",
   "intro": "Early sessions focus on <strong>pairing</strong>: the technician spends time doing your child’s favorite things, follows their lead, and asks very little. It can look like “just playing.” It’s actually the foundation for everything else — kids learn best from people they trust and enjoy.",
   "blocks": [
     ("note", "<strong>Good to know:</strong> it’s normal for a child to be shy, upset or unsure at first. Technicians are trained for this. Give it a few sessions, and tell us if it isn’t getting easier."),
   ]},
  {"id": "sample", "hand": "A sample session", "title": "From hello to goodbye", "band": "b-sky",
   "intro": "Every child’s session is different, and the length comes from your child’s plan. This is just a picture of how one might flow.",
   "blocks": [
     ("steps", [
       ("Arrival", "Hello and check-in", "The technician arrives at the scheduled time and checks in with you for a minute: How was the night? Anything new today? Any change in medicine, sleep or routine?"),
       ("Warm-up", "Play to get going", "A few minutes of something your child loves, to get settled and motivated."),
       ("Learning", "Teaching woven into play", "Most teaching happens inside activities your child enjoys — asking for a turn, naming the toy, taking turns, following a direction during a game."),
       ("Practice", "Short, focused bursts", "Quick rounds of practice on specific skills, with lots of encouragement and a break or favorite activity right after."),
       ("Routines", "Real-life skills", "Practice on whatever matters at your house: washing hands, snack time, getting shoes on, waiting, cleaning up, moving from one activity to the next."),
       ("Wrap-up", "Data and notes", "Before leaving, the technician finishes collecting the session’s data and updates your child’s record, so your BCBA can see exactly how it went."),
     ]),
   ]},
  {"id": "see", "hand": "What you might notice", "title": "Things that can look odd at first — and why we do them",
   "blocks": [
     ("cards", [
       ("You might see", "Lots of praise and rewards", "Rewards help new skills take hold. As a skill becomes easy, rewards fade to the everyday kind — a smile, a high five, getting what you asked for.", "tint-sun", "i-star"),
       ("You might see", "The technician writing or tapping", "That’s live data. It’s how your BCBA knows what’s working without guessing.", "tint-sky", "i-assess"),
       ("You might see", "Help that slowly disappears", "At first the technician might guide your child’s hand or say the first sound of a word. That help fades on purpose, until your child does it on their own.", "tint-meadow", "i-hand"),
       ("You might see", "A calm, planned response to hard moments", "If your child has a big reaction, the technician follows the behavior plan your BCBA has already talked through with you. You’ll never be surprised by a strategy.", "tint-coral", "i-heart"),
     ]),
   ]},
  {"id": "you", "hand": "Where you fit in", "title": "Your part during a session", "band": "b-meadow",
   "blocks": [
     ("split", [
       ("ticks", [
         "<strong>A parent or another trusted adult needs to be home</strong> for in-home sessions. You don’t have to hover — just be nearby.",
         "<strong>Jump in when invited.</strong> Watching and trying strategies during sessions is one of the fastest ways to learn them.",
         "<strong>A space with fewer distractions helps</strong> for some activities — but your normal, lived-in house is exactly right.",
         "<strong>Share the small stuff.</strong> A rough night, a new medicine, a family change — it all helps us read the day.",
       ]),
       ("cards", [
         ("Your BCBA’s visits", "Supervision, built in", "Your BCBA regularly joins sessions to watch, coach the technician, update programs and answer your questions. Save your questions — that’s a great time to ask.", "", "i-assess"),
       ]),
     ]),
     ("p", "At our Tulsa center, sessions happen in our playrooms, and the team will walk you through drop-off and pick-up. In daycare or community settings, we coordinate with the staff there."),
   ]},
 ]},
# ---------------------------------------------------------------- 4
{"slug": "the-assessment", "n": 4, "nav": "The assessment", "read": "4-minute read", "icon": "i-assess", "tint": "tint-coral",
 "title": "The assessment: what to expect",
 "card": "What to have ready, what happens during the visits, and how the treatment plan gets made.",
 "lede": "The assessment isn’t a test your child can pass or fail. It’s how your BCBA gets to know your child — and your family — well enough to write a plan that actually fits.",
 "short": [
   "It usually takes 2–4 visits with a BCBA, at home or wherever therapy will happen.",
   "Your child doesn’t need to “perform.” A normal day — even a hard one — tells us the most.",
   "You’ll read the goals and the plan before anything is sent to your insurer.",
 ],
 "sections": [
  {"id": "before", "hand": "Before the first visit", "title": "Helpful to have ready (but don’t stress)",
   "intro": "Pull together whatever you have. If you don’t have something, that’s fine — your BCBA will work with what’s there.",
   "blocks": [
     ("split", [
       ("ticks", [
         "A diagnosis report or evaluation, if your child has one — or, in Colorado, the physician’s letter recommending ABA",
         "Any IEP, IFSP or school/daycare reports",
         "Reports from speech, occupational or other therapists",
         "A list of medicines, allergies and anything medical we should know",
       ]),
       ("ticks", [
         "Your child’s favorite things: snacks, toys, shows, songs, activities",
         "The parts of the day that are hardest right now",
         "Your top two or three hopes — “I wish my child could…”",
         "Questions you want to ask (write them down as you think of them)",
       ]),
     ]),
   ]},
  {"id": "during", "hand": "During the visits", "title": "What actually happens", "band": "b-sky",
   "blocks": [
     ("steps", [
       ("Talking with you", "Caregiver interview", "Your BCBA asks about your child’s history, what a typical day looks like, what’s going well, what’s hard, and what matters most to you. This is the most important part — you’re the expert on your child."),
       ("Watching and playing", "Observation", "Your BCBA watches your child play and go through normal routines, and plays with them too. No preparation needed."),
       ("Skills check", "Structured skills assessment", "Play-based activities that check communication, play, self-help, social and learning skills. We often use tools like the ABLLS-R or VB-MAPP."),
       ("Everyday skills", "Adaptive questionnaire", "A standardized set of questions about everyday skills — like the Vineland-3 — that you answer with your BCBA’s help."),
       ("If needed", "A closer look at hard behavior", "If challenging behavior is a concern, your BCBA looks at when it happens, what comes before and after, and what it might be doing for your child. That’s how we find a kinder, more effective way to help."),
     ]),
   ]},
  {"id": "tips", "hand": "A few tips", "title": "To get the most out of it",
   "blocks": [
     ("cards", [
       ("Honestly", "A hard day is useful", "If your child melts down during the assessment, don’t apologize. It shows us exactly what we need to help with.", "tint-sun", "i-heart"),
       ("Really", "No need to tidy up", "Your normal routines and your normal house are the most helpful thing to see.", "tint-meadow", "i-home"),
       ("Please", "Say what matters to you", "If something your BCBA suggests doesn’t fit your family, your culture or your priorities, say so. The goals are yours too.", "tint-sky", "i-talk"),
     ]),
   ]},
  {"id": "after", "hand": "After the visits", "title": "From assessment to approved plan", "band": "b-meadow",
   "blocks": [
     ("steps", [
       ("Writing", "Your BCBA writes the plan", "It includes your child’s goals, how each will be taught, how hard moments will be handled, goals for family guidance, and the recommended hours."),
       ("Reviewing", "You read it together", "Your BCBA walks you through the plan in plain language. Ask questions, change what doesn’t fit, and sign when you’re comfortable."),
       ("Approving", "We send it to your insurer", "We submit the plan and hours request for approval. This can take days to a few weeks, and we’ll tell you as soon as we hear."),
       ("Starting", "Scheduling and your technician", "Once approved, we set your schedule and introduce your technician."),
     ]),
     ("note", "<strong>This happens again about every six months.</strong> A reassessment checks progress, updates goals, and renews the approval with your insurer. You’ll be part of it every time."),
   ]},
 ]},
# ---------------------------------------------------------------- 5
{"slug": "your-part", "n": 5, "nav": "Your part", "read": "4-minute read", "icon": "i-home", "tint": "tint-lilac",
 "title": "What we’ll ask of you — and what you can count on from us",
 "card": "The handful of things that make ABA work, and the promises we make in return.",
 "lede": "You don’t need to be an expert, and you don’t need to do it all at once. ABA works best as a partnership, so here’s what we’ll ask — openly, up front — and what you can expect from us in return.",
 "short": [
   "An adult at home for in-home sessions, and at least two hours a month of family guidance with your BCBA.",
   "A steady schedule — and a heads-up when plans change.",
   "Keep your insurance current, and talk to us when something isn’t working.",
 ],
 "sections": [
  {"id": "ask", "hand": "What we ask", "title": "Six things that make the biggest difference",
   "blocks": [
     ("cards", [
       ("1", "Be home for in-home sessions", "A parent or another trusted adult needs to be in the home during in-home sessions. You can go about your day — just stay nearby and available.", "tint-sun", "i-home"),
       ("2", "Family guidance: at least two hours a month", "Time with your BCBA, practicing strategies in your real routines — bath time, car seats, the grocery store. It’s required by insurers, and it’s where a lot of the lasting change comes from. Other caregivers are welcome to join.", "tint-meadow", "i-talk"),
       ("3", "Keep the schedule steady", "Consistency is how skills stick. Frequent cancellations can quietly undo months of progress — and insurers look at attendance when they review continued hours.", "tint-sky", "i-blocks"),
       ("4", "Give us a heads-up", "As much notice as you can. <strong>Two weeks</strong> for planned vacations. <strong>Same-day cancellations by 6:00 a.m.</strong>, by call or text. If your child is sick — fever, vomiting, anything contagious — please cancel; we’ll do the same if our staff is sick.", "tint-coral", "i-letter"),
       ("5", "Keep your insurance current", "Tell us the day your insurance changes. Watch your mail for Medicaid renewal paperwork and send it back quickly — a lapse in coverage is the most common reason therapy pauses, and it’s completely preventable.", "tint-lilac", "i-shield"),
       ("6", "Talk to us", "Tell us about changes at home — sleep, medicine, a move, a new baby. And tell us when something isn’t working: a goal that doesn’t matter to you, a time slot that’s become impossible, a technician who isn’t the right fit.", "tint-sun", "i-heart"),
     ]),
   ]},
  {"id": "practice", "hand": "In between sessions", "title": "Practice, without the homework feeling", "band": "b-sky",
   "intro": "Your BCBA will give you one or two things to try at a time — not a binder. Things like:",
   "blocks": [
     ("ticks", [
       "Waiting a beat before handing over the snack, so your child has a chance to ask.",
       "Using the same few words for a routine every time (“shoes, coat, car”).",
       "Noticing and cheering the moments that go right — they’re easy to miss on a busy day.",
     ]),
     ("p", "Small, consistent moments across the day add up to more than any single session."),
   ]},
  {"id": "promise", "hand": "What you can count on", "title": "Our side of the partnership",
   "blocks": [
     ("ticks", [
       "<strong>The same friendly face whenever we can.</strong> We match technicians for continuity and keep them with your family.",
       "<strong>A heads-up if we need to cancel</strong> — and a real effort to send someone else to cover.",
       "<strong>A BCBA who answers your questions</strong> and explains things in plain language.",
       "<strong>Goals you agreed to,</strong> and progress data you can see any time.",
       "<strong>Respect for your home, your culture and your language.</strong> Caregiver paperwork is available in Spanish — just ask.",
       "<strong>Honesty</strong> — about cost, timelines, and what ABA can and can’t do.",
     ]),
   ]},
  {"id": "overwhelmed", "hand": "If it feels like a lot", "title": "Most families find their rhythm in a few weeks", "band": "b-meadow",
   "blocks": [
     ("p", "New schedules, new people in your home, new words — it’s a lot at the start. That’s normal. If the schedule isn’t sustainable for your family, tell us early. We’d much rather rework it together than have you burn out."),
     ("note", "<strong>You’re not doing this alone.</strong> Any question, any time — call your local office or email <a href=\"mailto:info@actaba.com\">info@actaba.com</a>."),
   ]},
 ]},
]

# ------------------------------------------------------------------ HTML

def _cards(items, cols=None):
    n = cols or (3 if len(items) % 3 == 0 or len(items) > 4 else 2 if len(items) != 1 else 1)
    cls = {1: "grid", 2: "grid c2", 3: "grid c3"}[n]
    out = []
    for k, t, b, tint, ic in items:
        out.append(f'<div class="card {tint} stack g10">{ico(ic) if ic else ""}<span class="k">{k}</span><h3>{t}</h3><p class="small muted">{b}</p></div>')
    return f'<div class="{cls}">' + "".join(out) + '</div>'

def _steps(items):
    li = "".join(f'<li class="gstep"><b class="gnum" aria-hidden="true">{i}</b><div class="stack g6"><span class="when">{lab}</span><h3>{t}</h3><p class="muted measure">{b}</p></div></li>' for i, (lab, t, b) in enumerate(items, 1))
    return f'<ol class="gsteps">{li}</ol>'

def _faq(items):
    return '<div class="faqs">' + "".join(f'<details class="faq" open><summary>{q}</summary><div class="a">{a}</div></details>' for q, a in items) + '</div>'

def _block(kind, data):
    from p_pages import chart
    if kind == "p": return f'<p class="muted measure">{data}</p>'
    if kind == "ticks": return f'<div class="card">{ticks(data)}</div>'
    if kind == "x": return f'<div class="card tint-coral stack g10"><span class="k">Things we’ll never tell you</span>{ticks(data, "ticks x")}</div>'
    if kind == "pills": return '<div class="pills">' + "".join(f'<span class="pill">{t}</span>' for t in data) + '</div>'
    if kind == "cards": return _cards(data)
    if kind == "steps": return _steps(data)
    if kind == "faq": return _faq(data)
    if kind == "note": return f'<div class="note">{data}</div>'
    if kind == "callout": return f'<div class="callout">{data}</div>'
    if kind == "chart": return chart()
    if kind == "split": return '<div class="split">' + "".join(_block(k, d) if k != "cards" else _cards(d, 1) for k, d in data) + '</div>'
    raise ValueError(kind)

def _section(s):
    band = f' band {s["band"]}' if s.get("band") else ''
    intro = f'<p class="lede measure">{s["intro"]}</p>' if s.get("intro") else ''
    blocks = "".join(_block(k, d) for k, d in s["blocks"])
    hc = {"b-sky": " sky", "b-meadow": " meadow"}.get(s.get("band"), "")
    return f'''<section class="sec gsec{band}" id="{s["id"]}"><div class="wrap stack g28">
  <div class="stack g14"><span class="hand{hc}">{s["hand"]}</span><h2>{s["title"]}</h2>{intro}</div>
  {blocks}
</div></section>'''

def _ghead(eyebrow, title, lede, extra=""):
    return f'''<section class="phead">
  <div class="hero-sky" aria-hidden="true"><svg class="sun" viewBox="0 0 200 200" focusable="false"><use href="#sunsym"/></svg></div>
  <div class="wrap stack g14"><span class="hand">{eyebrow}</span><h1>{title}</h1><p class="lede measure">{lede}</p>{extra}</div>
  {strip()}
</section>'''

PRINT_HEAD = f'''<div class="print-only print-brand"><svg viewBox="0 0 44 44" aria-hidden="true"><use href="#logo"/></svg><div><strong>Adventure Child Therapy</strong><span>Your family guide · actaba.com/guide</span></div></div>'''
PRINT_FOOT = f'''<div class="print-only print-foot">Questions? {PHONES} · info@actaba.com · actaba.com/guide</div>'''

def _toolbar(g):
    return f'''<div class="gtools no-print"><span class="pill">{g["read"]}</span><span class="pill">Guide {g["n"]} of 5</span>
<a class="go" href="/guide/pdf/{g["slug"]}.pdf" download>Download PDF {ARROW}</a><button class="linkbtn" type="button" data-print>Print</button></div>'''

def _pager(g):
    i = g["n"] - 1
    prev = GUIDES[i - 1] if i > 0 else None
    nxt = GUIDES[i + 1] if i < len(GUIDES) - 1 else None
    p = f'<a class="card gpage" href="/guide/{prev["slug"]}/"><span class="k">&larr; Guide {prev["n"]}</span><h4>{prev["nav"]}</h4></a>' if prev else '<a class="card gpage" href="/guide/"><span class="k">&larr; All guides</span><h4>Your family guide</h4></a>'
    n = f'<a class="card gpage next" href="/guide/{nxt["slug"]}/"><span class="k">Next: Guide {nxt["n"]} &rarr;</span><h4>{nxt["nav"]}</h4></a>' if nxt else '<a class="card gpage next" href="/families/#start"><span class="k">Ready? &rarr;</span><h4>Start intake</h4></a>'
    return f'<nav class="gpager no-print" aria-label="Guide pages">{p}{n}</nav>'

def _short(g):
    return f'''<div class="card tint-sun gshort stack g10"><span class="k">The short version</span>{ticks(g["short"])}<p class="tiny">That’s really all you need. The rest is here whenever you want more.</p></div>'''

def _closing():
    return f'''<section class="sec tight gclose"><div class="wrap"><div class="cta">
  <div class="stack g14"><span class="hand">Questions?</span><h2 style="max-width:24ch">Call us — a real person will help.</h2>
  <p class="muted measure">{PHONES} · <a href="mailto:info@actaba.com">info@actaba.com</a></p></div>
  <svg class="kite-art" viewBox="0 0 120 220" aria-hidden="true" focusable="false"><use href="#kitesym"/></svg>
</div></div></section>'''

def guide_body(g, print_mode=False):
    sections = "".join(_section(s) for s in g["sections"])
    extra = _toolbar(g) if not print_mode else ''
    head = _ghead(f'Family guide · {g["n"]} of 5', g["title"], g["lede"], extra)
    return f'''<div class="guide" data-guide="{g["slug"]}">
{PRINT_HEAD}
{head}
<section class="sec tight"><div class="wrap">{_short(g)}</div></section>
{sections}
{_pager(g)}
{_closing() if not print_mode else ''}
{PRINT_FOOT}
</div>'''

def add_promo(families_html):
    """Insert the family-guide card under the five-step trail on /families/."""
    old = '<section class="sec" id="route"><div class="wrap">'
    card = (f'<a class="card tint-sun" href="/guide/" style="flex-direction:row;align-items:center;gap:18px;flex-wrap:wrap;text-decoration:none;color:inherit;max-width:920px;margin-top:40px">'
            f'{ico("i-letter","ico lg")}<div class="stack g6" style="flex:1;min-width:220px"><span class="k">New to ABA?</span><h3>Read our five-part family guide</h3>'
            f'<p class="small muted">What ABA is, what a session looks like, what happens at the assessment, and what we’ll ask of you — in short, friendly reads.</p></div>'
            f'<span class="go">Open the guide {ARROW}</span></a>')
    i = families_html.index(old)
    j = families_html.index('</div></section>', i)
    return families_html[:j] + card + families_html[j:]

def page_fn(g):
    return lambda: guide_body(g)

def hub():
    cards = "".join(f'''<a class="card {g["tint"]} gcard" href="/guide/{g["slug"]}/">
  <div class="gcard-top">{ico(g["icon"], "ico lg")}<b class="gbig" aria-hidden="true">{g["n"]}</b></div>
  <span class="k">{g["read"]}</span><h3>{g["nav"] if g["n"] != 5 else "What we’ll ask of you"}</h3><p class="small muted" style="flex:1">{g["card"]}</p><span class="go">Read guide {g["n"]} {ARROW}</span></a>''' for g in GUIDES)
    return f'''<div class="guide guide-hub">
{PRINT_HEAD}
{_ghead("Welcome to Adventure Child Therapy", "Your family guide", "Reaching out is the hardest step, and you’ve already taken it. These five short reads explain what ABA is, how it works, and what the next few months will look like. Read them in order, or just the one you need today. There’s no test.", '<div class="gtools no-print"><a class="go" href="/guide/pdf/act-family-guide.pdf" download>Download all five as one PDF ' + ARROW + '</a><button class="linkbtn" type="button" data-print>Print this page</button></div>')}
<section class="sec"><div class="wrap stack g28">
  <div class="grid c3 ghub">{cards}
    <div class="card gcard gcard-help stack g10">{ico("i-talk", "ico lg")}<span class="k">Rather talk?</span><h3>Call a real person</h3><p class="small muted" style="flex:1">Every question is a good question — especially the ones you feel silly asking.</p><p class="small">{CO_TEL.replace("<a ", '<a class="go" ')}<br>Colorado</p><p class="small">{OK_TEL.replace("<a ", '<a class="go" ')}<br>Oklahoma</p><p class="small">{NC_TEL.replace("<a ", '<a class="go" ')}<br>North Carolina</p></div>
  </div>
  <div class="note measure"><strong>Prefer Spanish?</strong> Our caregiver handbook and intake paperwork are available in Spanish. Just let us know. · <span lang="es"><strong>¿Prefiere español?</strong> Tenemos el manual para cuidadores y los formularios de admisión en español. Solo díganos.</span></div>
</div></section>
<section class="sec band b-meadow"><div class="wrap split">
  <div class="stack g14"><span class="hand meadow">Where things stand</span><h2>What happens next</h2>
  <p class="muted">Our team is already working on the next step with you. Here’s the whole road at a glance — Guide 2 walks through it in more detail.</p>
  {btn("/guide/how-it-works/", "How it works")}</div>
  <div class="card">{ticks(["<strong>Intake call or form</strong> — about 10 minutes", "<strong>Paperwork on file</strong> — depends on your state", "<strong>Insurance check and approval</strong> — days to weeks", "<strong>Assessment</strong> — usually 2–4 visits", "<strong>Sessions begin</strong> — with family guidance from day one"])}</div>
</div></section>
{_closing()}
{PRINT_FOOT}
</div>'''

def print_all():
    """One long page with all five guides, used only to render the combined PDF."""
    parts = []
    for g in GUIDES:
        parts.append(guide_body(g, print_mode=True))
    return '<div class="print-book">' + '<div class="pb"></div>'.join(parts) + '</div>'

GUIDE_CSS = """
/* ---- family guide ---- */
.gtools{display:flex;flex-wrap:wrap;gap:10px 16px;align-items:center;margin-top:6px}
.linkbtn{font:inherit;font-weight:600;color:var(--meadow-ink);background:none;border:0;padding:0;cursor:pointer;text-decoration:underline;text-underline-offset:3px}
.gshort{max-width:860px;margin-inline:auto}
.gshort .ticks li{font-size:1.06rem;color:var(--ink)}
.gsteps{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:14px;max-width:920px;counter-reset:g}
.gstep{display:grid;grid-template-columns:52px minmax(0,1fr);gap:16px;align-items:start;background:var(--surface);border:2px solid var(--line);border-radius:var(--r-lg);padding:18px 22px}
.band .gstep{border-color:transparent}
.gnum{display:grid;place-items:center;width:46px;height:46px;border-radius:50%;background:var(--sun);color:var(--on-sun);font-family:var(--f-display);font-weight:800;font-size:1.35rem;box-shadow:0 3px 0 var(--sun-deep)}
.gstep .when{align-self:flex-start}
.gcard{text-decoration:none;color:inherit;gap:10px}
.gcard-top{display:flex;justify-content:space-between;align-items:flex-start}
.gbig{font-family:var(--f-display);font-weight:800;font-size:3rem;line-height:.8;color:var(--ink);opacity:.18}
.gcard-help{border-style:dashed}
.gpager{max-width:var(--maxw,1180px);margin:0 auto;padding:clamp(28px,4vw,48px) clamp(16px,4vw,40px) 0;display:grid;grid-template-columns:1fr 1fr;gap:18px}
.gpage{text-decoration:none;color:inherit;gap:4px}
.gpage.next{text-align:right;background:var(--band-sun);border-color:transparent}
@media (max-width:640px){.gpager{grid-template-columns:1fr}.gpage.next{text-align:left}.gstep{grid-template-columns:40px minmax(0,1fr);padding:16px}.gnum{width:38px;height:38px;font-size:1.1rem}}
.print-only{display:none}
@media print{
  @page{size:letter;margin:.55in .6in}
  html,body{background:#fff !important}
  *{-webkit-print-color-adjust:exact;print-color-adjust:exact}
  .no-print,.hdr,.topstrip,.ftr,.skip,.gclose,.phead .hero-sky,.phead svg.strip,.strip{display:none !important}
  .print-only{display:block}
  .print-brand{display:flex !important;align-items:center;gap:10px;padding-bottom:10px;margin-bottom:6px;border-bottom:3px solid #FFC845}
  .print-brand svg{width:36px;height:36px}
  .print-brand strong{display:block;font-family:var(--f-display);font-size:15pt;line-height:1}
  .print-brand span{font-size:9pt;color:#555}
  .print-foot{margin-top:18px;padding-top:8px;border-top:2px solid #E8E2D6;font-size:8.5pt;color:#555;text-align:center}
  .phead{padding:10px 0 4px !important;background:none !important;min-height:0 !important}
  .phead h1{font-size:26pt !important}
  .phead .lede{font-size:11pt}
  .wrap{padding-inline:0 !important;max-width:none !important}
  .sec,.sec.tight{padding-block:12px !important}
  .band{background:none !important}
  .band::before,.band::after{display:none !important}
  h2{font-size:17pt !important}
  h3{font-size:12.5pt !important}
  body{font-size:10.5pt}
  .lede{font-size:11pt !important}
  .card,.gstep,.note,.callout,details.faq{break-inside:avoid;box-shadow:none !important}
  .card:not([class*="tint-"]),.gstep{border:1.5px solid #E8E2D6 !important}
  h2,h3,.hand{break-after:avoid}
  .grid.c3{grid-template-columns:repeat(3,minmax(0,1fr)) !important}
  .grid.c2,.split{grid-template-columns:repeat(2,minmax(0,1fr)) !important}
  .ghub{grid-template-columns:repeat(2,minmax(0,1fr)) !important}
  details.faq summary::after{display:none}
  details.faq .a{display:block !important}
  .pb{break-before:page}
  .print-book .guide + .guide{break-before:page}
  .chart-card svg{max-height:2.4in}
  a{color:inherit;text-decoration:none}
  .card{padding:12px 14px !important;gap:5px !important;border-radius:12px !important}
  .card .ico,.card .ico.lg{width:30px !important;height:30px !important}
  .gstep{padding:10px 14px !important;grid-template-columns:34px minmax(0,1fr) !important;gap:10px !important;border-radius:12px !important}
  .gsteps{gap:8px !important}
  .gnum{width:30px !important;height:30px !important;font-size:12pt !important;box-shadow:none !important}
  .stack.g28{gap:12px !important}.stack.g14{gap:6px !important}.grid{gap:10px !important}.split{gap:14px !important}
  .small{font-size:9.5pt !important}
  .measure{max-width:none !important}
  .note,.callout{padding:10px 14px !important}
  .pill{border:1px solid #DDEBF3}
  .gbig{display:none}
}
"""

# ------------------------------------------------------------------ Markdown (team-editable copy)

def _md(s):
    s = re.sub(r'<a href="([^"]+)"[^>]*>(.*?)</a>', lambda m: f'[{m.group(2)}]({m.group(1).replace("mailto:", "mailto:")})', s)
    s = re.sub(r'</?strong>', '**', s)
    s = re.sub(r'</?em>', '*', s)
    s = re.sub(r'<[^>]+>', '', s)
    return s.replace('&amp;', '&').replace('&rarr;', '→').replace('&larr;', '←')

def _md_block(kind, data):
    if kind in ("p", "note", "callout"):
        pre = "> " if kind != "p" else ""
        return pre + _md(data)
    if kind in ("ticks",): return "\n".join(f"- {_md(x)}" for x in data)
    if kind == "x": return "**Things we’ll never tell you**\n\n" + "\n".join(f"- {_md(x)}" for x in data)
    if kind == "pills": return "\n".join(f"- {_md(x)}" for x in data)
    if kind == "cards": return "\n\n".join(f"**{_md(t)}** — {_md(b)}" for k, t, b, *_ in data)
    if kind == "steps": return "\n".join(f"{i}. **{_md(t)}** ({_md(lab)}). {_md(b)}" for i, (lab, t, b) in enumerate(data, 1))
    if kind == "faq": return "\n\n".join(f"**{_md(q)}**\n{_md(a)}" for q, a in data)
    if kind == "chart": return ""
    if kind == "split": return "\n\n".join(x for x in (_md_block(k, d) for k, d in data) if x)
    raise ValueError(kind)

def to_markdown(g):
    out = [f"# {_md(g['title'])}", "", f"*Family guide {g['n']} of 5 · {g['read']} · live page: actaba.com/guide/{g['slug']}/*", "", _md(g["lede"]), "",
           "## The short version", "", "\n".join(f"- {_md(x)}" for x in g["short"]), ""]
    for s in g["sections"]:
        out += [f"## {_md(s['title'])}", ""]
        if s.get("intro"): out += [_md(s["intro"]), ""]
        for k, d in s["blocks"]:
            b = _md_block(k, d)
            if b: out += [b, ""]
    out += ["---", "", "Questions? Colorado (720) 432-8989 · Oklahoma (918) 764-8544 · North Carolina (336) 270-9453 · info@actaba.com"]
    return "\n".join(out)
