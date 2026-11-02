# LinkCard

Havola kartasi: sayt belgisi, nomi va manzili. Referenslar, manbalar va foydali havolalar ro‘yxati uchun.

## Tuzilma
```html
<div class="link-adder"><svg …/><input type="url" placeholder="…" /><button class="chip-button is-on">Qo‘shish</button></div>
<ul class="link-cards">
  <li class="link-card">
    <a class="link-open" href="…" target="_blank" rel="noopener noreferrer">
      <span class="link-badge site-pinterest">P</span>
      <span class="link-meta"><strong>Pinterest</strong><small>pinterest.com/…</small></span>
      <svg class="link-arrow" …/>
    </a>
    <button class="icon-button is-danger" aria-label="Olib tashlash">…</button>
  </li>
</ul>
```

## Qoidalar
- To‘r: `minmax(220px, 1fr)`, oraliq 8px. Karta `sheet-card`, `r-sm`; hoverda `fill-hover`, strelka `accent-ink` va yuqori-o‘ngga 2px.
- Belgi 36px, 10px radius, sayt bosh harfi 19px/700 (katta matn: brend rangi ustida ham 3:1 dan yuqori). Tanilgan saytlar o‘z rangida: `site-pinterest` #e60023, `site-behance` #1769ff, `site-dribbble` #ea4c89, `site-instagram` gradient, `site-figma` #1e1e1e, `site-telegram` #229ed9. Boshqalari `accent-soft` + `accent-ink`.
- Nom — tanilgan sayt nomi yoki domen; ostida domen va yo‘l, bir qatorda qisqaradi.
- Havola qo‘shishda `https://` o‘zi qo‘shiladi; noto‘g‘ri bo‘lsa ostida `field-hint tone-warn`.
