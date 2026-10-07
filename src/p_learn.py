"""Micro-courses: six short vertical videos texted to Colorado families after intake.

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
{"n": 1, "slug": "what-is-aba", "title": "What is applied behavior analysis?", "guide": "/guide/what-is-aba/",
 "blurb": "The science in plain words — and what good applied behavior analysis should look like for your child.",
 "beats": [
  {"say": "Welcome to Adventure Child Therapy! In the next minute, let's talk about what applied behavior analysis actually is, in plain words.",
   "v": {"kind": "title", "kicker": "Lesson 1 of 6", "title": "What is applied behavior analysis?", "icon": "i-seed"}},
  {"say": "Applied behavior analysis is the science of how learning works. We look at what happens around your child, and use it to teach new skills that make everyday life easier.",
   "v": {"kind": "chips", "kicker": "In plain words", "title": "Applied Behavior Analysis", "items": ["The science of how learning works", "Teaching skills that make life easier"]}},
  {"say": "We look at three simple things: what happens right before a behavior, the behavior itself, and what happens right after.",
   "v": {"kind": "flow", "kicker": "The big idea", "title": "Before, during, after", "items": ["Before", "Behavior", "After"]}},
  {"say": "Say your child screams for crackers, and eventually the crackers come. That's what any loving parent would do. Nobody did anything wrong. Screaming just works. So we teach a quicker way to ask: a word, a sign, a picture, or a device. And we make sure asking works better than screaming ever did.",
   "v": {"kind": "swap", "kicker": "An example", "title": "Snack time", "old": "Screaming gets crackers", "new": "Asking gets crackers — faster"}},
  {"say": "Big skills get broken into small steps, practiced mostly through play and everyday routines. A lot of good applied behavior analysis looks like play, and that's on purpose.",
   "v": {"kind": "chips", "kicker": "How it's taught", "title": "Small steps, lots of play", "items": ["Small, doable steps", "Mostly through play", "Everyday routines"]}},
  {"say": "We measure progress every session, so you can see what's working. And if something isn't working, we change it.",
   "v": {"kind": "chart", "kicker": "Progress you can see", "title": "Measured every session"}},
  {"say": "Your team: a Board Certified Behavior Analyst who designs the plan, a behavior technician who works with your child, and you, the expert on your child.",
   "cap": "Your team: a Board Certified Behavior Analyst who designs the plan, a behavior technician who works with your child, and you, the expert on your child.",
   "v": {"kind": "team", "kicker": "Who's who", "title": "Your child's team", "items": [["Board Certified Behavior Analyst", "Designs the plan", "i-assess"], ["Technician", "Works with your child", "i-blocks"], ["You", "The expert on your child", "i-heart"]]}},
  {"say": "Next up: how it all works at Adventure Child Therapy, from your first call to your first session.",
   "v": {"kind": "next", "kicker": "Up next", "title": "Lesson 2: How it works"}},
 ]},
# ------------------------------------------------------------------ 2
{"n": 2, "slug": "how-it-works", "title": "How it works", "guide": "/guide/how-it-works/",
 "blurb": "The road from your first call to your first session, and how hours are decided.",
 "beats": [
  {"say": "Here's the road from your first call to your first session. You won't walk it alone. We handle the paperwork with you.",
   "v": {"kind": "title", "kicker": "Lesson 2 of 6", "title": "How it works", "icon": "i-letter"}},
  {"say": "Step one is intake, and you've already done it! Step two is paperwork. In Colorado, your child doesn't need an autism diagnosis to start. A letter from your child's doctor recommending ABA is enough.",
   "v": {"kind": "steps", "kicker": "Five stops", "title": "Getting started", "done": 1, "focus": 2, "items": ["Intake", "Doctor's letter", "Insurance approval", "Assessment", "Sessions begin"]}},
  {"say": "Step three: we check your insurance and ask for approval. With Health First Colorado, approved services cost your family nothing. With a commercial plan, we'll tell you exactly what your plan says.",
   "v": {"kind": "steps", "kicker": "Five stops", "title": "Getting started", "done": 2, "focus": 3, "items": ["Intake", "Doctor's letter", "Insurance approval", "Assessment", "Sessions begin"]}},
  {"say": "Step four is the assessment: usually two to four visits with a Board Certified Behavior Analyst. You'll read the goals before anything is final.",
   "cap": "Step four is the assessment: usually 2 to 4 visits with a Board Certified Behavior Analyst. You'll read the goals before anything is final.",
   "v": {"kind": "steps", "kicker": "Five stops", "title": "Getting started", "done": 3, "focus": 4, "items": ["Intake", "Doctor's letter", "Insurance approval", "Assessment", "Sessions begin"]}},
  {"say": "And step five: sessions begin, with a technician matched to your schedule and your area.",
   "v": {"kind": "steps", "kicker": "Five stops", "title": "Getting started", "done": 4, "focus": 5, "items": ["Intake", "Doctor's letter", "Insurance approval", "Assessment", "Sessions begin"]}},
  {"say": "How many hours? That comes from the assessment, not a phone call. Your Board Certified Behavior Analyst recommends hours that fit your child's needs and your family's life, and your insurance approves them.",
   "cap": "How many hours? That comes from the assessment, not a phone call. Your Board Certified Behavior Analyst recommends hours that fit your child's needs and your family's life, and your insurance approves them.",
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
   "v": {"kind": "title", "kicker": "Lesson 3 of 6", "title": "A typical session", "icon": "i-blocks"}},
  {"say": "The first few weeks are about building trust. The technician does your child's favorite things, follows their lead, and asks for very little. It's the foundation for everything else.",
   "v": {"kind": "chips", "kicker": "The first few weeks", "title": "First, we build trust", "items": ["Favorite things", "Following their lead", "Asking very little"]}},
  {"say": "A typical session has a quick check-in with you, some play to get going, teaching woven into activities your child enjoys, short bursts of practice, and real-life routines like handwashing, snack time, and shoes on.",
   "v": {"kind": "steps", "kicker": "A sample session", "title": "Hello to goodbye", "items": ["Quick check-in", "Play to get going", "Teaching through play", "Short practice bursts", "Real-life routines"]}},
  {"say": "You'll see lots of praise and rewards. They help new skills take hold, then fade to everyday ones, like a high five.",
   "v": {"kind": "chips", "kicker": "What you might see", "title": "Lots of praise", "items": ["Rewards help skills stick", "Then they fade", "To everyday ones, like a high five"]}},
  {"say": "You'll see the technician tapping on a tablet. That's live data. They collect it all session long and update your child's record, so your Board Certified Behavior Analyst can see exactly how it went.",
   "cap": "You'll see the technician tapping on a tablet. That's live data. They collect it all session long and update your child's record, so your Board Certified Behavior Analyst can see exactly how it went.",
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
  {"say": "The assessment isn't a test your child can pass or fail. It's how your Board Certified Behavior Analyst gets to know your child, and your family.",
   "cap": "The assessment isn't a test your child can pass or fail. It's how your Board Certified Behavior Analyst gets to know your child, and your family.",
   "v": {"kind": "title", "kicker": "Lesson 4 of 6", "title": "The assessment", "icon": "i-assess"}},
  {"say": "It usually takes two to four visits, at home, or wherever therapy will happen.",
   "cap": "It usually takes 2 to 4 visits, at home, or wherever therapy will happen.",
   "v": {"kind": "chips", "kicker": "How long", "title": "2 to 4 visits", "items": ["At home", "Or wherever therapy will happen"]}},
  {"say": "Your Board Certified Behavior Analyst will talk with you about your child's history, a typical day, what's going well, and what's hard. This is the most important part. You're the expert on your child.",
   "cap": "Your Board Certified Behavior Analyst will talk with you about your child's history, a typical day, what's going well, and what's hard. This is the most important part. You're the expert on your child.",
   "v": {"kind": "chips", "kicker": "Talking with you", "title": "You're the expert", "items": ["Your child's history", "A typical day", "What's going well", "What's hard"]}},
  {"say": "They'll watch your child play, do some play-based skills activities, and go through a standard set of questions about everyday skills with you.",
   "v": {"kind": "steps", "kicker": "During the visits", "title": "What happens", "items": ["Talking with you", "Watching your child play", "Play-based skills activities", "Everyday-skills questions"]}},
  {"say": "A few tips. A hard day is actually useful, so don't apologize. No need to tidy up. And tell us what matters most to your family.",
   "v": {"kind": "chips", "kicker": "A few tips", "title": "Keep it real", "items": ["A hard day is useful", "No need to tidy up", "Say what matters to you"]}},
  {"say": "It helps to have ready: your doctor's letter or any evaluation, school or therapy reports, and a list of your child's favorite things.",
   "v": {"kind": "chips", "kicker": "Helpful to have ready", "title": "Don't stress", "items": ["Doctor's letter or evaluation", "School or therapy reports", "Your child's favorite things"]}},
  {"say": "Afterward, your Board Certified Behavior Analyst writes the plan and walks you through it, and we send it to your insurance for approval. Then we schedule your sessions. About every six months, we'll reassess together.",
   "cap": "Afterward, your Board Certified Behavior Analyst writes the plan and walks you through it, and we send it to your insurance for approval. Then we schedule your sessions. About every 6 months, we'll reassess together.",
   "v": {"kind": "steps", "kicker": "After the visits", "title": "From visits to sessions", "items": ["Board Certified Behavior Analyst writes the plan", "You read it together", "Insurance approval", "Sessions scheduled"]}},
  {"say": "Next up: how many hours a week ABA usually takes, and what your family will need to keep open.",
   "v": {"kind": "next", "kicker": "Up next", "title": "Lesson 5: How many hours?"}},
 ]},
# ------------------------------------------------------------------ 5
{"n": 5, "slug": "how-many-hours", "title": "How many hours?", "guide": "/guide/how-it-works/#hours",
 "blurb": "How many hours a week ABA usually takes, how your number is set, and what to keep open.",
 "beats": [
  {"say": "How many hours a week will this take? It's one of the first questions families ask, so here's a straight answer.",
   "v": {"kind": "title", "kicker": "Lesson 5 of 6", "title": "How many hours?", "icon": "i-star"}},
  {"say": "We ask families to keep at least ten hours a week open for sessions. That's our minimum, so there's enough time for new skills to really take hold.",
   "cap": "We ask families to keep at least 10 hours a week open for sessions. That's our minimum, so there's enough time for new skills to really take hold.",
   "v": {"kind": "chips", "kicker": "Our minimum", "title": "At least 10 hours a week", "items": ["Kept open for sessions", "Enough time for skills to stick"]}},
  {"say": "Most plans land somewhere between ten and forty hours a week. Focused programs, aimed at a few specific goals, are often ten to fifteen hours. Programs that cover more areas often run fifteen to twenty-five. And comprehensive programs, for children who need support in lots of areas, can be twenty-five hours or more.",
   "cap": "Most plans land somewhere between 10 and 40 hours a week. Focused programs, aimed at a few specific goals, are often 10 to 15 hours. Programs that cover more areas often run 15 to 25. And comprehensive programs, for children who need support in lots of areas, can be 25 hours or more.",
   "v": {"kind": "steps", "kicker": "Typical ranges", "title": "Hours a week", "items": ["Focused: about 10–15", "Broader: about 15–25", "Comprehensive: 25 or more"]}},
  {"say": "Your exact number comes from the assessment. Your Board Certified Behavior Analyst recommends hours based on your child's needs and your family's real life, and your insurance approves them.",
   "v": {"kind": "chips", "kicker": "Your number", "title": "Set by the assessment", "items": ["Your child's needs", "Your family's real life", "Insurance approval"]}},
  {"say": "Sessions are usually scheduled in blocks, like weekday mornings, early afternoons, or after school, built around school, daycare, and family time.",
   "v": {"kind": "steps", "kicker": "When sessions happen", "title": "In weekday blocks", "items": ["Mornings, 8 to 12", "Afternoons, 12 to 3", "After school, 3 to 6"]}},
  {"say": "On top of sessions, plan for family guidance with your Board Certified Behavior Analyst: at least two hours a month. And for in-home sessions, a parent or another trusted adult needs to be home.",
   "cap": "On top of sessions, plan for family guidance with your Board Certified Behavior Analyst: at least 2 hours a month. And for in-home sessions, a parent or another trusted adult needs to be home.",
   "v": {"kind": "chips", "kicker": "Also on the calendar", "title": "Your time, too", "items": ["Family guidance, 2 hrs a month", "An adult home for in-home sessions"]}},
  {"say": "Hours aren't forever. As your child's skills grow, hours usually come down, and we plan that step-down with you.",
   "v": {"kind": "chips", "kicker": "Over time", "title": "Hours change", "items": ["Skills grow", "Hours usually come down", "Planned together with you"]}},
  {"say": "Next up, the last lesson: your part, and what you can count on from us.",
   "v": {"kind": "next", "kicker": "Up next", "title": "Lesson 6: Your part"}},
 ]},
# ------------------------------------------------------------------ 6
{"n": 6, "slug": "your-part", "title": "Your part", "guide": "/guide/your-part/",
 "blurb": "The handful of things that make ABA work, and the promises we make in return.",
 "beats": [
  {"say": "ABA works best as a partnership. Here's what we'll ask of you, and what you can count on from us.",
   "v": {"kind": "title", "kicker": "Lesson 6 of 6", "title": "Your part", "icon": "i-home"}},
  {"say": "One: be home for in-home sessions. Two: family guidance with your Board Certified Behavior Analyst, at least two hours a month. It's where a lot of lasting change happens.",
   "cap": "One: be home for in-home sessions. Two: family guidance with your Board Certified Behavior Analyst, at least 2 hours a month. It's where a lot of lasting change happens.",
   "v": {"kind": "steps", "kicker": "What we ask", "title": "Six things", "focus": 2, "items": ["Be home for sessions", "Family guidance, 2 hrs/month", "Keep the schedule steady", "Give us a heads-up", "Keep insurance current", "Talk to us"]}},
  {"say": "Three: keep the schedule steady. Consistency is how skills stick. Four: give us a heads-up. Two weeks for vacations, and same-day cancellations by six a.m., by call or text.",
   "cap": "Three: keep the schedule steady. Consistency is how skills stick. Four: give us a heads-up. Two weeks for vacations, and same-day cancellations by 6 a.m., by call or text.",
   "v": {"kind": "steps", "kicker": "What we ask", "title": "Six things", "focus": 4, "items": ["Be home for sessions", "Family guidance, 2 hrs/month", "Keep the schedule steady", "Give us a heads-up", "Keep insurance current", "Talk to us"]}},
  {"say": "Five: keep your insurance current. Watch your mail for Health First Colorado renewal paperwork, and send it back quickly. A lapse in coverage is the most common reason therapy pauses.",
   "v": {"kind": "steps", "kicker": "What we ask", "title": "Six things", "focus": 5, "items": ["Be home for sessions", "Family guidance, 2 hrs/month", "Keep the schedule steady", "Give us a heads-up", "Keep insurance current", "Talk to us"]}},
  {"say": "Six: talk to us. If something isn't working, tell us, and we'll change it.",
   "v": {"kind": "steps", "kicker": "What we ask", "title": "Six things", "focus": 6, "items": ["Be home for sessions", "Family guidance, 2 hrs/month", "Keep the schedule steady", "Give us a heads-up", "Keep insurance current", "Talk to us"]}},
  {"say": "From us: the same friendly face whenever we can, a Board Certified Behavior Analyst who answers your questions, goals you agreed to, and honesty, always.",
   "cap": "From us: the same friendly face whenever we can, a Board Certified Behavior Analyst who answers your questions, goals you agreed to, and honesty, always.",
   "v": {"kind": "chips", "kicker": "What you can count on", "title": "Our side", "items": ["A familiar face", "Answers to your questions", "Goals you agreed to", "Honesty, always"]}},
  {"say": "It's a lot at first, and most families find their rhythm in a few weeks. You're not doing this alone. Questions? Call us at " + PHONE_CO_SAY + ".",
   "cap": "It's a lot at first, and most families find their rhythm in a few weeks. You're not doing this alone. Questions? Call us at " + PHONE_CO + ".",
   "v": {"kind": "phone", "kicker": "You're not alone", "title": "Call us anytime"}},
 ]},
]

def lesson(n):
    return LESSONS[n - 1]
