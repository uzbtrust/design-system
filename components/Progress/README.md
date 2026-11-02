# Progress

Jarayonning ikki ko‘rinishi: bosqichlar chizig‘i (`steps`) va voqealar tarixi (`timeline`).

## Tuzilma
```html
<ol class="steps" style="grid-template-columns: repeat(3, 1fr)" aria-label="Bosqich">
  <li class="is-done"><span class="step-dot"><svg …/></span><span class="step-label">Qoralama</span></li>
  <li class="is-current" aria-current="step"><span class="step-dot">2</span><span class="step-label">…</span></li>
  <li><span class="step-dot">3</span><span class="step-label">…</span></li>
</ol>
<ol class="timeline">
  <li><span class="timeline-dot"></span><p><strong>Kim</strong> nima qildi<time>29-okt, 14:05</time></p><p class="timeline-message">…</p></li>
</ol>
```

## Qoidalar
- Bosqich: tepada 3px chiziq (`chip`; o‘tilgan va joriysi `accent`), 20px raqamli doira (o‘tilgan va joriysi `accent-fill`, oq raqam), 13px yorliq. Joriysi `fg` 600. Bekor qilinsa `steps is-cancelled` — hammasi 0.45 shaffof.
- Tarix: yangisi tepada; birinchi nuqta `accent`, qolganlari `fg-4`; nuqtalar `line` chiziq bilan ulangan. Vaqt 12px `fg-3` `tabular-nums`. Izoh `fg-2`.
- Bo‘lim sarlavhasi `sheet-section-title`: 13px/600, oddiy harflarda, `track-caption`.
