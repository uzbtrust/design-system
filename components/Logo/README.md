# Logo

Tizim logosi — bir tekis ko‘k (`#0071E3`) yulduz; yonida nik yozuvi bilan wordmark hosil qiladi: veb-sahifada «uzbtrust», faylda «Abdurakhmonov». Har bir ishda doim turadi.

## Fayllar
- `assets/Logos/uzbtrust-logo.svg` — viewBox 2560×2560, shaffof fon, atrofida bo‘sh joy bilan. Ilova ikonkasi, favicon, avatar, ijtimoiy tarmoq rasmi uchun.
- `assets/Logos/uzbtrust-star.svg` — viewBox 1400×1346, bo‘sh joyi qirqilgan. Wordmark, hujjat sarlavhasi va matn yonida ishlatish uchun.
- SVG — asosiy fayl, istalgan o‘lchamda tiniq. Xuddi shu nomdagi `.png` (2560×2560, 1400×1346) — zaxira, faqat SVG qabul qilinmaydigan joyda.

## Tuzilma
```html
<!-- Veb-sahifada -->
<a class="wordmark" href="/"><span class="uzbtrust-mark" aria-hidden="true"></span><span class="wordmark-text">uzbtrust</span></a>
<!-- Faylda (PDF, hujjat, taqdimot, rasm): xuddi shu wordmark, matni «Abdurakhmonov» -->
```
Favicon — avval PNG, keyin SVG: SVG'ni qo‘llaydigan brauzer uni oladi, qolganlari PNG'ni.
```html
<link rel="icon" type="image/png" href="uzbtrust-logo.png">
<link rel="icon" type="image/svg+xml" href="uzbtrust-logo.svg">
```

## Qoidalar
- Rang faqat `#0071E3` (`accent` ning yorug‘ qiymati) — qorong‘u mavzuda ham o‘zgarmaydi. Gradient, soya, kontur, aylantirish, cho‘zish yo‘q.
- Fon: oq (4.7:1), `bg-alt` (4.3:1) yoki qora (4.5:1); qorong‘u `bg-elev` ustida ham 3.6:1 — grafik belgi uchun yetarli. Ko‘k yoki rangli fon ustiga qo‘yilmaydi — buning uchun alohida oq variant kerak bo‘ladi.
- Wordmark: yulduz matn o‘lchamidan ~1.3 baravar baland (17px matn — 22px yulduz, 9px oraliq). Matn 600, harf oralig‘i o‘lchamga qarab (17px — `track-body`, 44px — `track-display`), rangi `fg`. Nom aynan shu yozilishda: veb-sahifada «uzbtrust», faylda «Abdurakhmonov».
- Atrofidagi bo‘sh joy — kamida yulduz enining chorak qismi. Eng kichik o‘lcham — 16px (favicon).
- `uzbtrust-mark` — yulduzning CSS ichidagi nusxasi: `dist/uzbtrust.css` ulangan joyda fayl yo‘lisiz ishlaydi, eni `width` bilan beriladi. HTML va sayt uchun shuni ishlating; favicon, PDF va rasm uchun — fayllarni.
- Standart holat: foydalanuvchi logo yoki ikon haqida alohida aytmasa, yulduz va `Signature` har bir ishda turadi (`docs/brand.md` → «Standart belgi»). Foydalanuvchi o‘z logosini bersa, u navigatsiya va favicon'ga o‘tadi; imzo pastda qoladi.
