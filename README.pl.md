[🇬🇧 English version](README.md)

# Narzędzia do edycji naukowej w środowisku cyfrowym

Zestaw narzędzi Pythona do przetwarzania wariantów tekstowych i generowania 
aparatu krytycznego w formacie XML zgodnym z TEI, opracowany na potrzeby 
platformy [TEI Panorama](https://tei.nplp.pl).

> **Uwaga:** Narzędzia zostały przygotowane zgodnie z wytycznymi kodowania 
> platformy TEI Panorama. W przypadku korzystania z innego środowiska TEI 
> konieczne może być dostosowanie formatu wyjściowego do własnych wytycznych.

## Kontekst

Narzędzia powstały w ramach projektu:

**Cyfrowa „Lalka": arcyedycja arcydzieła. Naukowa edycja cyfrowa „Lalki" 
Bolesława Prusa wraz z cyfrowym kompendium wiedzy o powieści**  
NPRH/DN/SP/0157/2024/14

## Narzędzia

### Procesor odmian TEI app/rdg (`tei-app-processor/`)

Przetwarza rejestr odmian tekstowych i wstawia aparaty krytyczne 
`<app>`/`<rdg>` zgodne z TEI bezpośrednio za frazami bazowymi w tekście.

**Format wyjściowy:**
```xml
tekst bazowy<app>
    <rdg wit="Tekst edycji">tekst bazowy</rdg>
    <rdg wit="Świadek">wariant</rdg>
</app>
```

**Dostępny w trzech wersjach:**
- `procesor_tei.ipynb` — notebook Google Colab
- `procesor_tei.py` — samodzielny skrypt Python
- `procesor_tei_app.html` — interfejs przeglądarkowy, bez instalacji

#### Pliki wejściowe

**`config.txt`** — mapowanie nazw świadków na formy kanoniczne.  
Przydatne do normalizacji numerów tomów (np. `L11 = L1`, `L12 = L1`).

```
rkps      = rkps
KCodz     = KCodz
L1        = L1
L11       = L1
L12       = L1
```

**`odmiany.txt`** — rejestr odmian tekstowych, jeden wpis w wierszu:

```
w. 1 tekst bazowy] wariant Świadek
w. 4 tekst] wariant1 Świadek1] wariant2 Świadek2, Świadek3
s. 117 w. 6 tekst] wariant Świadek1, Świadek2
```

Wpisy mogą rozciągać się na kilka wierszy — linie kontynuacji są 
automatycznie sklejane. Grupy wariantów można rozdzielać znakami `]` lub `;`.

**Plik z tekstem wejściowym** — czysty tekst bez znaczników.

#### Sposób użycia

**Google Colab:** otwórz `procesor_app.ipynb` w Colabie i uruchamiaj 
komórki kolejno (`Shift+Enter`).

**Przeglądarka:** otwórz `procesor_tei_app.html` w dowolnej nowoczesnej 
przeglądarce. Wgraj trzy pliki wejściowe, kliknij przycisk, pobierz wynik. 
Całe przetwarzanie odbywa się lokalnie — żadne dane nie są przesyłane 
na serwer.

**Python:**
```bash
python procesor_app.py
```
Przed uruchomieniem zmień ścieżki do plików na dole skryptu.

#### Wymagania

Python 3.x — nie są wymagane żadne zewnętrzne biblioteki.

## Pliki przykładowe

Przykładowe pliki wejściowe i wyjściowe znajdują się w folderze `example/`.

## Dodatkowe informacje

Interfejs html powstał przy pomocy AI - Claude (Anthropic). 

## Licencja

Licencja MIT

---

*Anna Mędrzecka-Stefańska | Pracownia Edycji i Monografii Cyfrowych — [nplp.pl](https://nplp.pl)*
