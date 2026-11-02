# Stepper

Son kiritish: minus, katta raqam va plus bitta pill ichida.

## Tuzilma
```html
<div class="stepper" role="group" aria-label="Soni">
  <button aria-label="Kamaytirish"><svg …/></button>
  <input type="number" inputmode="numeric" value="3" />
  <button aria-label="Ko‘paytirish"><svg …/></button>
  <span class="stepper-unit">ta</span>
</div>
```

## Qoidalar
- Pill `fill` fon, 3px ichki chegara. Tugmalar 40px doira, `bg-elev` va yengil soya; chegaradagi tugma `disabled` (0.35).
- Raqam 22px/600, `tabular-nums`, markazda; brauzer strelkalari yashirilgan. Birlik 15px `fg-3`.
- Fokusda butun guruhga 3px `accent-soft` halqa.
