# LocalNav

Sahifa yoki mahsulot ichidagi yopishqoq navigatsiya: chapda sahifa nomi, o‘ngda bo‘limlar va bitta kichik asosiy amal.

## Tuzilma
```html
<nav class="localnav" aria-label="Hisobot bo‘limlari">
  <div class="localnav-inner">
    <a class="localnav-title" href="#top">Hisobot 2026</a>
    <ul class="localnav-links" id="ln-links">
      <li><a class="localnav-link" aria-current="page">Umumiy</a></li>
      <li><a class="localnav-link" href="#raqamlar">Raqamlar</a></li>
    </ul>
    <button class="localnav-toggle" type="button" aria-label="Bo‘limlar" aria-expanded="false" aria-controls="ln-links"><svg …chevron-down /></button>
    <a class="btn btn-primary btn-xs" href="…">Yuklab olish</a>
  </div>
</nav>
```

## Qoidalar
- Balandlik `nav-h` (52px), telefonda 48px; `position: sticky; top: 0`. Fon `glass-nav` + blur, pastda 1px `line-soft`. Ichki eni `max-narrow` + 22px chetlar.
- Sarlavha 21px/600 (`text-nav-title`, `track-intro`), telefonda 19px. Odatda `GlobalNav` dan keyin keladi.
- Havolalar 12px `fg`, oraliq 24px, hoverda `accent-ink`. Joriy bo‘lim havola emas: `aria-current` va `fg-3`.
- O‘ngda faqat bitta amal: `btn btn-primary btn-xs` (12px, 24px balandlik, bosish maydoni 44px). Ikkinchi amal kerak bo‘lsa — havola sifatida ro‘yxatga.
- ≤734px: havolalar yashirinadi, `chevron-down` tugmasi chiqadi; bosilganda `.localnav` ga `is-open`, havolalar panel bo‘lib pastga ochiladi (17px, qatorlar orasida `line-soft`), chevron 180° buriladi.
- Qorong‘u band ustida — `data-theme="dark"`.

## Iste’molchi beradi
Sahifa nomi, 2–5 bo‘lim havolasi (ankerlar), joriy bo‘lim, bitta amal va telefondagi ochish/yopish skripti.
