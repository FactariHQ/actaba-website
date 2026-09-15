from p_shared import *

def phead_pro(eyebrow, title, lede, glance, anchors):
    g = "".join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in glance)
    a = '<nav class="anchors" aria-label="On this page">' + "".join(f'<a href="{h}">{t}</a>' for h, t in anchors) + '</nav>'
    return f'''<section class="phead-pro"><div class="wrap">
  <div class="stack g14"><span class="hand">{eyebrow}</span><h1>{title}</h1><p class="lede measure">{lede}</p>{a}</div>
  <dl class="glance">{g}</dl>
</div></section>'''

def sec_head(label, title, lede=None):
    l = f'<p class="muted measure">{lede}</p>' if lede else '<span></span>'
    return f'<div class="sec-head"><div class="stack g10"><span class="hand">{label}</span><h2>{title}</h2></div>{l}</div>'

def providers():
    inst = "refform"
    form = f'''<form class="act" data-form="referral" data-inst="{inst}" novalidate>
      <div class="f2">{field(inst,"ref_name","Your name",required=True,auto="name")}{field(inst,"ref_org","Practice or organization",required=True,auto="organization")}</div>
      <div class="f2">{field(inst,"ref_email","Email",typ="email",required=True,auto="email")}{field(inst,"ref_phone","Phone",typ="tel",auto="tel")}</div>
      <div class="f2">{field(inst,"ref_role","Your role",kind="select",options=["Pediatrician / physician","Diagnosing psychologist","School or district team","Case manager","SLP / OT / PT","Other"])}{field(inst,"ref_region","Family’s area",kind="select",required=True,options=["Denver metro","Grand Junction / Western Slope","Pueblo / Southern Colorado","Tulsa","Ada","Elsewhere — tell us below"])}</div>
      <div class="f2">{field(inst,"ref_dx","Documentation",kind="select",required=True,options=["Physician letter recommending ABA (Colorado)","Diagnostic evaluation complete — report available","Evaluation in progress","Neither yet"])}{field(inst,"ref_payer","Payer",kind="select",options=["Health First Colorado","SoonerCare / SoonerSelect","Commercial","Unknown"])}</div>
      {field(inst,"ref_notes","Routing notes",kind="textarea",placeholder="Area, urgency, caregiver availability, and whether the family expects our call. Do not include protected health information — records are collected through a secure link.")}
      {consent(inst)}
      <div><button class="btn btn-primary" type="submit">Submit referral {ARROW}</button></div>
      <div class="form-status" role="status" aria-live="polite" data-status></div>
    </form>'''
    glance = [
      ("Fax", '<span class="tnum">(303) 374-5911</span>'),
      ("Colorado", CO_TEL),
      ("Oklahoma", OK_TEL),
      ("Service areas", "Denver metro, Grand Junction, Pueblo, Tulsa, Ada"),
      ("Payers", "Health First Colorado, SoonerCare and SoonerSelect, commercial plans after verification"),
    ]
    return f'''<div data-route="providers" class="pro" data-title="For providers | Adventure Child Therapy" hidden>
{phead_pro("For referring providers", "Referral information", "For pediatricians, diagnosticians, school teams, case managers and allied health providers: what to send, how referrals are handled, and what you can expect from us after the handoff.", glance,
  [("#/providers#referral-requirements","Requirements"),("#/providers#coverage","Coverage"),("#/providers#records","Records"),("#/providers#refer","Submit a referral")])}

<section class="sec" id="referral-requirements" style="scroll-margin-top:90px"><div class="wrap stack g28">
  {sec_head("Requirements", "What to send, and what happens next", "Documentation requirements differ by state. Colorado does not require an autism diagnosis to begin ABA; Oklahoma does.")}
  <div class="grid c3">
    <div class="card"><span class="k">Documentation</span><h3>What to send</h3>{ticks(["Colorado: a letter from the child’s physician recommending ABA — an autism diagnosis is not required to start","Oklahoma: the diagnostic evaluation report (ASD or other qualifying diagnosis)","Caregiver name and best contact number","Insurance carrier and member ID","Any prescription or order the payer requires","Relevant IEP, related-service or medical notes, where you have consent to share them"])}</div>
    <div class="card"><span class="k">Our commitments</span><h3>What we do</h3>{ticks(["We contact the family directly; you do not need to follow up to complete the handoff.","If we cannot serve the family’s area or plan, we tell you promptly rather than holding the referral.","We do not give families a start date we cannot keep.","With consent, we coordinate with you: IEP meetings, progress data, and a named supervising BCBA."])}</div>
    <div class="card"><span class="k">Limitations</span><h3>What we cannot do</h3>{ticks(["In Oklahoma, ABA cannot begin without a diagnostic evaluation on file.","ABA delivered in a school setting is not reimbursable by Medicaid except on a time-limited basis during a transition into or out of clinic.","We do not recommend hours before an assessment."], "ticks neg")}</div>
  </div>
  <div class="callout"><span class="tag">Colorado</span><p class="muted"><strong>No diagnosis is required to refer.</strong> A letter from you recommending ABA is sufficient to start services. Please send the referral rather than holding it while the family waits for an evaluation. Oklahoma referrals do require a diagnostic evaluation on file.</p></div>
</div></section>

<section class="sec band" id="coverage" style="scroll-margin-top:90px"><div class="wrap stack g28">
  {sec_head("Coverage", "Service areas and payers")}
  <div class="lead-list">
    <div><h4>Colorado</h4><p class="muted">Denver metro, Grand Junction and Pueblo. In-home and community-based services, including daycare and school settings where the treatment plan calls for it. Billed to Health First Colorado and commercial plans after benefit verification.</p></div>
    <div><h4>Oklahoma</h4><p class="muted">Tulsa and Tulsa County: center-based services at 1217 East 48th Street, Suite 101, plus in-home services. Ada and nearby communities: in-home services. Billed to SoonerCare, SoonerSelect plans (Aetna Better Health of Oklahoma, Blue Cross and Blue Shield of Oklahoma, Oklahoma Complete Health, Humana Healthy Horizons) and commercial plans after benefit verification.</p></div>
    <div><h4>Outside these areas</h4><p class="muted">Please refer anyway and note the family’s location. We track unmet demand by ZIP code, and it informs where we open next, beginning with North Carolina.</p></div>
  </div>
</div></section>

<section class="sec" id="records" style="scroll-margin-top:90px"><div class="wrap split" style="align-items:start">
  <div class="stack g14">
    <span class="hand">Records</span>
    <h2>Sending records securely</h2>
    <p class="muted measure">Do not attach protected health information to the referral form. Submit the referral, and we will reply with a secure link for the diagnostic report and any records you have consent to share.</p>
  </div>
  <div class="card stack g14">
    <div class="lead-list" style="border-top:0">
      <div style="grid-template-columns:minmax(0,.8fr) minmax(0,1.4fr)"><span class="k">Fax</span><span class="tnum">(303) 374-5911</span></div>
      <div style="grid-template-columns:minmax(0,.8fr) minmax(0,1.4fr)"><span class="k">Colorado</span><span>{CO_TEL}</span></div>
      <div style="grid-template-columns:minmax(0,.8fr) minmax(0,1.4fr)"><span class="k">Oklahoma</span><span>{OK_TEL}</span></div>
      <div style="grid-template-columns:minmax(0,.8fr) minmax(0,1.4fr);border-bottom:0"><span class="k">Email</span><span><a href="mailto:info@actaba.com">info@actaba.com</a> <span class="tiny">(no clinical details)</span></span></div>
    </div>
  </div>
</div></section>

<section class="sec band" id="refer" style="scroll-margin-top:90px"><div class="wrap">
  <div class="panel stack g20" id="refform-form">
    <div class="stack g10"><span class="hand">Referral</span><h2>Submit a referral</h2><p class="muted measure">One form, no account or portal. We will contact the family and confirm the outcome with you.</p></div>
    {form}
  </div>
</div></section>
</div>'''

