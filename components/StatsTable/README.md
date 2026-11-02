# StatsTable

Statistika jadvali: har qatorda ism, bitta rangli gorizontal ustun va raqamlar. Telefonda kartalarga aylanadi.

## Tuzilma
```html
<div class="stats-table" role="table" style="--cols: minmax(150px,1.3fr) minmax(150px,1.5fr) 64px 100px 1fr">
  <div class="stats-head" role="row"><span role="columnheader">…</span>…</div>
  <div class="stats-row" role="row">
    <span class="stats-person" role="cell"><span class="avatar avatar-sm">A</span><strong>…</strong></span>
    <span class="stats-bar-cell" role="cell" data-label="Natija"><span class="stats-bar"><span style="width:64%"></span></span><span class="stats-num">27</span></span>
    <span class="stats-num" role="cell" data-label="Soni">9</span>
  </div>
</div>
```

## Qoidalar
- Ustunlar `--cols` bilan beriladi (standart: `minmax(200px, 2fr) 1fr 1fr`). Yuza `card`, `r-lg`.
- Sarlavha 44px, 12px/600 oddiy harflarda `fg-3`. Qator 64px, orasida `line-soft`.
- Ustun: 10px balandlik, `chip` izi, `accent` to‘ldirish, boshi o‘qqa yopishgan, uchi 4px yumaloq; eni eng kattasiga nisbatan. 0.8s o‘sadi.
- Raqamlar 16px/600 `tabular-nums`; past ko‘rsatkich `is-low` (`warn`). Ikkilamchi son `small` 12px `fg-3`.
- ≤860px: sarlavha yashirinadi, har qator ikki ustunli kartaga aylanadi; yorliq `data-label` dan olinadi.
- Qatorni bosib ochiladigan qilish mumkin: `stats-person is-button` + `stats-chevron`, ichida `stats-expand` (masalan, shu qatorning `BarChart`i).
