# Gallery

Gorizontal karusel: skroll bilan suriladigan kartalar, ostida nuqtali navigatsiya va ikki doira strelka. Asosiy lahzalar, xususiyatlar yoki rasmlar to‘plami uchun.

## Tuzilma
```html
<section class="band" aria-label="Asosiy lahzalar">
  <div class="band-head"><h2 class="band-title">Bir qarashda.</h2><a class="link-more" href="…">Hammasi</a></div>
  <div class="gallery">
    <ul class="gallery-track">
      <li class="gallery-item">
        <figure class="gallery-card">
          <figcaption class="gallery-caption copy-highlight is-sm"><strong>Asosiy fikr.</strong> Kulrang davomi.</figcaption>
          …vizual…
          <button class="media-button" type="button" aria-label="Animatsiyani qo‘yish"><svg …play /></button>
        </figure>
      </li>
    </ul>
    <div class="gallery-controls">
      <div class="dotnav"><button class="dotnav-dot" type="button" aria-label="1-karta" aria-current="true"></button>…</div>
      <div class="paddlenav">
        <button class="paddle" type="button" aria-label="Oldingi" disabled><svg …chevron-left /></button>
        <button class="paddle" type="button" aria-label="Keyingi"><svg …chevron-right /></button>
      </div>
    </div>
  </div>
</section>
```

## Qoidalar
- Karta eni `min(82%, 696px)`, oraliq 20px, `scroll-snap` bilan; birinchi karta kontent chetiga (`max` + `gutter`) tekislanadi, qolgani ekran chetigacha ko‘rinib turadi. Skroll chizig‘i ko‘rinmaydi.
- Karta: `card` yuzasi, `r-lg`, ichki chegara 28px (telefonda 22px). Izoh — `copy-highlight is-sm`: kulrang `fg-3` 600, asosiy gap `<strong>` da `fg`.
- Boshqaruvlar kartalardan 48px pastda: markazda `dotnav` (`control-bg` pill, nuqta 8px: `fg-3`, joriysi `fg`), o‘ngda `paddle` lar (36px doira, `control-bg`, ikon `fg`, bosish maydoni 44px). Chetda turgan strelka `disabled` (opacity 0.4).
- Video yoki animatsiya bo‘lsa — karta burchagida `media-button` (36px, `media-control` + blur): play/pauza, `aria-label` holatga qarab almashadi. Avtomatik aylanish yo‘q.
- Strelka bitta karta eniga suradi (`scrollBy`, `behavior: smooth`, reduced-motion'da `auto`); nuqtalar skroll holatidan yangilanadi. JS ishlamasa ham kartalar qo‘l bilan suriladi.
- Bo‘lim sarlavhasi — `band-head`: chapda `band-title` (`text-tile`), o‘ngda `link-more`.

## Iste’molchi beradi
Kartalar (izoh va vizual), har biri uchun nuqta yorlig‘i, strelka va nuqtalarni boshqaruvchi kichik skript.
