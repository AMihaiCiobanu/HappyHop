# -*- coding: utf-8 -*-
"""Asamblează paginile statice Happy & Hop. Output = HTML complet, fără dependențe."""
import os, io, re, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)   # rădăcina site-ului
SITE = "https://happyhop.ro"

def asset(rel):
    """Adauga o amprenta a continutului la CSS/JS: `site.css?v=ab12cd34`.
    Fara ea, browserele si hostingul servesc mai departe versiunea veche dupa un update."""
    path = os.path.join(OUT, rel)
    try:
        h = hashlib.md5(io.open(path, "rb").read()).hexdigest()[:8]
    except OSError:
        return rel
    return "%s?v=%s" % (rel, h)


_SPRITE_ALL = io.open(os.path.join(HERE, "sprite.html"), encoding="utf-8").read().strip()
_SYMBOLS = {name: markup for markup, name
            in re.findall(r'(<symbol id="(i-[a-z-]+)".*?</symbol>)', _SPRITE_ALL, re.S)}


def sprite_for(markup):
    """Doar simbolurile folosite efectiv in pagina — restul nu are ce cauta in HTML."""
    used = sorted(set(re.findall(r'<use href="#(i-[a-z-]+)">', markup)))
    missing = [u for u in used if u not in _SYMBOLS]
    if missing:
        raise SystemExit("Iconuri lipsa din sprite.html: %s" % ", ".join(missing))
    return ('<svg xmlns="http://www.w3.org/2000/svg" style="display:none" aria-hidden="true" focusable="false">'
            + "".join(_SYMBOLS[u] for u in used) + "</svg>")

TEL1 = "0726347494"; TEL1F = "0726 347 494"
TEL2 = "0740750993"; TEL2F = "0740 750 993"
WA   = "40726347494"
FACEBOOK = "https://www.facebook.com/people/Happy-si-Hop/100064721647929/"
# Profilurile sociale: apar in footer si ca `sameAs` in datele structurate.
SOCIAL = [FACEBOOK]
WA_GEN  = "https://wa.me/%s?text=Bun%%C4%%83%%20ziua!%%20A%%C8%%99%%20dori%%20informa%%C8%%9Bii%%20despre%%20Happy%%20%%26%%20Hop." % WA
WA_PARTY= "https://wa.me/%s?text=Bun%%C4%%83%%20ziua!%%20A%%C8%%99%%20dori%%20s%%C4%%83%%20rezerv%%20o%%20petrecere%%20la%%20Happy%%20%%26%%20Hop." % WA

NAV = [
    ("index.html",    "Acasă"),
    ("atractii.html", "Atracții"),
    ("petreceri.html","Petreceri"),
    ("locatii.html",  "Locații"),
    ("galerie.html",  "Galerie"),
    ("contact.html",  "Contact"),
]

def icon(name, cls=""):
    c = ' class="%s"' % cls if cls else ""
    return '<svg%s aria-hidden="true"><use href="#%s"></use></svg>' % (c, name)

def nav_items(current):
    """Paginile de locatie nu sunt in meniu — evidentiem parintele lor, `Locații`."""
    if current.startswith("loc-de-joaca-"):
        current = "locatii.html"
    out = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == current else ""
        out.append('<li><a href="%s"%s>%s</a></li>' % (href, cur, label))
    return "\n          ".join(out)

