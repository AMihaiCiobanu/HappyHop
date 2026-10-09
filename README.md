# Happy & Hop — site static

Site vitrină pentru locurile de joacă Happy & Hop din Iași: 11 pagini HTML + CSS + JavaScript
simplu, fără framework și fără dependențe de instalat. Publicat pe GitHub Pages direct din
branch-ul `main`: https://amihaiciobanu.github.io/HappyHop/

## Structura

```
index.html                     Acasă
atractii.html                  Cele 7 zone de joacă, siguranță, reguli de acces
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
css/site.css                   componente, secțiuni, hartă, responsive
js/site.js                     meniu mobil, lightbox, animații, validare formular, WhatsApp
assets/img/                    fotografii optimizate (400 / 800 / 1600 px), fiecare în AVIF + JPG
assets/brand/                  logo, favicon, apple-touch-icon, imagine Open Graph
robots.txt, sitemap.xml

_tools/                        generatorul paginilor — nu se publică
_source-photos/                fotografiile originale — nu se publică
deploy.sh                      construiește dist/ pentru o găzduire clasică (nu e folosit de Pages)
dist/                          rezultatul lui deploy.sh (ignorat de git)
```

## Rulare locală

```bash
python3 -m http.server 5173
```

Apoi deschide http://localhost:5173.

## Publicare

Site-ul e pe **GitHub Pages**, cu sursa `main` / rădăcina repo-ului
(repo `AMihaiCiobanu/HappyHop`, Settings → Pages). **Orice push pe `main` ajunge live** în
aproximativ un minut, la https://amihaiciobanu.github.io/HappyHop/. Nu e nevoie de `dist/`.

- Pages publică rădăcina prin Jekyll, care ignoră folderele ce încep cu `_`: de aceea
  `_tools/` și `_source-photos/` nu ajung pe site. **Nu adăuga un fișier `.nojekyll`** — le-ar
  publica pe amândouă.
- Toate linkurile din pagini sunt relative (`css/site.css`, `assets/img/…`), așa că site-ul
  merge la fel sub `/HappyHop/` și, mai târziu, la rădăcina domeniului.
- Starea ultimului build: `gh api repos/AMihaiCiobanu/HappyHop/pages/builds/latest`.

### Domeniul happyhop.ro

`happyhop.ro` arată încă site-ul vechi (hosting-ul actual, `138.199.246.140`). Ca să treacă pe Pages:

1. În Settings → Pages → Custom domain scrie `happyhop.ro`. GitHub face un commit cu fișierul
   `CNAME` pe `main` — rulează `git pull` după aceea.
2. La registrarul domeniului: patru înregistrări `A` pentru `happyhop.ro` către
   `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`, și `www` ca
   `CNAME` către `amihaiciobanu.github.io`.
3. După ce DNS-ul s-a propagat, bifează **Enforce HTTPS**.

`canonical`, `sitemap.xml` și `robots.txt` folosesc deja `https://happyhop.ro`, deci copia de
pe `github.io` nu concurează în Google cu domeniul real.

### Altă găzduire (opțional)

```bash
./deploy.sh
```

Creează `dist/` (~5,3 MB) cu paginile, `css/`, `js/` și `assets/` — fără `_source-photos/` și
fără `_tools/`. Pe o găzduire clasică (cPanel, FTP) se urcă conținutul lui `dist/`, nu
rădăcina proiectului.

## Cum modifici conținutul

Textele, structura paginilor și meniul stau în **`_tools/pages.py`** și **`_tools/gen.py`**.
După orice modificare:

```bash
cd _tools && python3 gen.py
```

Comanda rescrie complet fișierele `.html` din rădăcină. Poți edita și direct HTML-ul (e HTML
obișnuit, fără șabloane), dar modificările se pierd la următoarea rulare a generatorului — și
nu se propagă în celelalte 10 pagini, pentru că header-ul, footer-ul și iconurile sunt scrise
identic în fiecare fișier.

