# Cheatsheet
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

Poleg tega sem zaradi Debiana moral ustvariti SSH ključ za uporabo z gitom.

``` bash
ssh-keygen -t ed25519 -C "your_email@example.com"
ssh-keygen -t rsa -b 4096 -C "your_email@example.com" #RSA je univerzalno bolj podprt, toda zame je delovala prva opcija

cat ~/.ssh/id_ed25519.pub #To kopiraj v SSH ključ na gitu
ssh _T git@github.com #Testiraj povezavo do gita

#Če ne želiš vsakič vpisovati fraze
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
ssh-add ~/.ssh/id_rsa #Če si naredil RSA ključ

#Na koncu dodaj še spodnji tekst na dnu in poženi skripto
nano ~/.bashrc
eval "$(ssh-agent -s)" > /dev/null #to kopiraj
ssh-add -q ~/.ssh/id_ed25519 #to kopiraj

source ~/.bashrc
```

## Jupyterhub
Zadnja izbira za kreiranje spletne strani je bil Jupyterhub. Prvo sem seveda sledil [navodilom za inštalacijo](https://jupyterhub.readthedocs.io/en/stable/tutorial/quickstart.html).

Po inštalaciji se moraš malo zafrkavati s konfiguracijo, nato pa je naprej zelo enostavno spreminjanje datoteke `jupyterhub_config.py`. Seveda moraš stvar pognati, da deluje tudi po odklopu iz strežnika, za kar moraš uporabiti posebno komando.

``` bash
nohup setsid jupyterhub -f jupyterhub_config.py > jupyterhub.log 2>&1 < /dev/null &

ps aux | grep jupyterhub #Tako dobiš ID
kill PID
```