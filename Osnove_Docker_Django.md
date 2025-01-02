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

### 1. Ustvarjanje Django projekta
Prvo namestim Python, nato:

```bash
# Ustvarim virtualno okolje
python -m venv venv
source venv/bin/activate

# Namestim Django
pip install django

# Ustvarim Django projekt
django-admin startproject myproject
cd myproject
```

### 2. Dodajanje Dockerja
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

### 3. Gradnja in zagon kontejnerja

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
