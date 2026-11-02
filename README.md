# uzbtrust

Har qanday ish uchun yagona vizual til: sayt, veb-ilova, PDF hujjat, taqdimot, rasm. Kayfiyati — **sokin, aniq, ortiqchasiz**. Bitta urg‘u rangi (`#0071e3`), tizim shrifti, katta sarlavhalar va ko‘p bo‘sh joy.

## Tez boshlash

Namunalarni brauzerda ko‘rish: [uzbtrust.github.io/design-system](https://uzbtrust.github.io/design-system/)

Sahifaga bitta fayl ulanadi — tokenlar va 38 ta komponent:

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/uzbtrust/design-system@v1/dist/uzbtrust.css">
```

```html
<html lang="uz" data-theme="light">
  …
  <h1 class="page-title">Hisobotlar.<span class="dim">3 tasi bugun tugaydi.</span></h1>
  <button class="btn btn-primary" type="button">Saqlash</button>
</html>
```

Mavzular: `light`, `dark`, `print` (`<html data-theme="…">`). Bitta blokni qorong‘u qilish uchun o‘sha blokka `data-theme="dark"` qo‘ying.

## AI bilan ishlatish

Istalgan AI'ga (Claude, ChatGPT, Cursor…) shunday yozing:

> Dizayn uchun github.com/uzbtrust/design-system dan foydalan.

Agent `AGENTS.md` ni o‘qiydi: qaysi faylni qachon ochish, CSS'ni qanday ulash, logo va ikonlarni qayerdan olish, qaysi qoidalarga amal qilish shu yerda yozilgan.

## Tuzilma

| Yo‘l | Nima |
|---|---|
| `AGENTS.md` | AI agentlar uchun ko‘rsatma |
| `docs/brand.md` | Brend kitobi: tamoyillar, rang, tipografiya, muhitga qarab qoidalar |
| `docs/01-ovoz.md` · `02-harakat.md` · `03-tekshiruv.md` · `04-sayt.md` | Matn va til, harakat, tekshiruv ro‘yxati, sayt qolipi |
| `tokens.json` | Barcha tokenlar: rang (3 mavzu), tipografiya, oraliq, radius, soya, maket |
| `components/bundle.css` | Komponentlar uslublari (manba) |
| `components/<Nom>/` | Har komponent: `README.md` (tuzilma, qoidalar) va `example.html` (namuna) |
| `dist/uzbtrust.css` | Ulanadigan fayl: `tokens.css` + `bundle.css` |
| `dist/tokens.css` | Faqat tokenlar (CSS o‘zgaruvchilar va type klasslari) |
| `fonts/` | Inter 4.1 (variable) — SF yo‘q qurilmalar uchun uning o‘rnini bosuvchi, OFL |
| `assets/Logos` · `Icons` · `Marks` | Logo (PNG), 43 ta Lucide ikoni (SVG), mahsulot belgisi namunalari |
| `examples/site.html` | To‘liq sayt namunasi |
| `scripts/build.py` | `dist/` ni qayta yig‘adi |

## Komponentlar

- **Sayt:** [GlobalNav](components/GlobalNav) · [LocalNav](components/LocalNav) · [Ribbon](components/Ribbon) · [Tile](components/Tile) · [InfoCard](components/InfoCard) · [Gallery](components/Gallery) · [Accordion](components/Accordion) · [Footer](components/Footer)
- **Sahifa va qobiq:** [Topbar](components/Topbar) · [PageHead](components/PageHead) · [Hero](components/Hero) · [Facts](components/Facts) · [DocumentPage](components/DocumentPage) · [Logo](components/Logo)
- **Amallar:** [Button](components/Button) · [IconButton](components/IconButton) · [ChipButton](components/ChipButton) · [Segmented](components/Segmented) · [Stepper](components/Stepper)
- **Formalar:** [Field](components/Field) · [PillField](components/PillField) · [StackedFields](components/StackedFields) · [DatePicker](components/DatePicker) · [DropZone](components/DropZone)
- **Ro‘yxat, karta, ma’lumot:** [InsetList](components/InsetList) · [Card](components/Card) · [LinkCard](components/LinkCard) · [StatsTable](components/StatsTable) · [BarChart](components/BarChart) · [Progress](components/Progress)
- **Holat va xabar:** [Notice](components/Notice) · [Toast](components/Toast) · [Sheet](components/Sheet) · [Empty](components/Empty) · [StatusGlyph](components/StatusGlyph) · [Tag](components/Tag) · [Stars](components/Stars) · [Avatar](components/Avatar)

## Shrift

- **SF bor qurilmalarda** — tizimning o‘z shrifti: `--font-sans` → SF Pro, `--font-mono` → SF Mono, `--font-serif` → New York, `--font-rounded` → SF Pro Rounded.
- **Boshqa qurilmalarda** (Windows, Android, Linux) — **Inter 4.1**, SF'ga eng yaqin ochiq shrift. U `fonts/` da turadi va `dist/uzbtrust.css` bilan o‘zi ulanadi; SF bor qurilmada yuklanmaydi ham. Litsenziya: SIL OFL 1.1 (`fonts/LICENSE.txt`).
- SF shrift fayllari repoga qo‘shilmaydi: ularning litsenziyasi tarqatishni taqiqlaydi.

## Versiyalar

`@v1` har doim 1.x ning eng oxirgi tegini oladi. Aniq versiya kerak bo‘lsa: `@v1.0.0`. O‘zgarishdan keyin:

```bash
python3 scripts/build.py
```

so‘ng commit va yangi teg (`v1.0.1`, `v1.1.0`…).
