# Segmented

Sirpanuvchi indikatorli segmentli tanlov: bo‘limlar, filtr yoki rejim orasidan bittasi.

## Tuzilma
```html
<div class="segmented" role="group" aria-label="Bo‘limlar">
  <span class="segmented-ind" aria-hidden="true"></span>
  <button type="button" aria-pressed="true">Umumiy</button>
  <button type="button" aria-pressed="false">Hujjatlar <span class="seg-count">3</span></button>
</div>
```

## Xulq
- Indikator (`segmented-ind`) faol tugmaning `offsetLeft` / `offsetWidth` iga qarab joylashadi. O‘lchangach ildizga `is-measured`, keyingi kadrda `is-animated` qo‘shiladi — birinchi chizilishda indikator «uchib kelmaydi».
- Kenglik 0 bo‘lsa (yopiq dialog ichida), o‘lchanmaydi: CSS zaxirasi faol tugmaning o‘ziga `seg-thumb` fon beradi.
- Hisoblagich o‘zgarsa, tugma eni o‘zgaradi — qayta o‘lchang (`ResizeObserver`).
- Sirpanish: 0.45s `--ease-out` (transform + width).

## Variantlar
- Oddiy: 30px, 13px. Yuqori panelda (`.topnav`) 14px va 18px chegara.
- `segmented-block` — butun kenglik, teng ustunlar, 34px (kirish oynasi).
- `seg-count` — tugma ichidagi `fg-3` son.

## Iste’molchi beradi
Variantlar ro‘yxati, tanlangan qiymat va `aria-label`.
