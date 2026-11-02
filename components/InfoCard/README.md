# InfoCard

Statik ma’lumot kartasi: sarlavha, bir-ikki jumlali tavsif va pastda bitta kichik amal. Yuklab olinadigan narsalar, shablonlar va resurslar ro‘yxati uchun.

## Tuzilma
```html
<div class="info-grid">
  <article class="info-card">
    <h3 class="info-title">Hisobot</h3>
    <p class="info-text">Yillik va choraklik hisobot qolipi…</p>
    <a class="btn btn-primary btn-xs" href="…">Yuklab olish</a>
  </article>
  …
</div>
```

## Qoidalar
- To‘r: 2 ustun, oraliq 20px, eni `max-narrow` (980px); ≤734px da 1 ustun, oraliq 12px.
- Yuza `card` (yorug‘da `bg-alt`, qorong‘uda `bg-elev`), `r-md`, chegarasiz va soyasiz — butun karta bosilmaydi, faqat tugma.
- Ichki chegara 21 / 28 / 28px. Sarlavha 24px/600 (`text-group`, `track-title`), tavsif 14px (`text-sm`) `fg`, 4 qatorgacha.
- Amal pastga tekislanadi (`margin-top: auto`), shuning uchun qatordagi tugmalar bir chiziqda turadi: `btn btn-primary btn-xs` yoki `link-more`.
- Bosiladigan, hoverda ko‘tariladigan karta kerak bo‘lsa — `Card`.

## Iste’molchi beradi
Sarlavha, qisqa tavsif va bitta amal (havola yoki yuklab olish manzili).
