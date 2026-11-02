# Sayt

uzbtrust sayt sahifasi: oq va kulrang bandlar, katta sarlavhalar, shisha navigatsiya, kam so‘z. Murakkab effektlarsiz — oddiy va sokin veb tili.

## Sahifa tuzilishi

1. `Ribbon` — ixtiyoriy, bitta e’lon.
2. `GlobalNav` — 44px, sahifa bilan birga ketadi.
3. `LocalNav` — 52px, yopishqoq: sahifa nomi, bo‘limlar, bitta `btn-xs` amal. Bo‘lim yoki mahsulotlar oilasi boshida ostidan `ChapterNav` — ikonli bo‘limlar qatori.
4. Birinchi ekran: bosh sahifada `Tile` to‘ri (bitta `tile-hero` + ikki ustunli tile'lar), ichki sahifada `Hero`, video bo‘lsa `VideoHero`, yoki `band` + `band-head`.
5. Bandlar: `bg` va `bg-alt` navbat bilan, har biri `band-y` ichki chegara bilan. Ichida — `band-head` (chapda `band-title`, o‘ngda `link-more`), `copy-highlight` paragraf, `InfoCard` to‘ri, `Gallery`, `Specs` (texnik xususiyatlar va solishtirish), `StatsTable`, `Accordion`. Uzun tushuntirish «Batafsil» tugmasidan `Modal` da ochiladi.
6. `Footer` — izohlar, xarita, huquqiy qator.

## O‘lchamlar

| Narsa | Qiymat | Token |
|---|---|---|
| GlobalNav | 44px, havolalar 12px | `globalnav-h`, `text-footnote` |
| LocalNav | 52px, sarlavha 21px/600, havolalar 12px | `nav-h`, `text-nav-title` |
| Kontent ustuni | 980px + 22px chetlar | `max-narrow` |
| Katta tile | 692px, tepadan 56px, sarlavha 56px | `text-tile` |
| Kichik tile | 580px, tepadan 53px, sarlavha 40px, oraliq 12px | `text-tile-sm`, `s-3` |
| Band | 72–136px yuqori va past | `band-y` |
| Tugmalar | 17px/44 · 14px/36 · 12px/24 | `btn`, `btn-sm`, `btn-xs` |
| Galereya strelkasi | 36px doira, `control-bg` | `paddle` |
| Footer | 12px/16, `fg-3`, havola `fg-2` | `text-footnote` |

## Qorong‘u bloklar

- Butun sahifa: `<html data-theme="dark">`. Bitta blok: `<section data-theme="dark">` — mavzu oroli; ichidagi har bir token qorong‘u qiymatini oladi, komponentlarga hech narsa qo‘shilmaydi.
- Bosh sahifada yorug‘ va qorong‘u tile'lar navbatma-navbat. Qorong‘u tile foni — `bg` (#000).
- To‘liq qorong‘u sahifa: `dark` mavzu, bandlar `bg` (#000) va `bg-alt` (#111113), kartalar `card` (#1c1c1e).

## Matn

- Bosh sahifa tile'ida: nom yoki asosiy fikr (nuqta bilan), bir qatorli davomi, ikki amal. Davomi va’da yoki holat: «Kam so‘z, aniq raqam.»
- Band sarlavhasi qisqa, nuqta bilan: «Bir qarashda.», «Savollar.». Ostidagi paragraf — `copy-highlight`: kulrang tushuntirish, asosiy gap qora.
- Havolalar — fe’l yoki ot: «Batafsil», «Yuklab olish», «Hammasi». Tugma va `link-more` matni 1–2 so‘z.
- Izoh kerak bo‘lgan raqam yoniga `¹`, matni `Footer` dagi `footnotes` ga.

## Tekshiruv

- Yuqoridan pastga: `Ribbon` (bo‘lsa) → `GlobalNav` → `LocalNav` → kontent → `Footer`; ortiqcha panel yo‘q.
- 375, 768 va 1440px: GlobalNav 833px dan, LocalNav 734px dan menyuga o‘tadi; tile'lar telefonda bitta ustun.
- Har bandda bitta urg‘u: bitta `btn-primary` yoki bitta `eyebrow-new`.
- Qorong‘u orollarda matn va tugmalar o‘qiladi (tokenlar o‘zi almashadi — qo‘lda rang yozilmagan).
- Shrift faqat `dist/uzbtrust.css` orqali: SF bor qurilmada SF, boshqasida Inter. Boshqa veb-shrift ulanmagan.
