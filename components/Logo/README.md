# Logo

uzbtrust logosi — bir tekis ko‘k (`#0071E3`) yulduz; yonida kichik harflarda «uzbtrust» yozuvi bilan wordmark hosil qiladi.

## Fayllar
- `assets/Logos/uzbtrust-logo.svg` — viewBox 2560×2560, shaffof fon, atrofida bo‘sh joy bilan. Ilova ikonkasi, favicon, avatar, ijtimoiy tarmoq rasmi uchun.
- `assets/Logos/uzbtrust-star.svg` — viewBox 1400×1346, bo‘sh joyi qirqilgan. Wordmark, hujjat sarlavhasi va matn yonida ishlatish uchun.
- SVG — asosiy fayl, istalgan o‘lchamda tiniq. Xuddi shu nomdagi `.png` (2560×2560, 1400×1346) — zaxira, faqat SVG qabul qilinmaydigan joyda.

## Tuzilma
```html
<a class="wordmark" href="/"><img src="uzbtrust-star.svg" alt="" width="22"><span class="wordmark-text">uzbtrust</span></a>
```
Favicon: `<link rel="icon" type="image/svg+xml" href="uzbtrust-logo.svg">`, eski brauzerlar uchun yonida `<link rel="icon" type="image/png" href="uzbtrust-logo.png">`.

## Qoidalar
- Rang faqat `#0071E3` (`accent` ning yorug‘ qiymati) — qorong‘u mavzuda ham o‘zgarmaydi. Gradient, soya, kontur, aylantirish, cho‘zish yo‘q.
- Fon: oq (4.7:1), `bg-alt` (4.3:1) yoki qora (4.5:1); qorong‘u `bg-elev` ustida ham 3.6:1 — grafik belgi uchun yetarli. Ko‘k yoki rangli fon ustiga qo‘yilmaydi — buning uchun alohida oq variant kerak bo‘ladi.
- Wordmark: yulduz matn o‘lchamidan ~1.3 baravar baland (17px matn — 22px yulduz, 9px oraliq). Matn 600, harf oralig‘i o‘lchamga qarab (17px — `track-body`, 44px — `track-display`), rangi `fg`. Nom doim kichik harflarda: «uzbtrust».
- Atrofidagi bo‘sh joy — kamida yulduz enining chorak qismi. Eng kichik o‘lcham — 16px (favicon).
- Mahsulotlarning o‘z belgisi bo‘lsa (`assets/Marks` qolipi), uzbtrust logosi ularning o‘rnini bosmaydi: u muallif belgisi — footer, «haqida», hujjat muqovasi va shaxsiy sahifalar uchun.