def header(current):
    return """  <a class="skip-link" href="#main">Sari la conținut</a>

  <header class="site-header">
    <div class="container site-header__inner">
      <a class="brand" href="index.html">
        <img src="assets/brand/logo.png" alt="" width="46" height="46">
        <span>
          <span class="brand__name">Happy&nbsp;<span>&amp;</span>&nbsp;Hop</span>
          <span class="brand__tag">Loc de joacă · Iași</span>
        </span>
      </a>

      <nav class="nav" aria-label="Navigare principală">
        <ul>
          %s
        </ul>
      </nav>

      <a class="btn btn--primary btn--sm header-cta" href="tel:%s">%s<span>%s</span></a>

      <button class="nav-toggle" type="button" data-nav-toggle aria-expanded="false" aria-controls="mobile-panel">
        <span class="sr-only">Deschide meniul</span>%s
      </button>
    </div>
  </header>

  <div class="mobile-panel" id="mobile-panel" role="dialog" aria-modal="true" aria-label="Meniu principal" hidden>
    <div class="mobile-panel__top">
      <a class="brand" href="index.html">
        <img src="assets/brand/logo.png" alt="" width="46" height="46">
        <span class="brand__name">Happy&nbsp;<span>&amp;</span>&nbsp;Hop</span>
      </a>
      <button class="nav-toggle" type="button" data-nav-close>
        <span class="sr-only">Închide meniul</span>%s
      </button>
    </div>
    <nav aria-label="Navigare mobilă">
      <ul>
        %s
      </ul>
    </nav>
    <div class="mobile-panel__cta">
      <a class="btn btn--primary btn--block" href="tel:%s">%s Sună acum</a>
      <a class="btn btn--wa btn--block" href="%s" target="_blank" rel="noopener">%s WhatsApp</a>
    </div>
  </div>
""" % (nav_items(current), TEL1, icon("i-phone"), TEL1F, icon("i-menu"),
       icon("i-close"), nav_items(current), TEL1, icon("i-phone"), WA_GEN, icon("i-wa"))

FOOTER = """  <footer class="site-footer">
    <div class="site-footer__wave" aria-hidden="true">
      <svg viewBox="0 0 1440 60" preserveAspectRatio="none"><path d="M0 60V22c120 22 240 30 360 22s240-30 360-34 240 12 360 22 240 6 360-10v38Z"/></svg>
    </div>
    <div class="container">
      <div class="site-footer__grid">
        <div>
          <a class="brand" href="index.html">
            <img src="assets/brand/logo.png" alt="" width="52" height="52">
            <span>
              <span class="brand__name">Happy&nbsp;<span>&amp;</span>&nbsp;Hop</span>
              <span class="brand__tag">Loc de joacă · Iași</span>
            </span>
          </a>
          <p style="margin-top:1rem;max-width:34ch">Cel mai vesel loc de joacă din Iași: 700&nbsp;m² de trambuline, tobogane, piscine cu bile și petreceri de neuitat.</p>
        </div>

        <div>
          <h3>Navigare</h3>
          <ul class="footer-list">
            <li><a href="index.html">Acasă</a></li>
            <li><a href="atractii.html">Atracții</a></li>
            <li><a href="petreceri.html">Petreceri</a></li>
            <li><a href="locatii.html">Locații</a></li>
            <li><a href="galerie.html">Galerie</a></li>
            <li><a href="contact.html">Contact</a></li>
          </ul>
        </div>

        <div>
          <h3>Locații</h3>
          <ul class="footer-list">
            <li><a href="loc-de-joaca-socola.html">Bd. Socola 27A (lângă Jumbo), Iași</a></li>
            <li><a href="loc-de-joaca-moldova-mall.html">Moldova Mall, Șos. Păcurari 121, Iași</a></li>
            <li><a href="loc-de-joaca-miroslava.html">Family Market Miroslava — în curând</a></li>
          </ul>
        </div>

        <div>
          <h3>Contact</h3>
          <ul class="footer-list">
            <li><a href="tel:%s">%s</a></li>
            <li><a href="tel:%s">%s</a></li>
            <li><a href="%s" target="_blank" rel="noopener">Scrie-ne pe WhatsApp</a></li>
            <li><a href="%s" target="_blank" rel="noopener">Facebook</a></li>
          </ul>
        </div>
      </div>

      <div class="site-footer__bottom">
        <p>© <span data-year>2026</span> Happy &amp; Hop · happyhop.ro</p>
        <p><a href="politica-confidentialitate.html">Politica de confidențialitate și cookies</a></p>
        <p class="footer-madeby">
          <a href="https://softsapps.com" target="_blank" rel="noopener" aria-label="Made by SoftApps">
            <span class="madeby-label">Made by</span>
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 100" role="img" aria-label="SoftApps">
              <defs>
                <linearGradient id="saLogo" x1="0" y1="0" x2="1" y2="1">
                  <stop offset="0" stop-color="#22d3ee" />
                  <stop offset="0.5" stop-color="#7c3aed" />
                  <stop offset="1" stop-color="#ec4899" />
                </linearGradient>
              </defs>
              <rect x="6" y="14" width="72" height="72" rx="20" fill="#0a0e1a" />
              <rect x="6" y="14" width="72" height="72" rx="20" fill="none" stroke="url(#saLogo)" stroke-width="2.5" />
              <path d="M56 38 C56 31 49 29 42 29 C34 29 28 32 28 39 C28 47 37 49 42 51 C47 53 56 55 56 63 C56 70 48 72 42 72 C35 72 28 70 28 62" fill="none" stroke="url(#saLogo)" stroke-width="8" stroke-linecap="round" />
              <text x="96" y="62" font-family="system-ui, sans-serif" font-size="42" font-weight="700" fill="currentColor">Soft<tspan fill="url(#saLogo)">Apps</tspan></text>
            </svg>
          </a>
        </p>
      </div>
    </div>
  </footer>

  <a class="float-wa" href="%s" target="_blank" rel="noopener" aria-label="Scrie-ne pe WhatsApp">%s</a>

  <div class="mobile-bar">
    <a class="btn btn--primary" href="tel:%s">%s Sună</a>
    <a class="btn btn--wa" href="%s" target="_blank" rel="noopener">%s WhatsApp</a>
  </div>

  <script src="{js_site}" defer></script>
""" % (TEL1, TEL1F, TEL2, TEL2F, WA_GEN, FACEBOOK, WA_GEN, icon("i-wa"), TEL1, icon("i-phone"), WA_GEN, icon("i-wa"))