JOBS_PRO = [
  ("rbt-denver-ft","Full-time Registered Behavior Technician","Denver metro · In-home","Full-time, salaried",
   "Salaried. Base pay does not change when a family cancels; billable hours above the base are paid in addition. Figures are provided on the first screening call.",
   "Salary stability without the variability of hourly pay.",
   ["Approximately 7 sessions per week, Monday–Friday; afternoon and 3–6pm availability preferred","Base set against 23 billable hours per week, with hours above the base paid in addition","Consistent caseload within your geographic region","Accessible BCBA supervision","Mileage reimbursed; drive time is not paid hourly","Serving ZIP codes 80011, 80017, 80108, 80110, 80138, 80231, 80234, 80247"]),
  ("rbt-denver-pt","Part-time Behavior Technician / RBT","Denver metro · In-home","Part-time",
   "Hourly, based on experience, certification and performance. The rate is provided on the first screening call.",
   "Structured, supervised part-time clinical work with consistent hours.",
   ["Under 23 billable hours per week, paid for direct service time","Afternoon (12–3pm) and early evening (3–6pm) availability strongly preferred","Minimum availability: two days per week, or 10–12 hours","RBT certification support for uncertified candidates","Pathway to full-time salaried and Lead RBT roles"]),
  ("rbt-gj-ft","Full-time Registered Behavior Technician","Grand Junction · In-home","Full-time, salaried",
   "Salaried, with billable hours above the base paid in addition. Figures are provided on the first screening call.",
   "Western Slope families face some of the longest waits for ABA in Colorado. This role directly expands local access.",
   ["Approximately 7 sessions per week, Monday–Friday","Consistent caseload, clustered to limit drive time","Paid training and professional development","Mileage reimbursed"]),
  ("rbt-gj-pt","Part-time Behavior Technician / RBT","Grand Junction · In-home","Part-time",
   "Hourly, based on experience and certification. The rate is provided on the first screening call.",
   "Consistent afternoon and early-evening sessions with local supervision.",
   ["Under 23 billable hours per week","Afternoon and early evening availability preferred","Minimum availability: two days per week, or 10–12 hours","RBT certification support for uncertified candidates"]),
  ("rbt-tulsa","Behavior Technician / RBT","Tulsa · Center-based","Full-time and part-time",
   "Hourly for full-time and part-time, on set shifts at our Tulsa center. The rate is provided on the first screening call.",
   "Center-based work on scheduled shifts, alongside an on-site clinical team.",
   ["Set shifts at the center, with no driving between family homes","On-site team, with Lead RBTs leading onboarding","Paid training, including Safety-Care certification","Spanish-speaking candidates especially encouraged to apply"]),
  ("bcba","Board Certified Behavior Analyst (BCBA)","Denver · Grand Junction · Tulsa","Full-time",
   "Competitive compensation, discussed directly on the first call.",
   "A caseload sized for meaningful supervision, dedicated administrative support, and a leadership team with direct clinic operations experience.",
   ["Caseloads sized so supervision is substantive","Dedicated administrative team for scheduling, authorizations and billing","Input into hiring and case assignment","BACB CEUs supported"]),
]

