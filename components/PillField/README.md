# PillField

Ro‘yxat ustidagi asboblar paneli uchun pill shaklidagi qidiruv va tanlov maydonlari.

## Tuzilma
```html
<div class="toolbar">
  <div class="toolbar-filters">
    <label class="pill-field search-pill"><svg …/><input type="search" placeholder="Qidirish" /><button class="pill-clear" aria-label="Tozalash">…</button></label>
    <label class="pill-field select-pill"><svg …/><select>…</select><svg …/></label>
  </div>
  <div class="segmented">…</div>
</div>
```

## Qoidalar
- 34px pill, `fill` fon, ikon `fg-3`, matn 14px `fg`. Fokusda `bg-elev` + ko‘k halqa (`Field` bilan bir xil).
- Qidiruv 168px; ≤640px da qolgan joyni egallaydi. Tozalash tugmasi 18px `fg-4` doira, faqat qiymat bo‘lsa.
- Sensorda kamida 40px.
