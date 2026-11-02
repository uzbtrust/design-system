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
  <script>document.documentElement.dataset.theme = matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";</script>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/uzbtrust/design-system@v1/dist/uzbtrust.css">
</head>
```

- Tashqi CSS ulab bo‘lmaydigan muhitda (artifact, sandbox, bitta faylli HTML): `dist/uzbtrust.css` matnini `<style>` ichiga qo‘ying.
- React, Vue va boshqalar: shu CSS'ni global ulang, komponent README'sidagi HTML tuzilmasini o‘sha freymvorkda takrorlang. Klass nomlari o‘zgarmaydi.
- Rang, oraliq, radius, soya — faqat `var(--…)` orqali. Hex yoki px'ni qo‘lda yozmang. Barcha tokenlar: `tokens.json`.
- Mavzu: `<html data-theme="light|dark|print">`. Bitta blokni qorong‘u qilish: o‘sha blokka `data-theme="dark"`.

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
- Logo — SVG (asosiy). SVG qabul qilinmaydigan joyda (ba’zi ijtimoiy tarmoqlar, ofis dasturlari) xuddi shu manzildagi `.png` zaxirani oling. Favicon: avval PNG, keyin SVG `<link rel="icon">`.

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
