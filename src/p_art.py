# Shared SVG defs, scenes and icons — all colors come from theme tokens.
DEFS = r"""<svg aria-hidden="true" focusable="false" style="position:absolute;width:0;height:0;overflow:hidden">
<defs>
  <filter id="pc" x="-10%" y="-30%" width="120%" height="160%"><feDropShadow dx="0" dy="-3" stdDeviation="3.2" flood-color="#1b1d36" flood-opacity=".16"/></filter>
  <filter id="pcd" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="0" dy="3" stdDeviation="2.4" flood-color="#1b1d36" flood-opacity=".18"/></filter>
</defs>
<symbol id="logo" viewBox="0 0 44 44">
  <rect x="1" y="1" width="42" height="42" rx="14" fill="var(--hero-sky)"/>
  <circle cx="31" cy="13" r="5.2" fill="var(--sun)"/>
  <path d="M1 30 C9 21 15 20 22 25 C28 29 34 22 43 24 V30 C43 37.7 36.7 43 29 43 H15 C7.3 43 1 37.7 1 30Z" fill="var(--hill-3)"/>
  <path d="M1 35 C10 30 18 31 25 34 C31 36.5 37 34 43 33 V29 C43 36.7 36.7 43 29 43 H15 C7.3 43 1 37.7 1 35Z" fill="var(--hill-5)"/>
  <path d="M9 40 C14 36 16 33 21 32 C26 31 27 27 31 26" fill="none" stroke="var(--trail)" stroke-width="2" stroke-linecap="round" stroke-dasharray=".5 4"/>
</symbol>
<symbol id="strip" viewBox="0 0 1440 110" preserveAspectRatio="none">
  <path d="M0 52 C200 18 380 30 560 44 C760 60 900 12 1100 22 C1260 30 1360 48 1440 40 V110 H0Z" fill="var(--hill-2)"/>
  <path d="M0 74 C220 50 420 60 640 72 C860 84 1040 48 1240 58 C1340 63 1400 70 1440 66 V110 H0Z" fill="var(--hill-3)" filter="url(#pc)"/>
  <path d="M0 92 C240 80 520 88 760 94 C1000 100 1200 80 1440 86 V110 H0Z" fill="var(--paper)" filter="url(#pc)"/>
</symbol>
<symbol id="ftrhills" viewBox="0 0 1440 84" preserveAspectRatio="none">
  <path d="M0 40 C160 10 330 18 520 34 C720 50 880 6 1080 16 C1240 24 1350 42 1440 34 V84 H0Z" fill="var(--hill-4)" opacity=".75"/>
  <path d="M0 62 C230 40 440 50 660 62 C880 74 1080 42 1280 50 C1360 53 1410 58 1440 56 V84 H0Z" fill="var(--ftr-bg)"/>
</symbol>
<symbol id="sunsym" viewBox="0 0 200 200">
  <g style="opacity:var(--sunrays)">
    <circle cx="100" cy="100" r="96" fill="var(--sun)" opacity=".18"/>
    <circle cx="100" cy="100" r="76" fill="var(--sun)" opacity=".32"/>
  </g>
  <circle cx="100" cy="100" r="54" fill="var(--sun)" filter="url(#pcd)"/>
  <circle cx="84" cy="86" r="10" fill="#fff" opacity=".35"/>
</symbol>
<symbol id="cloudsym" viewBox="0 0 200 90">
  <path d="M28 78 C8 78 4 54 24 50 C22 30 48 22 62 36 C70 12 112 8 122 36 C134 24 162 30 160 52 C184 50 192 78 170 78Z" fill="var(--cloud)" filter="url(#pcd)"/>
</symbol>
<symbol id="kitesym" viewBox="0 0 120 220">
  <path d="M60 6 L104 56 L60 116 L16 56Z" fill="var(--coral)" filter="url(#pcd)"/>
  <path d="M60 6 L104 56 L60 56Z" fill="var(--sun)"/>
  <path d="M60 56 L16 56 L60 116Z" fill="var(--sky)"/>
  <path d="M60 6 V116 M16 56 H104" stroke="#fff" stroke-width="2.4" opacity=".7"/>
  <path d="M60 116 C44 134 76 150 58 168 C44 182 70 196 60 216" fill="none" stroke="var(--ink-3)" stroke-width="2" stroke-linecap="round"/>
  <path d="M50 140 l10 -6 l0 12z M66 140 l-10 -6 l0 12z" fill="var(--sun-deep)"/>
  <path d="M48 178 l10 -6 l0 12z M64 178 l-10 -6 l0 12z" fill="var(--coral)"/>
</symbol>
<symbol id="pin" viewBox="0 0 66 66">
  <circle cx="33" cy="33" r="30" fill="var(--sun)" filter="url(#pcd)"/>
  <circle cx="33" cy="33" r="24" fill="none" stroke="#fff" stroke-width="2.5" stroke-dasharray="3 5" opacity=".8"/>
</symbol>
<symbol id="pin-sky" viewBox="0 0 66 66"><circle cx="33" cy="33" r="30" fill="var(--sky)" filter="url(#pcd)"/><circle cx="33" cy="33" r="24" fill="none" stroke="#fff" stroke-width="2.5" stroke-dasharray="3 5" opacity=".8"/></symbol>
<symbol id="pin-meadow" viewBox="0 0 66 66"><circle cx="33" cy="33" r="30" fill="var(--meadow)" filter="url(#pcd)"/><circle cx="33" cy="33" r="24" fill="none" stroke="#fff" stroke-width="2.5" stroke-dasharray="3 5" opacity=".8"/></symbol>
<symbol id="pin-coral" viewBox="0 0 66 66"><circle cx="33" cy="33" r="30" fill="var(--coral)" filter="url(#pcd)"/><circle cx="33" cy="33" r="24" fill="none" stroke="#fff" stroke-width="2.5" stroke-dasharray="3 5" opacity=".8"/></symbol>
<symbol id="flag" viewBox="0 0 66 66"><circle cx="33" cy="33" r="30" fill="var(--coral)" filter="url(#pcd)"/><path d="M26 48 V18" stroke="#fff" stroke-width="3" stroke-linecap="round"/><path d="M27 19 H45 L40 26 L45 33 H27Z" fill="var(--sun)"/></symbol>
<symbol id="leaf" viewBox="0 0 20 20"><path d="M4 16 C4 8 9 3 17 3 C17 11 12 16 4 16Z" fill="var(--meadow)"/><path d="M4 16 L12 8" stroke="var(--paper)" stroke-width="1.4" stroke-linecap="round"/></symbol>
<symbol id="squiggle" viewBox="0 0 48 30"><path d="M3 6 C14 2 26 6 30 14 C33 20 36 24 44 25" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/><path d="M37 19 L44 25 L36 28" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></symbol>

<!-- service & door icons (48x48) -->
<symbol id="i-assess" viewBox="0 0 48 48"><rect x="27" y="29" width="8" height="18" rx="4" transform="rotate(-45 31 38)" fill="var(--coral)"/><circle cx="21" cy="21" r="15" fill="var(--sky)" filter="url(#pcd)"/><circle cx="21" cy="21" r="9.5" fill="var(--surface)"/><path d="M16 21.5 l3.4 3.4 L26 18" fill="none" stroke="var(--meadow-ink)" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></symbol>
<symbol id="i-blocks" viewBox="0 0 48 48"><rect x="6" y="26" width="17" height="17" rx="3.5" fill="var(--sky)" filter="url(#pcd)"/><rect x="25" y="26" width="17" height="17" rx="3.5" fill="var(--meadow)" filter="url(#pcd)"/><rect x="15" y="7" width="17" height="17" rx="3.5" transform="rotate(8 23.5 15.5)" fill="var(--sun)" filter="url(#pcd)"/><circle cx="23.5" cy="15.5" r="3" fill="#fff" opacity=".8"/><path d="M12 34.5h5M33.5 30v9" stroke="#fff" stroke-width="2.6" stroke-linecap="round" opacity=".85"/></symbol>
<symbol id="i-home" viewBox="0 0 48 48"><path d="M8 22 L24 8 L40 22Z" fill="var(--coral)" filter="url(#pcd)"/><rect x="11" y="21" width="26" height="21" rx="3" fill="var(--sun)" filter="url(#pcd)"/><path d="M24 37 C17 32 16 28 18.5 25.6 C20.3 24 22.6 24.6 24 26.4 C25.4 24.6 27.7 24 29.5 25.6 C32 28 31 32 24 37Z" fill="var(--coral)"/></symbol>
<symbol id="i-star" viewBox="0 0 48 48"><rect x="7" y="6" width="34" height="38" rx="5" fill="var(--surface)" stroke="var(--sky)" stroke-width="3" filter="url(#pcd)"/><path d="M13 15h10M13 22h7" stroke="var(--line-2)" stroke-width="2.6" stroke-linecap="round"/><path d="M31 18 l3.2 6.4 7 1-5.1 5 1.2 7L31 34.1l-6.3 3.3 1.2-7-5.1-5 7-1z" fill="var(--sun)" stroke="var(--sun-deep)" stroke-width="1.2" stroke-linejoin="round"/></symbol>
<symbol id="i-bowl" viewBox="0 0 48 48"><path d="M34 6 C38 6 40 10 38 14 L30 24" stroke="var(--sun-deep)" stroke-width="3.2" stroke-linecap="round" fill="none"/><ellipse cx="24" cy="24" rx="19" ry="4.6" fill="var(--sun)"/><path d="M5 24 H43 C43 34 35 42 24 42 C13 42 5 34 5 24Z" fill="var(--meadow)" filter="url(#pcd)"/><circle cx="16" cy="31" r="2.4" fill="#fff" opacity=".7"/><circle cx="24" cy="34" r="2.4" fill="#fff" opacity=".7"/><circle cx="32" cy="31" r="2.4" fill="#fff" opacity=".7"/></symbol>
<symbol id="i-talk" viewBox="0 0 48 48"><path d="M5 10 C5 7 7 5 10 5 H28 C31 5 33 7 33 10 V21 C33 24 31 26 28 26 H15 L8 32 V26 C6 25.5 5 23.5 5 21Z" fill="var(--sky)" filter="url(#pcd)"/><path d="M43 23 C43 20 41 18 38 18 H22 C19 18 17 20 17 23 V32 C17 35 19 37 22 37 H33 L40 43 V37 C42 36.5 43 34.5 43 32Z" fill="var(--coral)" filter="url(#pcd)"/><circle cx="24" cy="28" r="2" fill="#fff"/><circle cx="30" cy="28" r="2" fill="#fff"/><circle cx="36" cy="28" r="2" fill="#fff"/></symbol>
<symbol id="i-shirt" viewBox="0 0 48 48"><path d="M17 6 C19 10 29 10 31 6 L43 12 L38 22 L34 20 V42 H14 V20 L10 22 L5 12Z" fill="var(--meadow)" filter="url(#pcd)"/><path d="M24 26 C20.5 23.4 20 21 21.4 19.6 C22.4 18.7 23.4 19.1 24 20 C24.6 19.1 25.6 18.7 26.6 19.6 C28 21 27.5 23.4 24 26Z" fill="var(--sun)"/></symbol>
<symbol id="i-pack" viewBox="0 0 48 48"><path d="M17 10 C17 5 31 5 31 10" fill="none" stroke="var(--sun-deep)" stroke-width="3.2"/><rect x="9" y="10" width="30" height="33" rx="9" fill="var(--coral)" filter="url(#pcd)"/><rect x="14" y="26" width="20" height="12" rx="4" fill="var(--sun)"/><path d="M14 30 H34" stroke="var(--sun-deep)" stroke-width="2"/></symbol>
<symbol id="i-hand" viewBox="0 0 48 48"><circle cx="24" cy="24" r="20" fill="var(--sky)" filter="url(#pcd)"/><path d="M14 26 C18 26 20 20 24 20 C28 20 30 26 34 26" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/><path d="M17 31 H31" stroke="#fff" stroke-width="3" stroke-linecap="round"/><circle cx="24" cy="14" r="3" fill="var(--sun)"/></symbol>
<symbol id="i-heart" viewBox="0 0 48 48"><path d="M24 42 C8 31 4 22 10 14 C14.6 8.4 21 9.6 24 14.4 C27 9.6 33.4 8.4 38 14 C44 22 40 31 24 42Z" fill="var(--coral)" filter="url(#pcd)"/><path d="M14 18 C15 15 17 14 19 14" stroke="#fff" stroke-width="2.6" stroke-linecap="round" fill="none" opacity=".7"/></symbol>
<symbol id="i-letter" viewBox="0 0 48 48"><rect x="5" y="11" width="38" height="28" rx="5" fill="var(--sun)" filter="url(#pcd)"/><path d="M6 13 L24 27 L42 13" fill="none" stroke="var(--sun-deep)" stroke-width="3" stroke-linejoin="round"/><circle cx="36" cy="33" r="7" fill="var(--meadow)"/><path d="M32.6 33.2 l2.4 2.4 4.2-4.6" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></symbol>
<symbol id="i-seed" viewBox="0 0 48 48"><path d="M24 44 V22" stroke="var(--hill-5)" stroke-width="3.2" stroke-linecap="round"/><path d="M24 26 C24 16 16 10 7 10 C7 20 14 26 24 26Z" fill="var(--meadow)" filter="url(#pcd)"/><path d="M24 22 C24 12 32 6 41 6 C41 16 34 22 24 22Z" fill="var(--hill-4)" filter="url(#pcd)"/><rect x="12" y="38" width="24" height="7" rx="3.5" fill="var(--coral)"/></symbol>
<symbol id="i-shield" viewBox="0 0 48 48"><path d="M24 4 L40 10 V22 C40 33 33 40 24 44 C15 40 8 33 8 22 V10Z" fill="var(--sky)" filter="url(#pcd)"/><path d="M17 24 l5 5 L32 18" fill="none" stroke="#fff" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/></symbol>

<!-- mini landscapes for each community (200x96) -->
<symbol id="m-denver" viewBox="0 0 200 96" preserveAspectRatio="xMidYMid slice">
  <rect width="200" height="96" fill="var(--band-sky)"/>
  <circle cx="160" cy="24" r="12" fill="var(--sun)"/>
  <path d="M-4 70 L34 28 L52 46 L78 16 L104 50 L126 32 L160 66 L204 50 V96 H-4Z" fill="var(--hill-1)"/>
  <path d="M78 16 L90 30 L84 29 L78 34 L72 30 L68 27Z M34 28 L42 37 L34 36 L28 35Z" fill="#fff" opacity=".85"/>
  <path d="M-4 78 C40 60 80 64 120 72 C150 78 180 66 204 68 V96 H-4Z" fill="var(--hill-3)" filter="url(#pc)"/>
  <path d="M-4 88 C50 80 110 84 204 82 V96 H-4Z" fill="var(--hill-5)" filter="url(#pc)"/>
</symbol>
<symbol id="m-gj" viewBox="0 0 200 96" preserveAspectRatio="xMidYMid slice">
  <rect width="200" height="96" fill="var(--band-sun)"/>
  <circle cx="40" cy="22" r="12" fill="var(--sun)"/>
  <path d="M-4 58 H40 L46 40 H104 L112 58 H124 L130 46 H176 L182 60 H204 V96 H-4Z" fill="var(--coral)" opacity=".75"/>
  <path d="M46 40 H104 L106 46 H44Z M130 46 H176 L178 50 H129Z" fill="var(--coral-ink)" opacity=".35"/>
  <path d="M-4 76 C40 64 90 70 130 74 C160 77 184 70 204 70 V96 H-4Z" fill="var(--hill-3)" filter="url(#pc)"/>
  <path d="M-4 88 C60 82 120 86 204 83 V96 H-4Z" fill="var(--hill-5)" filter="url(#pc)"/>
</symbol>
<symbol id="m-pueblo" viewBox="0 0 200 96" preserveAspectRatio="xMidYMid slice">
  <rect width="200" height="96" fill="var(--band-meadow)"/>
  <circle cx="150" cy="22" r="12" fill="var(--sun)"/>
  <path d="M-4 56 C30 44 60 48 90 54 C120 60 160 44 204 50 V96 H-4Z" fill="var(--hill-2)"/>
  <path d="M-4 70 C40 62 80 66 120 68 C150 70 180 62 204 64 V96 H-4Z" fill="var(--hill-3)" filter="url(#pc)"/>
  <path d="M60 96 C70 86 110 84 104 76 C98 70 130 68 150 66 L160 67 C140 70 112 72 118 78 C126 88 92 90 84 96Z" fill="var(--sky)"/>
  <path d="M-4 90 C40 86 50 88 64 92 L60 96 H-4Z M150 96 C170 88 190 88 204 88 V96Z" fill="var(--hill-5)"/>
</symbol>
<symbol id="m-ada" viewBox="0 0 200 96" preserveAspectRatio="xMidYMid slice">
  <rect width="200" height="96" fill="var(--band-sun)"/>
  <circle cx="54" cy="28" r="13" fill="var(--sun)"/>
  <path d="M-4 58 C30 46 62 50 92 56 C124 62 160 46 204 52 V96 H-4Z" fill="var(--hill-2)"/>
  <path d="M-4 72 C36 64 76 70 112 72 C146 74 176 64 204 66 V96 H-4Z" fill="var(--hill-3)" filter="url(#pc)"/>
  <rect x="139" y="50" width="4" height="14" rx="1.5" fill="var(--coral-ink)"/>
  <circle cx="141" cy="46" r="11" fill="var(--hill-4)" filter="url(#pc)"/>
  <rect x="159" y="56" width="3" height="10" rx="1.5" fill="var(--coral-ink)"/>
  <circle cx="160.5" cy="53" r="8" fill="var(--meadow)" filter="url(#pc)"/>
  <path d="M-4 88 C50 80 110 86 204 82 V96 H-4Z" fill="var(--hill-5)" filter="url(#pc)"/>
</symbol>
<symbol id="m-tulsa" viewBox="0 0 200 96" preserveAspectRatio="xMidYMid slice">
  <rect width="200" height="96" fill="var(--coral-soft)"/>
  <circle cx="100" cy="46" r="26" fill="var(--sun)" opacity=".9"/>
  <path d="M-4 66 C40 58 80 60 120 62 C160 64 180 58 204 60 V96 H-4Z" fill="var(--hill-2)"/>
  <rect x="116" y="44" width="40" height="26" rx="2" fill="var(--surface)" filter="url(#pcd)"/>
  <path d="M112 46 L136 30 L160 46Z" fill="var(--sky)"/>
  <rect x="131" y="55" width="10" height="15" rx="2" fill="var(--sun-deep)"/>
  <circle cx="123" cy="53" r="3" fill="var(--sky)"/><circle cx="149" cy="53" r="3" fill="var(--sky)"/>
  <path d="M-4 80 C50 72 100 76 150 78 C170 79 190 74 204 74 V96 H-4Z" fill="var(--hill-4)" filter="url(#pc)"/>
  <path d="M20 78 v-10 M26 78 v-14 M32 78 v-9" stroke="var(--hill-5)" stroke-width="2.4" stroke-linecap="round"/>
</symbol>
</svg>"""

