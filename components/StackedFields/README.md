# StackedFields

Bir-biriga yopishgan maydonlar guruhi (Apple ID uslubi): kirish, ro‘yxatdan o‘tish, parol.

## Tuzilma
```html
<div class="stacked-fields">
  <label><span class="sr-only">Login</span><input placeholder="Login" /></label>
  <label class="password-row"><span class="sr-only">Parol</span><input type="password" placeholder="Parol" /><button class="icon-button" aria-label="Parolni ko‘rsatish"><svg …/></button></label>
</div>
<button class="btn btn-primary btn-lg btn-block">Kirish</button>
<p class="login-help">… <button class="link-inline">…</button></p>
```

## Qoidalar
- Guruh `bg-elev`, 14px radius, ichki 1px `line-control` kontur (3.6:1); fokusda butun guruh ko‘k halqa oladi. Qatorlar orasi 1px `line`.
- Maydon 56px, chetlari 18px, 17px matn. Yorliq `sr-only` — placeholder ko‘rinadigan yorliq vazifasini bajaradi.
- Karta eni 400px gacha; ustida `segmented-block`, ostida bitta `btn-lg btn-block` va `login-help` (14px, `fg-3`, markazda).
- Parol: ko‘rsatish/yashirish ikoni (`eye` / `eye-off`), yangi parol uchun izoh «Kamida 8 ta belgi».
