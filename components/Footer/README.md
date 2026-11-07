# Footer

Sayt pastki qismi: izohlar, bo‘limlar xaritasi va huquqiy qator. Hammasi 12px, kulrang, `bg-alt` fonda.

## Tuzilma
```html
<footer class="sitefoot">
  <div class="sitefoot-inner">
    <ol class="footnotes"><li>Ma’lumotlar 2026-yil oktabr holatiga.</li></ol>
    <nav class="sitefoot-dir" aria-label="Sayt xaritasi">
      <div class="sitefoot-col">
        <h3 class="sitefoot-title">Loyihalar</h3>
        <ul><li><a href="…">…</a></li></ul>
      </div>
      …
    </nav>
    <div class="sitefoot-legal">
      <p class="sitefoot-copy">© 2026 Loyiha nomi.</p>
      <ul class="sitefoot-links"><li><a href="…">Maxfiylik</a></li><li><a href="…">Shartlar</a></li></ul>
      <a class="signature" href="https://github.com/uzbtrust/design-system"><span class="uzbtrust-mark" aria-hidden="true"></span>Dizayn: <strong>Abdurakhmonov</strong></a>
      <p class="sitefoot-locale">O‘zbekiston</p>
    </div>
  </div>
</footer>
```

## Qoidalar
- Fon `bg-alt`, eni `max-narrow` + 22px chetlar. Matn 12px (`text-footnote`, `track-caption`) `fg-3` (4.7:1), havolalar `fg-2`, hoverda tagiga chiziladi; ustun sarlavhasi `fg` 600.
- Tartib: izohlar (sahifada `¹`, `²` bilan belgilangan gaplar uchun) → 1px `line` → xarita → 1px `line` → huquqiy qator.
- Xarita 5 ustun, 833px dan 3, 734px dan 2 ustun. Ustunda 3–7 havola, ustunlar soni bo‘limlarga qarab.
- Huquqiy qator: © yil va loyiha nomi, havolalar `line-strong` tik chiziq bilan ajraladi, `Signature` imzosi, o‘ngda til/mamlakat. Imzo standart holatda doim turadi.
- Sensorli ekranda har havola 44px balandlikda.
- Ilova ichida bu footer emas, oddiy `.foot` ishlatiladi.

## Iste’molchi beradi
Izohlar (bo‘lmasa `footnotes` tushiriladi), ustunlar va havolalar, huquqiy matn.
