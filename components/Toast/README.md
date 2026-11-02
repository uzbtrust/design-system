# Toast

Ekran tepasidan tushadigan bildirishnoma banneri (iOS bildirishnomasi kabi): bitta jumla va ixtiyoriy bitta amal.

## Tuzilma
```html
<div class="toast-region" aria-live="polite">
  <div class="toast" role="status"><svg …/><span class="toast-text">Saqlandi</span><button class="toast-action">Qaytarish</button></div>
</div>
```

## Qoidalar
- Tepada markazda, `glass-solid` + `saturate(180%) blur(30px)`, `r-md`, `0 0 0 1px line-soft` + `shadow-md`. Balandligi 56px, matn 15px `fg`.
- Ikon: muvaffaqiyat `good`, xato (`is-error`) `bad`. Matn bir qatorda, 44ch gacha.
- Amal — ko‘k matnli tugma (`accent-ink`), hoverda `fill`.
- Yuqoridan 16px pastga va 0.96 dan 0.5s `--ease-out` bilan tushadi, bir necha soniyadan keyin yo‘qoladi. Bir vaqtda bitta bildirishnoma.
- Muhim xato bannerda emas, joyida (`Notice` / `error-message`) ko‘rsatiladi.
