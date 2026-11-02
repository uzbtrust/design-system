# ChapterNav

Ikonli bo‘limlar qatori: har bo‘lim — katta ikon yoki kichik rasm va ostida nomi. Sayt bo‘limi yoki mahsulotlar oilasi boshida, `LocalNav` ostida.

## Tuzilma
```html
<nav class="chapternav" aria-label="Bo‘limlar">
  <ul class="chapternav-items">
    <li><a class="chapternav-link" href="…" aria-current="page">
      <span class="chapternav-icon"><svg …stroke-width="1.5" /></span>
      <span class="chapternav-label">Umumiy</span>
    </a></li>
    <li><a class="chapternav-link" href="…">
      <span class="chapternav-icon"><svg … /></span>
      <span class="chapternav-new">Yangi</span>
      <span class="chapternav-label">Shablonlar</span>
    </a></li>
  </ul>
</nav>
```

## Qoidalar
- Bandlar markazda, oraliq 20px; sig‘masa gorizontal suriladi (skroll chizig‘i ko‘rinmaydi), sahifa yonga surilmaydi. Pastda 32px (`s-6`) bo‘sh joy.
- Ikon maydoni 64px balandlikda: Lucide ikoni 36px, chiziq 1.5, `currentColor`; yoki ≤64px balandlikdagi rasm (`<img>`, `alt=""` — nom ostida yozilgan).
- Nom 14px/600 (`text-sm`), `fg-2`, bir qatorda; hoverda `fg`. Joriy bo‘lim — `aria-current`: nom `fg`, ikon `accent-ink`.
- «Yangi» — `chapternav-new` (12px/600, `new` rangi) nom ustida, butun qatorda bittadan ko‘p emas.
- 4–9 band. Har band bir-ikki so‘z.

## Iste’molchi beradi
Bo‘limlar (nom, havola, ikon yoki rasm), joriy bo‘lim, ixtiyoriy «Yangi» belgisi.
