# BarChart

Kunlik ustunli grafik: bitta o‘lchov — bitta rang. Har ustunga kursor olib borilsa, kun va son chiqadi.

## Tuzilma
```html
<figure class="chart">
  <figcaption class="chart-head"><span><strong>Sarlavha</strong><small>Jami · davr</small></span><span class="chart-best">Eng ko‘p: …</span></figcaption>
  <div class="chart-body">
    <div class="chart-y"><span>6</span><span>3</span><span>0</span></div>
    <div class="chart-plot">
      <span class="chart-gridline" style="bottom:100%"></span><span class="chart-gridline" style="bottom:50%"></span>
      <div class="chart-bars" style="grid-template-columns:repeat(14,minmax(0,1fr))">
        <button class="chart-bar" style="--h:66%" aria-label="…"><span class="bar-fill"></span></button> …
      </div>
    </div>
  </div>
  <div class="chart-x" style="grid-template-columns:repeat(14,minmax(0,1fr))"><span>…</span>…<span>Bugun</span></div>
</figure>
```

## Qoidalar
- Yuza `card`, `r-lg`; balandlik 180px (≤640px da 150px). Ustunlar `accent`, faqat yuqori burchaklari 4px yumaloq; nol qiymat — 2px `chip` chiziq.
- Y o‘qi «yaxshi» maksimumga yaxlitlanadi (1, 2, 4, 6, 8, 10 × 10ⁿ): 0, o‘rtasi va tepa. To‘r chizig‘i `line-soft`, o‘q `line`.
- Hover/fokusda boshqa ustunlar 0.45 shaffoflikka tushadi; izoh (`chart-tip`, `tooltip-bg`) ustun tepasida, sarlavhani yopmaydi (`bottom: calc(min(78%, h) + 10px)`). Chetlarda chapga/o‘ngga suriladi.
- X o‘qida har ikkinchi (ko‘p kunda — har oltidan biri) sana; oxirgisi «Bugun» `accent-ink` 600.
- 45 dan ortiq ustunda oraliq 1px (`is-dense`). Har ustun `aria-label` bilan to‘liq qiymatni aytadi.
- Bir nechta seriya kerak bo‘lsa: `data-1`, `data-2`, `data-3` (README → Rang).
