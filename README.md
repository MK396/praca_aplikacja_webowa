# ♻️ Aplikacja webowa do segregacji odpadów i edukacji ekologicznej

Aplikacja webowa oparta na frameworku **Django**, wykorzystująca głębokie sieci neuronowe (**TensorFlow/Keras**) do automatycznej klasyfikacji odpadów i wskazywania odpowiedniego pojemnika, gdzie je wyrzucić.

Projekt został stworzony w ramach pracy inżynierskiej.

---

## 🧠 Zbiór danych i skuteczność modeli

Do wytrenowania modeli wykorzystano zbiór danych składający się łącznie z **58 372 obrazów** podzielonych na 7 kategorii odpadów.

Aplikacja udostępnia dwa modele sieci neuronowych:

* **Model autorski:** Zaprojektowana od podstaw, głęboka konwolucyjna sieć neuronowa. Po zastosowaniu mechanizmów zapobiegających przeuczeniu (m.in. augmentacja danych, warstwy Dropout) oraz optymalizacji rozdzielczości obrazów, model końcowy osiągnął bardzo dobrą ogólną skuteczność na poziomie **90%** na zbiorze testowym.
* **ResNet50V2:** Zaawansowany model wykorzystujący bazę konwolucyjną początkowo wytrenowaną na zbiorze ImageNet. Poprzez zastosowanie techniki fine-tuningu polegającej na odmrożeniu i dotrenowaniu 10 ostatnich warstw klasyfikatora, model osiągnął ostateczną skuteczność na poziomie **96%**.

## 📸 Demo

[demo.webm](https://github.com/user-attachments/assets/0147fc80-cd04-4630-b808-d49f4058ebcc)

---

## 🚀 Funkcjonalności

- **Klasyfikacja obrazów:** użytkownik przesyła zdjęcie odpadu, a system rozpoznaje jego kategorię.
- **Sekcja edukacyjna:** użytkownik ma możliwość sprawdzenia co można wyrzucać do danych pojemników, klikając na ikonkę podpisanego i oznaczonego kolorem kosza.
- **Modele AI:** możliwość wyboru między modelem autorskim a modelem ResNet50V2 (oba znajdują się w katalogu `classifier/cnn_model`).

---

## 🛠️ Technologie

- **Backend:** Python 3.12, Django  
- **AI/ML:** TensorFlow, Keras, NumPy  
- **Frontend:** HTML, CSS  

---

## ⚙️ Instrukcja uruchomienia

Aby uruchomić projekt lokalnie, wykonaj poniższe kroki:

### 1. Klonowanie repozytorium

Ponieważ projekt zawiera modele sztucznej inteligencji ważące ponad 100 MB, do ich prawidłowego pobrania wymagany jest **Git LFS (Large File Storage)**. 

Upewnij się, że masz go zainstalowanego, aktywuj go, a następnie sklonuj projekt:

```bash
git lfs install
git clone https://github.com/MK396/praca_aplikacja_webowa.git
cd praca_aplikacja_webowa
```

### 2. Konfiguracja środowiska wirtualnego

#### Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```
#### macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalacja zależności
```bash
cd praca_site
pip install -r requirements.txt
```

### 4. Konfiguracja zmiennych środowiskowych (.env)
1. Upewnij się, że znajdujesz się w katalogu `praca_site` (tam, gdzie plik `manage.py`).
2. Uruchom poniższe polecenie, aby wygenerować bezpieczny klucz kryptograficzny, utworzyć plik `.env` i od razu go w nim zapisać:

**Dla Windows:**
```bash
python -c "from django.core.management.utils import get_random_secret_key; open('.env', 'w').write(f'SECRET_KEY=\'{get_random_secret_key()}\'\n')"
```
**Dla macOS/Linux:**
```bash
python3 -c "from django.core.management.utils import get_random_secret_key; open('.env', 'w').write(f'SECRET_KEY=\'{get_random_secret_key()}\'\n')"
```
   
### 5. Uruchomienie serwera

Będąc w katalogu praca_site uruchom serwer za pomocą poniższego polecenia
```bash
python manage.py runserver
```
Aplikacja będzie dostępna pod adresem: http://127.0.0.1:8000/
