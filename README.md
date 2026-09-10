# actaba.com

Public website for **Adventure Child Therapy (ACT ABA)** — Colorado and Oklahoma.

Live at **https://actaba.com**, served by GitHub Pages from this repository.

## How it works

The site is generated from Python sources in `src/` and deployed by GitHub Actions on every push to `main`
(`.github/workflows/deploy.yml`):

1. `src/build_static.py` writes the static site to `src/dist/` — nine pages, CSS, JS, `404.html`, redirects for the old
   WordPress URLs, `sitemap.xml`, `robots.txt`, `CNAME` and the favicon.
2. `src/render_images.py` renders the social share image (`og-image.png`) and the Apple touch icon with Playwright.
3. `actions/deploy-pages` publishes `src/dist/`.

| File | What it holds |
| --- | --- |
| `src/p_css.py` | Design tokens (light, dark, and the professional register used on Providers and Careers) and all component CSS |
| `src/p_art.py` | Paper-cut illustrations, icons and community mini-landscapes as SVG symbols |
| `src/p_shared.py` | Shared content: intake steps, FAQs, services, clinical values, pillars, benefits, locations, form helpers |
| `src/p_pages.py` | Family-facing pages: home, families, services, what is ABA, locations, about, contact |
| `src/p_pro.py` | Providers and Careers pages |
| `src/build_static.py` | Page shell, SEO metadata, JSON-LD, form wiring, legacy redirects, sitemap |
| `src/render_images.py` | Share image and touch icon renderer |

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
