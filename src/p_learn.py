"""Micro-courses: five short vertical videos texted to Colorado families after intake.

LESSONS is the single source of truth for the narration, the on-screen visuals and the
/learn/ watch pages. render_videos.py turns each lesson into an MP4 (AI narrator + burned-in
captions); build_static.py turns each into a watch page at /learn/<n>/.

Each beat = one narrated moment:
  say  - what the narrator reads (spelled for speech: "six a.m.", digits spelled out)
  cap  - optional caption text when it should differ from `say` (defaults to `say`)
  v    - the visual: dict with "kind" and its fields
Visual kinds: title, chips, steps, flow, swap, chart, team, next, phone
"""

PHONE_CO = "(720) 432-8989"
PHONE_CO_SAY = "seven two zero, four three two, eight nine eight nine"

LESSONS = [
# ------------------------------------------------------------------ 1
{"n": 1, "slug": "what-is-aba", "title": "What is ABA?", "guide": "/guide/what-is-aba/",
 "blurb": "The science in plain words — and what good ABA should look like for your child.",
 "beats": [
  {"say": "Welcome to Adventure Child Therapy! In the next minute, let's talk about what ABA actually is, in plain words.",
   "v": {"kind": "title", "kicker": "Lesson 1 of 5", "title": "What is ABA?", "icon": "i-seed"}},
  {"say": "A. B. A. stands for applied behavior analysis. It's a way of teaching that looks closely at what helps your child learn, and what gets in the way.",
   "cap": "ABA stands for applied behavior analysis. It's a way of teaching that looks closely at what helps your child learn, and what gets in the way.",
   "v": {"kind": "chips", "kicker": "ABA means", "title": "Applied Behavior Analysis", "items": ["What helps your child learn", "What gets in the way"]}},
  {"say": "We look at three simple things: what happens right before a behavior, the behavior itself, and what happens right after.",
   "v": {"kind": "flow", "kicker": "The big idea", "title": "Before, during, after", "items": ["Before", "Behavior", "After"]}},
  {"say": "Say your child screams for crackers, and screaming works. So we teach a quicker way to ask: a word, a sign, a picture, or a device. And we make sure asking works better than screaming ever did.",
   "v": {"kind": "swap", "kicker": "An example", "title": "Snack time", "old": "Screaming gets crackers", "new": "Asking gets crackers — faster"}},
  {"say": "Big skills get broken into small steps, practiced mostly through play and everyday routines. A lot of good ABA looks like play, and that's on purpose.",
   "v": {"kind": "chips", "kicker": "How it's taught", "title": "Small steps, lots of play", "items": ["Small, doable steps", "Mostly through play", "Everyday routines"]}},
  {"say": "We measure progress every session, so you can see what's working. And if something isn't working, we change it.",
   "v": {"kind": "chart", "kicker": "Progress you can see", "title": "Measured every session"}},
  {"say": "Your team: a B. C. B. A. who designs the plan, a behavior technician who works with your child, and you, the expert on your child.",
   "cap": "Your team: a BCBA who designs the plan, a behavior technician who works with your child, and you, the expert on your child.",
   "v": {"kind": "team", "kicker": "Who's who", "title": "Your child's team", "items": [["BCBA", "Designs the plan"], ["Technician", "Works with your child"], ["You", "The expert on your child"]]}},
  {"say": "Next up: how ABA works at Adventure Child Therapy, from your first call to your first session.",
   "v": {"kind": "next", "kicker": "Up next", "title": "Lesson 2: How it works"}},
 ]},
# ------------------------------------------------------------------ 2
{"n": 2, "slug": "how-it-works", "title": "How it works", "guide": "/guide/how-it-works/",
 "blurb": "The road from your first call to your first session, and how hours are decided.",
 "beats": [
  {"say": "Here's the road from your first call to your first session. You won't walk it alone. We handle the paperwork with you.",
   "v": {"kind": "title", "kicker": "Lesson 2 of 5", "title": "How it works", "icon": "i-letter"}},
  {"say": "Step one is intake, and you've already done it! Step two is paperwork. In Colorado, your child doesn't need an autism diagnosis to start. A letter from your child's doctor recommending ABA is enough.",
   "v": {"kind": "steps", "kicker": "Five stops", "title": "Getting started", "done": 1, "focus": 2, "items": ["Intake", "Doctor's letter", "Insurance approval", "Assessment", "Sessions begin"]}},
  {"say": "Step three: we check your insurance and ask for approval. With Health First Colorado, approved services cost your family nothing. With a commercial plan, we'll tell you exactly what your plan says.",
   "v": {"kind": "steps", "kicker": "Five stops", "title": "Getting started", "done": 2, "focus": 3, "items": ["Intake", "Doctor's letter", "Insurance approval", "Assessment", "Sessions begin"]}},
  {"say": "Step four is the assessment: usually two to four visits with a B. C. B. A. You'll read the goals before anything is final.",
   "cap": "Step four is the assessment: usually 2 to 4 visits with a BCBA. You'll read the goals before anything is final.",
   "v": {"kind": "steps", "kicker": "Five stops", "title": "Getting started", "done": 3, "focus": 4, "items": ["Intake", "Doctor's letter", "Insurance approval", "Assessment", "Sessions begin"]}},
  {"say": "And step five: sessions begin, with a technician matched to your schedule and your area.",
   "v": {"kind": "steps", "kicker": "Five stops", "title": "Getting started", "done": 4, "focus": 5, "items": ["Intake", "Doctor's letter", "Insurance approval", "Assessment", "Sessions begin"]}},
  {"say": "How many hours? That comes from the assessment, not a phone call. Your B. C. B. A. recommends hours that fit your child's needs and your family's life, and your insurance approves them.",
   "cap": "How many hours? That comes from the assessment, not a phone call. Your BCBA recommends hours that fit your child's needs and your family's life, and your insurance approves them.",
   "v": {"kind": "chips", "kicker": "Hours", "title": "Where hours come from", "items": ["Your child's needs", "Your family's life", "Insurance approval"]}},
  {"say": "Waiting is the hardest part. We won't promise a date we can't keep, but we'll keep you posted, and you can call us anytime.",
   "v": {"kind": "phone", "kicker": "While you wait", "title": "We'll keep you posted"}},
  {"say": "Next up: what a session actually looks like.",
   "v": {"kind": "next", "kicker": "Up next", "title": "Lesson 3: A typical session"}},
 ]},
# ------------------------------------------------------------------ 3
{"n": 3, "slug": "a-session", "title": "A typical session", "guide": "/guide/a-session/",
 "blurb": "Building trust first, a session from hello to goodbye, and where you fit in.",
 "beats": [
  {"say": "Most families are surprised by how much an ABA session looks like play. Here's what to expect.",
   "v": {"kind": "title", "kicker": "Lesson 3 of 5", "title": "A typical session", "icon": "i-blocks"}},
  {"say": "The first few weeks are about building trust. The technician does your child's favorite things, follows their lead, and asks for very little. It's the foundation for everything else.",
   "v": {"kind": "chips", "kicker": "The first few weeks", "title": "First, we build trust", "items": ["Favorite things", "Following their lead", "Asking very little"]}},
  {"say": "A typical session has a quick check-in with you, some play to get going, teaching woven into activities your child enjoys, short bursts of practice, and real-life routines like handwashing, snack time, and shoes on.",
   "v": {"kind": "steps", "kicker": "A sample session", "title": "Hello to goodbye", "items": ["Quick check-in", "Play to get going", "Teaching through play", "Short practice bursts", "Real-life routines"]}},
  {"say": "You'll see lots of praise and rewards. They help new skills take hold, then fade to everyday ones, like a high five.",
   "v": {"kind": "chips", "kicker": "What you might see", "title": "Lots of praise", "items": ["Rewards help skills stick", "Then they fade", "To everyday ones, like a high five"]}},
  {"say": "You'll see the technician tapping on a tablet. That's live data. They collect it all session long and update your child's record, so your B. C. B. A. can see exactly how it went.",
   "cap": "You'll see the technician tapping on a tablet. That's live data. They collect it all session long and update your child's record, so your BCBA can see exactly how it went.",
   "v": {"kind": "chart", "kicker": "What you might see", "title": "Live data, every session"}},
  {"say": "And you'll see help that slowly disappears, on purpose, until your child does it on their own.",
   "v": {"kind": "chips", "kicker": "What you might see", "title": "Help that fades", "items": ["Lots of help at first", "A little less", "On their own!"]}},
  {"say": "For in-home sessions, a parent or another trusted adult needs to be home. You don't have to hover. Just stay nearby, and jump in when you're invited.",
   "v": {"kind": "chips", "kicker": "Your part", "title": "Stay nearby", "items": ["A trusted adult at home", "No need to hover", "Jump in when invited"]}},
  {"say": "Next up: what happens at the assessment.",
   "v": {"kind": "next", "kicker": "Up next", "title": "Lesson 4: The assessment"}},
 ]},
# ------------------------------------------------------------------ 4
{"n": 4, "slug": "the-assessment", "title": "The assessment", "guide": "/guide/the-assessment/",
 "blurb": "What happens during the visits, what to have ready, and how the plan gets made.",
 "beats": [
  {"say": "The assessment isn't a test your child can pass or fail. It's how your B. C. B. A. gets to know your child, and your family.",
   "cap": "The assessment isn't a test your child can pass or fail. It's how your BCBA gets to know your child, and your family.",
   "v": {"kind": "title", "kicker": "Lesson 4 of 5", "title": "The assessment", "icon": "i-assess"}},
  {"say": "It usually takes two to four visits, at home, or wherever therapy will happen.",
   "cap": "It usually takes 2 to 4 visits, at home, or wherever therapy will happen.",
   "v": {"kind": "chips", "kicker": "How long", "title": "2 to 4 visits", "items": ["At home", "Or wherever therapy will happen"]}},
  {"say": "Your B. C. B. A. will talk with you about your child's history, a typical day, what's going well, and what's hard. This is the most important part. You're the expert on your child.",
   "cap": "Your BCBA will talk with you about your child's history, a typical day, what's going well, and what's hard. This is the most important part. You're the expert on your child.",
   "v": {"kind": "chips", "kicker": "Talking with you", "title": "You're the expert", "items": ["Your child's history", "A typical day", "What's going well", "What's hard"]}},
  {"say": "They'll watch your child play, do some play-based skills activities, and go through a standard set of questions about everyday skills with you.",
   "v": {"kind": "steps", "kicker": "During the visits", "title": "What happens", "items": ["Talking with you", "Watching your child play", "Play-based skills activities", "Everyday-skills questions"]}},
  {"say": "A few tips. A hard day is actually useful, so don't apologize. No need to tidy up. And tell us what matters most to your family.",
   "v": {"kind": "chips", "kicker": "A few tips", "title": "Keep it real", "items": ["A hard day is useful", "No need to tidy up", "Say what matters to you"]}},
  {"say": "It helps to have ready: your doctor's letter or any evaluation, school or therapy reports, and a list of your child's favorite things.",
   "v": {"kind": "chips", "kicker": "Helpful to have ready", "title": "Don't stress", "items": ["Doctor's letter or evaluation", "School or therapy reports", "Your child's favorite things"]}},
  {"say": "Afterward, your B. C. B. A. writes the plan and walks you through it, and we send it to your insurance for approval. Then we schedule your sessions. About every six months, we'll reassess together.",
   "cap": "Afterward, your BCBA writes the plan and walks you through it, and we send it to your insurance for approval. Then we schedule your sessions. About every 6 months, we'll reassess together.",
   "v": {"kind": "steps", "kicker": "After the visits", "title": "From visits to sessions", "items": ["BCBA writes the plan", "You read it together", "Insurance approval", "Sessions scheduled"]}},
  {"say": "Next up, the last lesson: your part, and what you can count on from us.",
   "v": {"kind": "next", "kicker": "Up next", "title": "Lesson 5: Your part"}},
 ]},
# ------------------------------------------------------------------ 5
{"n": 5, "slug": "your-part", "title": "Your part", "guide": "/guide/your-part/",
 "blurb": "The handful of things that make ABA work, and the promises we make in return.",
 "beats": [
  {"say": "ABA works best as a partnership. Here's what we'll ask of you, and what you can count on from us.",
   "v": {"kind": "title", "kicker": "Lesson 5 of 5", "title": "Your part", "icon": "i-home"}},
  {"say": "One: be home for in-home sessions. Two: family guidance with your B. C. B. A., at least two hours a month. It's where a lot of lasting change happens.",
   "cap": "One: be home for in-home sessions. Two: family guidance with your BCBA, at least 2 hours a month. It's where a lot of lasting change happens.",
   "v": {"kind": "steps", "kicker": "What we ask", "title": "Six things", "focus": 2, "items": ["Be home for sessions", "Family guidance, 2 hrs/month", "Keep the schedule steady", "Give us a heads-up", "Keep insurance current", "Talk to us"]}},
  {"say": "Three: keep the schedule steady. Consistency is how skills stick. Four: give us a heads-up. Two weeks for vacations, and same-day cancellations by six a.m., by call or text.",
   "cap": "Three: keep the schedule steady. Consistency is how skills stick. Four: give us a heads-up. Two weeks for vacations, and same-day cancellations by 6 a.m., by call or text.",
   "v": {"kind": "steps", "kicker": "What we ask", "title": "Six things", "focus": 4, "items": ["Be home for sessions", "Family guidance, 2 hrs/month", "Keep the schedule steady", "Give us a heads-up", "Keep insurance current", "Talk to us"]}},
  {"say": "Five: keep your insurance current. Watch your mail for Health First Colorado renewal paperwork, and send it back quickly. A lapse in coverage is the most common reason therapy pauses.",
   "v": {"kind": "steps", "kicker": "What we ask", "title": "Six things", "focus": 5, "items": ["Be home for sessions", "Family guidance, 2 hrs/month", "Keep the schedule steady", "Give us a heads-up", "Keep insurance current", "Talk to us"]}},
  {"say": "Six: talk to us. If something isn't working, tell us, and we'll change it.",
   "v": {"kind": "steps", "kicker": "What we ask", "title": "Six things", "focus": 6, "items": ["Be home for sessions", "Family guidance, 2 hrs/month", "Keep the schedule steady", "Give us a heads-up", "Keep insurance current", "Talk to us"]}},
  {"say": "From us: the same friendly face whenever we can, a B. C. B. A. who answers your questions, goals you agreed to, and honesty, always.",
   "cap": "From us: the same friendly face whenever we can, a BCBA who answers your questions, goals you agreed to, and honesty, always.",
   "v": {"kind": "chips", "kicker": "What you can count on", "title": "Our side", "items": ["A familiar face", "Answers to your questions", "Goals you agreed to", "Honesty, always"]}},
  {"say": "It's a lot at first, and most families find their rhythm in a few weeks. You're not doing this alone. Questions? Call us at " + PHONE_CO_SAY + ".",
   "cap": "It's a lot at first, and most families find their rhythm in a few weeks. You're not doing this alone. Questions? Call us at " + PHONE_CO + ".",
   "v": {"kind": "phone", "kicker": "You're not alone", "title": "Call us anytime"}},
 ]},
]

def lesson(n):
    return LESSONS[n - 1]
