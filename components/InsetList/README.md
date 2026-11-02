# InsetList

Guruhlangan «inset» ro‘yxat: kulrang yuza ichida qatorlar, chapda holat belgisi, o‘ngda meta va chevron.

## Tuzilma
```html
<section class="group">
  <h2 class="group-head">Jarayonda <span class="group-count">3</span></h2>
  <ul class="inset-list">
    <li class="list-row is-in_progress">
      <span class="row-glyph"><svg class="glyph glyph-in_progress">…</svg></span>
      <button class="row-open" type="button">
        <span class="row-main"><span class="row-title">…</span><span class="row-desc">…</span></span>
        <span class="row-meta">…teglar, muddat, son…</span>
        <svg class="row-chevron" …/>
      </button>
    </li>
  </ul>
</section>
```

## Qoidalar
- Yuza `card`, `r-lg`, `overflow: hidden`. Qator kamida 68px; ajratuvchi `line-soft` chapdan 60px dan boshlanadi.
- Butun qator bosiladi (`row-open::after` qatorni qoplaydi). Fokusda ichki 2px `accent` halqa.
- Nomi `text-row` (17px/400), bir qatorda `…` bilan qisqaradi; izoh 14px `fg-3`. Qaytarilgan ish izohi `is-returned` (`warn`).
- Holatlar: `is-done` — nom `fg-3`; `is-cancelled` — nom chizilgan; `is-in_review` — nom 600.
- Hover: `row-hover` fon, chevron `fg-3` va 2px o‘ngga.
- ≤719px da meta nom ostiga tushadi, chevron o‘ngda markazda qoladi.
- Guruh sarlavhasi 20 → 24px/600, yonida son `fg-3` va ixtiyoriy izoh (`group-hint`). Guruhlar orasi 36–52px.
- Dialog ichida qator 60px, nom 16px, yuza `sheet-card`.
- Sozlamalar, fayllar, kontaktlar, mundarija — har qanday ro‘yxat uchun. Holat belgisi kerak bo‘lmasa `row-glyph` o‘rniga ikon yoki avatar qo‘yiladi.
