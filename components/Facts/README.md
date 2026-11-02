# Facts

Katta raqamlar qatori: sarlavha ostida asosiy ko‘rsatkichlar. Ilovada bosilganda ro‘yxatni saralaydi; hujjat va slaydda oddiy raqam bloki.

## Tuzilma
```html
<div class="facts" role="group" aria-label="Saralash">
  <button class="fact is-active" aria-pressed="true"><span class="fact-num">24</span><span class="fact-label">Jami</span></button>
  <button class="fact is-bad">…</button>
</div>

<!-- statik variant: hujjat, slayd, bosh sahifa -->
<ul class="stat-list"><li class="stat"><span class="stat-num">12</span><span class="stat-label">loyiha</span></li></ul>
```

## Qoidalar
- `fact-num`: 36 → 52px, 600, `track-display`, `tabular-nums`; raqam qanday bo‘lsa shunday (4, 24). Yorliq 13px `fg-3`.
- Tepada 1px `line` va 26px oraliq. Oraliq 28–72px; ≤520px da ikki ustunli to‘r.
- Holatlar: `is-active` — raqam va yorliq `accent-ink`; `is-bad` — raqam `bad`; `disabled` — raqam `fg-4` (nol). Hoverda raqam `accent`.
- Raqam darhol ko‘rsatiladi; sanab chiqish faqat marketing sahifasida, skroll bilan.
- `stat-list` — bosh sahifadagi markazlashgan uch ulkan raqam (40 → 96px), `bg-alt` bandi ichida.
