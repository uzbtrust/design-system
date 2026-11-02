# DocumentPage

Chop etiladigan yoki PDF hujjat sahifasi: muqova sarlavhasi, raqamlar, bo‘limlar, chegarali grafik va jadval — `print` mavzusida.

## Tuzilma
```html
<html data-theme="print">                 <!-- PDF yasashda; brauzerda chop oldidan qo‘yiladi -->
<article>
  <header>                                <!-- 8mm oraliq + 1px #999 chiziq -->
    <p class="eyebrow">Turi · yil</p>
    <h1>Asosiy fikr.<br><span class="dim">Davomi.</span></h1>
    <p>Kirish (12pt, #333)</p>
  </header>
  <ul class="stat-list">…</ul>            <!-- 2–4 ta katta raqam -->
  <h2>Bo‘lim</h2><p>…</p>
  <figure>…grafik…</figure>               <!-- 1px #aaa chegara, radius 6px, bo‘linmaydi -->
  <table>…</table>
</article>
```

## Qoidalar
- Sahifa: A4 (yoki Letter), chetlari 18mm (yuqori), 16mm (yon), 20mm (past). Bir ustun.
- Matn: sarlavha 26pt/1.1/600, kirish 12pt, bo‘lim sarlavhasi ≈20pt, asosiy matn 11pt/1.45, izoh va manba 9pt. Matn qora (`fg`), ikkilamchi `fg-3` (#424245).
- Ekrandagi kartalar chopda fonsiz: 1px #aaa chegara, radius 6px. Soya, shisha va gradient yo‘q.
- Grafik — bitta o‘lchov, bitta `accent` rang; bir nechta seriya bo‘lsa `data-1` / `data-2` / `data-3`.
- Jadval: sarlavha 9pt/600, oddiy harflarda, `fg-3`, qatorlar orasida `line-soft`, raqamlar o‘ngga tekislangan, `tabular-nums`.
- Sarlavha sahifa oxirida yolg‘iz qolmaydi, rasm/jadval/grafik bo‘linmaydi, paragrafda kamida 3 qator.
- Havolalar matn rangida; kerakli manzil matnning o‘zida yoziladi.

Namuna 72 dpi masshtabda (1pt = 1px); haqiqiy hujjatda o‘lchamlar punktda beriladi.
