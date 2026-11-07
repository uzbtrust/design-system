# Topbar

Yopishqoq shisha yuqori panel: chapda wordmark, markazda bo‘limlar segmenti, o‘ngda mavzu va hisob menyusi.

## Tuzilma
```html
<header class="topbar">
  <div class="topbar-inner">
    <a class="wordmark" href="/"><svg class="wordmark-mark">…</svg><span class="wordmark-text">Loyiha</span></a>
    <nav class="topnav" aria-label="Bo‘limlar"><div class="segmented">…</div></nav>
    <div class="top-actions">
      <button class="icon-button theme-toggle">…</button>
      <div class="menu-wrap">
        <button class="account-button" aria-expanded="false"><span class="avatar">A</span></button>
        <div class="menu" role="menu">
          <div class="menu-head">…</div>
          <button class="menu-item" role="menuitem">…</button>
        </div>
      </div>
    </div>
  </div>
</header>
```

## Qoidalar
- Balandlik `nav-h` (52px), ichki eni `max`, chetlari `gutter`. Fon `glass` + `saturate(180%) blur(20px)`, pastda 1px `line-soft`.
- Wordmark: belgi 22px, nom 17px/600; ≤640px da nom yashiriladi. Standart holatda — yulduz (`<span class="uzbtrust-mark" aria-hidden="true"></span>`) va loyiha nomi, nom berilmagan bo‘lsa «uzbtrust»; foydalanuvchi o‘z logosini bersa — o‘sha (`assets/Marks` qolipi).
- `topnav` markazda absolyut turadi; ≤640px da oqimga qaytadi, yorliqlar qisqaradi (`nav-long` / `nav-short`).
- Segmentda 2–4 bo‘lim; foydalanuvchi roliga qarab o‘zgarishi mumkin.
- Menyu: 256px, `glass-solid` + blur 30px, `r-md`, `shadow-md`; 0.3s `ease-out` bilan yuqori o‘ng burchakdan ochiladi. Bandlar 42px, ikon `fg-3`.
- Statik sayt yoki hujjat sahifasida o‘ng tomonda mavzu va qidiruv qoladi; hisob menyusi faqat kirish talab qiladigan ilovada.
