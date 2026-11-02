# Brend kitobi

uzbtrust — har qanday ish uchun yagona vizual til: veb-ilova, sayt, PDF hujjat, taqdimot, rasm yoki grafik. Kayfiyati — **sokin, diqqatli, ortiqchasiz**. Natija qaysi ko‘rinishda bo‘lmasin, bir qo‘l ishi ekani bilinib turadi.

## «uzbtrust'ni ishlat» deyilganda

Bu bo‘lim — tizimni qo‘llaydigan har kim (inson yoki agent) uchun qisqa buyruqlar.

1. **Avval shu README'ni o‘qing**, keyin kerakli komponent README'sini. Ranglar, o‘lchamlar va masofalar `tokens.json` da; ularni o‘zingizdan o‘ylab topmang.
2. **Muhitni aniqlang** va mavzuni tanlang: ekran uchun `light` (va kerak bo‘lsa `dark`), qog‘ozga yoki PDF'ga — `print`. Pastdagi «Muhitga qarab» bo‘limiga amal qiling.
3. **Tilni aniqlang:** foydalanuvchi so‘ragan yoki loyiha ishlatadigan til. «Ovoz va matn» bo‘limidagi shu til qoidasini qo‘llang. O‘zbekcha — standart.
4. **Faqat tizimdagi narsalardan foydalaning:** bitta urg‘u rangi (`accent`), SF shrift to‘plami, `r-*` radiuslar, 8px shkala, Lucide ikonlari, `assets/Logos` dagi logo. Yangi rang, gradient, shrift yoki emoji qo‘shmang.
5. **Mavjud ishni o‘tkazishda** «Mavjud loyihani o‘tkazish» bo‘limidagi tartibga amal qiling: tuzilma va matn saqlanadi, ko‘rinish almashadi.
6. **Oxirida tekshiring** — «Tekshiruv» bo‘limidagi ro‘yxat bo‘yicha.

## Muhitga qarab

### Veb-ilova va sayt
- `dist/uzbtrust.css` ni ulang — tokenlar va komponentlar bitta faylda (`tokens.json` va `components/bundle.css` dan `scripts/build.py` yig‘adi). Rang, oraliq, radius va soyani faqat `var(--…)` orqali oling — hex yoki px'ni qo‘lda yozmang.
- Mavzu `<html>` da almashadi: `data-theme="dark"` yoki `class="dark"`. Uni sahifa chizilishidan oldin `<head>` dagi kichik skript bilan o‘rnating. Odatda tizim mavzusiga ergashing; foydalanuvchi o‘zi bosgandagina tanlovni saqlang.
- Komponentlar — CSS klasslari va qat’iy HTML tuzilmasi. React, Vue yoki oddiy HTML — farqi yo‘q: komponent README'sidagi tuzilmani o‘sha freymvorkda takrorlang.
- Ilova qolipi: shisha `Topbar` → `PageHead` (yoki bosh sahifada `Hero`) → `Facts` → asosiy kontent (`InsetList`, `Card` to‘ri, `StatsTable`) → oddiy `.foot`.
- Sayt qolipi: `Ribbon` → `GlobalNav` → yopishqoq `LocalNav` → `ChapterNav` (ixtiyoriy) → `Tile` to‘ri, `Hero` yoki `VideoHero` → `bg` / `bg-alt` band'lar (`band-head`, `InfoCard`, `Gallery`, `Specs`, `Accordion`; «Batafsil» — `Modal`) → `Footer`. Batafsil — «Sayt» bo‘limi.
- Mavzu oroli: istalgan blokka `data-theme="dark"` (yoki `"light"`) qo‘ying — tokenlar shu blok ichida almashadi. Qorong‘u tile, qorong‘u band yoki qorong‘u hero shunday yasaladi.

