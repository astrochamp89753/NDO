# Cheatsheet
Ta dokument je bolj mišljen za uporabo v razvoju spletne strani, mogoče pa komu tudi olajša delo (vse kar sem uporabil bo tu zbrano na eni lokaciji, če bi kdo podobno naredil spletno stran si lahko pomaga s to datoteko).

---
## Uvod
Ideja spletne strani je interakcijski način učenja snovi, ki se jo uči pri predmetu **NDO**. V sklopu predmeta in z nekaj raziskovanja (več o temu v [virih](https://github.com/astrochamp89753/NDO/blob/main/Viri.md)) smo se odločili za naslednje teme:

- integratorji
- čas/theta na tirnicah
- gravitacijska frača
- trki teles
- raketna enačba
- Keplerjevi zakoni
- baricenter
- kozmične hitrosti
- Hohmannov tir
- poljubna sprememba hitrosti

Vsako temo smo probali razložiti in prikazati na čim bolj intuitiven način, za kar smo uporabili **jupyter notebook** - spletno aplikacijo, s katero lahko ustvarjamo interaktivne dokumente (zvezke), ki prikazuje rezultate kode in slike v realnem času. Če se uporabnik na spletni strani prijavi, svoje datoteke lahko tudi shrani na faksovem strežniku.

## Git
Zaradi enostavnosti sem se odločil uporabiti [git](https://aguaclara.github.io/aguaclara_tutorial/git-and-github/git-in-the-command-line.html). Najbolj pomembni ukazi so:

``` bash
git clone <INSERT URL> #Klonira repo in ustvari mapo
git status #Preveri stanje mape - ali se je kaj spremenilo

git pull #Mapo spremeni tako, da se sklada z najkasnejšim repo-m

git add -A #Izbor datotek za naložitev na repo, -A izbere vse
git commit -m "Commit Message" #Potrditev sprememb, z -m "" se izognemo vim-u
git push #Naložitev datotek na repo
```

## Jupyter-book
Z nekaj dela smo hitro ugotovili, da ustvariti lastno spletno stran ni tako lahko in vzame veliko dela, zato smo se odločili, da bomo uporabili okolje [jupyter-book](https://jupyterbook.org/en/stable/intro.html). Ta zelo olajša gradnjo spletne strani, seveda pa smo morali nekaj stvari spremeniti tudi sami.

Navodila prepisana iz spletne strani za prvih nekaj korakov:

``` bash
pip install -U jupyter-book
jupyter-book create astrosim_book/ #Osnovna spletna stran
jupyter-book build astrosim_book/ #Ustvari HTML stran

cd _build/html
python -m http.server 8000 #Zagon strani na lokalnem strežniku, dostopno na localhost:8000
```

Vse nadaljnje spremembe se upoštevajo z dodatnimi klici funkcije build in zagonom strani.

## Node.js
Za lažjo kontrolo nad uporabniki in bazami smo se odločili za [Node.js](https://nodejs.org/en/about).
Za uporabo je kar nekaj dela toda se splača. Na debian strežniku lahko poženeš kodo za inštalacijo (ali poglej na to [stran](https://nodejs.org/en/download) za druge sisteme):

``` bash
# Download and install nvm:
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash

# in lieu of restarting the shell
\. "$HOME/.nvm/nvm.sh"

# Download and install Node.js:
nvm install 22

# Verify the Node.js version:
node -v # Should print "v22.15.0".
nvm current # Should print "v22.15.0".

# Verify npm version:
npm -v # Should print "10.9.2".
```
