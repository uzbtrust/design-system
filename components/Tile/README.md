# Tile

Sayt bosh sahifasining promo bloki: tepada markazda sarlavha, bir qatorli davomi, ikki tugma, ostida katta rasm yoki vizual. Bitta katta (`tile-hero`) va ikki ustunli kichiklar.

## Tuzilma
```html
<section class="tile-grid">
  <article class="tile tile-hero" data-theme="dark">
    <div class="tile-copy">
      <p class="eyebrow eyebrow-new">Yangi</p>
      <h2 class="tile-title">Yil yakunlari.</h2>
      <p class="tile-sub">Kam so‘z, aniq raqam.</p>
      <div class="tile-ctas">
        <a class="btn btn-primary" href="…">Batafsil</a>
        <a class="btn btn-secondary" href="…">Yuklab olish</a>
      </div>
      <p class="tile-callout">PDF · 24 sahifa</p>
    </div>
    <div class="tile-media"><img src="…" alt="…" /></div>
  </article>
  <article class="tile">…</article>
  <article class="tile" data-theme="dark">…</article>
</section>
```

## Qoidalar
- To‘r: tile'lar orasida 12px (`s-3`), chetlarda 12px; `tile-hero` butun kenglikda, chetsiz. Burchaklar to‘g‘ri (radius 0); telefonda bitta ustun.
- Katta tile: balandligi 692px, tepadan 56px; sarlavha `text-tile` (`--fs-tile` 32 → 56px, `track-tile`), davomi 19 → 28px (`track-eyebrow`). Kichik tile: 580px, tepadan 53px; sarlavha `text-tile-sm` (32 → 40px), davomi `text-intro`.
- Fon: yorug‘ tile — `bg-alt`, katta tile — `bg`; qorong‘u tile — `data-theme="dark"` (fon `bg`, ya’ni #000). Yorug‘ va qorong‘u tile'lar navbatma-navbat keladi.
- Tugmalar: `btn-primary` + `btn-secondary` (17px, 44px), telefonda 14px/36px. Ikkitadan ko‘p emas; bittasi bo‘lishi mumkin.
- `eyebrow-new` («Yangi», `new` rangi) — faqat haqiqatan yangi narsa uchun, sahifada bittadan. `tile-callout` — muddat yoki format, `fg-3`.
- Vizual: rasm, video yoki tizim tokenlari bilan chizilgan grafik (`data-1`). Matn ustiga chiqmaydi, pastga tekislanadi. Gradient va soya yo‘q.
- Kirish harakati faqat bosh sahifada: `.rise` (`02-harakat`).

## Iste’molchi beradi
Sarlavha, bir qatorli davomi, 1–2 amal (havola manzili bilan), ixtiyoriy `tile-callout` va vizual (rasm uchun `alt`).
