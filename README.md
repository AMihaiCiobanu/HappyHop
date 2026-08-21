# Happy & Hop — site static

Site vitrină pentru locurile de joacă Happy & Hop din Iași. HTML + CSS + JavaScript simplu,
fără framework, fără build step obligatoriu, fără dependențe instalate. Se poate publica pe
orice găzduire care servește fișiere (Netlify, Vercel, cPanel, hosting-ul actual).

## Structura

```
index.html                     Acasă
atractii.html                  Cele 7 zone de joacă + reguli
petreceri.html                 Pachete, prețuri (1490 / 1990 lei), extraopțiuni, FAQ
locatii.html                   Hub-ul locațiilor, cu link către fiecare pagină
loc-de-joaca-socola.html       Pagină proprie: Bd. Socola 27A
loc-de-joaca-moldova-mall.html Pagină proprie: Moldova Mall
loc-de-joaca-miroslava.html    Pagină proprie: Family Market Miroslava (în curând)
galerie.html                   Galerie foto cu lightbox
contact.html                   Telefoane, formular care compune mesaj WhatsApp
politica-confidentialitate.html
404.html
css/base.css                   reset, culori, tipografie, butoane
css/site.css                   componente, secțiuni, responsive
js/site.js                     meniu mobil, lightbox, animații, formular WhatsApp
assets/img/                    fotografii optimizate (400 / 800 / 1600 px)
assets/brand/                  logo, favicon, imagine Open Graph
_source-photos/                fotografiile originale — NU se urcă pe server
_tools/                        generator opțional de pagini — NU se urcă pe server
deploy.sh                      construiește dist/ cu exact fișierele publice
robots.txt, sitemap.xml
```

## Rulare locală

```bash
python3 -m http.server 5173
```

Apoi deschide http://localhost:5173.

## Publicare

```bash
./deploy.sh
```

Creează `dist/` cu paginile, `css/`, `js/` și `assets/` — fără `_source-photos/` (2,6 MB de
originale) și fără `_tools/`. Urci conținutul lui `dist/`, nu rădăcina proiectului.

## Cum modifici conținutul

Paginile sunt HTML obișnuit — deschizi fișierul și editezi textul. Locuri utile:

- **Prețurile petrecerilor** — `petreceri.html`, secțiunea `id="preturi"`.
- **Programul locațiilor** — `locatii.html` (listele `<dl class="hours">`) și `contact.html`.
- **Telefoanele** — apar în header, footer, bara de jos și pe pagina de contact.
  Caută `0726347494` și `0740750993`. Numărul de WhatsApp apare ca `40726347494`
  (prefix internațional, fără `+`). `js/site.js` nu conține numere: formularul citește
  linkul din atributul `data-wa-url` al formularului, deci e suficient să schimbi HTML-ul.
- **Culorile brandului** — `css/base.css`, blocul `:root` (`--hh-blue`, `--hh-pink`, …).

### Generatorul opțional (`_tools/`)

Header-ul, footer-ul și setul de iconuri sunt identice în toate paginile. Ca să nu le modifici
manual în 8 fișiere, poți folosi generatorul:

```bash
cd _tools && python3 gen.py
```

**Atenție:** comanda rescrie complet toate fișierele `.html` din rădăcină. Dacă ai editat direct
HTML-ul, modificările se pierd. Fie lucrezi doar în `_tools/pages.py` și regenerezi, fie ștergi
folderul `_tools/` și editezi HTML-ul direct. Generatorul nu este necesar pentru publicare.

## Imagini

Fotografiile originale stau în `_source-photos/`. Variantele servite în pagini sunt generate cu
`sips` (inclus în macOS):

```bash
for f in _source-photos/*.jpg; do b=$(basename "$f" .jpg); ow=$(sips -g pixelWidth "$f" | awk '/pixelWidth/{print $2}'); for w in 400 800 1600; do [ "$w" -le "$ow" ] && sips --resampleWidth $w -s format jpeg -s formatOptions 45 "$f" --out "assets/img/${b}-${w}.jpg"; done; [ "$ow" -lt 1600 ] && sips -s format jpeg -s formatOptions 45 "$f" --out "assets/img/${b}-max.jpg"; done
```

Sufixul `-max` înseamnă „lățimea originală”, folosit la pozele verticale mai înguste de 1600 px.

Dacă înlocuiești o poză cu una de altă dimensiune, actualizează și `IMG_DIMS` din
`_tools/pages.py` — de acolo se calculează `width`/`height` și descriptorii `srcset`, ca
raportul de aspect declarat în HTML să fie mereu cel real.

WebP ar reduce încă ~30% din greutate, dar `sips` nu scrie WebP. Dacă vrei:

