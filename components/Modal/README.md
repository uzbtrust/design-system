# Modal

Butun ekranli ma’lumot oynasi: sahifa ustida katta karta, o‘ng yuqorida yopishqoq yopish tugmasi. «Batafsil»dan ochiladigan uzun tushuntirish, galereya yoki jadval uchun. Qisqa amal va forma uchun — `Sheet`.

## Tuzilma
```html
<button class="btn btn-secondary" type="button" data-modal="m1">Batafsil</button>

<dialog class="modal" id="m1" aria-labelledby="m1-title">
  <div class="modal-frame">
    <div class="modal-bar">
      <button class="modal-close" type="button" aria-label="Yopish"><svg …x /></button>
    </div>
    <div class="modal-content">
      <p class="eyebrow">Hisobot</p>
      <h2 class="modal-title" id="m1-title">Bir yil — bir sahifada.</h2>
      <p class="copy-highlight"><strong>Asosiy gap.</strong> Kulrang davomi.</p>
      …
    </div>
  </div>
</dialog>
```

## Qoidalar
- Native `<dialog>`, `showModal()` bilan ochiladi: Escape yopadi, fokus oyna ichida qoladi va yopilgach tugmaga qaytadi. Ochiq paytda sahifa skroll qilinmaydi.
- Parda `backdrop` + `blur(6px)`. Karta `bg-elev`, `r-xl`, `shadow-lg`, eni `max-wide` gacha, tepa-pastdan 48px (`s-7`); uzun kontent oyna ichida suriladi.
- Yopish tugmasi 36px doira, `control-bg`, ikon `x` `fg`, bosish maydoni 44px; kontent surilganda ham o‘ng yuqorida turadi.
- Ichi: eyebrow → `modal-title` (`--fs-h1`, 600, `track-hero`) → `copy-highlight` → kontent (`Gallery`, `Specs`, rasm). Ichki chegara 96px (`s-9`) va yon tomondan 24–120px.
- Kirish: 14px pastdan va 0.965 masshtabdan 0.5s `ease-out` (`02-harakat` → Dialog).
- ≤734px: karta butun ekranni egallaydi, burchaklarsiz.

## Iste’molchi beradi
Ochuvchi tugma, sarlavha (`aria-labelledby` uchun `id`), kontent va ochish/yopish skripti (`showModal()`, `close()`).
