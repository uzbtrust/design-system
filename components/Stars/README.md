# Stars

Muhimlik yoki baho: 1–5 yulduz. Ro‘yxatda kichik ko‘rsatkich, formada tanlagich.

## Tuzilma
```html
<span class="stars" role="img" aria-label="Muhimlik: 3 yulduz"><svg class="on" …/>…</span>
<div class="star-picker" role="group" aria-label="Muhimlik">
  <button aria-pressed="false" aria-label="1 yulduz" class="on"><svg …/></button> …
  <span class="star-picker-value">3 / 5</span>
</div>
```

## Qoidalar
- Yoqilgan yulduz `star` rangida (to‘ldirilgan), o‘chig‘i `fg-4` (kontur). Ro‘yxatda 12px, tanlagichda 24px tugmalar 40px.
- Tanlangan yulduzni qayta bosish bahoni olib tashlaydi. Hover oldindan ko‘rsatadi.
- `star` — App Store kabi kulrang (`fg-2`), fonda 9:1 dan yuqori. Yoqilgan va o‘chiq yulduz shakl bilan ajraladi: to‘ldirilgan va kontur. Shunga qaramay qiymat doim matn bilan ham yoziladi («3 / 5», `aria-label`).
