# Sheet

Varaq ko‘rinishidagi dialog: sarlavha, aylanadigan tana va pastda amallar. Telefonda pastdan chiqadi.

## Tuzilma
```html
<dialog class="sheet" aria-labelledby="t">        <!-- sheet-sm (440px) · sheet (560px) · sheet-lg (720px) -->
  <div class="sheet-head">
    <div><p class="eyebrow">Turi · #012</p><h2 id="t">Sarlavha</h2></div>
    <button class="icon-button sheet-close" aria-label="Yopish"><svg …/></button>
  </div>
  <div class="sheet-body">
    <dl class="props"><div class="prop"><dt>Kalit</dt><dd>Qiymat</dd></div></dl>
    <section class="sheet-section"><h3 class="sheet-section-title">Bo‘lim</h3>…</section>
  </div>
  <div class="sheet-foot">…amallar…</div>
</dialog>
```

## Xulq
- `showModal()` bilan ochiladi; fokus birinchi maydonga o‘tadi (forma bo‘lsa), yopilganda oldingi elementga qaytadi.
- Escape, parda ustiga bosish yoki ✕ yopadi. Yopilishda `is-closing` (0.18s), keyin olib tashlanadi. Ichma-ich dialogda faqat yuqoridagisi yopiladi (`e.target` tekshiriladi).
- Ochilish: 14px pastdan va 0.965 dan 0.5s `--ease-out`; parda `backdrop` + `blur(6px)`. Orqa sahifa aylanmaydi (`html:has(dialog[open])`).
- ≤640px: butun kenglik, yuqori burchaklar 26px, pastdan siljib chiqadi; pastki amallar teng kenglikka yoyiladi.

## Qoidalar
- Yuza `bg-elev`, radius 28px, `0 0 0 1px line-soft` + `shadow-lg`. Ichki guruhlar `sheet-card` + `r-md`.
- Sarlavha 24 → 28px/600. Eyebrow — tur va raqam.
- `props` — kalit/qiymat ro‘yxati: kalit `fg-3`, qiymat 500 o‘ngda; `tone-warn` / `tone-bad` ma’no uchun.
- Pastda: chapda xavfli `btn-text is-danger`, o‘ngda `btn-quiet` + bitta `btn-primary`.
