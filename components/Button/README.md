# Button

Pill shaklidagi tugma: ekranda bitta asosiy amal `btn-primary`, qolganlari yumshoqroq.

## Tuzilma
```html
<button class="btn btn-primary" type="button">Saqlash</button>
<button class="btn btn-secondary" type="button"><svg …/> Yangi hujjat</button>
<a class="link-more" href="…">Batafsil</a>
<button class="btn-text is-danger" type="button"><svg …/> O‘chirish</button>
```

## Variantlar
- `btn-primary` — `accent-fill` fon, oq yozuv (4.7:1). Bir ekranda bitta. Hoverda `accent-hover`, bosilganda `accent-press` — ikkalasi biroz to‘qroq.
- `btn-secondary` — chiziqli pill: shaffof fon, `accent-ink` yozuv va 1px kontur; hoverda `accent-fill` fon va oq yozuv.
- `btn-quiet` — `fill` fon, `fg` yozuv: «Bekor qilish», neytral amal.
- `btn-danger` — chiziqli pill: `bad` yozuv va kontur; hoverda `danger-fill` fon va oq yozuv (5.4:1). Faqat tasdiqlash dialogidagi o‘chirish; boshqa joyda — `btn-text is-danger`.
- O‘lchamlar: `btn` — 17px, 44px (asosiy); `btn-sm` — 14px, 36px (telefondagi `Tile`, zich bloklar); `btn-xs` — 12px, 24px (`LocalNav`, `InfoCard`); `btn-lg` — 18px, 52px (hero va kirish oynasi). `btn-sm` va `btn-xs` ko‘rinishi kichik, bosish maydoni baribir 44px (`::before`). `btn-block` — butun kenglik.
- `link-more` — `›` li matnli havola, ikkilamchi amal uchun; hoverda `›` 3px suriladi.
- `btn-text` — ramkasiz matnli tugma (`is-danger` bilan qizil): varaq pastidagi kichik amallar.

## Qoidalar
- Balandlik kamida 44px, gorizontal ichki chegara 22px, matn 17px/400, `track-body`.
- Bosilganda `scale(.97)`, hover faqat sichqonchada. O‘chirilgan — opacity 0.4.
- Ikon matndan oldin, 16–18px, oraliq 0.4em. Jarayonda yozuv o‘rniga aylanuvchi `loader-circle` (`.spin`).
- Matn fe’l bilan, sentence case: «Saqlash», «Yuborish», «Davom etish». Foydalanuvchi o‘z nomidan bosadigan tugma birinchi shaxsda bo‘lishi mumkin: «Men olaman», «Tayyor».

## Iste’molchi beradi
Yozuv, ixtiyoriy ikon, `type` va `disabled` holati.
