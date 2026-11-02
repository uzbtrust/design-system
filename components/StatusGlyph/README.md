# StatusGlyph

Jarayon holatining shakli: bo‘sh doira → yarim → nuqtali doira → belgi → ✕. Rang emas, shakl o‘zgaradi.

## Tuzilma
```html
<svg class="glyph glyph-in_progress" viewBox="0 0 24 24" aria-hidden="true">
  <circle class="glyph-ring" cx="12" cy="12" r="10" />
  <path class="glyph-half" d="M12 5.5a6.5 6.5 0 0 0 0 13Z" />
  <circle class="glyph-dot" cx="12" cy="12" r="4" />
  <circle class="glyph-fill" cx="12" cy="12" r="10" />
  <path class="glyph-mark" d="m7.6 12.3 3 3 5.8-6.3" />
  <path class="glyph-cross" d="m8.5 8.5 7 7m0-7-7 7" />
</svg>
```

## Holatlar
- `glyph-todo` — `fg-4` doira (ochiq). `glyph-in_progress` — chap yarmi to‘lgan. `glyph-in_review` — nuqtali doira. `glyph-done` — to‘liq `accent` doira, oq belgi chiziladi. `glyph-cancelled` — ✕, qator nomi chizib qo‘yiladi.
- O‘tish: to‘ldiruvchi 0.45s `--ease-spring` bilan kattalashadi, belgi 0.35s da chiziladi.
- Belgi dekor (`aria-hidden`); holat nomi yonida `sr-only` yoki teg bilan yoziladi.
- Har qanday bosqichli jarayon uchun: vazifa, buyurtma, hujjat, bob o‘qilishi. Hujjat va PDF'da statik SVG sifatida ishlatiladi.