### Hujjat va PDF
- Mavzu `print`: oq fon, qora matn (`fg` #000), ikkilamchi matn `fg-3` (#424245), havola va urg‘u `accent` (#0066cc), soya yo‘q.
- Sahifa chetlari: yuqori 18mm, yon 16mm, past 20mm. Bir ustun, butun kenglik.
- Matn: sarlavha `text-print-title` (26pt/1.1, 600), kirish `text-print-lead` (12pt, #333), bo‘limlar `text-print-h2`, asosiy matn `text-print-body` (11pt/1.45), izoh `text-print-small` (9pt).
- Sarlavha ostida 8mm oraliq va 1px #999 chiziq. Muqova — `Hero` naqshi: ikki qatorli sarlavha (ikkinchisi `fg-3`), chapga tekislangan, tugmalarsiz.
- Kartalar va qutilar fonsiz: 1px #aaa chegara, radius 6px. Rasm, jadval, grafik va karta sahifa o‘rtasida bo‘linmaydi (`break-inside: avoid`); sarlavha sahifa oxirida yolg‘iz qolmaydi (`break-after: avoid`); paragrafda kamida 3 qator (`orphans/widows: 3`).
- Havolalar matn rangida, tagiga chizilmagan. Animatsiya, shisha va hover — yo‘q.
- Raqamlar katta va `tabular-nums` (`Facts`, `stat-list`), grafiklar `BarChart` qoidalarida, bir o‘lchov — bir rang.

### Taqdimot va slayd
- 16:9, har slaydda bitta fikr. Fon `bg` va `bg-alt` almashadi (qorong‘u zal uchun `dark`).
- Sarlavha `text-hero` yoki `text-h1` + kulrang `.dim` davomi; matn `text-lead`. Raqamli slayd — `text-stat` ulkan raqam va ostida bir qator izoh.
- Chetlardan kamida 64px (`s-8`). Bir slaydda bitta `accent` urg‘u; qolgani neytral.

### Rasm, ijtimoiy tarmoq, grafik
- Fon oq yoki `bg-alt` (qorong‘u variant: `bg` #000 / `bg-elev`). Matn chapga yoki markazga, sarlavha 600, harf oralig‘i o‘lchamga qarab (`track-*`).
- Bitta urg‘u rangi, katta bo‘sh joy. Ma’lumot grafiklari: seriyalar `data-1`, `data-2`, `data-3`; matn `chart-ink`, o‘q `chart-axis`, to‘r `chart-grid`.

## Mavjud loyihani o‘tkazish

1. **Inventarizatsiya:** loyihadagi ranglar, shriftlar, radiuslar, soyalar va komponentlarni ro‘yxatlang.
2. **Tokenlar:** har rangni eng yaqin rolga moslang (fon → `bg`/`bg-alt`, matn → `fg`/`fg-3`, brend rangi → `accent`, xato → `bad`, ogohlantirish → `warn`). Bir nechta urg‘u rangi bo‘lsa, bittasi qoladi.
3. **Shrift:** veb-shriftlarni olib tashlang, `--font` (SF to‘plami) qo‘ying. O‘lchamlarni type uslublariga moslang.
4. **Shakl:** radiuslar `r-sm` / `r-md` / `r-lg` / `r-pill` ga; chegarali kartalar chegarasiz `card` yuzasiga; soyalar faqat hover, menyu va dialogda.
5. **Komponentlar:** tugmalar → `Button`, tablar → `Segmented`, ro‘yxatlar → `InsetList`, modallar → `Sheet`, xabarlar → `Toast` / `Notice`, formalar → `Field`. Mos keladigani yo‘q bo‘lsa, eng yaqin naqshdan yangisini tizim tokenlari bilan quring.
6. **Matn:** til qoidalari bo‘yicha qayta ko‘rib chiqing (sentence case, qo‘shtirnoq, ‘ va ’ belgilari).
7. **Tekshiruv:** ikki mavzu, uch kenglik, klaviatura, kontrast.

Tuzilma, ma’lumot va funksiya o‘zgarmaydi — faqat ko‘rinish va ovoz.

## Tamoyillar

1. **Bo‘sh joy — dizayn.** Katta vertikal ritm, qisqa satrlar. Shubha bo‘lsa, chiziq, quti yoki yorliqni olib tashlang.
2. **Tipografiya ishni bajaradi.** Katta sarlavha (600, o‘lchamga mos `track-*`), ostida kulrang `.dim` davomi. Ikkilamchi matn `fg-3`. Har ekranda (sahifada, slaydda) aniq uch daraja.
3. **Chiziq emas, yuza.** Kartalar `card` foni, `r-lg` radius, chegarasiz. Ingichka chiziq (`line-soft`) faqat ro‘yxat qatorlari orasida.
4. **Shisha yuqori panel.** `glass` + `backdrop-filter: saturate(180%) blur(20px)` + pastki qirrada 1px `line-soft`.
5. **Bitta urg‘u rangi.** `accent` (ko‘k) — faqat asosiy amal va faol holat uchun. Ma’no ranglari (`bad`, `warn`, `good`) faqat ma’no uchun.
6. **Pill va havola.** Asosiy amal — to‘ldirilgan `accent` pill. Ikkilamchisi — chiziqli pill (`accent-ink` kontur, hoverda to‘liq ko‘k) yoki `›` li `.link-more`.
7. **Hammasi 8px shkalada.** Kontent eni `max`, o‘qish ustuni `read`.

## Rang

- **Fon.** Yorug‘da `bg` (#fff) va `bg-alt` (#f5f5f7) bo‘limma-bo‘lim almashadi. Qorong‘uda `bg` (#000), `bg-alt` (#111113), `bg-elev` (#1c1c1e). Bej, yashil qog‘oz tusi, gradient va rangli nur yo‘q.
- **Matn.** `fg` — asosiy; `fg-3` — izoh, lead, `.dim`; `fg-2` — ikon va teg; `fg-4` — faqat bezak va o‘chirilgan holat, matn uchun emas.
- **Urg‘u.** `accent` — fokus halqasi, indikator, grafik ustuni. Oq matn turadigan ko‘k fon (asosiy tugma, tanlangan kun, bosqich raqami) — doim `accent-fill`. Ko‘k matn — `accent-ink`, yumshoq fon — `accent-soft`. Hover va bosilish biroz to‘qlashadi (`accent-hover`, `accent-press`).
- **Ma’no ranglari.** `bad` — xato, kechikish, o‘chirish; `warn` — bugun, muhim, qaytarilgan; `good` — muvaffaqiyat. Ular hech qachon yolg‘iz kelmaydi: doim so‘z yoki shakl bilan. Fonlari `bad-soft`, `warn-soft`; xavfli tugma chiziqli (`bad`), hoverda `danger-fill`. Yulduz (baho, muhimlik) — `star`, kulrang.
- **Neytral to‘ldirishlar.** `fill` — maydon, sokin tugma, segment izi; `fill-hover`; `chip` — teg va strelka doirasi; `row-hover` — qator hoveri.
- **Sayt.** `glass-nav` — `GlobalNav` va `LocalNav` foni; `control-bg` — galereya strelkalari va `dotnav`; `media-control` — rasm yoki video ustidagi play/pauza; `new` — faqat «Yangi» yorlig‘i, fon emas.
- **Ma’lumot.** Seriyalar `data-1` (ko‘k), `data-2` (to‘q sariq), `data-3` (binafsha); `data-ref` — punktir; maydonlar `data-1-area`, `data-2-area`, `data-neg-area`; grafik matni `chart-ink`, o‘qlar `chart-axis`, to‘r `chart-grid`. Bitta o‘lchovli grafik faqat `accent` da chiziladi.

## Tipografiya

- **Shrift.** `--font` — qurilmaning tizim shrifti: SF bor qurilmada SF Pro, optik o‘lchami o‘zi tanlanadi (≈20px dan katta — Display, kichik — Text). `--font-mono` → SF Mono, `--font-serif` → New York, `--font-rounded` → SF Pro Rounded (`ui-rounded`). SF yo‘q joyda (Windows, Android, Linux) — **Inter 4.1** (`InterVariable`, `fonts/`), SF'ga eng yaqin ochiq shrift: og‘irliklari va optik o‘lchami SF kabi ishlaydi, `track-*` unga ham qo‘llanadi. SF bor qurilmada Inter yuklanmaydi.
- **SF shrift fayllari tizimga qo‘shilmaydi.** SF Pro, SF Compact, SF Mono va New York litsenziyasi ularni saytga, PDF'ga yoki boshqa ishga joylashni va tarmoqda tarqatishni taqiqlaydi. Figma'da maket chizish uchun shriftni o‘z kompyuteringizga rasmiy manbadan o‘rnating. Tizimdagi yagona `@font-face` — Inter (SIL OFL 1.1). Og‘irliklar: 400 — matn va tugma, 500 — kichik urg‘u, 600 — sarlavha, raqam, qalin matn. 700 ishlatilmaydi (faqat havola belgisidagi harf). Formula uchun `--serif`, kod uchun `--mono`.
- **Sarlavha naqshi.** Birinchi qator — asosiy fikr, nuqta bilan tugaydi (`text-title` yoki `text-hero`, `fg`). Ikkinchi qator `.dim` (`fg-3`) — holat yoki davomi. Tepada `text-eyebrow`: sana yoki bo‘lim nomi, oddiy harflarda.
- **O‘lchamlar suyuq.** Ekranda `--fs-hero`, `--fs-title`, `--fs-h1`, `--fs-h3`, `--fs-lead` `clamp()` bilan o‘sadi; type uslublari eng katta qiymatni ko‘rsatadi. Chop uchun `Print` guruhidagi uslublar.
- **Harf oralig‘i** o‘lchamga bog‘liq: ≥80px `track-super` (−0.015em), 64–72px `track-hero` (−0.009em), 56px `track-tile` (−0.005em), 40–48px `track-display` (−0.003em), 32px `track-headline` (+0.004em), 28px `track-eyebrow` (+0.007em), 24px `track-title` (+0.009em), 19–21px `track-intro` (+0.011em), 17px `track-body` (−0.022em), 14–15px `track-small` (−0.016em), 12–13px `track-caption` (−0.01em). Shkaladan tashqari qiymat yozmang.
- **Sayt shkalasi** (px / qator balandligi): 80/84 `text-title` · 64/68 `text-h1` · 56/60 `text-tile` · 48/52 `text-h2` · 40/44 `text-tile-sm` · 32/36 `text-subhead` · 28/32 `text-h3` · 24/28 `text-group` · 21/29 `text-intro` · 17/25 `text-body` · 14/20 `text-sm` · 12/16 `text-footnote`. Sarlavhalar 600, matn 400.
- **Ajratilgan paragraf** (`.copy-highlight`): butun paragraf `fg-3` rangida 600, asosiy gap `<strong>` ichida `fg`. «<strong>Raqam so‘zdan kuchli.</strong> Har bo‘limda bitta ko‘rsatkich.» Bir bandda bitta.
- **«Yangi»** — `.eyebrow-new` (`new` rangi): sarlavha ustidagi bitta so‘z, sahifada bittadan.
- **Raqamlar** doim `tabular-nums`, 600. Raqam qanday bo‘lsa shunday yoziladi (4, 24) — oldiga nol qo‘shilmaydi, tartib raqami bezak sifatida katta yozilmaydi. Ilova ichida raqam darhol ko‘rinadi; sanab chiqish faqat marketing sahifasida.
- **Bosh harflar** bilan yozilgan yorliq yo‘q: eyebrow, teg, jadval va bo‘lim sarlavhalari oddiy harflarda (qisqartmalar bundan mustasno).
- **Qator sindirish.** Sarlavhada `text-wrap: balance`, paragrafda `pretty`.
- **Chegaralar.** Eng kichik matn 12px (9pt), asosiy matn ekranda kamida 16px (odatda 17px), chopda 11pt. Lead eni 30–34em, o‘qish ustuni `read`.

## Oraliq va maket

- Shkala: `s-1` 4 · `s-2` 8 · `s-3` 12 · `s-4` 16 · `s-5` 24 · `s-6` 32 · `s-7` 48 · `s-8` 64 · `s-9` 96 · `s-10` 140.
- Kenglik: kontent `max` (1120px), sayt ustuni `max-narrow` (980px — navigatsiya, footer, FAQ, `InfoCard`), o‘qish `read` (700px), uch ustunli qobiq `max-wide` (1280px). Chetlar `gutter` (20 → 48px); sayt navigatsiyasi va footerda 22px.
- Ritm: sahifa boshi 44–96px, band ichki chegarasi `band-y` (72–136px), ro‘yxat guruhlari orasi 36–52px. Sayt band'lari `bg` va `bg-alt` almashib keladi; tile'lar orasida 12px.
- Karta to‘ri: 1 ustun → 2 (600px dan) → 3 (960px dan); oraliq 16px, keng ekranda 20px. Yolg‘iz qolgan oxirgi karta butun qatorni egallaydi.
- Mobil birinchi: 375, 768 va 1440px. Gorizontal skroll bo‘lmasin: keng jadval o‘z konteynerida skroll qiladi yoki kartaga aylanadi.

## Yuzalar, radius, soya

- **Karta:** `card` foni, `r-lg`, soyasiz. Ekranda hoverda `bg-elev` + `shadow-md` + 4px ko‘tariladi; katta raqam va strelka `accent` ga aylanadi.
- **Ro‘yxat:** `inset-list` — `card` ustida qatorlar. Ajratuvchi `line-soft` ikon ustunidan keyin boshlanadi.
- **Dialog:** `bg-elev`, radius 28px, `0 0 0 1px line-soft` + `shadow-lg`, parda `backdrop` + `blur(6px)`. Telefonda pastdan chiqadigan varaq.
- **Radiuslar:** maydon `r-sm`, guruh va menyu `r-md`, karta `r-lg`, katta yuza `r-xl`, tugma/teg/segment `r-pill`. Chopda qutilar 6px.
- **Soya** kam: hover'dagi karta, menyu, kalendar, bildirishnoma — `shadow-md`; dialog — `shadow-lg`; tooltip — `shadow-sm`. Chopda yo‘q.

## Holatlar

- **Hover** faqat `@media (hover: hover)` ichida: `fill-hover`, chiziqli tugma esa to‘liq rangga o‘tadi; `›` 3px suriladi.
- **Bosish:** tugma `scale(.97)`, ikon tugma `.9`, karta `.98`, chip `.96`.
- **Fokus:** `:focus-visible` — 2px yaxlit `accent` halqa + 2px oraliq (har fonda kamida 3.8:1). Ro‘yxat qatorida ichki 2px `accent`. Maydonlarda ichki 1.5px `accent` va tashqi 4px `accent-soft`.
- **O‘chirilgan:** opacity 0.35–0.4.
- **Bosish maydoni:** sensorda kamida 44×44px.

## Ikonografiya

- **Tizim:** Lucide (`lucide-react` / `lucide` 0.577.0), chiziq 1.75 — matnning oddiy og‘irligiga mos (kichik meta ikonlarida 1.8). Tanlangan holatda ikon to‘ldirilgan variantga o‘tadi. O‘lchami 16–24px, matn bilan bir chiziqda. Rangi `currentColor` — odatda `fg-2`/`fg-3`, faol holatda `accent-ink`.
- **Qo‘lda chizilgan ikon** kerak bo‘lsa: 24×24 viewBox, 1.5px yumaloq uchli chiziq, Lucide ruhida.
- Emoji va ikon-shrift yo‘q. Tipografik belgilar mumkin: `›` (davomi), `·` (ajratuvchi), `—`.
- `assets/Icons` — 43 ta Lucide ikonining aynan nusxasi (fayllarda standart chiziq 2 va #6e6e73; kodda `stroke-width="1.75"` va `currentColor`). Kerakli ikon bu yerda bo‘lmasa, Lucide'dan oling.
- Holat belgilari (`StatusGlyph`): bo‘sh doira → yarim to‘ldirilgan → nuqtali doira → belgili to‘la doira → ✕ li doira.

## Logo va wordmark

- **uzbtrust logosi** — bir tekis ko‘k (`#0071E3`) yulduz, `assets/Logos` da. Ikonka va favicon uchun `uzbtrust-logo.svg` (bo‘sh joyli), matn yonida `uzbtrust-star.svg` (qirqilgan); SVG — asosiy fayl, xuddi shu nomdagi PNG — zaxira. Rang qorong‘u fonda ham o‘zgarmaydi; gradient, soya va kontur qo‘shilmaydi, ko‘k yoki rangli fon ustiga qo‘yilmaydi. Batafsil — `Logo` komponenti.
- **Wordmark:** yulduz + «uzbtrust» (doim kichik harflarda), 17px/600 matn yonida 22px yulduz, oraliq 9px. Logoni qayta chizmang va taxminiy nusxasini yasamang — faqat fayllarni ishlating.
- **Mahsulot belgisi qolipi:** `accent` rangli yumaloq kvadrat (burchak radiusi tomonning ~25%i) ichida oq belgi, yonida nom. Belgi 20–22px, nomgacha 9px, hoverda opacity 0.72; telefonda nom yashiriladi. Namunalar — `assets/Marks`.

## Mavzular

- **`light`** — standart. **`dark`** — ekran uchun; faqat tokenlar o‘zgaradi, komponentlar `var(--…)` orqali o‘zi moslashadi. **`print`** — qog‘oz va PDF.
- Mavzu butun sahifaga (`<html>`) yoki bitta blokka qo‘yiladi: `<section data-theme="dark">` — mavzu oroli (qora tile va bandlar).
- Ekranda `theme-color` meta va mavzu birinchi chizilishdan oldin qo‘yiladi. Almashinuv View Transitions bilan (0.35–0.45s).

## Kirish imkoniyati

- Matn kontrasti WCAG AA: oddiy matn 4.5:1, 24px+ matn va ma’noli ikon/chegara 3:1. Har rang tokenining izohida qaysi fonda qancha ekani yozilgan.
- Holat hech qachon faqat rang bilan berilmaydi: shakl va so‘z ham bo‘ladi.
- Semantik HTML, `aria-pressed` segment va chiplarda, `aria-label` faqat ikonli tugmalarda. Dialog Escape bilan yopiladi va fokusni joyiga qaytaradi.
- `prefers-reduced-motion` barcha animatsiyani o‘chiradi. Kontent hech qachon JS ortida yashirilmaydi.

## Kontrast

- Tizimdagi barcha matn juftlari WCAG AA'ga javob beradi (4.5:1, katta matn 3:1). Fokus halqasi, boshqaruv chegarasi va ma’noli ikonlar — kamida 3:1. Bu `light`, `dark` va `print` mavzularining har birida tekshirilgan; raqamlar har token izohida.
- Oq matn ko‘k fon ustida — faqat `accent-fill`, qizil fon ustida — faqat `danger-fill`. `accent` (qorong‘uda 3.65:1) va `bad` (qorong‘uda 3.4:1) oq matn ostiga fon qilib qo‘yilmaydi.
- Boshqaruv konturi — `line-control`. `line-strong` va `line` faqat bezak chiziqlari.
- Kiritish maydonlari (`input`, `pill-field`, `stepper`) chegarasiz, `fill` fonli: fondan farqi 1.1:1, ular yorliq va placeholder orqali taniladi. Maydon chegarasi uchun ham qat’iy 3:1 kerak bo‘lgan ishda ichki 1px `line-control` kontur qo‘shing.
- Uchinchi tomon belgilaridagi brend ranglari (Pinterest, Dribbble, Telegram…) o‘zgartirilmaydi; ulardagi harf 19px/700 — katta matn sifatida 3:1 dan yuqori.
