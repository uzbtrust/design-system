# Avatar

Bosh harflardan iborat dumaloq belgi: rasm o‘rniga, doim neytral kulrang gradientda.

## Tuzilma
```html
<span class="avatar avatar-sm" aria-hidden="true">AB</span>
<span class="person-chip"><span class="avatar avatar-sm">AB</span><span>Ism</span></span>
```

## Qoidalar
- O‘lchamlar: `avatar-sm` 24px (10px matn), oddiy 40px (15px), `avatar-lg` 72px (26px). Matn oq, 600.
- Fon `--avatar` — yorug‘da #6e737f → #4f545e, qorong‘uda #737378 → #4f4f54; oq harflar ikkala mavzuda kamida 4.7:1. Rangli avatar yo‘q: odamlar rang bilan ajratilmaydi.
- Bosh harflar: ismning birinchi ikki so‘zidan, katta harf bilan. Avatar dekor — `aria-hidden`, ism yonida matn bilan yoziladi.