Locuri utile:

| Ce schimbi | Unde |
|---|---|
| Locații: nume, adresă, program, coordonate, link Maps | `LOCATIONS` din `_tools/pages.py` |
| Prețurile petrecerilor | `page_petreceri()` din `_tools/pages.py` (și `_party_service()` pentru datele structurate) |
| Telefoane, WhatsApp, Facebook | constantele din capul lui `_tools/gen.py` (`TEL1`, `TEL2`, `WA`, `FACEBOOK`, `SOCIAL`) |
| Mesajele de eroare ale formularului | atributele `data-eroare` din `page_contact()` |
| Culorile brandului | `css/base.css`, blocul `:root` (`--hh-blue`, `--hh-pink`, …) |
| Iconuri SVG | `_tools/sprite.html` |

Programul unei locații se scrie **o singură dată**, în `LOCATIONS`, și apare peste tot: hero-ul
de pe prima pagină, cardurile, hub-ul, pagina locației și JSON-LD-ul.

> **Atenție dacă editezi CSS/JS de mână:** paginile linkează fișierele cu o amprentă a
> conținutului (`css/site.css?v=f442f409`), calculată la rularea generatorului. Dacă modifici
> un fișier CSS sau JS fără să rulezi apoi `gen.py`, browserele vor continua să servească
> versiunea veche din cache.

## Imagini

Fotografiile originale stau în `_source-photos/`. Variantele servite în pagini se generează cu
`sips` (inclus în macOS):

```bash
for f in _source-photos/*.jpg; do b=$(basename "$f" .jpg); ow=$(sips -g pixelWidth "$f" | awk '/pixelWidth/{print $2}'); for w in 400 800 1600; do [ "$w" -le "$ow" ] && sips --resampleWidth $w -s format jpeg -s formatOptions 45 "$f" --out "assets/img/${b}-${w}.jpg"; done; [ "$ow" -lt 1600 ] && sips -s format jpeg -s formatOptions 45 "$f" --out "assets/img/${b}-max.jpg"; done
```

Sufixul `-max` înseamnă „lățimea originală", folosit la pozele verticale mai înguste de 1600 px.

Fiecare variantă JPG are și o pereche **AVIF** (~45% mai ușoară la aceeași calitate). Paginile le
servesc printr-un `<picture>` (generat de `img_tag()` din `_tools/pages.py`): browserele care știu
AVIF îl iau pe acela, celelalte rămân pe JPG. După ce adaugi sau înlocuiești o poză, refă și AVIF-urile:

```bash
for f in assets/img/*.jpg; do b=$(basename "$f" .jpg); n=${b%-*}; w=${b##*-}; src=_source-photos/$n.jpg; if [ "$w" = max ]; then sips -s format avif -s formatOptions 50 "$src" --out "assets/img/$b.avif"; else sips -s format avif -s formatOptions 50 --resampleWidth $w "$src" --out "assets/img/$b.avif"; fi; done
```

