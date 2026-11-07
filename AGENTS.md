# AGENTS.md — uzbtrust dizayn tizimi

Siz (AI agent) bu faylni foydalanuvchi «github.com/uzbtrust/design-system dan foydalan», «uzbtrust uslubida yasa» yoki «dizayn tizimimni ishlat» deganda o‘qiysiz. Vazifa — so‘ralgan narsani (sayt, ilova, test sahifa, PDF, slayd, rasm) shu tizimning rangi, shrifti, komponentlari va resurslari bilan yasash. O‘zingizdan rang, shrift yoki uslub o‘ylab topmang.

## O‘qish tartibi

1. `docs/brand.md` — brend kitobi: tamoyillar, rang, tipografiya, muhitga qarab qoidalar. **Doim birinchi.**
2. Muhitga qarab: sayt — `docs/04-sayt.md`; matn va til — `docs/01-ovoz.md`; animatsiya — `docs/02-harakat.md`.
3. Ishlatadigan har bir komponentning `components/<Nom>/README.md` fayli (tuzilma va qoidalar) va `example.html` (tayyor namuna).
4. Oxirida `docs/03-tekshiruv.md` bo‘yicha tekshiring.

Repo klonlanmagan bo‘lsa, fayllarni shu manzildan oling:
`https://raw.githubusercontent.com/uzbtrust/design-system/main/<yo‘l>`

## Ulash (veb)

Bitta CSS fayl — tokenlar va barcha komponentlar:

```html
<!doctype html>
<html lang="uz">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#ffffff" media="(prefers-color-scheme: light)">
  <meta name="theme-color" content="#000000" media="(prefers-color-scheme: dark)">
  <link rel="icon" href="https://cdn.jsdelivr.net/gh/uzbtrust/design-system@v1/assets/Logos/uzbtrust-logo.png" type="image/png">
  <link rel="icon" href="https://cdn.jsdelivr.net/gh/uzbtrust/design-system@v1/assets/Logos/uzbtrust-logo.svg" type="image/svg+xml">
  <script>document.documentElement.dataset.theme = matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";</script>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/uzbtrust/design-system@v1/dist/uzbtrust.css">
</head>
<body>
  …
  <!-- Footer bo‘lsa, imzo uning ichida; bo‘lmasa shu qator: -->
  <div class="signature-row"><a class="signature" href="https://github.com/uzbtrust/design-system"><span class="uzbtrust-mark" aria-hidden="true"></span>Dizayn: <strong>Abdurakhmonov</strong></a></div>
</body>
```

- Tashqi CSS ulab bo‘lmaydigan muhitda (artifact, sandbox, bitta faylli HTML): `dist/uzbtrust.css` matnini `<style>` ichiga qo‘ying.
- React, Vue va boshqalar: shu CSS'ni global ulang, komponent README'sidagi HTML tuzilmasini o‘sha freymvorkda takrorlang. Klass nomlari o‘zgarmaydi.
- Rang, oraliq, radius, soya — faqat `var(--…)` orqali. Hex yoki px'ni qo‘lda yozmang. Barcha tokenlar: `tokens.json`.
- Mavzu: `<html data-theme="light|dark|print">`. Bitta blokni qorong‘u qilish: o‘sha blokka `data-theme="dark"`.
- Maket: sahifa bo‘limi — `<section class="band">` (kulrang — `band band-alt`), ichida kontent `.narrow` (980px) yoki `.wrap` (1120px) ga o‘raladi; o‘z CSS'ingizda kenglik va chet yozmang. Yordamchi klasslarning to‘liq ro‘yxati: `docs/brand.md` → «Yordamchi klasslar».

## Qaysi komponent

| Kerak | Komponent |
|---|---|
| Forma (ro‘yxatdan o‘tish, ariza, aloqa) | `Field` — `.form` ichida; xato `aria-invalid` + `field-hint tone-bad` |
| Kirish oynasi (login va parol) | `StackedFields` |
| Afzallik yoki xususiyat kartalari | `InfoCard` — `info-grid is-3`, tugma ixtiyoriy |
| Bosiladigan kartalar (bo‘lim, hujjat) | `Card` — `card-grid` ichida |
| Savol-javob | `Accordion` |
| Sahifa boshi | `Hero` (`<section class="hero wrap">`), video bo‘lsa `VideoHero` |
| Yuborilgandan keyingi xabar | `Notice` (joyida) yoki `Toast` |

## Resurslar

Logo, ikon va belgilarni shu repodan oling. Qayta chizmang, taxminiy nusxa yasamang.

| Nima | Manzil |
|---|---|
| Logo (bo‘sh joyli, favicon/ikonka) | `https://cdn.jsdelivr.net/gh/uzbtrust/design-system@v1/assets/Logos/uzbtrust-logo.svg` |
| Yulduz (matn yonida, navigatsiyada) | `https://cdn.jsdelivr.net/gh/uzbtrust/design-system@v1/assets/Logos/uzbtrust-star.svg` |
| Ikonlar (Lucide 0.577.0, 43 ta) | `https://cdn.jsdelivr.net/gh/uzbtrust/design-system@v1/assets/Icons/<nom>.svg` |
| Mahsulot belgisi namunalari | `assets/Marks/` |

