# actaba.com

Public website for **Adventure Child Therapy (ACT ABA)** — Colorado and Oklahoma.

Live at **https://actaba.com**, served by GitHub Pages from this repository.

## How it works

The site is generated from Python sources in `src/` and deployed by GitHub Actions on every push to `main`
(`.github/workflows/deploy.yml`):

1. `src/build_static.py` writes the static site to `src/dist/` — nine pages plus the six-page family guide, CSS, JS, `404.html`, redirects for the old
   WordPress URLs, `sitemap.xml`, `robots.txt`, `CNAME` and the favicon.
2. `src/render_images.py` renders the social share image (`og-image.png`), the Apple touch icon, and the family-guide PDFs (`/guide/pdf/*.pdf`) with Playwright.
3. `actions/deploy-pages` publishes `src/dist/`.

| File | What it holds |
| --- | --- |
| `src/p_css.py` | Design tokens (light, dark, and the professional register used on Providers and Careers) and all component CSS |
| `src/p_art.py` | Paper-cut illustrations, icons and community mini-landscapes as SVG symbols |
| `src/p_shared.py` | Shared content: intake steps, FAQs, services, clinical values, pillars, benefits, locations, form helpers |
| `src/p_pages.py` | Family-facing pages: home, families, services, what is ABA, locations, about, contact |
| `src/p_pro.py` | Providers and Careers pages |
| `src/p_guide.py` | New-family guide (`/guide/` hub + five reads). All copy lives in `GUIDES`; the same data drives the web pages, the print/PDF layout and the Markdown team copy (`to_markdown`) |
| `src/build_static.py` | Page shell, SEO metadata, JSON-LD, form wiring, legacy redirects, sitemap |
| `src/render_images.py` | Share image, touch icon and guide PDF renderer; also calls `render_videos.build_media()` |
| `src/p_learn.py` | Family micro-course content: narration, captions and on-screen visuals for the five videos (`LESSONS`) |
| `src/p_learnpages.py` | `/learn/` hub and the five watch pages (`/learn/1/` … `/learn/5/`) |
| `src/render_videos.py` | Renders the micro-course MP4s: Kokoro TTS narration (voice `af_heart`), burned-in captions, paper-cut animation |

## Editing locally

```bash
cd src
python3 build_static.py          # writes dist/
python3 -m http.server -d dist   # preview at http://localhost:8000
```

Rendering images locally needs `pip install playwright`, `python -m playwright install chromium`, and the Fontsource
packages unpacked into `../fonts` (see the workflow for the exact commands).

## Forms

- **Intake** — the existing *ACT ABA Intake* Jotform (231875318826061), embedded on `/families/` and `/contact/`.
- **Provider referral** — the site form posts to Jotform *ACT Website – Provider Referral* (262524494233053).
- **Job application** — the site form posts to Jotform *ACT Website – Job Application* (262524661979066).

Both custom forms email info@actaba.com and store submissions in Jotform. Field mappings live in the `JOTFORM` object in
`src/build_static.py`; if a question is added or reordered in Jotform, update the mapping. Neither form collects protected
health information.

## DNS (Google Cloud DNS)

- `actaba.com` A → 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153
- `www.actaba.com` CNAME → factarihq.github.io
- MX, SPF and other TXT records belong to Google Workspace mail and are unrelated to hosting.

## Content rules

- Colorado does not require an autism diagnosis to start ABA (physician letter is enough); Oklahoma and North Carolina do.
- Expansion markets listed publicly: North Carolina only.
- No software vendor names, no parent partner names, and no pay figures on the public site.

## Family guide

`/guide/` is a hub for families who have just reached out, with five short reads: `/guide/what-is-aba/`, `/guide/how-it-works/`,
`/guide/a-session/`, `/guide/the-assessment/`, `/guide/your-part/`. Each page has a Download PDF link; `/guide/pdf/act-family-guide.pdf`
is all five in one file (rendered from the unlinked, noindex `/guide/print/` page). PDFs are regenerated on every deploy, so edit the copy in
`src/p_guide.py` and push — the pages and PDFs update together.

## Family micro-course videos

`/learn/` holds five one-minute vertical videos (720×1280, captioned, AI-narrated) texted to Colorado families after intake;
short links are `actaba.com/learn/1` … `actaba.com/learn/5`. The narration, captions and visuals all come from `LESSONS` in
`src/p_learn.py`.

On each deploy `render_images.py` calls `render_videos.build_media()`. It hashes the video inputs (`p_learn.py`,
`render_videos.py`, `p_art.py`, `p_css.py`, voice, speed, fps, size) and compares that hash with
`https://actaba.com/learn/media/lessons.json`. If nothing changed, it downloads the live videos (seconds). If anything
changed, it installs `kokoro-onnx`, downloads the open Kokoro-82M model files (Apache-2.0) and re-renders all five
(about 15 minutes). Edit the words in `p_learn.py`, push, and the videos, captions (`.vtt`) and posters regenerate.

Render locally: `python3 render_videos.py --force` (all) or `python3 render_videos.py 3` (one lesson). Model files go in
`../tts/` (git-ignored).

The texting itself runs outside this repo: the "ACT Parent Texts — Colorado" Google Sheet (sequence, families, log) with
its Apps Script engine, sent daily from the clinic Google Voice line.

## New-hire "Before Day One" modules

`/start/` is an unlisted hub (noindex, not in the sitemap or nav) with six short modules for new behavior technicians to
read between accepting an offer and their first day: `/start/1/` … `/start/6/` (welcome and team, the first two weeks,
the RBT head start, and three ABA basics primers). Each ends with a three-question check. All copy lives in `MODULES`
in `src/p_start.py`; page layout, CSS and the small page script are in `src/p_startpages.py`.

Links arrive by text and email from the **ACT New Hire Drip** engine (Apps Script under josh@actaba.com, control sheet
"ACT New Hire Drip — Before Day One" in the TechnicianNewHire Drive folder) with a per-hire token (`?h=…`). When a token
is present, the page pings the engine's public beacon URL (`BEACON` in `p_startpages.py`) on open and on finishing the
check, so the team can see who opened and finished what. Pages work normally without a token.

Content rules for these pages: no software vendor names, no pay figures, no client details; early sessions are about
building trust (never "becoming friends").
