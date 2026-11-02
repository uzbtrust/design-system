# ChipButton

Kichik pill tugmalar: tezkor tanlov (`chip-button`) va yoqib-o‘chiriladigan sokin amallar (`quiet-button`).

## Tuzilma
```html
<button class="chip-button is-on" type="button" aria-pressed="true">Bugun</button>
<button class="quiet-button" type="button" aria-pressed="false">Taqdimot</button>
<kbd>⌘</kbd>
```

## Qoidalar
- `chip-button` 32px, 13px/400, `fill` fon. Yoqilganda `is-on`: `accent-soft` fon, `accent-ink` yozuv. Sensorda kamida 40px.
- `quiet-button` 32px, 14px/400 (sensorda 44px). Yoqilgan holat `aria-pressed="true"` yoki `is-on`.
- Holat doim `aria-pressed` bilan ham beriladi.
- `kbd` — klaviatura tugmasi belgisi; sensorli qurilmada yashiriladi.