Dacă înlocuiești o poză cu una de altă dimensiune, actualizează și `IMG_DIMS` din
`_tools/pages.py` — de acolo se calculează `width`/`height` și descriptorii `srcset`, ca
raportul de aspect declarat în HTML să fie mereu cel real (altfel pagina „sare" la încărcare).

Logo-ul din header și footer este `assets/brand/logo-104.png` (104 px, de 2× mărimea afișată);
`logo.png` (225 px) rămâne pentru datele structurate.

## SEO — stadiu

Date structurate publicate (JSON-LD, câte un `@graph` per pagină):

- `Organization` + `WebSite` pe prima pagină, cu logo, telefoane și `sameAs` către Facebook
- `AmusementPark` pentru fiecare din cele 3 locații — adresă, telefon, program, coordonate
  `geo`, `hasMap`; Miroslava apare fără program, cu „Deschidere în curând"
- `Service` cu cele două oferte de petreceri (1490 / 1990 lei, în RON) pe `petreceri.html`
- `FAQPage` pe `petreceri.html` și `BreadcrumbList` pe fiecare subpagină

Completate: coordonatele exacte ale celor 3 locații, linkul de Google Maps al fiecărui loc,
pagina de Facebook, titluri și descrieri unice pe fiecare pagină, canonical fără `index.html`,
`noindex` pe 404, sitemap cu 10 URL-uri.

Mai poate fi adăugat: **Instagram**, în lista `SOCIAL` din `_tools/gen.py`.

**Restul depinde de lucruri din afara site-ului**, în ordinea impactului: profil Google Business
revendicat pentru fiecare locație, recenzii Google, linkuri de pe paginile Moldova Mall și
Family Market, verificarea proprietății în Google Search Console și trimiterea `sitemap.xml`.

## Ce trebuie confirmat cu clientul

Aceste date au apărut contradictoriu pe site-ul vechi. Site-ul nou folosește varianta notată
mai jos; corectează dacă e cazul.

1. **Telefoane.** Site-ul folosește `0726 347 494` și `0740 750 993` (de pe pagina veche de
   contact). Posterul de petreceri din locație afișează alte numere: `0332407300` și
   `0736165612`. Vezi comentariul din `contact.html`.
2. **A doua locație.** Pagina veche „Locații" anunța *Family Market Miroslava*, iar pagina de
   contact lista *Strada Muntenimii 7 – Hotel Ildis*. Site-ul nou publică doar Miroslava, marcată
   „În curând". Dacă locația din Muntenimii funcționează, trebuie adăugată în `LOCATIONS`.
3. **Prețuri de intrare.** Nu există nicăieri tarife pentru Acces individual / Pachet family /
   Abonament lunar, așa că paginile trimit la telefon. Când primești cifrele, se completează în
   secțiunea „Pachete de joacă" din `page_index()`.
4. **Moldova Mall.** Pagina veche de contact spunea „deschidere în 15 mai"; locația apare
   funcțională în pozele din octombrie 2025, deci este prezentată ca deschisă.

## Note tehnice

- **Fără cookies proprii și fără analytics.** Resurse externe: Google Fonts (fonturile),
  Google Maps (harta integrată pe paginile de locație, se încarcă la derulare și poate seta
  cookies Google) și linkuri simple, care nu încarcă nimic în pagină: `wa.me`, Facebook,
  Google Maps și semnătura „Made by SoftApps" din footer. Serviciile care chiar încarcă ceva
  sunt descrise în `politica-confidentialitate.html`.
- **Formularul de contact nu trimite date nicăieri**: compune un mesaj și îl deschide în
  WhatsApp, de pe telefonul vizitatorului. Site-ul vechi nu publica nicio adresă de email, așa
  că nu s-a inventat una.
- **Fără JavaScript** formularul este ascuns, iar în locul lui apare un bloc cu linkul de
  WhatsApp și numărul de telefon — ca să nu existe un buton care pare că trimite, dar nu trimite.
  Restul conținutului (texte, meniu, poze, program) rămâne vizibil.
- **Validarea formularului** e făcută de site, cu mesaje în română. Bulele native ale
  browserului sunt dezactivate (`novalidate`), pentru că textul lor vine din limba interfeței
  browserului, nu din `lang="ro"`.
- **Iconuri**: fiecare pagină primește doar simbolurile SVG pe care le folosește, selectate
  automat de generator din `_tools/sprite.html`.
- **Accesibilitate**: contrast verificat AA, meniul mobil și lightbox-ul sunt dialoguri modale
  (`aria-modal`, fundal `inert`, focus trap, Escape), toate imaginile au `alt` în română,
  animațiile se opresc la `prefers-reduced-motion`.
- Înainte de publicare pe domeniul real, verifică `sitemap.xml`, `robots.txt` și
  `<link rel="canonical">` — toate conțin `https://happyhop.ro`.
