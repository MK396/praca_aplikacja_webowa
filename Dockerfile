FROM python:3.12-slim

# Instalacja zależności systemowych (w tym Git LFS do pobrania modeli)
RUN apt-get update && apt-get install -y git git-lfs && rm -rf /var/lib/apt/lists/*

# Ustawienie katalogu roboczego wewnątrz kontenera
WORKDIR /app

# Kopiowanie i instalacja wymagań Pythona
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiowanie całej reszty kodu aplikacji
COPY . .

# Hugging Face wymaga uruchomienia aplikacji na porcie 7860
EXPOSE 7860

# Komenda startowa uruchamiająca Django przez Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:7860", "--timeout", "120", "praca_site.wsgi:application"]