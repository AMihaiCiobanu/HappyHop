# -*- coding: utf-8 -*-
"""Conținutul paginilor Happy & Hop (texte preluate de pe happyhop.ro)."""

ATTRACTIONS = [
    ("i-balls",   "i-sky",    "Piscină cu bile",      "Un ocean de culori în care copiii se pot juca fără griji, cu tobogane care coboară direct în valuri de bile."),
    ("i-tramp",   "i-pink",   "Parc de trambuline",   "Pentru sărituri și energie nelimitată — inclusiv zonă de foam pit cu bureți moi pentru aterizări în siguranță."),
    ("i-slide",   "i-yellow", "Tobogane uriașe",      "Adrenalina este garantată! Tobogane rapide, în spirală și cu tuburi, pe mai multe niveluri."),
    ("i-volcano", "i-orange", "Vulcan pentru cățărat","Provocarea supremă pentru cei mici: un vulcan înalt de escaladat, cu prize colorate și saltea de protecție."),
    ("i-maze",    "i-green",  "Labirint interactiv",  "Stimulează creativitatea și spiritul de aventură, cu tuneluri, plase și obstacole pe mai multe etaje."),
    ("i-team",    "i-blue",   "Jocuri de echipă",     "Activități care dezvoltă cooperarea și prietenia, coordonate de personalul nostru."),
    ("i-coffee",  "i-sky",    "Zonă pentru părinți",  "Confort și relaxare cât timp copiii se distrează: mese, fotolii, cafea bună și vizibilitate spre spațiul de joacă."),
]

REASONS = [
    ("Siguranță maximă", "Echipamente moderne, materiale de calitate și personal calificat care supraveghează atent fiecare zonă."),
    ("Experiențe unice", "Activități care dezvoltă imaginația și abilitățile motrice, gândite pe vârste."),
    ("Distracție pentru toată familia", "Zonă dedicată părinților și activități adaptate pentru toate vârstele."),
    ("Evenimente tematice", "Săptămânal organizăm ateliere creative, spectacole și sesiuni speciale de joacă."),
    ("Abonamente avantajoase", "Reduceri pentru accesul regulat la Happy &amp; Hop, pentru copiii care revin des."),
]

# Recenzii Google, preluate textual: (numar de stele, text).
REVIEWS = [
    (5, "Best playground for kids! love it!"),
    (5, "Un loc minunat pentru copii, unde distracția este garantată! Cei mici s-au bucurat enorm de experiență și, fără ezitare, au dat 5 stele pentru cât de mult s-au distrat. Atmosfera prietenoasă și activitățile variate fac din acest loc o alegere excelentă pentru petrecerea timpului în familie. Recomand cu încredere!"),
    (4, "Un loc foarte frumos și aventuros pentru copilași, de o complexitate de la foarte ușor spre moderat. Au și o sală pentru petreceri aniversare, baia a fost îngrijită de fiecare dată. Pe alocuri sunt urme vizibile de uzură și ar mai trebui îmbunătățiri constante, cu mențiunea că nu se observă la prima vedere. În plus, ar fi foarte potrivit un anunț că e responsabilitatea părinților să își țină acasă copilașii bolnavi."),
    (5, "Un spațiu foarte distractiv și cerut de copilul nostru de 2 ani și jumătate. Aș menționa că e bine ca un părinte să fie cu ochii pe copil, pentru că în graba lor de copii se întâmplă des să se împingă sau lovească unii pe alții în diversele secțiuni de acolo."),
    (5, "Spațiul foarte mare, diversificat cât să satisfacă toți piticii care se plictisesc repede și caută activități mai diverse — însă în ziua în care am fost noi a fost foarte frig în interior. Ușa se deschide larg și tot frigul se simte cam până la jumătatea spațiului. În spate, spațiul era ok ca și temperatură."),
]

