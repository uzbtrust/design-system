# IconButton

Faqat ikondan iborat dumaloq 32px tugma: yopish, qidirish, tahrirlash, mavzu.

## Tuzilma
```html
<button class="icon-button" type="button" aria-label="Yopish"><svg …/></button>
```

## Variantlar
- `sheet-close` — `fill` fonli, dialog burchagidagi yopish tugmasi.
- `is-danger` — `bad` rangli ikon (havolani olib tashlash, o‘chirish).
- `theme-toggle` — ichida ikki ikon (`icon-moon`, `icon-sun`); `.dark` / `[data-theme="dark"]` da aylanib almashadi.

## Qoidalar
- `aria-label` majburiy. Ikon 16–18px, rangi `fg-2`, hoverda `fg` va `fill` fon.
- Ko‘rinmas `::before` bosish maydonini 44px ga kengaytiradi; sensorda tugmaning o‘zi 44px.
- Bosilganda `scale(.9)`.