def ico(name, cls="ico"):
    return f'<svg class="{cls}" aria-hidden="true" focusable="false"><use href="#{name}"/></svg>'

LOGO = '<svg width="42" height="42" aria-hidden="true" focusable="false"><use href="#logo"/></svg>'

HERO_SKY = r"""<div class="hero-sky" aria-hidden="true">
  <svg class="stars" viewBox="0 0 1440 500" preserveAspectRatio="xMidYMin slice" focusable="false"><g fill="#FFF6DF">
    <circle cx="120" cy="70" r="2"/><circle cx="300" cy="140" r="1.6"/><circle cx="520" cy="60" r="2.2"/><circle cx="760" cy="120" r="1.5"/><circle cx="900" cy="46" r="2"/><circle cx="1040" cy="170" r="1.7"/><circle cx="1320" cy="260" r="2"/><circle cx="640" cy="220" r="1.4"/><circle cx="220" cy="260" r="1.6"/>
  </g></svg>
  <svg class="cloud a" viewBox="0 0 200 90" focusable="false"><use href="#cloudsym"/></svg>
  <svg class="cloud b" viewBox="0 0 200 90" focusable="false"><use href="#cloudsym"/></svg>
  <svg class="sun" viewBox="0 0 200 200" focusable="false"><use href="#sunsym"/></svg>
  <svg class="kite" viewBox="0 0 120 220" focusable="false"><use href="#kitesym"/></svg>
</div>"""

