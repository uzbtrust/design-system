# Harakat

Silliq, biroz prujinali, hech qachon ko‘z-ko‘z qilmaydigan. Faqat `transform` va `opacity` animatsiya qilinadi (`top/left/width/height` — yo‘q; istisno: yopilib-ochiladigan blok balandligi `overflow: hidden` bilan). Harakat faqat ekranda: PDF, chop va statik rasmda hamma narsa yakuniy holatida turadi. Video yoki animatsion slaydda xuddi shu egri chiziqlar va davomiyliklar ishlatiladi.

## Tokenlar (bundle.css'da)

| O‘zgaruvchi | Qiymat | Qayerda |
|---|---|---|
| `--ease` | `cubic-bezier(0.28, 0.11, 0.32, 1)` | asosiy egri chiziq: hover, rang, kichik o‘tishlar |
| `--ease-out` | `cubic-bezier(0.16, 1, 0.3, 1)` | expo-out: kirish, dialog, indikator, karta ko‘tarilishi |
| `--ease-in-out` | `cubic-bezier(0.65, 0, 0.35, 1)` | joy almashish |
| `--ease-spring` | `cubic-bezier(0.34, 1.56, 0.64, 1)` | holat belgisi, yulduz bosilishi |
| `--t-fast` | `0.2s` | hover, bosish, rang |
| `--t` | `0.4s` | rang va shaffoflik o‘tishlari |
| `--t-slow` | `0.8s` | progress ustunlari, katta o‘zgarishlar |

GSAP ishlatilsa: davomiylik .25 / .5 / .8 / 1.2s; `expo.out` — kirishlar, `power3.out` — standart, `power3.inOut` — indikatorlar, `uzbtrust` CustomEase (0.28, 0.11, 0.32, 1) — mikro-harakatlar.

## Naqshlar

- **Kirish (`.rise`):** 26px pastdan ko‘tarilish + shaffoflik, 0.9s `ease-out`. Zinapoya qadami 70ms (`--i` indeksi bilan). Butun hero 1.4s dan oshmaydi. Faqat marketing va bosh sahifada, skroll bilan; ilova ekranlarida kontent darhol ko‘rinadi.
- **Segment indikatori** tanlangan tugmaga sirpanadi: 0.45s `ease-out`, transform va width bilan. Birinchi o‘lchashda animatsiyasiz turadi.
- **Raqamlar** ilovada darhol ko‘rinadi. Marketing sahifasida skroll bilan sanab chiqishi mumkin: 700ms, `1 − (1 − t)⁴` egri chiziq.
- **Dialog:** 14px pastdan va 0.965 masshtabdan 0.5s `ease-out` bilan chiqadi; yopilishi 0.18s `ease-in`. Telefonda varaq pastdan siljib chiqadi. Parda faqat shaffoflik bilan, `--t` davomida.
- **Menyu:** 0.94 masshtab va −4px dan 0.3s `ease-out`, burchagi yuqori o‘ng.
- **Bildirishnoma (`Toast`):** yuqoridan 16px pastga va 0.96 dan 0.5s `ease-out`.
- **Karta hover:** −4px, `shadow-md`, 0.5s `ease-out`. Raqam va strelka rangi `--t` da o‘zgaradi.
- **Holat belgisi:** to‘ldiruvchi 0.45s `ease-spring` bilan kattalashadi, belgi chizig‘i 0.35s da chiziladi (`stroke-dashoffset`).
- **Grafik ustunlari** balandligi 0.7s `ease-out` bilan o‘sadi.
- **Mavzu almashinuvi:** View Transitions, 0.35–0.45s.

## Qoidalar

- Har paragrafni animatsiya qilmang: faqat sarlavha, karta, rasm va birinchi ekran elementlari.
- Ilk yashirin holat JS orqali beriladi, CSS orqali emas. JS ishlamasa, kontent ko‘rinib turishi shart.
- `will-change` kam va vaqtincha ishlatiladi.
- `prefers-reduced-motion: reduce` da barcha animatsiya va o‘tish 0.001ms bo‘ladi, skroll silliqligi o‘chadi.
