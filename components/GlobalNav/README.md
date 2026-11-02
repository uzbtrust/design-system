# GlobalNav

Saytning eng yuqori navigatsiyasi (apple.com globalnav uslubida): chapda uzbtrust yulduzi, o‘rtada bo‘limlar teng taqsimlangan, o‘ngda qidiruv. Sayt va hujjat sahifalari uchun; ilova ichida — `Topbar`.

## Tuzilma
```html
<nav class="globalnav" aria-label="Asosiy">
  <div class="globalnav-inner">
    <a class="globalnav-brand" href="/"><img src="assets/Logos/uzbtrust-star.png" alt="uzbtrust" width="18" height="18"></a>
    <ul class="globalnav-list" id="gn-list">
      <li><a class="globalnav-link" href="…" aria-current="page">Bosh sahifa</a></li>
      <li><a class="globalnav-link" href="…">Loyihalar</a></li>
      …
    </ul>
    <div class="globalnav-actions">
      <button class="globalnav-icon" type="button" aria-label="Qidirish"><svg …search /></button>
      <button class="globalnav-icon globalnav-menu" type="button" aria-label="Menyu" aria-expanded="false" aria-controls="gn-list">
        <svg viewBox="0 0 24 24" …><path class="line line-1" d="M4 8.5h16" /><path class="line line-2" d="M4 15.5h16" /></svg>
      </button>
    </div>
  </div>
</nav>
```

## Qoidalar
- Balandlik `globalnav-h` (44px), telefonda 48px. Fon `glass-nav` + `saturate(180%) blur(20px)`, pastki chiziqsiz. Ichki eni `max-narrow` (980px) + 22px chetlar.
- Havolalar 12px (`text-footnote`), `fg-2`; hoverda va joriy sahifada (`aria-current="page"`) — `fg`. 5–8 bo‘lim, har biri bir-ikki so‘z.
- Yulduz 18px — `assets/Logos/uzbtrust-star.png`, rangi o‘zgarmaydi, hoverda opacity 0.72. Mahsulot saytida yulduz o‘rniga mahsulot belgisi (`assets/Marks` qolipi).
- Yopishqoq emas — sahifa bilan birga ketadi. Yopishqoq ikkinchi qator — `LocalNav`.
- ≤833px: ro‘yxat yashirinadi, ikki chiziqli menyu tugmasi chiqadi. Bosilganda `.globalnav` ga `is-open` va `aria-expanded="true"`: chiziqlar «×» ga aylanadi, ro‘yxat ekranni egallaydi, havolalar 28px/600 (`track-eyebrow`). Escape yopadi va fokusni tugmaga qaytaradi.
- Qorong‘u sahifa yoki qorong‘u hero ustida: `<nav class="globalnav" data-theme="dark">` — mavzu oroli.

## Iste’molchi beradi
Bo‘limlar ro‘yxati, joriy bo‘lim, qidiruv amali va menyu tugmasi skripti (`is-open` hamda `aria-expanded` ni almashtirish).