HILLS = r"""<svg class="hills" viewBox="0 0 1440 380" preserveAspectRatio="xMidYMax slice" aria-hidden="true" focusable="false">
  <g class="anim-rise">
    <path d="M0 196 C170 120 330 138 500 160 C690 186 820 84 1010 104 C1190 122 1310 168 1440 138 V380 H0Z" fill="var(--hill-1)"/>
    <path d="M598 164 l14 -30 l14 30z M626 160 l12 -24 l12 24z M1236 150 l13 -28 l13 28z" fill="var(--hill-4)" opacity=".55"/>
  </g>
  <g class="anim-rise l2">
    <path d="M0 250 C150 204 310 210 450 234 C620 263 760 176 950 190 C1130 204 1270 252 1440 214 V380 H0Z" fill="var(--hill-2)" filter="url(#pc)"/>
    <g filter="url(#pcd)">
      <rect x="924" y="160" width="52" height="36" rx="4" fill="var(--surface)"/>
      <path d="M914 166 L950 134 L986 166Z" fill="var(--coral)"/>
      <rect x="942" y="176" width="14" height="20" rx="3" fill="var(--sun-deep)"/>
      <circle cx="933" cy="175" r="4" fill="var(--sky)"/><circle cx="967" cy="175" r="4" fill="var(--sky)"/>
    </g>
    <path d="M1000 198 V152" stroke="var(--ink-3)" stroke-width="3" stroke-linecap="round"/>
    <path d="M1001 153 H1026 L1019 162 L1026 171 H1001Z" fill="var(--sun)"/>
  </g>
  <g class="anim-rise l3">
    <path d="M0 290 C200 252 380 262 560 282 C740 302 900 244 1100 256 C1260 266 1360 292 1440 276 V380 H0Z" fill="var(--hill-3)" filter="url(#pc)"/>
    <g filter="url(#pcd)">
      <rect x="404" y="252" width="8" height="26" rx="3" fill="var(--trunk)"/><circle cx="408" cy="240" r="24" fill="var(--hill-4)"/>
      <rect x="459" y="262" width="6" height="20" rx="3" fill="var(--trunk)"/><circle cx="462" cy="254" r="16" fill="var(--hill-5)"/>
      <rect x="1178" y="238" width="8" height="26" rx="3" fill="var(--trunk)"/><circle cx="1182" cy="226" r="26" fill="var(--hill-4)"/>
    </g>
  </g>
  <g class="anim-rise l4">
    <path d="M0 330 C220 306 420 312 640 324 C860 336 1060 302 1260 312 C1350 316 1400 324 1440 320 V380 H0Z" fill="var(--hill-4)" filter="url(#pc)"/>
    <path d="M0 362 C260 348 520 356 780 362 C1040 368 1240 350 1440 354 V380 H0Z" fill="var(--paper)" filter="url(#pc)"/>
    <path d="M330 372 C400 348 520 350 572 324 C616 302 700 300 760 276 C820 252 880 236 944 206" fill="none" stroke="var(--trail)" stroke-width="6" stroke-linecap="round" stroke-dasharray="0.5 16"/>
  </g>
</svg>"""

def strip():
    return '<svg class="strip" aria-hidden="true" focusable="false"><use href="#strip"/></svg>'

def mini(name, label):
    return f'<svg class="mini" viewBox="0 0 200 96" role="img" aria-label="{label}" focusable="false"><use href="#{name}"/></svg>'
