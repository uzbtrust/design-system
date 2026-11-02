# VideoHero

Video bilan kirish bloki: markazda eyebrow, ulkan sarlavha, lead va amallar, ostida butun kenglikdagi video (yoki rasm) va burchakda play/pauza tugmasi. Sayt yoki mahsulot sahifasining birinchi ekrani uchun.

## Tuzilma
```html
<section class="video-hero">
  <div class="video-hero-copy">
    <p class="eyebrow eyebrow-new">Yangi</p>
    <h1 class="video-hero-title">Yil yakunlari.</h1>
    <p class="video-hero-lead">Bir yilda nima qilindi — uch daqiqada.</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="…">Batafsil</a>
      <a class="link-play" href="…">Filmni ko‘rish <svg …circle-play /></a>
    </div>
  </div>
  <div class="video-hero-media">
    <video src="…" poster="…" muted playsinline loop aria-label="…"></video>
    <button class="media-button" type="button" aria-label="Videoni to‘xtatish"><svg …pause /></button>
  </div>
</section>
```

## Qoidalar
- Sarlavha `--fs-hero` (44 → 96px), 600, `track-super`; lead `text-intro` (`fg-3`), eni 34em gacha. Amallar `hero-actions` bilan: `btn-primary` + `link-play` (17px `accent-ink`, yonida 22px `circle-play` ikoni).
- Media 64px (`s-8`) pastda, butun kenglikda, burchaksiz; balandligi 16:9 ga mos (telefonda 4:5), lekin ekranning 80% idan oshmaydi; `object-fit: cover`. Video yuklanguncha `poster` va `bg-alt` fon ko‘rinadi.
- Video ovozsiz, `playsinline`. `prefers-reduced-motion: reduce` da avtomatik o‘ynamaydi — faqat `poster`. Play/pauza — `media-button` (36px, `media-control` + blur) o‘ng pastki burchakda, `aria-label` holatga qarab: «Videoni qo‘yish» / «Videoni to‘xtatish».
- Qorong‘u hero kerak bo‘lsa — `<section class="video-hero" data-theme="dark">`.
- Chopda media o‘rniga `poster` rasmi, tugmalar yo‘q.

## Iste’molchi beradi
Sarlavha, lead, 1–2 amal, video fayli va `poster` rasmi (yoki faqat rasm), video tavsifi (`aria-label`), play/pauza skripti.
