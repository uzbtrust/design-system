# DatePicker

Sana tanlash: tugma, tezkor chiplar va ostida ochiladigan kichik kalendar. Qo‘lda sana yozdirilmaydi.

## Tuzilma
```html
<div class="datepicker">
  <div class="date-row">
    <button class="date-trigger has-value" aria-expanded="true"><svg …/><span>3-noyabr, 2026</span></button>
    <button class="icon-button date-clear" aria-label="Sanani olib tashlash">…</button>
    <div class="quick-dates"><button class="chip-button is-on" aria-pressed="true">Bugun</button>…</div>
  </div>
  <div class="calendar" role="dialog" aria-label="Kalendar">
    <div class="cal-head"><button class="icon-button">‹</button><strong>Oktabr 2026</strong><button class="icon-button">›</button></div>
    <div class="cal-grid"><span class="cal-weekday">Du</span>…<button class="cal-day is-today">29</button>…</div>
  </div>
</div>
```

## Qoidalar
- Tugma 46px, `fill` fon; qiymat bo‘lsa `has-value` (`fg`, 500). Ochiqligida maydon kabi ko‘k halqa.
- Tezkor sanalar: Bugun, Ertaga, 3 kun, 1 hafta. Qayta bosish tanlovni bekor qiladi.
- Kalendar 320px gacha, `bg-elev`, `r-md`, `shadow-md`; 0.35s ochiladi. Hafta dushanbadan; Sh va Ya `fg-4`.
- Kun — dumaloq; bugun `accent-ink` 600; tanlangan `accent-fill` fon, oq matn; o‘tgan kunlar o‘chirilgan (o‘tmish sanasi kerak bo‘lmasa).
- Sana formati: «3-noyabr, 2026»; oy nomi sarlavhada bosh harf bilan.
