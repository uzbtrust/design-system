# Hero

Markazlashgan katta kirish bloki: eyebrow, ikki qatorli ulkan sarlavha (ikkinchisi kulrang), lead va amallar. Bosh sahifa, kirish oynasi, hujjat yoki taqdimot muqovasi uchun.

## Tuzilma
```html
<div class="login">
  <section class="hero wrap">
    <p class="eyebrow hero-eyebrow">Kim uchun yoki qachon</p>
    <h1 class="hero-title">Asosiy fikr.<span class="hero-dim dim">Bir jumlali davomi.</span></h1>
    <p class="hero-lead">Bir-ikki qatorli tushuntirish.</p>
    <div class="hero-actions"><button class="btn btn-primary btn-lg">…</button><a class="link-more">…</a></div>
  </section>
</div>
```

## Qoidalar
- Sarlavha `--fs-hero` (44 → 96px), 600, `track-hero`, qator balandligi 1.04. Birinchi qator nuqta bilan tugaydi; ikkinchi qator `.dim` (`fg-3`).
- Eyebrow 14px, harf oralig‘i 0.05em. Lead `--fs-lead`, `fg-3`, eni 30–34em, `text-wrap: balance`.
- Fon toza `bg` (yoki `bg-alt` bandi) — gradient va rangli nur yo‘q.
- Kirish: `.rise` zinapoyasi (`--i` = 0, 1, 2, 3; 70ms qadam).
- Chop etiladigan hujjat muqovasida: sarlavha 26pt chapga tekislangan, tugmalar yo‘q (README → Hujjat va PDF).
