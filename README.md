# ♻️ Aplikacja webowa do segregacji odpadów i edukacji ekologicznej

Aplikacja webowa oparta na frameworku **Django**, wykorzystująca głębokie sieci neuronowe (**TensorFlow/Keras**) do automatycznej klasyfikacji odpadów i wskazywania odpowiedniego pojemnika, gdzie je wyrzucić.

Projekt został stworzony w ramach pracy inżynierskiej.

---

## 📸 Demo



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

```bash
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

Ze względów bezpieczeństwa plik konfiguracyjny `.env` nie jest dołączony do repozytorium.

1. W katalogu głównym projektu `praca_site` utwórz nowy plik o nazwie `.env`.
2. Wygeneruj bezpieczny, losowy klucz kryptograficzny, uruchamiając w terminalu poniższe polecenie:
   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```
3. Skopiuj wyświetlony w terminalu klucz, otwórz plik .env i dodaj do niego poniższą linijkę:
   ```bash
   SECRET_KEY = 'tutaj_wklej_wygenerowany_klucz'
   ```
   
5. Uruchomienie serwera

Będąc w katalogu praca_site uruchom serwer za pomocą poniższego polecenia
```bash
python manage.py runserver
```
Aplikacja będzie dostępna pod adresem: http://127.0.0.1:8000/




