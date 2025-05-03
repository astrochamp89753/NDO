# Cheatsheet
Ta dokument je bolj mišljen za uporabo v razvoju spletne strani, mogoče pa komu tudi olajša delo (vse kar sem uporabil bo tu zbrano na eni lokaciji, če bi kdo podobno naredil spletno stran si lahko pomaga s to datoteko).

---
## Uvod
Ideja spletne strani je interakcijski način učenja snovi, ki se jo uči pri predmetu **NDO**. V sklopu predmeta in z nekaj raziskovanja (več o temu v [virih](https://github.com/astrochamp89753/NDO/blob/main/Viri.md)) smo se odločili za naslednje teme:

-integratorji
-čas/theta na tirnicah
-gravitacijska frača
-trki teles
-raketna enačba
-Keplerjevi zakoni
-baricenter
-kozmične hitrosti
-Hohmannov tir
-poljubna sprememba hitrosti

Vsako temo smo probali razložiti in prikazati na čim bolj intuitiven način, za kar smo uporabili **jupyter notebook** - spletno aplikacijo, s katero lahko ustvarjamo interaktivne dokumente (zvezke), ki prikazuje rezultate kode in slike v realnem času. Če se uporabnik na spletni strani prijavi, svoje datoteke lahko tudi shrani na faksovem strežniku.

## Git
Zaradi enostavnosti sem se odločil uporabiti [git](https://aguaclara.github.io/aguaclara_tutorial/git-and-github/git-in-the-command-line.html). Najbolj pomembni ukazi so:

'''bash
git clone <INSERT URL> #Klonira repo in ustvari mapo
git status #Preveri stanje mape - ali se je kaj spremenilo

git pull #Mapo spremeni tako, da se sklada z najkasnejšim repo-m

git add -A #Izbor datotek za naložitev na repo, -A izbere vse
git commit -m "Commit Message" #Potrditev sprememb, z -m "" se izognemo vim-u
git push #Naložitev datotek na repo
'''