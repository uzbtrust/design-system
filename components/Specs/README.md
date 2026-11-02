# Specs

Texnik xususiyatlar va solishtirish jadvali: chapda qator nomi, o‘ngda bir yoki bir nechta ustun qiymatlari. Hujjat, tarif, shablon yoki mahsulot variantlarini yonma-yon ko‘rsatish uchun.

## Tuzilma
```html
<section class="specs" style="--specs-cols: 2" aria-label="Solishtirish">
  <div class="specs-head">
    <span></span>
    <h3 class="specs-col-title">Qisqa hisobot<small>Har oy</small></h3>
    <h3 class="specs-col-title">To‘liq hisobot<small>Har chorak</small></h3>
  </div>
  <div class="specs-row">
    <h4 class="specs-label">Hajm</h4>
    <div class="specs-cell"><p class="specs-value">8 sahifa</p><p class="specs-note">Xulosa va 3 grafik</p></div>
    <div class="specs-cell"><p class="specs-value">24 sahifa</p><p class="specs-note">…</p></div>
  </div>
  <div class="specs-row">
    <h4 class="specs-label">Bo‘limlar</h4>
    <div class="specs-cell"><p class="specs-sub">Asosiy</p><ul class="specs-list"><li>…</li></ul></div>
    <div class="specs-cell"><span class="specs-none">—</span></div>
  </div>
</section>
```

## Qoidalar
- Eni `max-narrow` (980px). Qator nomi ustuni 216px, qiymat ustunlari teng, oraliq 30px. Ustunlar soni `--specs-cols` (1–4); bitta ustun — oddiy texnik xususiyatlar ro‘yxati.
- Qatorlar orasida 1px `line`, qator ichki chegarasi 38 / 51px. Qator nomi 24px/600 (`text-group`), qiymat matni 17px (`text-body`).
- Katta raqam — `specs-value` (28px/600, `tabular-nums`), ostida `specs-note` (14px `fg-3`). Ichki sarlavha — `specs-sub` (17px/600), ro‘yxat — `specs-list`, belgilarsiz.
- Solishtirishda `specs-head` ustun nomlari bilan `LocalNav` ostida yopishib turadi. Yo‘q qiymat — `specs-none` (`—`, `fg-3`), bo‘sh katak qoldirilmaydi.
- ≤734px: qator nomi ustunlar ustiga chiqadi, ustunlar yonma-yon qoladi (3 tadan ko‘p bo‘lsa — alohida jadvallarga bo‘ling).
- Chopda sarlavha yopishmaydi, qator sahifa o‘rtasida bo‘linmaydi.

## Iste’molchi beradi
Ustun nomlari (solishtirishda), qatorlar va har katak qiymati, `--specs-cols` soni.
