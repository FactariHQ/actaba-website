"""Render the Open Graph share image and the Apple touch icon into dist/.

Needs Playwright (Chromium) and the three Fontsource packages unpacked into
FONTS_DIR (default: ../fonts), e.g.
  npm pack @fontsource/baloo-2@5.3.0 @fontsource/lexend@5.3.0 @fontsource/patrick-hand@5.3.0
"""
import asyncio, os, pathlib, tempfile
from playwright.async_api import async_playwright
from p_css import CSS
from p_art import DEFS, HILLS

HERE = pathlib.Path(__file__).resolve().parent
DIST = HERE / "dist"
FONTS = pathlib.Path(os.environ.get("FONTS_DIR", HERE.parent / "fonts")).resolve()

def font(pkg, file):
    matches = sorted(FONTS.glob(f"{pkg}*/files/{file}"))
    if not matches:
        raise SystemExit(f"font not found: {pkg}/{file} under {FONTS}")
    return matches[0].as_uri()

FACES = f"""
@font-face{{font-family:"Baloo 2";font-weight:800;src:url({font('fontsource-baloo-2','baloo-2-latin-800-normal.woff2')})}}
@font-face{{font-family:"Baloo 2";font-weight:700;src:url({font('fontsource-baloo-2','baloo-2-latin-700-normal.woff2')})}}
@font-face{{font-family:"Lexend";font-weight:400;src:url({font('fontsource-lexend','lexend-latin-400-normal.woff2')})}}
@font-face{{font-family:"Patrick Hand";font-weight:400;src:url({font('fontsource-patrick-hand','patrick-hand-latin-400-normal.woff2')})}}
"""

OG = f"""<!doctype html><html><head><meta charset="utf-8"><style>{FACES}{CSS}
html,body{{margin:0;width:1200px;height:630px;overflow:hidden}}
.og{{position:relative;width:1200px;height:630px;background:linear-gradient(180deg,#DDF0FA 0%,#F2FAFE 90%);overflow:hidden}}
.og .copy{{position:absolute;left:72px;top:64px;width:760px;display:flex;flex-direction:column;gap:18px;z-index:3}}
.og .brand .b1{{font-size:1.9rem}} .og .brand .b2{{font-size:1.5rem}} .og .brand svg{{width:64px;height:64px}}
.og h1{{font-size:5.1rem;line-height:.98;margin-top:6px}}
.og .meta{{font-family:var(--f-hand);font-size:2rem;color:var(--coral-ink)}}
.og .sun{{right:70px;top:50px;width:190px}} .og .kite{{right:300px;top:150px;width:96px;animation:none;transform:rotate(-6deg)}}
.og .cloud{{animation:none}} .og .cloud.a{{left:auto;right:520px;top:24px;width:150px}}
.og .hills{{position:absolute;left:0;right:0;bottom:0;height:250px;margin:0}}
.og .anim-rise{{animation:none}}
</style></head><body>{DEFS}<div class="og">
<div class="hero-sky"><svg class="sun" viewBox="0 0 200 200"><use href="#sunsym"/></svg><svg class="cloud a" viewBox="0 0 200 90"><use href="#cloudsym"/></svg><svg class="kite" viewBox="0 0 120 220"><use href="#kitesym"/></svg></div>
<div class="copy"><div class="brand"><svg viewBox="0 0 44 44"><use href="#logo"/></svg><span class="bn"><span class="b1">Adventure Child Therapy</span><span class="b2">ABA your way</span></span></div>
<h1 style="position:relative;z-index:0">Every big adventure starts <span style="position:relative;display:inline-block;white-space:nowrap">close to home.<i style="position:absolute;left:-4px;right:-6px;bottom:.06em;height:.3em;background:#FFC845;border-radius:40% 60% 50% 45%/60% 40% 60% 40%;z-index:-1;transform:rotate(-1.2deg)"></i></span></h1>
<span class="meta">Kids’ ABA therapy · Colorado, Oklahoma &amp; North Carolina · actaba.com</span></div>
{HILLS}</div></body></html>"""

async def main():
    DIST.mkdir(exist_ok=True)
    icon = (DIST / "favicon.svg").read_text().replace("<svg ", '<svg width="180" height="180" ', 1)
    with tempfile.TemporaryDirectory() as tmp:
        og_path = pathlib.Path(tmp) / "og.html"; og_path.write_text(OG)
        ic_path = pathlib.Path(tmp) / "icon.html"
        ic_path.write_text(f'<!doctype html><html><head><style>html,body{{margin:0;width:180px;height:180px;background:#DDF0FA}}</style></head><body>{icon}</body></html>')
        async with async_playwright() as p:
            b = await p.chromium.launch()
            pg = await b.new_page(viewport={"width": 1200, "height": 630})
            await pg.goto(og_path.as_uri())
            await pg.evaluate("document.fonts.ready")
            if not await pg.evaluate("document.fonts.check('800 40px \"Baloo 2\"')"):
                raise SystemExit("Baloo 2 did not load for the share image")
            await pg.wait_for_timeout(300)
            await pg.screenshot(path=str(DIST / "og-image.png"))
            ic = await b.new_page(viewport={"width": 180, "height": 180})
            await ic.goto(ic_path.as_uri())
            await ic.screenshot(path=str(DIST / "apple-touch-icon.png"))
            await b.close()
    print("rendered og-image.png and apple-touch-icon.png")

if __name__ == "__main__":
    asyncio.run(main())
