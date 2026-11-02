# Accordion

Ochiladigan savol-javob ro‘yxati (FAQ): savol qatori va «+» belgisi, bosilganda javob ochiladi, «+» esa «−» ga aylanadi. Native `<details>` asosida.

## Tuzilma
```html
<div class="accordion">
  <details class="accordion-item" name="faq">
    <summary class="accordion-head">
      <span>Tizimni qanday ulayman?</span>
      <svg class="accordion-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" aria-hidden="true"><path d="M5 12h14" /><path class="v" d="M12 5v14" /></svg>
    </summary>
    <div class="accordion-body"><p>…</p></div>
  </details>
</div>
```

## Qoidalar
- Eni `max-narrow`; qatorlar orasida va tepada 1px `line`.
- Savol 19 → 24px/600 (`track-title`), qator ichki chegarasi 20px. Belgi 20px `fg-3`, hoverda `fg`; ochilganda tik chiziq 0.45s `ease-out` bilan yo‘qoladi.
- Javob 17px `fg-3` (`text-body`), eni 44em gacha, o‘ngdan 48px bo‘sh. Ochilishda 6px pastga siljib paydo bo‘ladi. Havolalar `accent-ink`.
- `name="faq"` — bir vaqtda bitta javob ochiq turadi (zamonaviy brauzerlarda); kerak bo‘lmasa olib tashlang.
- Savol — to‘liq jumla, so‘roq belgisi bilan; javob birinchi jumlada aniq javob beradi.
- Fokus: `summary` ichki 2px `accent` halqa. Bosh sahifadagi FAQ odatda `band` ichida, `band-head` sarlavhasi bilan.
- Chopda: barcha savollarni ochiq holda chiqaring (`details` ga `open`).

## Iste’molchi beradi
Savol va javoblar, ixtiyoriy `open` (birinchi savol ochiq turishi uchun).
