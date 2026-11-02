# DropZone

Fayl yuklash zonasi: bosish yoki sudrab tashlash; ustidan fayl o‘tganda ko‘k bo‘ladi.

## Tuzilma
```html
<div class="drop">           <!-- sudralayotganda: drop is-over -->
  <button class="drop-button" type="button">
    <span class="drop-icon"><svg …/></span>
    <span class="drop-text"><strong>Fayl qo‘shish</strong><small>Qaysi turlar · hajm chegarasi</small></span>
  </button>
</div>
```

## Qoidalar
- `fill` fon, `r-md`, kamida 64px. Ikon 40px doira `bg-elev` ichida `accent-ink`.
- `is-over`: `accent-soft` fon va ichki 1.5px `accent` kontur.
- Izohda ruxsat etilgan turlar va hajm. Yuklangan fayllar ostida ro‘yxat yoki rasm to‘ri bo‘lib chiqadi.