PAGE = """<!DOCTYPE html>
<html lang="ro">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
{canonical}
<meta name="theme-color" content="#1863DC">
<script>document.documentElement.className += " js";</script>

<meta property="og:type" content="website">
<meta property="og:locale" content="ro_RO">
<meta property="og:site_name" content="Happy &amp; Hop">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{site}/{url_path}">
<meta property="og:image" content="{site}/assets/brand/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">

<link rel="icon" href="assets/brand/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="assets/brand/apple-touch-icon.png">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@600;700;800&family=Nunito:wght@400;600;700&display=swap">
<link rel="stylesheet" href="{css_base}">
<link rel="stylesheet" href="{css_site}">
{extra_head}
</head>
<body>
{sprite}

{header}
  <main id="main">
{body}
  </main>

{footer}
</body>
</html>
"""

def keep_brand_together(html):
    """Leaga „Happy & Hop" cu spatii insecabile, dar doar in textul vizibil.
    Atributele (alt, meta, og), <title> si JSON-LD raman cu spatiu normal —
    acolo nbsp n-ajuta la nimic si strica datele structurate."""
    protected = []

    def stash(m):
        protected.append(m.group(0))
        return "\x00%d\x00" % (len(protected) - 1)

    html = re.sub(r'(?is)<(script|title)\b.*?</\1>', stash, html)
    html = re.sub(r'>([^<]+)<',
                  lambda m: ">" + m.group(1).replace("Happy &amp; Hop", "Happy&nbsp;&amp;&nbsp;Hop") + "<",
                  html)
    return re.sub(r'\x00(\d+)\x00', lambda m: protected[int(m.group(1))], html)


def build(slug, title, desc, body, extra_head="", indexable=True):
    url_path = "" if slug == "index.html" else slug
    canonical = ('<link rel="canonical" href="%s/%s">' % (SITE, url_path) if indexable
                 else '<meta name="robots" content="noindex, follow">')
    head = header(slug)
    html = PAGE.format(title=title, desc=desc, slug=slug, site=SITE, url_path=url_path,
                       canonical=canonical, sprite="{sprite}", header=head, body=body,
                       footer=FOOTER.replace("{js_site}", asset("js/site.js")),
                       extra_head=extra_head,
                       css_base=asset("css/base.css"), css_site=asset("css/site.css"),
                       js_site=asset("js/site.js"))
    html = html.replace("{sprite}", sprite_for(html))
    html = keep_brand_together(html)
    path = os.path.join(OUT, slug)
    io.open(path, "w", encoding="utf-8").write(html)
    print("%-34s %6.1f KB" % (slug, len(html.encode("utf-8")) / 1024.0))

if __name__ == "__main__":
    import pages
    pages.run(build, icon, dict(TEL1=TEL1, TEL1F=TEL1F, TEL2=TEL2, TEL2F=TEL2F,
                                WA=WA, WA_GEN=WA_GEN, WA_PARTY=WA_PARTY, SITE=SITE,
                                FACEBOOK=FACEBOOK, SOCIAL=SOCIAL))