```bash
brew install webp
for f in assets/img/*.jpg; do cwebp -q 78 "$f" -o "${f%.jpg}.webp"; done
```

apoi adaugi `<source type="image/webp" srcset="...">` în jurul fiecărui `<img>`.

## SEO — stadiu

Completate: coordonatele exacte ale celor trei locații (`geo` în `LOCATIONS`, `_tools/pages.py`),
linkul real de Google Maps al fiecărui loc (`place_url`) și pagina de Facebook
(`SOCIAL` în `_tools/gen.py` — apare în footer și ca `sameAs`).

Mai poate fi adăugat: **Instagram**, în lista `SOCIAL` din `_tools/gen.py`.

Harta de pe paginile de locație se construiește automat din `geo`; butoanele „Deschide în Google
Maps" folosesc `place_url`, cu rezervă pe căutare după adresă dacă lipsește. După orice
modificare: `cd _tools && python3 gen.py`.

Ce este deja publicat ca date structurate: `Organization` + `WebSite` (homepage),
`AmusementPark` pentru fiecare din cele 3 locații (cu adresă, telefon, program, hartă),
`Service` cu cele două oferte de petreceri (1490 / 1990 lei), `FAQPage` și `BreadcrumbList`
pe fiecare subpagină.

**Restul depinde de lucruri din afara site-ului**, în ordinea impactului: profil Google
Business revendicat pentru fiecare locație, recenzii Google, linkuri de pe paginile Moldova
Mall și Family Market, verificarea proprietății în Google Search Console și trimiterea
`sitemap.xml`.

## Ce trebuie confirmat cu clientul

Aceste date au apărut contradictoriu pe site-ul vechi. Site-ul nou folosește varianta notată
mai jos; corectează dacă e cazul.

1. **Telefoane.** Site-ul folosește `0726 347 494` și `0740 750 993` (de pe pagina veche de
   contact). Posterul de petreceri din locație afișează alte numere: `0332407300` și
   `0736165612`. Vezi comentariul din `contact.html`.
2. **A doua locație.** Pagina veche „Locații” anunța *Family Market Miroslava*, iar pagina de
   contact lista *Strada Muntenimii 7 – Hotel Ildis*. Site-ul nou publică doar Miroslava, marcată
   „În curând”. Dacă locația din Muntenimii funcționează, trebuie adăugată în `locatii.html`,
   `contact.html`, footer și `_tools/pages.py`.
3. **Prețuri de intrare.** Nu există nicăieri tarife pentru Acces individual / Pachet family /
   Abonament lunar, așa că paginile trimit la telefon. Când primești cifrele, se completează în
   secțiunea „Pachete de joacă” din `index.html`.
4. **Moldova Mall.** Pagina veche de contact spunea „deschidere în 15 mai”; locația apare
   funcțională în pozele din octombrie 2025, deci este prezentată ca deschisă.

## Note tehnice

- Formularul de contact nu trimite date nicăieri: compune un mesaj și îl deschide în WhatsApp,
  de pe telefonul vizitatorului. Site-ul vechi nu publica nicio adresă de email, așa că nu s-a
  inventat una. Fără JavaScript formularul este ascuns și în locul lui apare un bloc cu linkul
  de WhatsApp și numărul de telefon, ca să nu existe un buton care pare că trimite, dar nu trimite.
- Fără cookies, fără analytics. Singura resursă externă este Google Fonts.
- Tot conținutul este vizibil și fără JavaScript; JS adaugă doar meniul mobil, lightbox-ul,
  animațiile la scroll și formularul WhatsApp.
- Fiecare pagină primește doar iconurile SVG pe care le folosește (generatorul le selectează
  automat din `_tools/sprite.html`).
- CSS-ul și JS-ul sunt linkate cu o amprentă a conținutului (`site.css?v=f442f409`), recalculată
  la fiecare `gen.py`. Fără ea, browserele și hostingul continuă să servească versiunea veche
  după un update.
- Formularul de contact își face singur validarea, cu mesaje în română. Bulele native ale
  browserului sunt dezactivate (`novalidate`), pentru că textul lor vine din limba interfeței
  browserului, nu din `lang="ro"`. Mesajele se editează în atributele `data-eroare` din
  `_tools/pages.py`.
- Date structurate JSON-LD: `AmusementPark` (2 locații deschise) pe `index.html`, `FAQPage` pe
  `petreceri.html`.
- Înainte de publicare pe domeniul real, verifică `sitemap.xml` și `robots.txt` (conțin
  `https://happyhop.ro`) și `<link rel="canonical">` din fiecare pagină.