# `geo`: (latitudine, longitudine) pentru fiecare locatie. Se iau din Google Maps —
# click dreapta pe pin, prima linie din meniu copiaza coordonatele. Cat timp e None,
# schema se publica fara `geo` (mai bine lipsa decat gresita).
LOCATIONS = [
    dict(
        slug="socola", page="loc-de-joaca-socola.html",
        name="Bd. Socola 27A", short="Socola",
        sub="Rodotex, lângă magazinul Jumbo · Iași",
        street="Bulevardul Socola 27A", locality="Iași", geo=(47.1445682, 27.5960932),
        img="loc-de-joaca-tobogane", alt="Structura de joacă pe mai multe niveluri de la Happy &amp; Hop, Bulevardul Socola",
        portrait=True, status="Deschis",
        text="La Happy &amp; Hop vei găsi cel mai nou loc de joacă pentru copii din Iași. Te așteptăm cu atracții inedite pentru cei mici: piscină cu bile, tobogane, un vulcan înalt pentru cățărat, parc de trambuline și multe altele.",
        extra="Aici organizăm și petrecerile private de aniversare, cu sala de evenimente decorată tematic și acces în locul de joacă pe toată durata petrecerii. Zona de părinți are mese, fotolii și cafea, cu vedere directă spre spațiul de joacă.",
        hours=[("Luni", "13:00 – 20:00"), ("Marți – Duminică", "10:00 – 20:00")],
        schema_hours=[(["Monday"], "13:00", "20:00"),
                      (["Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "10:00", "20:00")],
        maps="Bulevardul Socola 27A, Iasi",
        place_url="https://www.google.com/maps/place/Happy+and+Hop,+loc+de+joaca/@47.1445682,27.5935183,875m/data=!3m2!1e3!4b1!4m6!3m5!1s0x40cafb00235f5b6d:0xa5b64b726e2bd437!8m2!3d47.1445682!4d27.5960932!16s%2Fg%2F11w7l67_5k",
        title="Loc de joacă pe Bd. Socola, Iași — Happy &amp; Hop",
        seo_title="Loc de joacă Socola, Iași — trambuline și petreceri | Happy & Hop",
        seo_desc="Loc de joacă pentru copii pe Bulevardul Socola 27A, lângă Jumbo: piscină cu bile, trambuline, tobogane și vulcan de cățărat. Luni 13–20, marți–duminică 10–20.",
        lead="Piscină cu bile, parc de trambuline, tobogane și vulcan de escaladat, pe Bulevardul Socola 27A — lângă magazinul Jumbo.",
    ),
    dict(
        slug="moldova-mall", page="loc-de-joaca-moldova-mall.html",
        name="Moldova Mall", short="Moldova Mall",
        sub="Șoseaua Păcurari 121 · Iași",
        street="Șoseaua Păcurari 121", locality="Iași", geo=(47.1668234, 27.513135),
        img="moldova-mall-interior", alt="Spațiul de joacă Happy &amp; Hop din Moldova Mall, cu tobogan în spirală și zonă de arcade",
        portrait=False, status="Deschis",
        text="Happy &amp; Hop vă așteaptă în Moldova Mall cu tobogane, trambuline, labirinturi, piscine cu bile și muuultă voie bună! Fiecare colț al spațiului de joacă e o aventură colorată, perfectă pentru copiii care vor să sară, să se cațere și să râdă cu gura până la urechi. Iar părinții se pot relaxa cu o cafea bună în timp ce cei mici se distrează în siguranță. Ne găsești vizavi de intrarea în Carrefour.",
        extra="Locația din mall e deschisă zilnic până la ora 22:00, deci merge și pentru o oră de joacă după cumpărături. Ne recunoști ușor după literele-balon de la intrare.",
        hours=[("Luni – Duminică", "10:00 – 22:00")],
        schema_hours=[(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "10:00", "22:00")],
        maps="Moldova Mall, Soseaua Pacurari 121, Iasi",
        title="Loc de joacă în Moldova Mall, Iași — Happy &amp; Hop",
        seo_title="Loc de joacă Moldova Mall, Iași — deschis zilnic | Happy & Hop",
        seo_desc="Loc de joacă pentru copii în Moldova Mall, Șos. Păcurari 121, vizavi de intrarea în Carrefour: tobogane, trambuline, labirinturi și piscine cu bile. Zilnic 10–22.",
        lead="Tobogane, trambuline, labirinturi și piscine cu bile în Moldova Mall, vizavi de intrarea în Carrefour. Deschis zilnic, 10:00–22:00.",
    ),
    dict(
        slug="miroslava", page="loc-de-joaca-miroslava.html",
        name="Family Market Miroslava", short="Miroslava",
        sub="Miroslava · Iași",
        street="Family Market Miroslava", locality="Miroslava", geo=(47.1461986, 27.5296538),
        img=None, alt="",
        portrait=False, status="În curând",
        text="Pregătim un nou spațiu Happy &amp; Hop în Family Market Miroslava. Programul de mai jos este cel anunțat pentru deschidere — sună-ne pentru data exactă.",
        extra="Până atunci, te așteptăm la celelalte două locații din Iași: Bulevardul Socola 27A și Moldova Mall.",
        hours=[("Luni – Duminică", "09:00 – 21:00")],
        schema_hours=[],
        maps="Family Market Miroslava, Iasi",
        place_url="https://www.google.com/maps/place/Family+Market+Miroslava/@47.1461986,27.5270789,875m/data=!3m2!1e3!4b1!4m6!3m5!1s0x40cafbab75f19f37:0x28635c3a278bc3dd!8m2!3d47.1461986!4d27.5296538!16s%2Fg%2F11rz7mzkpr",
        title="Loc de joacă în Family Market Miroslava — Happy &amp; Hop",
        seo_title="Loc de joacă Miroslava — se deschide în curând | Happy & Hop",
        seo_desc="Happy & Hop deschide în curând un loc de joacă pentru copii în Family Market Miroslava, lângă Iași. Program anunțat: zilnic 09:00–21:00.",
        lead="Deschidem în curând un nou loc de joacă în Family Market Miroslava. Program anunțat: zilnic, 09:00–21:00.",
    ),
]

GALLERY = [
    ("trambuline-foam-pit",   "1600", "Parcul de trambuline cu foam pit plin de bureți moi"),
    ("piscina-cu-bile",       "max",  "Piscina cu bile și toboganele pastelate"),
    ("loc-de-joaca-tobogane", "max",  "Structura de joacă pe mai multe niveluri, cu tobogane colorate"),
    ("trambuline-caramizi",   "max",  "Zona de cărămizi gigant, lângă parcul de trambuline"),
    ("moldova-mall-interior", "1600", "Interiorul locației din Moldova Mall, cu tobogan în spirală"),
    ("moldova-mall-fatada",   "1600", "Intrarea Happy &amp; Hop din Moldova Mall, cu litere-balon"),
    ("sala-petreceri",        "max",  "Sala de petreceri decorată cu rozete de hârtie"),
    ("petrecere-decor",       "max",  "Masă de petrecere cu fundal foto Happy Birthday"),
    ("petrecere-masa",        "max",  "Masa lungă pentru invitați, cu scaune colorate"),
    ("zona-parinti",          "max",  "Zona de relaxare pentru părinți, cu mese, fotolii și cafea"),
]

PARTY_INCLUDES = [
    ("i-ticket",  "Acces la toate atracțiile", "Trambuline, tobogane, piscină cu bile — pe toată durata evenimentului."),
    ("i-sparkle", "Decor tematic",             "Culori vesele și decor pe tema aleasă de sărbătorit."),
    ("i-cake",    "Meniu pentru cei mici și părinți", "Opțiuni adaptate tuturor preferințelor."),
    ("i-smile",   "Animator dedicat (opțional)", "Jocuri interactive și activități captivante."),
    ("i-mail",    "Invitație digitală",        "Personalizată cu personajul preferat al copilului tău."),
]

# Dimensiunile fisierelor originale din assets/img/_src/ (lătime x inaltime, in px).
# Sunt singura sursa de adevar pentru descriptorii `srcset` si pentru raportul de aspect
# scris in `width`/`height`. Daca reincarci o poza cu alte dimensiuni, actualizeaz-o aici.
IMG_DIMS = {
    "trambuline-foam-pit":   (1600, 900),
    "moldova-mall-interior": (1600, 1200),
    "moldova-mall-fatada":   (1600, 1200),
    "loc-de-joaca-tobogane": (810, 1080),
    "trambuline-caramizi":   (810, 1080),
    "piscina-cu-bile":       (810, 1080),
    "sala-petreceri":        (810, 1080),
    "petrecere-decor":       (810, 1080),
    "petrecere-masa":        (810, 1080),
    "zona-parinti":          (810, 1080),
}


def img_tag(name, widths, sizes, alt, cls="", extra="", base=800, eager=False):
    """<img> responsive. Inaltimea si descriptorii `w` se calculeaza din IMG_DIMS,
    ca raportul de aspect declarat sa fie mereu cel real (fara salt de layout)."""
    ow, oh = IMG_DIMS[name]
    def real_w(x):
        return ow if x == "max" else int(x)
    def srcset(ext):
        return ", ".join(["assets/img/%s-%s.%s %dw" % (name, x, ext, real_w(x)) for x in widths])
    default = "assets/img/%s-%s.jpg" % (name, widths[-1])
    w = min(base, ow)
    h = int(round(w * oh / float(ow)))
    loading = 'loading="eager" fetchpriority="high"' if eager else 'loading="lazy"'
    c = ' class="%s"' % cls if cls else ""
    # AVIF are ~55% din greutatea JPG-ului la aceeasi calitate; browserele vechi iau JPG-ul.
    return ('<picture><source type="image/avif" srcset="%s" sizes="%s">'
            '<img%s src="%s" srcset="%s" sizes="%s" width="%d" height="%d" alt="%s" %s decoding="async"%s></picture>'
            % (srcset("avif"), sizes, c, default, srcset("jpg"), sizes, w, h, alt, loading,
               (" " + extra) if extra else ""))


# ============================================================ INDEX
def page_index(icon, C):
    cards = "\n".join([
        """        <article class="card reveal">
          <div class="card__icon %s">%s</div>
          <h3>%s</h3>
          <p>%s</p>
        </article>""" % (color, icon(ic), title, text)
        for ic, color, title, text in ATTRACTIONS])

    reasons = "\n".join([
        """          <div class="reason">
            <span class="reason__badge">%d</span>
            <div>
              <h3>%s</h3>
              <p>%s</p>
            </div>
          </div>""" % (i + 1, t, d) for i, (t, d) in enumerate(REASONS)])

    strip = "\n".join([
        """          <a href="galerie.html" aria-label="Vezi galeria foto">%s</a>"""
        % img_tag(n, ["400", "800"], "(min-width:1024px) 16vw, (min-width:768px) 30vw, 45vw", alt)
        for n, _s, alt in GALLERY[:6]])

    reviews = "\n".join([
        """            <article class="review-card reveal">
              <div class="review-card__stars" aria-label="%d din 5 stele">%s</div>
              <p>„%s”</p>
              <span class="review-card__src">Recenzie Google</span>
            </article>""" % (stars, icon("i-star-fill") * stars, text)
        for stars, text in REVIEWS])

    def compact(l):
        """„Luni 13:00 – 20:00" -> „Luni 13–20": pe cardurile mici încape pe un rând."""
        txt = " · ".join("%s %s" % (d, t) for d, t in l["hours"])
        txt = txt.replace(":00", "").replace(" – ", "–")
        return txt if l["status"] == "Deschis" else "În curând · program anunțat: " + txt

    hero_facts = "\n".join(["""          <li>%s <span><a href="%s">%s</a> <span>%s</span></span></li>"""
                            % (icon("i-pin"), l["page"], l["name"],
                               compact(l) if l["status"] == "Deschis" else "în curând")
                            for l in LOCATIONS])

    loc_cards = "\n".join(["""          <article class="card card--cta reveal">
            <div class="card__icon %s">%s</div>
            <h3><a href="%s" style="text-decoration:none">%s</a></h3>
            <p>%s<br>%s</p>
            <a class="btn btn--outline btn--sm" href="%s">Vezi locația %s</a>
          </article>""" % (
        col, icon("i-pin"), l["page"], l["name"], l["sub"],
        compact(l), l["page"], icon("i-arrow"))
        for l, col in zip(LOCATIONS, ["i-blue", "i-pink", "i-yellow"])])

    return """
    <section class="hero">
      <div class="hero__media">
        %s
      </div>

      <span class="floaty floaty--1" aria-hidden="true"><svg viewBox="0 0 60 90"><ellipse cx="30" cy="34" rx="26" ry="32" fill="#FFC93C"/><path d="M30 66v8c0 6 8 5 8 13" stroke="#fff" stroke-width="2.5" fill="none" stroke-linecap="round"/></svg></span>
      <span class="floaty floaty--2" aria-hidden="true"><svg viewBox="0 0 60 90"><ellipse cx="30" cy="34" rx="26" ry="32" fill="#FE9ACC"/><path d="M30 66v8c0 6-8 5-8 13" stroke="#fff" stroke-width="2.5" fill="none" stroke-linecap="round"/></svg></span>
      <span class="floaty floaty--3" aria-hidden="true"><svg viewBox="0 0 60 90"><ellipse cx="30" cy="34" rx="26" ry="32" fill="#6FC24A"/><path d="M30 66v8c0 6 8 5 8 13" stroke="#fff" stroke-width="2.5" fill="none" stroke-linecap="round"/></svg></span>

      <div class="container hero__inner">
        <span class="hero__badge"><span class="dot"></span> 3 locații în Iași · deschis zilnic</span>
        <h1>Loc de joacă în Iași, <span class="hl">unde copiii sar de bucurie</span></h1>
        <p>700&nbsp;m² de aventură: trambuline, tobogane uriașe, piscine cu bile, vulcan de escaladat și labirinturi interactive. Iar aniversările devin petreceri de neuitat.</p>
        <div class="hero__actions">
          <a class="btn btn--sun" href="petreceri.html">%s Rezervă o petrecere</a>
          <a class="btn btn--ghost" href="atractii.html">Vezi atracțiile %s</a>
        </div>
        <ul class="hero__facts">
%s
        </ul>
      </div>

      <div class="hero__wave" aria-hidden="true">
        <svg viewBox="0 0 1440 70" preserveAspectRatio="none"><path d="M0 70V28c130-24 260-30 390-18s260 34 390 30 260-30 390-34 180 6 270 14v50Z"/></svg>
      </div>
    </section>

    <div class="container">
      <div class="stats reveal">
        <div class="stat"><p class="stat__num"><span data-count="700">700</span>&nbsp;m<sup>2</sup></p><p class="stat__label">spațiu de joacă</p></div>
        <div class="stat"><p class="stat__num"><span data-count="3">3</span></p><p class="stat__label">locații în Iași</p></div>
        <div class="stat"><p class="stat__num"><span data-count="7">7</span></p><p class="stat__label">zone de atracții</p></div>
        <div class="stat"><p class="stat__num"><span data-count="2.5">2,5</span>&nbsp;h</p><p class="stat__label">durata unei petreceri</p></div>
      </div>
    </div>

    <section class="section">
      <div class="container split">
        <div class="split__body reveal">
          <span class="eyebrow">%s Bine ai venit</span>
          <h2>O aventură de neuitat pentru cei mici</h2>
          <p class="lead">Happy &amp; Hop este mai mult decât un loc de joacă — este un univers magic unde copiii își pot explora imaginația și pot trăi momente unice alături de prieteni și familie.</p>
          <p>Cu o suprafață de 700&nbsp;m², oferim un spațiu sigur și captivant, dotat cu atracții moderne care fac orice vizită memorabilă. Fie că e vorba despre joacă liberă, activități de dezvoltare motrică sau evenimente tematice, la noi copiii găsesc mereu un mediu plin de energie și creativitate.</p>
          <ul class="checklist">
            <li>%s <span>Toate atracțiile sunt construite din materiale de calitate și verificate periodic.</span></li>
            <li>%s <span>Personal specializat, prezent permanent în sălile de joacă.</span></li>
            <li>%s <span>Zonă dedicată părinților, cu cafea și vedere spre spațiul de joacă.</span></li>
          </ul>
          <p><a class="btn btn--primary" href="atractii.html">Descoperă atracțiile %s</a></p>
        </div>

        <div class="split__media reveal">
          <div class="collage">
            <span class="collage__sticker">700 m² de joacă</span>
            <div class="collage__main">
              %s
            </div>
            <div class="collage__side">
              %s
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head reveal">
          <span class="eyebrow eyebrow--pink">%s Ce te așteaptă</span>
          <h2>Șapte zone, o singură zi de distracție</h2>
          <p class="lead">De la piscina cu bile la vulcanul de escaladat — fiecare colț are propria poveste.</p>
        </div>

        <div class="grid-cards" style="margin-top:var(--sp-7)">
%s
        </div>
      </div>
    </section>

    <section class="section--tight">
      <div class="container">
        <div class="panel reveal">
          <span class="eyebrow">%s De ce Happy &amp; Hop</span>
          <h2 style="margin-top:var(--sp-4)">Cinci motive pentru care copiii cer să revină</h2>
          <div class="reasons">
%s
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head reveal">
          <span class="eyebrow eyebrow--green">%s Pachete de joacă</span>
          <h2>Alege cum vrei să te joci</h2>
          <p class="lead">Fie că vrei o experiență unică pentru o zi sau acces nelimitat la distracție, avem pachete pentru toate preferințele.</p>
        </div>

        <div class="grid-cards" style="margin-top:var(--sp-7)">
          <article class="pass-card reveal">
            <div class="pass-card__icon i-sky">%s</div>
            <h3>Acces individual</h3>
            <p>Intrare valabilă pentru o sesiune de joacă, la oricare dintre locațiile deschise.</p>
          </article>
          <article class="pass-card reveal">
            <div class="pass-card__icon i-pink">%s</div>
            <h3>Pachet family</h3>
            <p>Ideal pentru familiile cu doi sau mai mulți copii care vin împreună la joacă.</p>
          </article>
          <article class="pass-card reveal">
            <div class="pass-card__icon i-yellow">%s</div>
            <h3>Abonament lunar</h3>
            <p>Acces nelimitat la toate atracțiile, cu reducere pentru vizitele regulate.</p>
          </article>
        </div>

        <p class="text-center" style="margin-top:var(--sp-5);color:var(--hh-muted)">Tarifele de intrare se afișează la recepție și diferă pe locații. Pentru prețul zilei, sună-ne la <a href="tel:%s">%s</a>.</p>
      </div>
    </section>

    <section class="section">
      <div class="container split split--reverse">
        <div class="split__body reveal">
          <span class="eyebrow eyebrow--yellow">%s Petreceri</span>
          <h2>Aniversarea copilului tău, fără stres</h2>
          <p class="lead">Ne ocupăm noi de toate detaliile: decor, meniu, invitație digitală și acces la locul de joacă pe toată durata evenimentului.</p>
          <ul class="checklist">
            <li>%s <span><strong>Varianta 1 — 1490 lei</strong> pentru 10 copii, 2,5 ore</span></li>
            <li>%s <span><strong>Varianta 2 — 1990 lei</strong> pentru 10 copii și 10 părinți, 2,5 ore</span></li>
            <li>%s <span>Extraopțiuni: pictură pe față, mascote animate, animator dedicat</span></li>
          </ul>
          <div class="hero__actions">
            <a class="btn btn--primary" href="petreceri.html">Vezi pachetele %s</a>
            <a class="btn btn--wa" href="%s" target="_blank" rel="noopener">%s Rezervă pe WhatsApp</a>
          </div>
        </div>
        <div class="split__media reveal">
          <div class="collage">
            <div class="collage__main">
              %s
            </div>
            <div class="collage__side">
              %s
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section--tight">
      <div class="container">
        <div class="section-head reveal">
          <span class="eyebrow">%s Unde ne găsești</span>
          <h2>Trei locații în Iași</h2>
        </div>

        <div class="grid-cards" style="margin-top:var(--sp-6)">
%s
        </div>

        <p class="text-center" style="margin-top:var(--sp-6)"><a class="btn btn--outline" href="locatii.html">Detalii și hărți %s</a></p>
      </div>
    </section>

    <section class="section--tight">
      <div class="container">
        <div class="section-head reveal">
          <span class="eyebrow eyebrow--pink">%s Galerie</span>
          <h2>Așa arată o zi la Happy &amp; Hop</h2>
        </div>
        <div class="gallery-strip" style="margin-top:var(--sp-6)">
%s
        </div>
        <p class="text-center" style="margin-top:var(--sp-6)"><a class="btn btn--outline" href="galerie.html">Vezi toată galeria %s</a></p>
      </div>
    </section>

    <section class="section--tight">
      <div class="container">
        <div class="section-head reveal">
          <span class="eyebrow eyebrow--yellow">%s Recenzii</span>
          <h2>Ce spun părinții despre noi</h2>
          <p class="lead">4,5 din 5 — recenzii reale de la familiile care ne-au vizitat, preluate de pe Google.</p>
        </div>

        <div class="reviews-slider" style="margin-top:var(--sp-6)" data-slider>
          <div class="reviews-slider__track" data-slider-track>
%s
          </div>
          <div class="reviews-slider__nav">
            <button type="button" class="slider-btn" data-slider-prev aria-label="Recenzia anterioară"><svg aria-hidden="true" style="transform:scaleX(-1)"><use href="#i-arrow"></use></svg></button>
            <button type="button" class="slider-btn" data-slider-next aria-label="Recenzia următoare">%s</button>
          </div>
        </div>
      </div>
    </section>

    <section class="section--tight">
      <div class="container">
        <div class="social-band reveal">
          <div class="social-band__head">
            <span class="eyebrow">%s Rămâi aproape</span>
            <h2>Urmărește-ne pe Facebook</h2>
            <p class="lead">Acolo anunțăm primii ofertele și reducerile, zilele tematice și concursurile cu premii — plus poze de la petreceri și noutăți despre locația nouă din Miroslava.</p>
          </div>

          <ul class="social-perks">
            <li>
              <span class="social-perks__icon i-yellow">%s</span>
              <div>
                <h3>Oferte și reduceri</h3>
                <p>Prețuri speciale la intrare, anunțate doar pe pagină.</p>
              </div>
            </li>
            <li>
              <span class="social-perks__icon i-pink">%s</span>
              <div>
                <h3>Evenimente și zile tematice</h3>
                <p>Ateliere, mascote și surprize — afli din timp când vin.</p>
              </div>
            </li>
            <li>
              <span class="social-perks__icon i-blue">%s</span>
              <div>
                <h3>Concursuri cu premii</h3>
                <p>Intrări gratuite și pachete de petrecere pentru urmăritori.</p>
              </div>
            </li>
          </ul>

          <div class="social-band__actions">
            <a class="btn btn--fb" href="%s" target="_blank" rel="noopener">%s Urmărește-ne pe Facebook</a>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="cta-band reveal">
          <h2>Rezervă o vizită acum!</h2>
          <p>Nu mai sta pe gânduri — hai la Happy &amp; Hop pentru o experiență de neuitat.</p>
          <div class="cta-band__actions">
            <a class="btn btn--primary" href="tel:%s">%s %s</a>
            <a class="btn btn--wa" href="%s" target="_blank" rel="noopener">%s WhatsApp</a>
          </div>
        </div>
      </div>
    </section>
""" % (
        img_tag("trambuline-foam-pit", ["400", "800", "1600"], "100vw",
                "Parcul de trambuline Happy &amp; Hop, cu zonă de foam pit plină de bureți moi",
                base=1600, eager=True),
        icon("i-cake"), icon("i-arrow"),
        hero_facts,
        icon("i-heart"),
        icon("i-check"), icon("i-check"), icon("i-check"), icon("i-arrow"),
        img_tag("piscina-cu-bile", ["400", "800", "max"], "(min-width:768px) 45vw, 90vw",
                "Piscina cu bile de la Happy &amp; Hop, cu tobogane pastelate"),
        img_tag("trambuline-caramizi", ["400", "800"], "(min-width:768px) 22vw, 42vw",
                "Zona cu cărămizi gigant din parcul de trambuline"),
        icon("i-sparkle"), cards,
        icon("i-star"), reasons,
        icon("i-ticket"),
        icon("i-ticket"), icon("i-family"), icon("i-calendar"),
        C["TEL1"], C["TEL1F"],
        icon("i-balloon"),
        icon("i-check"), icon("i-check"), icon("i-check"),
        icon("i-arrow"), C["WA_PARTY"], icon("i-wa"),
        img_tag("sala-petreceri", ["400", "800", "max"], "(min-width:768px) 45vw, 90vw",
                "Sala de petreceri Happy &amp; Hop, decorată cu rozete de hârtie și baloane"),
        img_tag("petrecere-decor", ["400", "800"], "(min-width:768px) 22vw, 42vw",
                "Masă de petrecere cu fundal foto Happy Birthday"),
        icon("i-map"), loc_cards, icon("i-arrow"),
        icon("i-sparkle"), strip, icon("i-arrow"),
        icon("i-star"), reviews, icon("i-arrow"),
        icon("i-heart"), icon("i-ticket"), icon("i-balloon"), icon("i-star"),
        C["FACEBOOK"], icon("i-fb"),
        C["TEL1"], icon("i-phone"), C["TEL1F"], C["WA_GEN"], icon("i-wa"),
    )


# ============================================================ helpers
def page_head(icon, eyebrow_icon, eyebrow, title, lead):
    return """
    <section class="page-head">
      <div class="container">
        <span class="eyebrow">%s %s</span>
        <h1>%s</h1>
        <p>%s</p>
      </div>
      <div class="page-head__wave" aria-hidden="true">
        <svg viewBox="0 0 1440 60" preserveAspectRatio="none"><path d="M0 60V24c140-20 280-26 420-14s280 30 420 26 280-26 420-30 180 6 180 6v48Z"/></svg>
      </div>
    </section>
""" % (icon(eyebrow_icon), eyebrow, title, lead)


def cta_band(icon, C, title="Rezervă o vizită acum!",
             text="Nu mai sta pe gânduri — hai la Happy &amp; Hop pentru o experiență de neuitat."):
    return """
    <section class="section">
      <div class="container">
        <div class="cta-band reveal">
          <h2>%s</h2>
          <p>%s</p>
          <div class="cta-band__actions">
            <a class="btn btn--primary" href="tel:%s">%s %s</a>
            <a class="btn btn--wa" href="%s" target="_blank" rel="noopener">%s WhatsApp</a>
          </div>
        </div>
      </div>
    </section>
""" % (title, text, C["TEL1"], icon("i-phone"), C["TEL1F"], C["WA_GEN"], icon("i-wa"))


# ============================================================ ATRACȚII
def page_atractii(icon, C):
    cards = "\n".join([
        """        <article class="card reveal">
          <div class="card__icon %s">%s</div>
          <h3>%s</h3>
          <p>%s</p>
        </article>""" % (color, icon(ic), title, text)
        for ic, color, title, text in ATTRACTIONS])

    return page_head(icon, "i-sparkle", "Atracții",
                     "Toate atracțiile Happy &amp; Hop",
                     "Șapte zone de joacă pe 700&nbsp;m², gândite pentru copii de toate vârstele — de la piscina cu bile la vulcanul de escaladat.") + """
    <section class="section">
      <div class="container">
        <div class="grid-cards">
%s
        </div>
      </div>
    </section>

    <section class="section--tight">
      <div class="container split">
        <div class="split__media reveal">
          <div class="collage">
            <span class="collage__sticker">Aterizare moale</span>
            <div class="collage__main">
              %s
            </div>
          </div>
        </div>
        <div class="split__body reveal">
          <span class="eyebrow eyebrow--green">%s Siguranță</span>
          <h2>Joacă liberă, dar niciodată nesupravegheată</h2>
          <p>Siguranța și confortul sunt esențiale pentru noi, așa că toate atracțiile sunt construite cu materiale de calitate și monitorizate atent de personal specializat.</p>
          <ul class="checklist">
            <li>%s <span>Zone separate pe vârste, ca cei mici să nu se intersecteze cu cei mari.</span></li>
            <li>%s <span>Saltele de protecție și foam pit la zonele de sărituri.</span></li>
            <li>%s <span>Personal calificat prezent permanent în sală.</span></li>
            <li>%s <span>Curățenie și verificarea echipamentelor la fiecare tură.</span></li>
          </ul>
        </div>
      </div>
    </section>

    <section class="section--tight">
      <div class="container">
        <div class="panel reveal">
          <span class="eyebrow">%s Bine de știut</span>
          <h2 style="margin-top:var(--sp-4)">Înainte să vii la joacă</h2>
          <div class="reasons">
            <div class="reason">
              <span class="reason__badge">%s</span>
              <div><h3>Șosete antiderapante</h3><p>Accesul în zonele de joacă se face cu șosete antiderapante, atât pentru copii, cât și pentru părinți.</p></div>
            </div>
            <div class="reason">
              <span class="reason__badge">%s</span>
              <div><h3>Program flexibil</h3><p>Locațiile sunt deschise zilnic. Verifică programul fiecărei locații înainte de vizită.</p></div>
            </div>
            <div class="reason">
              <span class="reason__badge">%s</span>
              <div><h3>Zonă pentru părinți</h3><p>Mese, fotolii și cafea bună, cu vedere directă spre spațiul de joacă.</p></div>
            </div>
            <div class="reason">
              <span class="reason__badge">%s</span>
              <div><h3>Evenimente tematice</h3><p>Săptămânal organizăm ateliere creative, spectacole și sesiuni speciale de joacă.</p></div>
            </div>
          </div>
        </div>
      </div>
    </section>
""" % (cards,
       img_tag("trambuline-foam-pit", ["400", "800", "1600"], "(min-width:768px) 45vw, 90vw",
               "Foam pit cu bureți moi, la parcul de trambuline"),
       icon("i-shield"),
       icon("i-check"), icon("i-check"), icon("i-check"), icon("i-check"),
       icon("i-info"),
       icon("i-check"), icon("i-clock"), icon("i-coffee"), icon("i-sparkle")) + cta_band(icon, C)


# ============================================================ PETRECERI
def page_petreceri(icon, C):
    includes = "\n".join([
        """          <article class="card reveal">
            <div class="card__icon %s">%s</div>
            <h3>%s</h3>
            <p>%s</p>
          </article>""" % (col, icon(ic), t, d)
        for (ic, t, d), col in zip(PARTY_INCLUDES, ["i-sky", "i-pink", "i-yellow", "i-green", "i-blue"])])

    v1 = ["2,5 ore de petrecere", "Acces în locul de joacă pe toată durata evenimentului",
          "1 apă și 1 suc pentru fiecare copil", "Pizza pentru copii",
          "Invitație digitală personalizată", "Lumânare pentru tort", "Balon cifră cu heliu"]
    v2 = ["2,5 ore de petrecere", "Acces în locul de joacă pe toată durata evenimentului",
          "1 apă și 1 suc pentru fiecare copil", "Pizza pentru copii",
          "1 cafea și 1 apă pentru fiecare părinte", "Pizza pentru părinți",
          "Invitație digitală personalizată", "Lumânare pentru tort", "Balon cifră cu heliu"]

    def li(items):
        return "\n".join(["            <li>%s <span>%s</span></li>" % (icon("i-check"), x) for x in items])

    return page_head(icon, "i-cake", "Petreceri",
                     "Petreceri de neuitat la Happy &amp; Hop",
                     "Transformă aniversarea copilului tău într-o aventură. Noi ne ocupăm de toate detaliile — tu doar te bucuri de moment.") + """
    <section class="section">
      <div class="container split">
        <div class="split__body reveal">
          <span class="eyebrow eyebrow--pink">%s Cum funcționează</span>
          <h2>Fiecare aniversare devine un eveniment magic</h2>
          <p class="lead">Oferim pachete complete pentru petreceri, astfel încât tu să te bucuri de moment, fără stres.</p>
          <p>Organizarea unei petreceri poate fi o provocare, dar noi ne ocupăm de toate detaliile pentru a ne asigura că micuțul tău și invitații săi vor avea parte de o zi de neuitat. Cu un spațiu generos, echipamente sigure și activități captivante, Happy &amp; Hop este locul ideal pentru a sărbători alături de familie și prieteni.</p>
          <div class="hero__actions" data-contact-zone>
            <a class="btn btn--wa" href="%s" target="_blank" rel="noopener">%s Verifică disponibilitatea</a>
            <a class="btn btn--outline" href="tel:%s">%s %s</a>
          </div>
        </div>
        <div class="split__media reveal">
          <div class="collage">
            <span class="collage__sticker">La mulți ani!</span>
            <div class="collage__main">
              %s
            </div>
            <div class="collage__side">
              %s
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section--tight">
      <div class="container">
        <div class="section-head reveal">
          <span class="eyebrow eyebrow--yellow">%s Incluse în pachet</span>
          <h2>Ce primești la fiecare petrecere</h2>
        </div>
        <div class="grid-cards" style="margin-top:var(--sp-7)">
%s
        </div>
      </div>
    </section>

    <section class="section" id="preturi">
      <div class="container">
        <div class="section-head reveal">
          <span class="eyebrow">%s Prețuri</span>
          <h2>Petrecere privată — alege varianta</h2>
          <p class="lead">Prețurile de mai jos sunt pentru petrecerea privată, cu acces în locul de joacă pe toată durata evenimentului.</p>
        </div>

        <div class="price-grid" style="margin-top:var(--sp-7)">
          <article class="price-card reveal">
            <div>
              <h3>Varianta 1</h3>
              <p style="color:var(--hh-muted)">Pentru grupul de copii</p>
            </div>
            <p class="price-card__amount">1490 lei <small>pentru 10 copii · 2,5 ore</small></p>
            <ul>
%s
            </ul>
            <a class="btn btn--outline btn--block" href="%s" target="_blank" rel="noopener">%s Rezervă Varianta 1</a>
          </article>

          <article class="price-card price-card--featured reveal">
            <span class="price-card__flag">Cea mai aleasă</span>
            <div>
              <h3>Varianta 2</h3>
              <p style="color:var(--hh-muted)">Copii și părinți, totul inclus</p>
            </div>
            <p class="price-card__amount">1990 lei <small>pentru 10 copii + 10 părinți · 2,5 ore</small></p>
            <ul>
%s
            </ul>
            <a class="btn btn--primary btn--block" href="%s" target="_blank" rel="noopener">%s Rezervă Varianta 2</a>
          </article>
        </div>

        <div class="note reveal" style="margin-top:var(--sp-5);max-width:60rem;margin-inline:auto">
          %s
          <p>Tortul nu este inclus în pachet și se aduce din exterior, însoțit de certificat de conformitate. Pentru grupuri mai mari de 10 copii sau pentru pachete personalizate, sună-ne și construim împreună oferta.</p>
        </div>
      </div>
    </section>

    <section class="section--tight">
      <div class="container">
        <div class="panel reveal">
          <span class="eyebrow">%s Extraopțiuni</span>
          <h2 style="margin-top:var(--sp-4)">Adaugă un plus de magie</h2>
          <div class="reasons">
            <div class="reason">
              <span class="reason__badge">%s</span>
              <div><h3>Pictură pe față</h3><p>Transformă copiii în personajele preferate, direct la petrecere.</p></div>
            </div>
            <div class="reason">
              <span class="reason__badge">%s</span>
              <div><h3>Mascote animate</h3><p>Apariții speciale ale eroilor preferați ai copiilor.</p></div>
            </div>
            <div class="reason">
              <span class="reason__badge">%s</span>
              <div><h3>Animator dedicat</h3><p>Jocuri interactive și activități captivante pe toată durata evenimentului.</p></div>
            </div>
            <div class="reason">
              <span class="reason__badge">%s</span>
              <div><h3>Baloane de săpun</h3><p>Momentul preferat al celor mici, inclus în pachetul Premium.</p></div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section--tight">
      <div class="container">
        <div class="section-head reveal">
          <span class="eyebrow eyebrow--green">%s Întrebări frecvente</span>
          <h2>Ce ne întreabă părinții</h2>
        </div>
        <div class="faq" style="margin-top:var(--sp-6)">
          <details><summary>Cât durează o petrecere?</summary><p>Ambele variante includ 2,5 ore de petrecere, cu acces în locul de joacă pe toată durata evenimentului.</p></details>
          <details><summary>Pot aduce tortul de acasă?</summary><p>Da. Tortul nu este inclus în pachet și se aduce din exterior, însoțit de certificat de conformitate.</p></details>
          <details><summary>Câți copii sunt incluși în preț?</summary><p>Pachetele sunt calculate pentru 10 copii. Varianta 2 include, în plus, meniu pentru 10 părinți. Pentru grupuri mai mari, sună-ne pentru o ofertă personalizată.</p></details>
          <details><summary>Ce include meniul copiilor?</summary><p>Pizza, o apă și un suc pentru fiecare copil. La Varianta 2 se adaugă pizza, cafea și apă pentru părinți.</p></details>
          <details><summary>Cum rezerv o petrecere?</summary><p>Ne scrii pe WhatsApp sau ne suni la <a href="tel:%s">%s</a> ori <a href="tel:%s">%s</a>. Verificăm disponibilitatea pentru data dorită și confirmăm rezervarea.</p></details>
          <details><summary>La ce locație se pot organiza petreceri?</summary><p>Petrecerile private se organizează la locația din Bulevardul Socola 27A (Rodotex, lângă Jumbo). Pentru Moldova Mall, întreabă-ne de disponibilitate.</p></details>
        </div>
      </div>
    </section>
""" % (icon("i-sparkle"), C["WA_PARTY"], icon("i-wa"), C["TEL1"], icon("i-phone"), C["TEL1F"],
       img_tag("sala-petreceri", ["400", "800", "max"], "(min-width:768px) 45vw, 90vw",
               "Sala de petreceri decorată cu rozete de hârtie, mese și scaune colorate"),
       img_tag("petrecere-masa", ["400", "800"], "(min-width:768px) 22vw, 42vw",
               "Masa lungă de petrecere cu scaune colorate și lumânare Happy Birthday"),
       icon("i-heart"), includes,
       icon("i-ticket"),
       li(v1), C["WA_PARTY"], icon("i-wa"),
       li(v2), C["WA_PARTY"], icon("i-wa"),
       icon("i-info"),
       icon("i-star"), icon("i-paint"), icon("i-smile"), icon("i-sparkle"), icon("i-balloon"),
       icon("i-info"),
       C["TEL1"], C["TEL1F"], C["TEL2"], C["TEL2F"]) + cta_band(
        icon, C, "Rezervă petrecerea perfectă",
        "Contactează-ne pentru a verifica disponibilitatea și pentru a rezerva data dorită.")


# ============================================================ LOCAȚII
def maps_link(loc):
    """Linkul real al locului din Google Maps. Fara el, cautare dupa adresa."""
    import urllib.parse
    if loc.get("place_url"):
        return loc["place_url"].replace("&", "&amp;")
    if loc.get("geo"):
        return "https://www.google.com/maps/search/?api=1&amp;query=%s,%s" % loc["geo"]
    return "https://www.google.com/maps/search/?api=1&amp;query=" + urllib.parse.quote(loc["maps"])


def map_embed(loc):
    """Harta incorporata, centrata pe coordonatele exacte. Fara cheie API si fara
    JavaScript; iframe-ul se incarca doar cand ajunge aproape de ecran."""
    if not loc.get("geo"):
        return ""
    lat, lng = loc["geo"]
    src = "https://www.google.com/maps?q=%s,%s&amp;z=17&amp;hl=ro&amp;output=embed" % (lat, lng)
    return ('<div class="map-embed"><iframe src="%s" title="Harta către Happy &amp; Hop — %s" '
            'loading="lazy" referrerpolicy="no-referrer-when-downgrade" '
            'allowfullscreen></iframe></div>' % (src, loc["name"]))


def loc_media(loc):
    if loc["img"]:
        widths = ["400", "800", "max"] if loc["portrait"] else ["400", "800", "1600"]
        return '<div class="loc-card__media">%s<span class="loc-card__badge%s">%s</span></div>' % (
            img_tag(loc["img"], widths, "(min-width:768px) 45vw, 92vw", loc["alt"]),
            "" if loc["status"] == "Deschis" else " loc-card__badge--soon", loc["status"])
    return ('<div class="loc-card__media"><div class="loc-card__media--empty">'
            '<p style="font-family:var(--font-display);font-weight:800;font-size:1.3rem;color:var(--hh-deep)">'
            'Deschidem în curând</p></div>'
            '<span class="loc-card__badge loc-card__badge--soon">%s</span></div>' % loc["status"])


def loc_hours(loc):
    return "\n".join(["            <div><dt>%s</dt><dd>%s</dd></div>" % (d, t) for d, t in loc["hours"]])


# ============================================================ LOCAȚII (hub)
def page_locatii(icon, C):
    cards = []
    for loc in LOCATIONS:
        cards.append("""      <article class="loc-card reveal" id="%s">
        %s
        <div class="loc-card__body">
          <div>
            <h2 style="font-size:var(--fs-h3)"><a href="%s" style="text-decoration:none">%s</a></h2>
            <p style="color:var(--hh-muted);font-weight:700">%s</p>
          </div>
          <p>%s</p>
          <dl class="hours">
%s
          </dl>
          <div class="loc-card__actions">
            <a class="btn btn--primary btn--sm" href="%s">Vezi detalii %s</a>
            <a class="btn btn--outline btn--sm" href="%s" target="_blank" rel="noopener">%s Deschide în Maps</a>
          </div>
        </div>
      </article>""" % (loc["slug"], loc_media(loc), loc["page"], loc["name"], loc["sub"],
                       loc["text"], loc_hours(loc),
                       loc["page"], icon("i-arrow"), maps_link(loc), icon("i-map")))

    return page_head(icon, "i-pin", "Locații",
                     "Locurile noastre de joacă din Iași",
                     "Ne găsești în trei puncte din oraș. Fiecare locație are pagina ei, cu program, adresă și hartă.") + """
    <section class="section">
      <div class="container" style="display:grid;gap:var(--sp-6)">
%s
      </div>
    </section>
""" % "\n".join(cards) + cta_band(
        icon, C, "Vino la joacă azi",
        "Sună-ne pentru tarife, disponibilitate sau rezervări de petreceri.")


# ============================================================ LOCAȚIE (pagină proprie)
def page_locatie(loc, icon, C):
    others = [l for l in LOCATIONS if l["slug"] != loc["slug"]]
    other_cards = "\n".join(["""          <article class="card card--cta reveal">
            <div class="card__icon %s">%s</div>
            <h3><a href="%s" style="text-decoration:none">%s</a></h3>
            <p>%s<br>%s</p>
            <a class="btn btn--outline btn--sm" href="%s">Vezi locația %s</a>
          </article>""" % (col, icon("i-pin"), l["page"], l["name"], l["sub"],
                           " · ".join("%s %s" % (d, t) for d, t in l["hours"]),
                           l["page"], icon("i-arrow"))
        for l, col in zip(others, ["i-blue", "i-pink"])])

    is_open = loc["status"] == "Deschis"
    gallery_names = ["piscina-cu-bile", "trambuline-caramizi", "sala-petreceri"]
    strip = "\n".join(["""          <a href="galerie.html" aria-label="Vezi galeria foto">%s</a>"""
                       % img_tag(n, ["400", "800"], "(min-width:1024px) 22vw, 45vw",
                                 dict((g[0], g[2]) for g in GALLERY)[n])
                       for n in gallery_names])

    hero_media = (img_tag(loc["img"],
                          (["400", "800", "max"] if loc["portrait"] else ["400", "800", "1600"]),
                          "(min-width:768px) 45vw, 90vw", loc["alt"])
                  if loc["img"] else
                  '<div class="loc-card__media--empty" style="border-radius:var(--r-lg)">'
                  '<p style="font-family:var(--font-display);font-weight:800;font-size:1.3rem;'
                  'color:var(--hh-deep)">Deschidem în curând</p></div>')

    map_section = ("""
    <section class="section--tight">
      <div class="container">
        <div class="section-head reveal">
          <span class="eyebrow eyebrow--green">%s Cum ajungi</span>
          <h2>Ne găsești aici</h2>
          <p class="lead">%s</p>
        </div>
        <div class="reveal" style="margin-top:var(--sp-6)">
          %s
        </div>
        <p class="text-center" style="margin-top:var(--sp-5)">
          <a class="btn btn--primary" href="%s" target="_blank" rel="noopener">%s Deschide în Google Maps</a>
        </p>
      </div>
    </section>
""" % (icon("i-map"), loc["sub"], map_embed(loc), maps_link(loc), icon("i-map"))) if loc.get("geo") else ""

    attractions_section = """
    <section class="section--tight">
      <div class="container">
        <div class="section-head reveal">
          <span class="eyebrow eyebrow--pink">%s Ce găsești aici</span>
          <h2>Atracțiile din locație</h2>
          <p class="lead">Piscină cu bile, parc de trambuline, tobogane uriașe, vulcan de cățărat, labirint interactiv, jocuri de echipă și o zonă dedicată părinților.</p>
        </div>
        <div class="gallery-strip gallery-strip--three" style="margin-top:var(--sp-6)">
%s
        </div>
        <p class="text-center" style="margin-top:var(--sp-6)"><a class="btn btn--outline" href="atractii.html">Vezi toate atracțiile %s</a></p>
      </div>
    </section>
""" % (icon("i-sparkle"), strip, icon("i-arrow")) if is_open else ""

    body = """
    <section class="section">
      <div class="container split">
        <div class="split__media reveal">
          <div class="collage">
            <span class="collage__sticker">%s</span>
            <div class="collage__main">
              %s
            </div>
          </div>
        </div>
        <div class="split__body reveal">
          <span class="eyebrow">%s %s</span>
          <h2>Despre această locație</h2>
          <p class="lead">%s</p>
          <p>%s</p>
          <dl class="hours" style="max-width:26rem">
%s
          </dl>
          <div class="hero__actions">
            <a class="btn btn--outline" href="%s" target="_blank" rel="noopener">%s Deschide în Maps</a>
            <a class="btn btn--primary" href="tel:%s">%s %s</a>
          </div>
        </div>
      </div>
    </section>
%s
%s
    <section class="section--tight">
      <div class="container">
        <div class="section-head reveal">
          <span class="eyebrow eyebrow--yellow">%s Petreceri</span>
          <h2>Aniversări la Happy &amp; Hop</h2>
          <p class="lead">Petrecere privată de la 1490 lei pentru 10 copii: 2,5 ore, decor tematic, pizza, invitație digitală și acces în locul de joacă pe toată durata evenimentului.</p>
        </div>
        <p class="text-center" style="margin-top:var(--sp-5)"><a class="btn btn--primary" href="petreceri.html">Vezi pachetele de petreceri %s</a></p>
      </div>
    </section>

    <section class="section--tight">
      <div class="container">
        <div class="section-head reveal">
          <span class="eyebrow">%s Celelalte locații</span>
          <h2>Mai suntem și aici</h2>
        </div>
        <div class="grid-cards grid-cards--two" style="margin-top:var(--sp-6)">
%s
        </div>
      </div>
    </section>
""" % (loc["status"], hero_media,
       icon("i-pin"), loc["sub"], loc["text"], loc["extra"], loc_hours(loc),
       maps_link(loc), icon("i-map"), C["TEL1"], icon("i-phone"), C["TEL1F"],
       map_section, attractions_section,
       icon("i-cake"), icon("i-arrow"),
       icon("i-map"), other_cards)

    return page_head(icon, "i-pin", "Locație", loc["title"], loc["lead"]) + body + cta_band(
        icon, C, "Te așteptăm la joacă",
        "Sună-ne pentru tarife, program sau rezervarea unei petreceri.")


# ============================================================ GALERIE
def page_galerie(icon, C):
    items = []
    for name, big, alt in GALLERY:
        full = "assets/img/%s-%s.jpg" % (name, big)
        portrait = big == "max"
        items.append("""        <button type="button" data-full="%s" data-caption="%s">
          %s
        </button>""" % (full, alt,
                        img_tag(name, ["400", "800"], "(min-width:1280px) 22vw, (min-width:768px) 30vw, 46vw",
                                alt)))

    return page_head(icon, "i-sparkle", "Galerie",
                     "Galerie foto",
                     "Trambuline, tobogane, piscine cu bile și petreceri — așa arată o zi la Happy &amp; Hop.") + """
    <section class="section">
      <div class="container">
        <div class="gallery" data-gallery>
%s
        </div>
        <p class="text-center" style="margin-top:var(--sp-6);color:var(--hh-muted)">Apasă pe o fotografie pentru a o vedea mare.</p>
      </div>
    </section>

    <div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="Galerie foto" hidden>
      <button class="lightbox__btn lightbox__close" type="button"><span class="sr-only">Închide</span>%s</button>
      <button class="lightbox__btn lightbox__prev" type="button"><span class="sr-only">Fotografia anterioară</span>%s</button>
      <img alt="">
      <button class="lightbox__btn lightbox__next" type="button"><span class="sr-only">Fotografia următoare</span>%s</button>
      <p class="lightbox__cap"></p>
    </div>
""" % ("\n".join(items), icon("i-close"), icon("i-chev-l"), icon("i-chev-r")) + cta_band(icon, C)


# ============================================================ CONTACT
def page_contact(icon, C):
    return page_head(icon, "i-phone", "Contact",
                     "Hai să vorbim",
                     "Pentru orice informații ne poți suna, ne poți scrie pe WhatsApp sau ne poți vizita la oricare dintre locații.") + """
    <section class="section" data-contact-zone>
      <div class="container split">
        <div class="split__body reveal">
          <h2>Trimite-ne un mesaj</h2>
          <p class="lead">Completează formularul și mesajul se deschide direct în WhatsApp, gata de trimis.</p>

          <form class="form needs-js" data-wa-form data-wa-url="%s" novalidate style="margin-top:var(--sp-5)">
            <div class="field">
              <label for="nume">Nume</label>
              <input id="nume" name="nume" type="text" autocomplete="name" required
                     aria-describedby="err-nume" data-eroare="Scrie-ne numele tău.">
              <p class="field__error" id="err-nume" role="alert" hidden></p>
            </div>
            <div class="field">
              <label for="subiect">Despre ce este vorba?</label>
              <select id="subiect" name="subiect">
                <option>Rezervare petrecere</option>
                <option>Tarife și abonamente</option>
                <option>Program și locații</option>
                <option>Altceva</option>
              </select>
            </div>
            <div class="field">
              <label for="mesaj">Mesaj</label>
              <textarea id="mesaj" name="mesaj" required aria-describedby="err-mesaj"
                        data-eroare="Scrie mesajul, ca să știm cu ce te putem ajuta."></textarea>
              <p class="field__error" id="err-mesaj" role="alert" hidden></p>
            </div>
            <div class="field field--check">
              <input id="acord" name="acord" type="checkbox" required aria-describedby="err-acord"
                     data-eroare="Bifează acordul cu politica de confidențialitate.">
              <label for="acord">Sunt de acord cu <a href="politica-confidentialitate.html">politica de confidențialitate</a>.</label>
              <p class="field__error" id="err-acord" role="alert" hidden></p>
            </div>
            <button class="btn btn--wa" type="submit">%s Trimite pe WhatsApp</button>
            <p class="form__hint">Mesajul se deschide în aplicația WhatsApp, de pe numărul tău. Nu stocăm nimic pe site.</p>
          </form>

          <div class="no-js-fallback note" style="margin-top:var(--sp-5)">
            %s
            <p>Formularul are nevoie de JavaScript, care este dezactivat în browserul tău.
               Scrie-ne direct pe <a href="%s" target="_blank" rel="noopener">WhatsApp</a>
               sau sună la <a href="tel:%s">%s</a>.</p>
          </div>
        </div>

        <div class="split__media reveal" style="display:grid;gap:var(--sp-4);align-content:start">
          <!-- DE CONFIRMAT: posterul de petreceri afișat în locație listează alte două numere,
               0332407300 și 0736165612. Până la confirmarea proprietarului, site-ul folosește
               numerele de pe pagina de contact a site-ului vechi (cele de mai jos). -->
          <div class="contact-tile">
            <div class="contact-tile__icon i-blue">%s</div>
            <div>
              <h3 style="font-size:1.05rem">Telefon</h3>
              <p><a href="tel:%s">%s</a><br><a href="tel:%s">%s</a></p>
            </div>
          </div>

          <div class="contact-tile">
            <div class="contact-tile__icon i-green">%s</div>
            <div>
              <h3 style="font-size:1.05rem">WhatsApp</h3>
              <p><a href="%s" target="_blank" rel="noopener">Scrie-ne direct</a></p>
            </div>
          </div>

          <div class="contact-tile">
            <div class="contact-tile__icon i-pink">%s</div>
            <div>
              <h3 style="font-size:1.05rem">Bd. Socola 27A, Iași</h3>
              <p style="color:var(--hh-muted)">Rodotex, lângă magazinul Jumbo<br>Luni 13:00–20:00 · Marți–Duminică 10:00–20:00</p>
            </div>
          </div>

          <div class="contact-tile">
            <div class="contact-tile__icon i-yellow">%s</div>
            <div>
              <h3 style="font-size:1.05rem">Moldova Mall, Iași</h3>
              <p style="color:var(--hh-muted)">Șos. Păcurari 121, vizavi de intrarea în Carrefour<br>Luni–Duminică 10:00–22:00</p>
            </div>
          </div>

          <div class="contact-tile">
            <div class="contact-tile__icon i-sky">%s</div>
            <div>
              <h3 style="font-size:1.05rem">Family Market Miroslava</h3>
              <p style="color:var(--hh-muted)">În curând<br>Program anunțat: Luni–Duminică 09:00–21:00</p>
            </div>
          </div>
        </div>
      </div>
    </section>
""" % (C["WA_GEN"], icon("i-wa"),
       icon("i-info"), C["WA_GEN"], C["TEL1"], C["TEL1F"],
       icon("i-phone"), C["TEL1"], C["TEL1F"], C["TEL2"], C["TEL2F"],
       icon("i-wa"), C["WA_GEN"],
       icon("i-pin"), icon("i-pin"), icon("i-clock"))


# ============================================================ POLITICĂ
def page_politica(icon, C):
    return page_head(icon, "i-shield", "Legal",
                     "Politica de confidențialitate și cookies",
                     "Cum tratăm datele tale atunci când ne contactezi sau vizitezi acest site.") + """
    <section class="section">
      <div class="container">
        <div class="prose">
          <h2>Cine suntem</h2>
          <p>Acest site prezintă locurile de joacă pentru copii Happy &amp; Hop din Iași și serviciile de organizare a petrecerilor aniversare. Ne poți contacta telefonic la <a href="tel:%s">%s</a> sau <a href="tel:%s">%s</a>.</p>

          <h2>Ce date colectăm</h2>
          <p>Site-ul este static și nu stochează date pe server. Nu folosim conturi, coșuri de cumpărături sau formulare care salvează informații.</p>
          <ul>
            <li><strong>Formularul de contact</strong> — datele introduse (nume, subiect, mesaj) nu sunt trimise către acest site. Ele sunt folosite doar pentru a compune un mesaj pe care îl trimiți tu, din aplicația WhatsApp instalată pe dispozitivul tău.</li>
            <li><strong>Apeluri telefonice și mesaje WhatsApp</strong> — atunci când ne contactezi, primim numărul tău de telefon și conținutul mesajului, pe care le folosim exclusiv pentru a-ți răspunde și, dacă e cazul, pentru a organiza rezervarea.</li>
          </ul>

          <h2>Cookies</h2>
          <p>Site-ul nu instalează cookies proprii și nu folosește instrumente de analiză a traficului. Singura excepție este harta Google de pe paginile locațiilor, care poate seta cookies Google în momentul în care se încarcă. Fonturile sunt încărcate de la Google Fonts, ceea ce presupune o cerere către serverele Google, care poate înregistra adresa IP a vizitatorului, conform politicii proprii de confidențialitate.</p>

          <h2>Servicii externe</h2>
          <ul>
            <li><strong>WhatsApp</strong> (Meta) — pentru conversațiile inițiate de tine prin butoanele de pe site.</li>
            <li><strong>Google Maps</strong> — harta de pe paginile locațiilor este încărcată direct de la Google, printr-un cadru integrat. Când ajungi cu derularea la ea, browserul tău face o cerere către serverele Google, care poate înregistra adresa IP și poate seta cookies proprii, conform politicii Google. Același lucru se întâmplă când apeși pe „Deschide în Google Maps”.</li>
            <li><strong>Facebook</strong> (Meta) — doar ca link către pagina noastră. Nu avem pixel de urmărire și niciun conținut Facebook încărcat în site.</li>
            <li><strong>Google Fonts</strong> — pentru fonturile afișate în pagină.</li>
          </ul>

          <h2>Cât păstrăm datele</h2>
          <p>Conversațiile purtate telefonic sau pe WhatsApp sunt păstrate atât timp cât sunt necesare pentru rezolvarea solicitării tale și pentru evidența rezervărilor.</p>

          <h2>Drepturile tale</h2>
          <p>Conform Regulamentului (UE) 2016/679 (GDPR), ai dreptul de acces la date, de rectificare, de ștergere, de restricționare a prelucrării, de opoziție și de portabilitate. Îți poți exercita aceste drepturi contactându-ne telefonic, la numerele de mai sus.</p>

          <h2>Copiii</h2>
          <p>Nu colectăm intenționat date despre copii. Rezervările și comunicarea se fac exclusiv cu părinții sau reprezentanții legali.</p>

          <h2>Modificări</h2>
          <p>Această politică poate fi actualizată. Versiunea afișată pe această pagină este cea în vigoare.</p>
        </div>
      </div>
    </section>
""" % (C["TEL1"], C["TEL1F"], C["TEL2"], C["TEL2F"])


# ============================================================ 404
def page_404(icon, C):
    return """
    <section class="section" style="padding-top:var(--sp-8)">
      <div class="container text-center">
        <span class="eyebrow eyebrow--pink">%s Ups!</span>
        <h1 style="margin-top:var(--sp-4);font-size:var(--fs-hero)">Pagina asta s-a dus la joacă</h1>
        <p class="lead measure mx-auto" style="margin-top:var(--sp-4)">Nu găsim pagina pe care o cauți. Hai înapoi la distracție.</p>
        <div class="cta-band__actions" style="margin-top:var(--sp-6)">
          <a class="btn btn--primary" href="index.html">%s Înapoi acasă</a>
          <a class="btn btn--outline" href="petreceri.html">Vezi petrecerile</a>
        </div>
      </div>
    </section>
""" % (icon("i-balloon"), icon("i-chev-l"))


# ============================================================ JSON-LD
import json as _json


def _ld(*nodes):
    """Un singur <script> cu @graph — noduri legate prin @id, nu duplicate."""
    data = {"@context": "https://schema.org", "@graph": [n for n in nodes if n]}
    return '<script type="application/ld+json">%s</script>' % _json.dumps(data, ensure_ascii=False)


def _org(C):
    node = {
        "@type": "Organization",
        "@id": C["SITE"] + "/#organizatie",
        "name": "Happy & Hop",
        "url": C["SITE"] + "/",
        "logo": {"@type": "ImageObject", "url": C["SITE"] + "/assets/brand/logo.png",
                 "width": 225, "height": 225},
        "image": C["SITE"] + "/assets/brand/og-image.jpg",
        "telephone": ["+4" + C["TEL1"], "+4" + C["TEL2"]],
        "areaServed": {"@type": "City", "name": "Iași"},
    }
    if C.get("SOCIAL"):
        node["sameAs"] = list(C["SOCIAL"])
    return node


def _website(C):
    return {
        "@type": "WebSite",
        "@id": C["SITE"] + "/#site",
        "url": C["SITE"] + "/",
        "name": "Happy & Hop",
        "inLanguage": "ro-RO",
        "publisher": {"@id": C["SITE"] + "/#organizatie"},
    }


def _place(loc, C):
    """Un loc de joacă. Miroslava n-are program publicat cât timp nu e deschisă."""
    node = {
        "@type": "AmusementPark",
        "@id": "%s/%s#loc" % (C["SITE"], loc["page"]),
        "name": "Happy & Hop — " + loc["short"],
        "url": "%s/%s" % (C["SITE"], loc["page"]),
        "telephone": "+4" + C["TEL1"],
        "priceRange": "$$",
        "currenciesAccepted": "RON",
        "parentOrganization": {"@id": C["SITE"] + "/#organizatie"},
        "address": {
            "@type": "PostalAddress",
            "streetAddress": loc["street"],
            "addressLocality": loc["locality"],
            "addressRegion": "Iași",
            "addressCountry": "RO",
        },
        "hasMap": maps_link(loc).replace("&amp;", "&"),
    }
    if loc["img"]:
        node["image"] = "%s/assets/img/%s-800.jpg" % (C["SITE"], loc["img"])
    if loc["geo"]:
        node["geo"] = {"@type": "GeoCoordinates",
                       "latitude": loc["geo"][0], "longitude": loc["geo"][1]}
    if loc["schema_hours"]:
        node["openingHoursSpecification"] = [
            {"@type": "OpeningHoursSpecification", "dayOfWeek": days,
             "opens": opens, "closes": closes}
            for days, opens, closes in loc["schema_hours"]]
    else:
        node["description"] = "Deschidere în curând."
    return node


def _breadcrumbs(C, trail):
    """trail = [(nume, slug_sau_None)] — ultimul element e pagina curentă."""
    return {
        "@type": "BreadcrumbList",
        "itemListElement": [
            dict({"@type": "ListItem", "position": i + 1, "name": name},
                 **({"item": "%s/%s" % (C["SITE"], slug)} if slug is not None else {}))
            for i, (name, slug) in enumerate(trail)],
    }


def _party_service(C):
    """Pachetele de petreceri, ca serviciu cu două oferte — prețurile devin citibile
    pentru Google, nu doar text în pagină."""
    def offer(name, price, desc):
        return {"@type": "Offer", "name": name, "price": price, "priceCurrency": "RON",
                "description": desc, "availability": "https://schema.org/InStock",
                "url": C["SITE"] + "/petreceri.html#preturi"}
    return {
        "@type": "Service",
        "@id": C["SITE"] + "/petreceri.html#serviciu",
        "name": "Petrecere privată pentru copii",
        "serviceType": "Organizare petreceri aniversare pentru copii",
        "provider": {"@id": C["SITE"] + "/#organizatie"},
        "areaServed": {"@type": "City", "name": "Iași"},
        "url": C["SITE"] + "/petreceri.html",
        "offers": [
            offer("Varianta 1 — 10 copii", "1490",
                  "2,5 ore, acces în locul de joacă, apă și suc pentru fiecare copil, pizza, invitație digitală, lumânare tort, balon cifră cu heliu."),
            offer("Varianta 2 — 10 copii și 10 părinți", "1990",
                  "2,5 ore, acces în locul de joacă, apă și suc pentru fiecare copil, pizza pentru copii și părinți, cafea și apă pentru părinți, invitație digitală, lumânare tort, balon cifră cu heliu."),
        ],
    }


def _faq():
    qa = [
        ("Cât durează o petrecere la Happy & Hop?", "Ambele variante includ 2,5 ore de petrecere, cu acces în locul de joacă pe toată durata evenimentului."),
        ("Cât costă o petrecere?", "Varianta 1 costă 1490 lei pentru 10 copii, iar Varianta 2 costă 1990 lei pentru 10 copii și 10 părinți."),
        ("Pot aduce tortul de acasă?", "Da. Tortul nu este inclus în pachet și se aduce din exterior, însoțit de certificat de conformitate."),
        ("Ce include meniul copiilor?", "Pizza, o apă și un suc pentru fiecare copil. La Varianta 2 se adaugă pizza, cafea și apă pentru părinți."),
        ("Unde se organizează petrecerile?", "Petrecerile private se organizează la locația din Bulevardul Socola 27A, lângă magazinul Jumbo. Pentru Moldova Mall, întreabă-ne de disponibilitate."),
    ]
    return {"@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qa]}


# ============================================================ RUN
def run(build, icon, C):
    crumbs = lambda *trail: _breadcrumbs(C, list(trail))

    build("index.html",
          "Loc de joacă pentru copii în Iași — trambuline și petreceri | Happy & Hop",
          "Loc de joacă pentru copii în Iași: 700 m² de trambuline, tobogane uriașe, piscine cu bile și vulcan de escaladat. Trei locații și petreceri aniversare complete.",
          page_index(icon, C),
          extra_head=_ld(_org(C), _website(C), *[_place(l, C) for l in LOCATIONS]))

    build("atractii.html",
          "Atracții — trambuline, tobogane și piscină cu bile | Happy & Hop Iași",
          "Cele șapte zone de joacă Happy & Hop: piscină cu bile, parc de trambuline, tobogane uriașe, vulcan de cățărat, labirint interactiv, jocuri de echipă și zonă pentru părinți.",
          page_atractii(icon, C),
          extra_head=_ld(crumbs(("Acasă", ""), ("Atracții", "atractii.html"))))

    build("petreceri.html",
          "Petreceri pentru copii în Iași — pachete și prețuri | Happy & Hop",
          "Petrecere privată de la 1490 lei pentru 10 copii: 2,5 ore, decor, pizza, invitație digitală și acces la locul de joacă. Rezervă pe WhatsApp.",
          page_petreceri(icon, C),
          extra_head=_ld(_party_service(C), _faq(),
                         crumbs(("Acasă", ""), ("Petreceri", "petreceri.html"))))

    build("locatii.html",
          "Locații Happy & Hop în Iași — Socola, Moldova Mall, Miroslava",
          "Program și adrese: Bd. Socola 27A (lângă Jumbo), Moldova Mall (Șos. Păcurari 121) și Family Market Miroslava — în curând.",
          page_locatii(icon, C),
          extra_head=_ld(*([_place(l, C) for l in LOCATIONS]
                           + [crumbs(("Acasă", ""), ("Locații", "locatii.html"))])))

    for loc in LOCATIONS:
        build(loc["page"], loc["seo_title"], loc["seo_desc"],
              page_locatie(loc, icon, C),
              extra_head=_ld(_place(loc, C),
                             crumbs(("Acasă", ""), ("Locații", "locatii.html"),
                                    (loc["short"], loc["page"]))))

    build("galerie.html",
          "Galerie foto — locurile de joacă Happy & Hop din Iași",
          "Fotografii din locurile de joacă Happy & Hop: trambuline, foam pit, piscine cu bile, tobogane și săli de petreceri.",
          page_galerie(icon, C),
          extra_head=_ld(crumbs(("Acasă", ""), ("Galerie", "galerie.html"))))

    build("contact.html",
          "Contact Happy & Hop Iași — telefon, WhatsApp, program",
          "Sună la 0726 347 494 sau 0740 750 993, scrie-ne pe WhatsApp ori vino la una dintre cele trei locații Happy & Hop din Iași.",
          page_contact(icon, C),
          extra_head=_ld(_org(C), crumbs(("Acasă", ""), ("Contact", "contact.html"))))

    build("politica-confidentialitate.html",
          "Politica de confidențialitate și cookies | Happy & Hop",
          "Cum tratăm datele personale și ce servicii externe folosește site-ul happyhop.ro.",
          page_politica(icon, C))

    build("404.html",
          "Pagina nu a fost găsită | Happy & Hop",
          "Pagina căutată nu există. Întoarce-te la Happy & Hop.",
          page_404(icon, C), indexable=False)
