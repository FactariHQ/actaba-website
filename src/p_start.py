"""New-hire pre-start modules ("Before Day One") — content only.

Six short modules texted and emailed to new behavior technicians between offer acceptance and their first day.
Short links: actaba.com/start/1 … actaba.com/start/6, hub at actaba.com/start/.
The same data drives the web pages (p_startpages.py) and is mirrored into the drip engine's Modules tab
(takeaways and text copy), so edit the copy here first.

House rules for this copy: no software vendor names, no pay figures, no client details, US spelling,
never describe early sessions as "becoming friends" (it is building trust), and never promise a timeline we
do not control.
"""

ADMIN_LINES = {
    "Colorado": ("(720) 432-8989", "+17204328989"),
    "Oklahoma": ("(918) 764-8544", "+19187648544"),
    "North Carolina": ("(336) 270-9453", "+13362709453"),
}

def tel(region):
    shown, raw = ADMIN_LINES[region]
    return f'<a href="tel:{raw}">{shown}</a>'

ADMIN_ALL = " · ".join(f"{r} {tel(r)}" for r in ADMIN_LINES)

MODULES = [
  {
    "n": 1, "slug": "welcome", "minutes": 5,
    "title": "Welcome to Adventure Child Therapy",
    "blurb": "Who we are, what a behavior technician does here, who is on your team, and the five questions we ask ourselves every day.",
    "sections": [
      ("Who we are",
       "<p>Adventure Child Therapy (ACT) is a small, clinician-led ABA practice. We have been serving kids and families since 2021: in-home across the Denver metro, Grand Junction and Pueblo in Colorado; at our Tulsa center and in homes around Ada in Oklahoma; and in homes and the community around Charlotte and Thomasville in North Carolina.</p>"
       "<p>Small is on purpose. It means the people who make decisions know the families, know the technicians, and can fix problems quickly.</p>"),
      ("What a behavior technician does here",
       "<p>You are the person a child sees most. You run one-on-one sessions in the child’s home, community, daycare, school or our center, following a treatment plan written by a Board Certified Behavior Analyst (BCBA). During every session you collect data on how the child is doing, and that data is what the BCBA uses to decide what to change.</p>"
       "<p>You will never be asked to invent a plan or make clinical calls on your own. Your job is to deliver the plan well, notice what is happening, and tell your BCBA.</p>"),
      ("Your team",
       "<ul class=\"ticks\">"
       "<li><span><strong>Your BCBA</strong> writes each child’s plan, supervises your sessions, and is your first stop for any clinical question.</span></li>"
       "<li><span><strong>Lead RBTs</strong> are experienced technicians who train you on each child before you work with that child on your own.</span></li>"
       "<li><span><strong>The admin team</strong> builds your schedule and is your point of contact from now until your first day, and for anything schedule-related after that.</span></li>"
       "<li><span><strong>Our leadership team</strong> covers operations, clinical quality and people. You will meet them, and their doors are open.</span></li>"
       "</ul>"),
      ("Five questions we ask ourselves",
       "<p>Our clinical values are written as questions because they are things we keep checking, not boxes we ticked once.</p>"
       "<ol class=\"vals\">"
       "<li><strong>Exceptional Clinical Care.</strong> Are we doing excellent behavior analysis?</li>"
       "<li><strong>Understand, Don’t Judge.</strong> Are we approaching people behaviorally, compassionately, and with dignity?</li>"
       "<li><strong>Build Bigger Lives.</strong> Are we improving what actually matters in the child’s life?</li>"
       "<li><strong>Make It Work in the Real World.</strong> Does treatment actually work across the places the child’s life happens?</li>"
       "<li><strong>Collaborate &amp; Be Transparent.</strong> Are we working openly and effectively with families, schools and daycares, outside partners, and one another?</li>"
       "</ol>"
       "<p>One of the four ways we measure our own success is <strong>Behavior Technician Support</strong>: technicians who feel trained, supported, and confident. If you ever do not feel that way, we want to hear it.</p>"),
    ],
    "takeaways": [
      "You run one-on-one sessions and collect data; a BCBA writes the plan and supervises.",
      "A Lead RBT trains you on each child before you work with that child on your own.",
      "The admin line is your point of contact until your first day.",
    ],
    "action": "Save the admin line in your phone as “ACT Admin” so our texts never look like spam.",
    "quiz": [
      ("Who writes a child’s treatment plan?",
       ["The behavior technician", "The child’s Board Certified Behavior Analyst (BCBA)", "The admin team"], 1,
       "The BCBA writes and adjusts the plan. You deliver it and collect the data the BCBA uses to make changes."),
      ("Which value asks whether treatment works across the places the child’s life actually happens?",
       ["Make It Work in the Real World", "Build Bigger Lives", "Exceptional Clinical Care"], 0,
       "A skill only counts when it shows up at home, at daycare, at the store and with new people, not just in sessions."),
      ("Before your first day, who is your main point of contact?",
       ["Your recruiter", "Your future BCBA", "The ACT admin line"], 2,
       "The admin team builds your schedule and sends your welcome details, so they are the people to text or call."),
    ],
  },
  {
    "n": 2, "slug": "first-weeks", "minutes": 5,
    "title": "What your first two weeks look like",
    "blurb": "What to finish before day one, when your welcome email arrives, what to bring, and how training works.",
    "sections": [
      ("Before your first day",
       "<ul class=\"ticks\">"
       "<li><span><strong>Finish your payroll onboarding.</strong> You received an email invitation to set up your payroll account (tax forms and direct deposit). Please finish it before day one so we can pay you on time. Can’t find the email? Check spam, then text the admin line.</span></li>"
       "<li><span><strong>Complete your background checks.</strong> We will send you what you need. Please do these quickly; you cannot work with children until they clear.</span></li>"
       "<li><span><strong>Send us a photo.</strong> We share it with your new teammates so they recognize you on your first day.</span></li>"
       "<li><span><strong>Watch your personal email and texts.</strong> Everything comes to the personal email and phone number you gave us until your ACT accounts are set up.</span></li>"
       "</ul>"),
      ("The Friday before you start",
       "<p>Schedules are finalized on Fridays, so your <strong>welcome email arrives by the end of the day on the Friday before your start date</strong>. It has your onboarding meeting date, time and address, the name of the person onboarding you, and the times to keep open for training sessions in your first week. We also text you to confirm you got it.</p>"
       "<p>We know waiting for details is hard. It comes Friday because that is when it is accurate, and an early email with the wrong times would be worse.</p>"
       "<div class=\"callout\"><span class=\"tag\">Bring</span><p class=\"small\">Your ID for employment paperwork: a passport, <em>or</em> a driver’s license plus your Social Security card or birth certificate.</p></div>"),
      ("Your first day",
       "<p>On the morning of your onboarding meeting, the admin team texts you your trainer’s name, start time, address and phone number. Please reply so we know you have it. At the meeting we set you up with your ACT email and the apps you will use for your schedule, team chat and session data.</p>"),
      ("How training works",
       "<p>For your first sessions you are scheduled alongside a Lead RBT or a BCBA. They model, coach and give you feedback using our training evaluations, and you are trained on <strong>each child</strong> before you work with that child on your own. Being available for a session does not mean you are trained on that child yet, and we never skip that step.</p>"
       "<p>Most new technicians are working independently on a case within two to three weeks. If we cannot book a trainer for one of your scheduled times early on, we tell you, and that time is paid time for your RBT coursework instead (more on that in module 3).</p>"),
    ],
    "takeaways": [
      "Finish payroll onboarding and background checks before day one.",
      "Your welcome email with your onboarding time and place arrives by end of day the Friday before you start.",
      "Bring a passport, or a driver’s license plus a Social Security card or birth certificate.",
    ],
    "action": "Open your payroll onboarding email today and finish any steps that are left.",
    "quiz": [
      ("When does your welcome email with your onboarding details arrive?",
       ["As soon as you accept the offer", "By end of day the Friday before your start date", "The morning of your first day"], 1,
       "Schedules are finalized on Fridays, so that is when the details are accurate."),
      ("Which of these can you bring as ID for your employment paperwork?",
       ["A passport", "A school ID", "A photo of your driver’s license"], 0,
       "A passport on its own works. Otherwise bring a driver’s license plus a Social Security card or birth certificate."),
      ("When can you work with a child on your own?",
       ["After your onboarding meeting", "As soon as you are available at that time", "After a Lead RBT or BCBA has trained you on that child"], 2,
       "Training is per child. You work independently with a child only after you have been trained on that child."),
    ],
  },
  {
    "n": 3, "slug": "rbt", "minutes": 6,
    "title": "Your RBT head start",
    "blurb": "What the Registered Behavior Technician credential is, the 45-day rule, the steps, and exactly what ACT pays for.",
    "sections": [
      ("What an RBT is",
       "<p>A Registered Behavior Technician (RBT) is a credential from the Behavior Analyst Certification Board (BACB). It shows you have the training and verified skills to deliver ABA under a BCBA’s supervision. Insurers, including Medicaid, require it.</p>"),
      ("The 45-day rule",
       "<div class=\"callout\"><span class=\"tag\">Required</span><p>The RBT credential is a requirement of your job. If you are hired without it, you need to earn it <strong>within 45 days of your start date</strong> to keep your position.</p></div>"
       "<p>That is very doable, and we will help. It is much easier if you plan it from the start instead of discovering it in week five.</p>"),
      ("The steps",
       "<ol class=\"steps\">"
       "<li><strong>Complete the 40-hour RBT training course.</strong> It is online and self-paced. We will tell you which course to use and how to enroll.</li>"
       "<li><strong>Pass your Initial Competency Assessment.</strong> A BCBA watches you perform the RBT skills, partly with real clients. We set this up for you once you are working.</li>"
       "<li><strong>Clear your background check.</strong></li>"
       "<li><strong>Apply in your BACB account.</strong> You create a free account at bacb.com and submit your application there.</li>"
       "<li><strong>Pass the RBT exam.</strong> It is a multiple-choice test taken at a Pearson VUE testing center.</li>"
       "</ol>"),
      ("What ACT pays for, and what it doesn’t",
       "<div class=\"grid c2\">"
       "<div class=\"card\"><h3>We pay for</h3><ul class=\"ticks\"><li><span>The 40-hour training course</span></li><li><span>Your first exam attempt</span></li><li><span>Your background check</span></li><li><span>Your child abuse and neglect check</span></li><li><span>Your competency assessment, done by our BCBAs with our clients</span></li></ul></div>"
       "<div class=\"card\"><h3>Good to know</h3><ul class=\"ticks neg\"><li><span>Time spent studying or doing coursework is not paid.</span></li><li><span>The one exception: in your first four weeks, if we cannot provide a trainer for your committed schedule, you are paid for that scheduled time to work on your RBT coursework.</span></li></ul></div>"
       "</div>"),
      ("How to get ahead",
       "<p>Starting the course before your first day is optional, and like other study time it is unpaid. But people who have the course mostly done by the end of their second week find the 45 days relaxed instead of tight. A pace of about two hours a day finishes the course in four weeks.</p>"
       "<p><strong>Already an RBT?</strong> Great. Make sure your certification is active and text the admin line your name exactly as it appears with the BACB so we can verify it.</p>"),
    ],
    "takeaways": [
      "If you aren’t an RBT yet, you need the credential within 45 days of your start date.",
      "ACT pays for the 40-hour course, your first exam attempt, both background checks, and the competency assessment.",
      "Study time is unpaid, except scheduled time we can’t fill with a trainer in your first four weeks.",
    ],
    "action": "Text the admin line “RBT course” and we’ll send you how to enroll in the course ACT pays for. Already an RBT? Text your name as it appears with the BACB.",
    "quiz": [
      ("If you start without the RBT credential, how long do you have to earn it?",
       ["45 days from your start date", "6 months", "There is no deadline"], 0,
       "The RBT credential is a job requirement, and the window is 45 days from your start date."),
      ("Which of these does ACT pay for?",
       ["Every hour you spend studying", "Your first RBT exam attempt", "Unlimited exam retakes"], 1,
       "ACT pays for the course, the first exam attempt, your background checks and the competency assessment. Study time is not paid, with one exception."),
      ("Who completes your Initial Competency Assessment?",
       ["A BCBA, with real clients", "You, as an online quiz", "The testing center"], 0,
       "A BCBA observes you performing RBT skills, and ACT arranges it once you are working with clients."),
    ],
  },
  {
    "n": 4, "slug": "why-behavior-happens", "minutes": 6,
    "title": "ABA basics 1: Why behavior happens",
    "blurb": "The ABCs of behavior, what reinforcement really means, why every behavior has a purpose, and how we build trust first.",
    "sections": [
      ("Behavior is anything a person does",
       "<p>ABA stands for applied behavior analysis: the science of how behavior is learned, used to teach skills that matter. In ABA, “behavior” is not a polite word for misbehavior. Saying “cookie,” washing hands, crying, and throwing a toy are all behaviors. If you can see it or count it, it is behavior.</p>"),
      ("The ABCs",
       "<p>Every behavior sits between two things:</p>"
       "<div class=\"abc\"><div><b>A</b><span>Antecedent</span><p>What happened right before</p></div><div><b>B</b><span>Behavior</span><p>What the person did</p></div><div><b>C</b><span>Consequence</span><p>What happened right after</p></div></div>"
       "<p><em>Example:</em> Mom puts the tablet away (A). Sam drops to the floor and cries (B). Mom gives the tablet back (C). Change the A or the C and, over time, the B changes too. That is the core idea behind nearly everything you will do.</p>"),
      ("Reinforcement",
       "<p><strong>Reinforcement is any consequence that makes a behavior more likely to happen again.</strong> It is defined by what it does, not by whether it is nice. Praise is only a reinforcer if it actually increases the behavior for that child. In the example above, getting the tablet back reinforced crying.</p>"
       "<p>“Positive” and “negative” do not mean good and bad. Positive means something is <em>added</em> (a high five, a toy). Negative means something is <em>taken away</em> (a hard task ends, a loud noise stops). Both make behavior more likely.</p>"),
      ("Every behavior has a purpose",
       "<p>Behavior keeps happening because it works for the person. We call that its <strong>function</strong>. The common ones are getting attention, getting an item or activity, escaping or avoiding something, and the way something feels (sensory). The same behavior can serve different functions for different kids, which is why your BCBA’s plan is specific to each child, and why you follow it exactly.</p>"),
      ("Build trust first",
       "<p>Your first sessions with a child are about <strong>building trust</strong>: you become someone associated with good things before you ask for anything hard. In ABA this is called pairing. It can look like a lot of play. It is on purpose, and it is clinical work.</p>"),
      ("Understand, don’t judge",
       "<p>Describe what you see, not what you think it means. “He hit the table twice and pushed the worksheet off” is useful. “He was being manipulative” is a guess about his insides, and it makes it harder to help. Kids are not giving you a hard time. They are having a hard time, and the behavior is telling you something.</p>"),
    ],
    "takeaways": [
      "Look at what happens before (A) and after (C) a behavior (B).",
      "Reinforcement is anything that makes a behavior more likely, defined by its effect, not by whether it’s nice.",
      "Every behavior serves a purpose; describe what you see without judging it.",
    ],
    "action": "Today, catch one ABC in everyday life (yours, a pet’s, a stranger’s in line) and name the A, B and C.",
    "quiz": [
      ("In ABA, what is reinforcement?",
       ["A reward the adult likes to give", "Any consequence that makes a behavior more likely to happen again", "A consequence that stops a behavior"], 1,
       "Reinforcement is defined by its effect. If the behavior doesn’t increase, it wasn’t a reinforcer for that child."),
      ("“Negative reinforcement” means…",
       ["Something is taken away, and the behavior becomes more likely", "Punishing a behavior", "Ignoring a child"], 0,
       "Negative means removal. When crying ends a hard task, escape from the task can reinforce crying."),
      ("Which note follows “Understand, Don’t Judge”?",
       ["“She was being defiant all session.”", "“He was trying to manipulate me.”", "“She said ‘no’ and walked away from the table three times.”"], 2,
       "Describe observable behavior. It is fair to the child and gives your BCBA something to work with."),
    ],
  },
  {
    "n": 5, "slug": "how-we-teach", "minutes": 6,
    "title": "ABA basics 2: How we teach",
    "blurb": "Prompts and fading, structured and natural teaching, motivation, and why a skill isn’t learned until it works in the real world.",
    "sections": [
      ("You teach from the plan",
       "<p>Each child has teaching programs written by their BCBA: what skill, how to ask, how to help, and what counts as correct. Your job is to run those programs the same way every time. Consistency is what lets a child learn quickly, and what lets your BCBA trust the data.</p>"),
      ("Prompts: just enough help",
       "<p>A <strong>prompt</strong> is help that makes the right response likely. From most help to least, prompts usually look like this:</p>"
       "<div class=\"ladder\"><span>Full physical</span><span>Partial physical</span><span>Model</span><span>Gesture</span><span>Verbal</span><span>Independent</span></div>"
       "<p>The goal is always to <strong>fade</strong> prompts so the child does the skill without us. Help that never fades turns into prompt dependence, where a child waits for you instead of responding. The program tells you which prompts to use and when to back off.</p>"),
      ("Two ways to teach",
       "<div class=\"grid c2\">"
       "<div class=\"card\"><h3>Structured (discrete trial) teaching</h3><p class=\"small muted\">Short, clear practice rounds: an instruction, the child’s response, then a consequence. Great for building a new skill quickly with lots of practice.</p></div>"
       "<div class=\"card\"><h3>Natural environment teaching</h3><p class=\"small muted\">Teaching inside play and daily routines, following the child’s interests. Asking for “bubbles” while blowing bubbles is the lesson.</p></div>"
       "</div><p>Most sessions mix both. Your BCBA decides the balance for each child.</p>"),
      ("Motivation runs the show",
       "<p>Children learn best when they want something. A child who just had a snack will not work hard for crackers. Part of your job is noticing what a child wants <em>right now</em> and using it, which is why a favorites list and a little setup before a session matter so much.</p>"),
      ("Make it work in the real world",
       "<p>A skill is not learned until it shows up with different people, in different places, with different materials. That is called <strong>generalization</strong>. Saying “help” to you at the table is a start. Saying “help” to Dad at the park is the goal.</p>"),
      ("Behavior plans",
       "<p>Some children have a behavior plan for challenging behavior. It says what to do before, during and after. Follow it exactly, every time, even when it feels slow. Doing something different “just this once” can teach a child that the challenging behavior works.</p>"),
    ],
    "takeaways": [
      "Run each program exactly as the BCBA wrote it; consistency is what makes kids learn.",
      "Use the least help that works, and fade prompts so the child does the skill on their own.",
      "A skill is learned when it works with new people, places and things (generalization).",
    ],
    "action": "Think of something you learned with help (driving, a recipe). Name the prompts you got and how they faded.",
    "quiz": [
      ("What is the goal with prompts?",
       ["Use as many as possible so the child is always right", "Fade them so the child does the skill independently", "Only use verbal prompts"], 1,
       "Prompts are temporary. Fading them is how a skill becomes the child’s own."),
      ("Asking for “bubbles” while you blow bubbles during play is an example of…",
       ["Natural environment teaching", "A behavior plan", "Prompt dependence"], 0,
       "Teaching inside play and routines, using what the child wants right now."),
      ("A child says “help” to you at the table but not to Dad at home. That skill still needs…",
       ["More prompts", "Generalization", "A new BCBA"], 1,
       "Generalization means the skill shows up with other people, places and materials."),
    ],
  },
  {
    "n": 6, "slug": "data-and-dignity", "minutes": 6,
    "title": "ABA basics 3: Data, dignity and doing it right",
    "blurb": "Why your data drives every decision, how to write notes anyone could check, protecting families’ privacy, and the professional basics.",
    "sections": [
      ("Your data drives every decision",
       "<p>Your BCBA is not in most of your sessions. The data you take is how they see what happened, and it decides whether a program moves forward, changes or stops. Take data <strong>in the moment</strong>, not from memory at the end. You will learn the app at onboarding; these are the main kinds you will use:</p>"
       "<ul class=\"ticks\">"
       "<li><span><strong>Count (frequency):</strong> how many times something happened.</span></li>"
       "<li><span><strong>Duration:</strong> how long it lasted.</span></li>"
       "<li><span><strong>Trial by trial:</strong> for each try, correct, incorrect, or prompted (and which prompt).</span></li>"
       "<li><span><strong>ABC notes:</strong> what came before and after a behavior.</span></li>"
       "</ul>"),
      ("Write notes anyone could check",
       "<p>Good notes are <strong>observable and measurable</strong>: someone else watching the same session would agree.</p>"
       "<div class=\"grid c2\"><div class=\"card\"><span class=\"k\">Instead of</span><p>“Rough session, he was upset most of the time.”</p></div>"
       "<div class=\"card\"><span class=\"k\">Write</span><p>“Cried 3 times (about 4 minutes total), each after the tablet was removed. Calmed within 2 minutes when offered a choice of two toys.”</p></div></div>"),
      ("Protect families’ privacy",
       "<ul class=\"ticks\">"
       "<li><span>Never post or share a client’s name, photo, address, school or anything that could identify them, including on social media and in personal texts.</span></li>"
       "<li><span>Talk about clients only with their team, in the places we set up for it.</span></li>"
       "<li><span>If a parent asks a clinical question you are not sure about, it is a good question for the BCBA. “Great question, I’ll make sure your BCBA sees it” is always a professional answer.</span></li>"
       "</ul>"),
      ("Professional basics",
       "<ul class=\"ticks\">"
       "<li><span><strong>Be on time and ready.</strong> Families plan their day around you. If you are running late or need to cancel, you will use our official process, which you’ll learn at onboarding, as early as you can.</span></li>"
       "<li><span><strong>Keep the relationship professional.</strong> Warm, yes. But no babysitting, side jobs or social media friendships with client families. RBTs follow the BACB’s RBT Ethics Code, and these lines protect you and the family.</span></li>"
       "<li><span><strong>In-home sessions need an adult home.</strong> A parent or another trusted adult stays nearby for every in-home session.</span></li>"
       "<li><span><strong>When something worries you, say so.</strong> If anything about a child’s safety or wellbeing concerns you, tell your BCBA that day. You’ll cover reporting duties in detail during training.</span></li>"
       "<li><span><strong>Ask.</strong> Nobody expects you to know everything in week one. Asking early is how good technicians get good.</span></li>"
       "</ul>"),
      ("You’re ready",
       "<p>That is the foundation. Your trainers will build on every piece of it, with real kids, in real sessions. Your welcome email comes the Friday before you start. We are glad you are here.</p>"),
    ],
    "takeaways": [
      "Take data in the moment; your BCBA makes decisions from it.",
      "Write notes someone else watching would agree with: what you saw, how often, how long.",
      "Never share anything that could identify a client, and bring clinical questions to the BCBA.",
    ],
    "action": "Reply to our text or email with one question you have about your first week. We’ll answer it before you start.",
    "quiz": [
      ("When should you record session data?",
       ["In the moment, during the session", "At the end of the day, from memory", "Only when something goes wrong"], 0,
       "Data taken in the moment is accurate, and your BCBA makes decisions from it."),
      ("Which is an observable, measurable note?",
       ["“He had a bad attitude today.”", "“She threw the puzzle 2 times after being asked to clean up.”", "“Session went fine.”"], 1,
       "Anyone watching would agree on what happened and how often."),
      ("A parent asks you a clinical question you’re unsure about. What’s the best response?",
       ["Give your best guess", "Look it up online together", "Let them know you’ll make sure their BCBA sees the question"], 2,
       "Clinical guidance comes from the BCBA. Passing it along is professional, not unhelpful."),
    ],
  },
]

def module(n):
    return MODULES[n - 1]
