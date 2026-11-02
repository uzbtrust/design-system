# Card

Bosiladigan karta: kichik eyebrow yoki haqiqiy ko‘rsatkich, sarlavha, qisqa izoh va meta. Bo‘lim, hujjat, odam yoki loyiha uchun.

## Tuzilma
```html
<div class="card-item">
  <a class="card-tile" href="…">
    <div class="card-top">
      <p class="eyebrow">Turi</p>                 <!-- yoki haqiqiy ko‘rsatkich: <span class="card-num">94%</span> -->
      <span class="card-arrow"><svg …/></span>
    </div>
    <div class="card-body"><h3 class="card-title">…</h3><p class="card-lead">…</p></div>
    <div class="card-foot">
      <div class="card-meta"><span>24 sahifa</span><span>6 grafik</span></div>
      <div class="card-tags"><span class="tag">…</span></div>
    </div>
  </a>
</div>
```

## Qoidalar
- Yuza `card` (yorug‘da `bg-alt`), `r-lg`, chegarasiz. Ichki chegara 28px, ≤599px da 22–24px.
- Tepada — kichik `eyebrow` (tur, bo‘lim) yoki haqiqiy ko‘rsatkich `card-num` (56 → 72px, 600): son, foiz, soat. Tartib raqami (01, 02) bezak sifatida yozilmaydi.
- Sarlavha 22 → 26px/600, `track-title`; izoh 15px `fg-3`, 2 qatorgacha. Meta 13px `fg-3`, `·` bilan ajraladi.
- Hover: `bg-elev` (qorong‘uda #232325), `shadow-md`, −4px; ko‘rsatkich `accent`; strelka doirasi `accent` fon va oq ikon. Bosish `scale(.98)`.
- To‘r: 1 → 2 → 3 ustun (600 / 960px), oraliq 16 → 20px. Yolg‘iz karta 640px dan keng bo‘lsa, yuqori qism chapga, matn o‘ngga o‘tadi.
- Hujjat va slaydda: hover va strelka yo‘q; chopda (`print`) fon o‘rniga 1px chiziq.
