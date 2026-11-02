# Fonts

**Inter 4.1** (variable, `InterVariable`) — San Francisco'ga eng yaqin ochiq shrift. Muallif: Rasmus Andersson, litsenziya: SIL Open Font License 1.1 (`LICENSE.txt`). Manba: github.com/rsms/inter, v4.1 relizi.

- `InterVariable.woff2` — oddiy, og‘irlik 100–900, optik o‘lcham (`opsz`) o‘qi bilan: kichik matnda Text, katta sarlavhada Display shakli o‘zi tanlanadi — SF Pro Text / Display kabi.
- `InterVariable-Italic.woff2` — kursiv.

## Qachon ishlaydi

`--font-sans` stekida Inter tizim shriftidan (SF) keyin, Helvetica Neue va Arial'dan oldin turadi.

- SF bor qurilmalarda — SF; Inter yuklanmaydi ham (brauzer ishlatilmaydigan shriftni yuklamaydi).
- Windows, Android, Linux — Inter. Ko‘rinish SF'ga juda yaqin: bir xil og‘irliklar, `track-*` harf oralig‘i, `tabular-nums` raqamlar.
- `@font-face` `dist/uzbtrust.css` ichida, yo‘l `../fonts/` — CDN orqali ulansa ham ishlaydi.

## Qoidalar

- SF Pro, SF Compact, SF Mono, New York fayllari bu papkaga qo‘shilmaydi: ularning litsenziyasi tarqatishni taqiqlaydi.
- Inter'dan boshqa veb-shrift qo‘shilmaydi. Og‘irliklar tizimdagidek: 400, 500, 600.
