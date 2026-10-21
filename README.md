# Aplikacja webowa do segregacji odpadów i edukacji ekologicznej

Aplikacja webowa oparta na **Django**, wykorzystująca głębokie sieci neuronowe (**TensorFlow / Keras**) do automatycznej klasyfikacji odpadów na podstawie zdjęć oraz wskazywania właściwego pojemnika.

Projekt powstał w ramach pracy inżynierskiej.

**Aplikacja online:** [https://klasyfikator.mkuzownik.tech/](https://klasyfikator.mkuzownik.tech/)

**Demo:** [demo.webm](https://github.com/user-attachments/assets/0147fc80-cd04-4630-b808-d49f4058ebcc)

---

## Spis treści

- [Opis projektu](#opis-projektu)
- [Funkcjonalności](#funkcjonalności)
- [Technologie](#technologie)
- [Hosting](#hosting)
- [Struktura projektu](#struktura-projektu)
- [Architektura](#architektura)
- [Modele AI](#modele-ai)

---

## Opis projektu

System łączy klasyfikację obrazów z edukacją ekologiczną. Użytkownik przesyła zdjęcie odpadu, a wybrany model sieci neuronowej zwraca kategorię (np. papier, szkło, bio) wraz z pewnością predykcji. Osobna sekcja edukacyjna wyjaśnia, co wolno, a czego nie wolno wrzucać do poszczególnych pojemników.

Aplikacja rozpoznaje **7 kategorii** odpadów:

| Kategoria | Opis |
|-----------|------|
| Biodegradowalne | Odpady organiczne |
| Elektroodpady | Zużyty sprzęt elektryczny |
| Szkło | Opakowania szklane |
| Zmieszane | Odpady resztkowe |
| Papier | Papier, karton, tektura |
| Metal i tworzywa sztuczne | Metale i plastik |
| Tekstylia | Odzież i tekstylia |

---

## Funkcjonalności

- **Klasyfikacja obrazów** — przesyłanie jednego lub wielu zdjęć; wynik z kategorią i pewnością modelu
- **Wybór modelu AI** — model autorski (CNN) lub ResNet50V2 (fine-tuning)
- **Sekcja edukacyjna** — interaktywne pojemniki z listą odpadów dozwolonych i zakazanych
- **Responsywny interfejs** — nawigacja z obsługą urządzeń mobilnych

| Ścieżka | Opis |
|---------|------|
| `/` | Strona główna |
| `/klasyfikacja/` | Rozpoznawanie odpadów ze zdjęć |
| `/segregacja/` | Edukacja — zasady segregacji |

---

## Technologie

| Warstwa | Stack |
|---------|--------|
| Backend | Python 3.11+, Django 5.2 |
| AI / ML | TensorFlow 2.20, Keras, NumPy, Pillow, OpenCV |
| Frontend | HTML, CSS (szablony Django) |
| Produkcja | Gunicorn, WhiteNoise, Docker |
| Konfiguracja | `python-decouple` (`.env`) |
| Baza danych | SQLite |

---

## Hosting

Aplikacja jest dostępna pod adresem **[https://klasyfikator.mkuzownik.tech/](https://klasyfikator.mkuzownik.tech/)**.

Hostowana jest na własnym serwerze **Proxmox**, w kontenerze **Docker** (Gunicorn + WhiteNoise), z konfiguracją proxy / Cloudflare (HTTPS, `CSRF_TRUSTED_ORIGINS`, `SECURE_PROXY_SSL_HEADER`).

---

## Struktura projektu

<details>
<summary>Rozwiń pełną strukturę katalogów</summary>

```
praca_aplikacja_webowa/
├── docker-compose.yml          # Orkiestracja kontenera
├── Dockerfile                  # Obraz produkcyjny (Gunicorn)
├── requirements.txt            # Zależności Pythona
├── README.md
└── praca_site/                 # Projekt Django
    ├── manage.py
    ├── praca_site/             # Konfiguracja projektu
    │   ├── settings.py
    │   ├── urls.py
    │   ├── views.py            # Strona główna
    │   ├── wsgi.py
    │   └── asgi.py
    ├── classifier/             # Aplikacja klasyfikacji AI
    │   ├── views.py
    │   ├── urls.py
    │   ├── templates/classifier/
    │   └── cnn_model/
    │       ├── predict.py              # Ładowanie modeli i inferencja
    │       ├── my_best_model_7.keras   # Model autorski (~73 MB)
    │       └── resnet50_best_3.keras   # ResNet50V2 (~120 MB)
    ├── segregation/            # Aplikacja edukacyjna
    │   ├── views.py
    │   ├── urls.py
    │   └── templates/
    ├── templates/              # Szablony globalne
    │   ├── layout.html
    │   └── homepage.html
    └── static/                 # CSS, ikony pojemników
        ├── css/style.css
        └── images/bins/
```

</details>

> Modele `.keras` (łącznie ok. **190 MB**) są przechowywane przez **Git LFS**.

---

## Architektura

### Przepływ żądania

```
Przeglądarka
    │
    ▼
Django (URLconf: praca_site/urls.py)
    │
    ├── /                → homepage (praca_site.views)
    ├── /klasyfikacja/   → classifier.views.classify_image
    │                         │
    │                         ▼
    │                    cnn_model.predict.predict_image
    │                         │
    │                         ├── Model autorski (256×256, normalizacja /255)
    │                         └── ResNet50V2 (128×128, preprocess_input)
    │
    └── /segregacja/     → segregation.views.main_page
                              (szablon + JS z listami odpadów)
```

### Aplikacje Django

| Aplikacja | Rola |
|-----------|------|
| `praca_site` | Konfiguracja projektu, strona główna, routing główny |
| `classifier` | Upload obrazów, wybór modelu, inferencja CNN, prezentacja wyników |
| `segregation` | Interaktywna sekcja edukacyjna o pojemnikach |

### Warstwa AI

1. Przy imporcie modułu `predict.py` oba modele `.keras` są ładowane do pamięci.
2. Widok `classify_image` przyjmuje pliki (`multipart/form-data`), skaluje podgląd i wywołuje `predict_image`.
3. Wynik (etykieta + pewność w %) oraz podgląd obrazu (Base64) wracają do szablonu.

### Frontend

- Szablon bazowy `layout.html` (nawigacja, hamburger menu)
- Style w `static/css/style.css`
- Grafiki pojemników w `static/images/bins/`
- Pliki statyczne w produkcji serwowane przez **WhiteNoise**

### Wdrożenie

```
Internet → Cloudflare (HTTPS) → Proxmox → Docker (Gunicorn :8000)
```

Kontener budowany z `Dockerfile` / `docker-compose.yml`: obraz `python:3.11-slim`, `collectstatic`, Gunicorn (1 worker).

---

## Modele AI

Do treningu wykorzystano zbiór **58 372 obrazów** w 7 klasach.

| Model | Plik | Wejście | Skuteczność (test) | Opis |
|-------|------|---------|-------------------|------|
| Autorski CNN | `my_best_model_7.keras` | 256×256 | **~90%** | Sieć konwolucyjna od podstaw; Dropout, augmentacja |
| ResNet50V2 | `resnet50_best_3.keras` | 128×128 | **~96%** | Fine-tuning (odmrożenie ostatnich warstw) na bazie ImageNet |

---
