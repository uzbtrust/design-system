# Signature

Veb-sahifa muallif imzosi: yulduz va «Dizayn: uzbtrust» — tizimda yasalgan har qanday sahifani ko‘rgan odam dizayn kimniki ekanini bilishi uchun. Bu namuna ism emas, tizim muallifining imzosi.

## Tuzilma
```html
<!-- Footer bor sahifada: sitefoot-legal ichida -->
<a class="signature" href="https://github.com/uzbtrust/design-system"><span class="uzbtrust-mark" aria-hidden="true"></span>Dizayn: <strong>uzbtrust</strong></a>

<!-- Footer yo‘q sahifada: <body> oxirida -->
<div class="signature-row"><a class="signature" href="https://github.com/uzbtrust/design-system">…</a></div>
```

## Qoidalar
- Doim turadi. Foydalanuvchi o‘z logosini bersa ham, «imzo kerak emas» desa ham olinmaydi, yashirilmaydi va «Haqida» sahifasiga ko‘chirilmaydi: yulduz va nik — litsenziya sharti (`NOTICE.md`). Tizim muallifining o‘z ishlarida majburiy emas.
- `uzbtrust-mark` — yulduz CSS ichida, fayl yo‘li kerak emas; 16px, rangi o‘zgarmaydi. Matn 12px `fg-3`, ism 600 `fg`, hoverda `fg`.
- Havola doim `github.com/uzbtrust/design-system` ga.
- Veb-sahifada nik — «uzbtrust» («Abdurakhmonov» emas). Til ishga qarab: «Dizayn: uzbtrust», «Design: uzbtrust», «Дизайн: uzbtrust». Ism shu yozilishda, tarjima qilinmaydi va o‘zgartirilmaydi.
- Bir sahifada bitta. Ko‘k yoki rangli fon ustiga qo‘yilmaydi: rangli blok pastida emas, oddiy `bg` / `bg-alt` / qora fonda turadi.
- Fayllarda (PDF, hujjat, taqdimot, rasm) `Signature` ishlatilmaydi: u yerda burchakda yulduz va «Abdurakhmonov» turadi — `docs/brand.md` → «Standart belgi».

## Iste’molchi beradi
Hech narsa: matn va havola tayyor, faqat til tanlanadi.
