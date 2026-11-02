# PageHead

Ichki sahifa sarlavhasi: eyebrow (sana), ulkan ikki qatorli sarlavha, lead va o‘ngda amallar.

## Tuzilma
```html
<header class="page-head">
  <div class="page-head-text">
    <p class="eyebrow"><span class="eyebrow-accent">29-oktabr</span> · Payshanba</p>
    <h1 class="page-title">{Qayer yoki kim}.<span class="dim">{holat jumlasi}</span></h1>
    <p class="page-lead">…</p>
  </div>
  <div class="page-actions">…</div>
</header>
```

## Qoidalar
- Sarlavha `--fs-title` (44 → 80px), 600, `track-hero`, qator 1.02. `.dim` — blok element, `fg-3`.
- Birinchi qator: qayer yoki kim («Hujjatlar.», ilova ichida «Salom, {ism}.» — faqat ism, familiyasiz). Ikkinchi qator: holatga qarab tanlangan bitta statik jumla — yozilib-o‘chmaydi va aylanib turmaydi.
- Eyebrow: sana `eyebrow-accent` (`accent-ink`) + `·` + hafta kuni.
- Amallar pastga tekislanadi; ≤640px da butun kenglikka yoyiladi.
- Ostidan odatda `Facts` (raqamlar qatori) keladi.