- Ikonni sahifaga inline SVG qilib qo‘ying: `stroke="currentColor"`, `stroke-width="1.75"`, 16–24px. Kerakli ikon yo‘q bo‘lsa — Lucide 0.577.0 dan xuddi shu parametrlar bilan.
- Logo rangi `#0071E3`, qorong‘u fonda ham o‘zgarmaydi; ko‘k yoki rangli fon ustiga qo‘yilmaydi.
- HTML'da yulduz uchun fayl kerak emas: `<span class="uzbtrust-mark" aria-hidden="true"></span>` — u `dist/uzbtrust.css` ichida.
- Logo — SVG (asosiy). SVG qabul qilinmaydigan joyda (ba’zi ijtimoiy tarmoqlar, ofis dasturlari) xuddi shu manzildagi `.png` zaxirani oling. Favicon: avval PNG, keyin SVG `<link rel="icon">`.

## Standart belgi

Foydalanuvchi logo yoki ikon haqida alohida aytmagan bo‘lsa, shu tizimda yasalgan **har bir ishda** muallif belgisi turadi — ko‘rgan odam dizayn kimniki ekanini bilsin. So‘ramasdan qo‘ying, ruxsat kutmang.

| Ish | Nima qo‘yiladi |
|---|---|
| Sayt, ilova | Favicon — `uzbtrust-logo`. Navigatsiyada yulduz (`uzbtrust-mark`) va loyiha nomi; nom berilmagan bo‘lsa «Abdurakhmonov». Pastda `Signature` |
| Test, bitta sahifa | Favicon va pastda `Signature` (`signature-row`) |
| PDF, hujjat | Birinchi sahifa tepasida yulduz 22px va «Abdurakhmonov»; oxirgi sahifa pastida «Dizayn: Abdurakhmonov», 9pt |
| Taqdimot | Muqovada wordmark (yulduz + «Abdurakhmonov»), qolgan slaydlarda pastki o‘ng burchakda yulduz 24px |
| Rasm, ijtimoiy tarmoq | Pastki burchakda yulduz, kichik tomonning ~6% i, chetdan ~4% |

- Ism aynan shunday yoziladi: **Abdurakhmonov**. Imzo tilga moslanadi: «Dizayn: Abdurakhmonov», «Design: Abdurakhmonov», «Дизайн: Abdurakhmonov».
- Foydalanuvchi o‘z logosini bersa — u navigatsiya va favicon'ga o‘tadi, imzo pastda qoladi. «Logo kerak emas» desa — yulduz olinadi, imzo qoladi. «Imzo kerak emas» desa — imzo ham olinadi.
- `©` qatoridagi nom — loyiha egasiniki, imzo bilan aralashtirmang.
- Yulduz rangi o‘zgarmaydi; ko‘k yoki rangli fon ustiga qo‘yilmaydi — bunday joyda oq yoki qora fonli bo‘sh joyga o‘tkazing.

## Asosiy qoidalar (qisqa)

- **Bitta urg‘u rangi:** `accent` (#0071e3). Asosiy amal — `btn btn-primary`, bir ekranda bitta. Ma’no ranglari (`bad`, `warn`, `good`) faqat ma’no uchun, doim so‘z bilan birga.
- **Shrift:** faqat `--font-sans` (va `--font-mono`, `--font-serif`, `--font-rounded`). SF bor qurilmada bu SF, boshqalarida — Inter (`dist/uzbtrust.css` uni `fonts/` dan o‘zi ulaydi). Boshqa veb-shrift, Google Fonts yoki SF shrift fayllarini **qo‘shmang**: SF litsenziyasi bu fayllarni saytga joylash va tarqatishni taqiqlaydi. CSS'ni inline qilsangiz, `@font-face` dagi `../fonts/…` yo‘lini `https://cdn.jsdelivr.net/gh/uzbtrust/design-system@v1/fonts/…` ga almashtiring.
- **Tipografiya:** sarlavha 600, harf oralig‘i o‘lchamga qarab (`track-*`), ikkinchi qator kulrang (`.dim`). Bosh harfli yorliq, emoji, gradient, rangli nur yo‘q.
- **Yuzalar:** kartalar `card` foni, `r-lg`, chegarasiz; soya faqat hover, menyu va dialogda.
- **Matn:** standart til — o‘zbekcha (lotin). `o‘`, `g‘` uchun ‘ (U+2018), tutuq belgisi ’ (U+2019), qo‘shtirnoq «…», sentence case. Haqiqiy odam ismlarini misol qilib yozmang — «Foydalanuvchi», «Ism va familiya».
- **Kirish imkoniyati:** matn kontrasti 4.5:1, bosish maydoni 44px, `prefers-reduced-motion` hurmat qilinadi.

## Muhitga qarab

- **Sayt:** `Ribbon` → `GlobalNav` → `LocalNav` → (`ChapterNav`) → `Tile` to‘ri, `Hero` yoki `VideoHero` → `bg` / `bg-alt` band'lar (`InfoCard`, `Gallery`, `Specs`, `Accordion`, «Batafsil» uchun `Modal`) → `Footer`. To‘liq namuna: `examples/site.html`.
- **Ilova:** `Topbar` → `PageHead` → `Facts` → `InsetList` / `Card` / `StatsTable`.
- **PDF va hujjat:** `data-theme="print"`, `DocumentPage` komponenti, `docs/brand.md` → «Hujjat va PDF».
- **Slayd, rasm, ijtimoiy tarmoq:** `docs/brand.md` → «Taqdimot va slayd», «Rasm, ijtimoiy tarmoq, grafik».

## Tizimni o‘zgartirish

Faqat foydalanuvchi so‘rasa. `tokens.json` yoki `components/bundle.css` o‘zgargach, `python3 scripts/build.py` bilan `dist/` ni qayta yig‘ing.
