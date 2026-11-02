# Ribbon

Sahifa tepasidagi bir qatorli e’lon tasmasi: bitta jumla va `›` li havola. Yangi hisobot, muddat yoki muhim o‘zgarish haqida.

## Tuzilma
```html
<aside class="ribbon" aria-label="E’lon">
  <p class="ribbon-text">2026-yil hisoboti endi PDF'da ham bor. <a class="link-more" href="…">Yuklab olish</a></p>
</aside>
```

## Qoidalar
- `GlobalNav` dan oldin, sahifaning eng tepasida. Bir sahifada bitta.
- Fon `bg-alt`, matn 14px (`text-sm`) `fg`, markazda, `text-wrap: balance`. Ichki chegara 14px va `gutter`.
- Havola — `link-more` (`accent-ink`, `›`), matn bilan bir qatorda.
- Ikon, yopish tugmasi, rangli fon va harakat yo‘q. Xato yoki ogohlantirish uchun emas — ular `Notice` / `banner`.
- Qorong‘u hero ustida: `data-theme="dark"` (fon `bg-alt` → #111113).

## Iste’molchi beradi
Bitta jumla va bitta havola.
