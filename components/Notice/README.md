# Notice

Joyida turadigan xabarlar: ma’lumot (`notice`), ogohlantirish (`notice is-warn`), sahifa banneri (`banner`) va forma xatosi (`error-message`).

## Tuzilma
```html
<div class="notice" role="note"><svg …/><p>…</p></div>
<div class="notice is-warn" role="note"><svg …/><p><strong>Sabab:</strong> …</p></div>
<div class="banner" role="alert"><span>…</span><button class="btn-text">Amal</button></div>
<p class="error-message" role="alert">…</p>
```

## Qoidalar
- `notice`: `accent-soft` fon, `r-sm`, 15px, ikon `accent-ink`. `is-warn`: `warn-soft` fon, ikon `warn`.
- `banner`: `bad-soft` fon, `bad` matn, 14px radius — butun sahifaga oid muammo.
- `error-message`: `bad-soft` + `bad`, 14px/500 — forma ostida, tugmadan oldin.
- Matn: nima bo‘ldi + nima qilish kerak. Ayblamaydi.
