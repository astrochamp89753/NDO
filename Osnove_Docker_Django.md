# Python, Docker in Django

## Uvod
Django (ogrodje v Pythonu) omogoča hitro in varno razvijanje spletnih aplikacij.
Docker omogoča pakiranje in izolacijo aplikacij v tako imenovane containerje, kar poenostavi distribucijo in namestitev.

Ta datoteka razlaga, kako delujejo Python, Docker in Django skupaj (torej nek osnovni pregled, bolj namenjen meni).
---

## Kaj je Django?
Django je visokoravno ogrodje za razvoj spletnih aplikacij, ki poudarja "ne ponavljaj se" (DRY - Don't Repeat Yourself) in "konvencije pred konfiguracijo". Ponuja orodja za:

- Upravljanje z bazo podatkov (ORM - Object-Relational Mapping).
- Upravljanje z avtentikacijo uporabnikov.
- Upravljanje z URL-ji in pogledi.
- Vgrajeno administrativno ploščo.

## Kaj je Docker?
Docker je platforma za razvoj, dostavo in izvajanje aplikacij z uporabo t.i. containerjev. Te vključujejo aplikacijo in vse njene odvisnosti (npr. Python, knjižnice itd.) in zagotavljajo, da aplikacija deluje enako ne glede na okolje.
---

## Uporaba Django z Dockerjem
S kombinacijo Django in Docker lahko razvijalci ustvarijo skalabilne in prenosljive aplikacije.

### 1. Ustvarjanje Django projekta z nekak osnovnimi lastnostmi
Prvo namestim Python, nato:

```bash
# Ustvarim virtualno okolje
python -m venv venv
django\Scripts\activate.bat

# Namestim Django
pip install django

# Ustvarim Django projekt
django-admin startproject testsite
cd testsite

# Preverim delovanje projekta (dobim IP in PORT na katerem dobim odziv)
python manage.py runserver # Server izklopim z CTRL+C

# Ustvarim prvo aplikacijo
python manage.py startapp main

# V aplikaciji (main) lahko spremenim kodo v views.py in tako nadziram prikaz na strani

# V aplikaciji (main) ustvarim novo datoteko urls.py v kateri shranim poti do različnih klicov funkcij v datoteki views.py

# Da povežem aplikacijo s projektom moram spremeniti urls.py v mapi projekta (testsite)

# Spremenim nastavitve projekta da aplikacijo lahko uporabljam tudi na drugih napravah (testsite/settings.py)
python manage.py migrate

# Dodam modele v aplikaciji (main) - ustvaril sem ToDoList in ToDoItem za test
python manage.py makemigrations main # Modele migriram v aplikacijo (main)
python manage.py migrate # Modele tudi apliciram

# Dodam nekaj testnih vnosov v bazo
python manage.py shell # Vnos naredim v terminalu z shellom
from main.models import ToDoList, ToDoItem
t = ToDoList(name="Testni List")
t.save()

# Preverim ali je shranitev delovala
ToDoList.objects.all() 
ToDoList.objects.get(id=1)
ToDoList.objects.get(name="Testni List")

# Zaradi definicije lista v razredu ToDoItem, vsak ToDoList ze vsebuje neko podatkovno mnozico
t.todoitem_set.all()
t.todoitem_set.create(text="Prva obveznost", complete=False)
t.todoitem_set.get(id=1)

# Dodatno lahko spremenim url, da preberem tudi id zeljenega lista z "<int:id>"
# S podatkom id lahko preberem podatke iz baze in jih uporabim za prikaz na strani

# Za lažje iskanje lahko uporabim filter
ToDoList.objects().filter(name__startswith='T')
ToDoList.objects().filter(id=2) # Uporabno, ker ne vrze errorja

# Lahko tudi izbrisem element
ToDoList.objects().get(id=1).delete()

# Da dobim dostop do admin/ ustvarim nove avtentikacijske podatke
python manage.py createsuperuser # Znotraj dostopa lahko nadziram dostop skupin in uporabnikov
# Znotraj admin.py lahko spremenim kodo, da imam nadzor nad podatki
```

### 2. Tvorba strani in njihovih lastnosti
V programu naredim domačo stran in jo povežem s programom kot v prejšnjem primeru.
Ustvarim novo mapo v katero bom shranjeval predloge (templates), v kateri moram imeti mapo z imenom aplikacije.
Ustvaril sem osnovno (base) predlogo, ki jo želim uporabiti na vsaki strani, nato pa še glavno predlogo, ki je vidna na prvem delu strani.
V kodi sem nato spremenil še, da server prikaže predloge namesto vnaprej napisane kode v programu (hardcoding).
V predlogi sem lahko ustvaril nove spremenljivke kot na primer {{name}}. Tem sem lahko pripisal vrednosti v dejanskem odzivu.
To sem lahko dodal v blok (block), ki ga lahko spremenim v html datoteki (če vpišem vrednost je to privzeta vrednost).
Znotraj html datotek lahko uporabim tudi kvazi-python kodo (to me je zelo presenetilo).

Zelo uporabni so tudi izpolnjevalni obrazci (forms) - osnovnega sem naredil za dodajanje v seznam, ki sem ga imel že prej.
Za tega sem naredil nov program forms.py, v katerem uporabim django.forms (zelo uporabno).
Ustvarim lahko tudi svoje obrazce za različne primere.

### 3. Dodajanje Dockerja
Ustvarim datoteke za Docker:

#### `Dockerfile`

```dockerfile
# Uporabim osnovno Python sliko
FROM python:3.9-slim

# Nastavim delovni direktorij v kontejnerju
WORKDIR /app

# Kopiram odvisnosti in namestim
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Kopiram aplikacijo
COPY . .

# Nastavim privzeti ukaz za zagon aplikacije
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

#### `docker-compose.yml`

```yaml
version: '3.9'
services:
  web:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    environment:
      - DEBUG=1
```

### 4. Gradnja in zagon kontejnerja

Ko imam pripravljene datoteke, zaženem naslednje ukaze:

```bash
# Ustvarim datoteko requirements.txt
pip freeze > requirements.txt

# Zgradim Docker sliko
docker-compose build

# Zaženem kontejner
docker-compose up
```

Django aplikacija bo na voljo na naslovu `http://localhost:8000`.

---

## Prednosti uporabe Dockerja z Django

1. **Prenosljivost**: Aplikacije lahko delujejo enako v razvojnih in produkcijskih okoljih.
2. **Enostavno skaliranje**: Docker omogoča zagon večih instanc aplikacije.
3. **Izolacija**: Ločena okolja za različne aplikacije.
---

## Zaključek
Kombinacija Python, Django in Docker je odlična izbira za moderne spletne aplikacije. Z uporabo Dockerja razvijalci zmanjšajo težave z okolji, Django pa poskrbi za učinkovit razvoj in varnost aplikacij.