def careers():
    inst = "applyform"
    jobs = "".join(f'''<details class="job" id="{jid}"><summary><span><span class="jt">{t}</span><span class="jm">{loc} · {kind}</span></span><span class="plus" aria-hidden="true">+</span></summary>
      <div class="job-body"><p class="pay">{pay}</p><p class="muted measure">{blurb}</p>{ticks(items)}<div>{btn("#/careers#apply","Apply for this role",extra="btn-sm")}</div></div></details>''' for jid, t, loc, kind, pay, blurb, items in JOBS_PRO)
    roles = [f"{t} — {loc.replace(' · ', ' — ')}" for _, t, loc, *_ in JOBS_PRO] + ["Other — describe below."]
    form = f'''<form class="act" data-form="careers" data-inst="{inst}" novalidate>
      <div class="f2">{field(inst,"app_name","Full name",required=True,auto="name")}{field(inst,"app_email","Email",typ="email",required=True,auto="email")}</div>
      <div class="f2">{field(inst,"app_phone","Phone",typ="tel",required=True,auto="tel")}{field(inst,"app_role","Position",kind="select",required=True,options=roles)}</div>
      <div class="f2">{field(inst,"app_cert","Certification",kind="select",options=["RBT — active","BCaBA","BCBA","Not yet certified, willing to pursue","Other"])}{field(inst,"app_zip","Home ZIP code",required=True,auto="postal-code",hint="Colorado in-home cases are clustered to keep commutes to 30 minutes or less.")}</div>
      {field(inst,"app_avail","Weekly availability",kind="textarea",required=True,rows=3,placeholder="Days and time blocks. Most sessions fall in the afternoon and 3–6pm. Minimum to hire: two days per week or 10–12 hours.")}
      {field(inst,"app_notes","Additional information",kind="textarea",rows=3)}
      {consent(inst)}
      <div><button class="btn btn-primary" type="submit">Submit application {ARROW}</button></div>
      <div class="form-status" role="status" aria-live="polite" data-status></div>
    </form>'''
    glance = [
      ("Open roles", f'<span class="tnum">{len(JOBS_PRO)}</span> positions'),
      ("Locations", "Denver metro, Grand Junction, Tulsa"),
      ("Employment", "Colorado in-home: salaried or hourly. Tulsa center: hourly shifts"),
      ("Compensation", "Provided on the first screening call"),
    ]
    pil = '<div class="grid c4">' + "".join(f'<div class="card"><h3>{t}</h3><p class="small muted">{d}</p></div>' for t, d, _ in PILLARS) + '</div>'
    ben = "".join(f'<div class="card"><h4>{t}</h4><p class="small muted">{d}</p></div>' for t, d in [
      ("Paid time off and paid sick time", "Accrued and usable."),
      ("Paid training", "Including Safety-Care (QBS) crisis-procedure certification."),
      ("Certification reimbursement", "RBT, BCaBA and BCBA exam costs are reimbursed."),
      ("Mileage reimbursement", "For Colorado in-home roles. Drive time is not paid hourly, and we disclose this on the first screening call."),
      ("Professional development", "CEU support and a defined pathway from BT to RBT to Lead RBT and full-time roles."),
      ("Scheduling by setting", "Colorado in-home schedules are built from your availability, with a target commute of 30 minutes or less. Tulsa center roles work set shifts on site."),
    ])
    return f'''<div data-route="careers" class="pro" data-title="Careers | Adventure Child Therapy" hidden>
{phead_pro("Careers", "Clinical careers at Adventure Child Therapy", "Behavior technician, RBT and BCBA positions in Colorado and Oklahoma. Terms are stated plainly and differ by setting: Colorado in-home technicians are salaried full-time or hourly part-time, with schedules built from their availability; Tulsa center technicians are hourly and work set shifts at the center.", glance,
  [("#/careers#pay","Pay structure"),("#/careers#roles","Open roles"),("#/careers#success","How success is measured"),("#/careers#benefits","Benefits"),("#/careers#apply","Apply")])}

<section class="sec" id="pay" style="scroll-margin-top:90px"><div class="wrap stack g28">
  {sec_head("Pay structure", "How compensation works", "Pay structure depends on the setting. Exact figures are shared on the first screening call, before any offer.")}
  <h3 style="margin:0">Colorado · In-home</h3>
  <div class="grid c3">
    <div class="card"><span class="k">Full-time</span><h3>Salaried, not hourly</h3><p class="small muted">Base pay is set against 23 billable hours per week, and every billable hour above that is paid in addition. Falling below 23 does not reduce your base, provided you maintain the availability agreed at hire.</p></div>
    <div class="card"><span class="k">Part-time</span><h3>Hourly, for direct service</h3><p class="small muted">Rate based on experience, certification and performance. Minimum to hire is two days per week, or 10–12 hours.</p></div>
    <div class="card"><span class="k">Scheduling</span><h3>Built from your availability</h3><p class="small muted">We do not hire into fixed shifts. Cases are clustered by ZIP code with a target commute of 30 minutes or less, starting at 2–4 sessions per week and growing from there.</p></div>
  </div>
  <h3 style="margin:0">Oklahoma · Tulsa center</h3>
  <div class="grid c3">
    <div class="card"><span class="k">Full-time and part-time</span><h3>Hourly, on set shifts</h3><p class="small muted">Technicians at our Tulsa center are paid hourly, full-time and part-time alike, and work scheduled shifts on site with the clinical team. Sessions happen at the center, so there is no driving between family homes.</p></div>
  </div>
</div></section>

<section class="sec band" id="roles" style="scroll-margin-top:90px"><div class="wrap stack g28">
  {sec_head("Open roles", "Current positions in Colorado and Oklahoma")}
  <div class="stack g10">{jobs}</div>
</div></section>

<section class="sec" id="success" style="scroll-margin-top:90px"><div class="wrap stack g28">
  {sec_head("How success is measured", "Four pillars of clinician success", "These are the standards we hold ourselves to and evaluate against. BCBA candidates are encouraged to ask about any of them in the interview.")}
  {pil}
  <p class="small muted measure"><strong>Clinical values:</strong> Exceptional Clinical Care · Understand, Don’t Judge · Build Bigger Lives · Make It Work in the Real World · Collaborate &amp; Be Transparent. Each is framed as a question we continue to ask.</p>
</div></section>

<section class="sec band" id="benefits" style="scroll-margin-top:90px"><div class="wrap stack g28">
  {sec_head("Benefits", "Benefits and terms")}
  <div class="grid c3">{ben}</div>
</div></section>

<section class="sec"><div class="wrap split">
  <div class="stack g14">
    <span class="hand">Career pathway</span>
    <h2>Advancement</h2>
    <p class="muted measure">Technicians advance into Lead RBT roles responsible for onboarding and training, into full-time positions, and, with reimbursement and supervision, toward BCaBA and BCBA certification. New hires typically reach independence on a case within two to three weeks; we hire in controlled cohorts to stay within training capacity.</p>
  </div>
  <div class="card stack g14">
    <h3>Before you apply</h3>
    {ticks(["Colorado positions are in family homes, mostly in the afternoon and early evening, and require reliable transportation.","In Colorado, mileage is reimbursed; drive time is not paid hourly.","Tulsa positions are hourly, on set shifts at the center.","Please list the availability you can reliably commit to — schedules are built directly from it."])}
  </div>
</div></section>

<section class="sec band" id="apply" style="scroll-margin-top:90px"><div class="wrap">
  <div class="panel stack g20" id="applyform-form">
    <div class="stack g10"><span class="hand">Application</span><h2>Apply</h2><p class="muted measure">Every application is reviewed by a member of our team, and every applicant receives a response.</p></div>
    {form}
  </div>
</div></section>
</div>'''
