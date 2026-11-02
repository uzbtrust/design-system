# Field

Forma maydoni: yorliq, kiritish va izoh. Chegarasiz, `fill` fonli, fokusda ko‘k halqa.

## Tuzilma
```html
<label class="field">
  <span class="field-label">Nomi <span class="optional">ixtiyoriy</span></span>
  <input class="input" />
  <span class="field-hint">Izoh</span>
</label>
<span class="select-wrap"><select class="input">…</select><svg …/></span>
```

## Qoidalar
- `input`: 46px, `r-sm`, `fill` fon, 17px. Fokusda `bg-elev` fon, ichki 1.5px `accent` va tashqi 4px `accent-soft`.
- `input-lg` (52px, 20px/500) — formaning asosiy maydoni (nom). `textarea.input` 112px dan, vertikal o‘lchanadi.
- Yorliq 13px/600 `fg-2`; ixtiyoriy belgisi `optional` (`fg-3`, 400). Majburiy maydonga yulduzcha qo‘yilmaydi — ixtiyoriylari belgilanadi.
- Izoh 13px `fg-3`; ogohlantirish `tone-warn` (500). Xato forma ostida `error-message`.
- Maydonlar orasi 18–20px.
