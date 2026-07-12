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
- `procesor_app.ipynb` — notebook Google Colab
- `procesor_app.py` — samodzielny skrypt Python
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

### Edytor emendacji i koniektur (`emendation-editor/`)

Przeglądarkowy edytor do rejestrowania emendacji i koniektur edytorskich, 
z eksportem do aparatu krytycznego TEI. Bez instalacji i bez serwera — 
jeden plik HTML, dane pozostają w przeglądarce.

**Format wyjściowy:**
```xml
<!-- t. I rozdz. VII -->
<app type="emendacja" resp="editor">
	<lem wit="Tekst edycji">czytanie przyjęte</lem>
	<rdg wit="KCodz">czytanie odrzucone</rdg>
	<annotation>uzasadnienie decyzji edytorskiej</annotation>
</app>
```

Lokalizacja (tom, rozdział) trafia do komentarza XML nad blokiem — w samym 
`<app>` nie ma na nią miejsca, kotwiczy się go w tekście bazowym.

**Funkcje:**
- Zamknięte, kaskadowe listy tomów i rozdziałów (struktura edycji *Lalki*)
- Wyszukiwarka pełnotekstowa, filtrowanie po tomie i rozdziale, sortowanie 
  (pozycyjnie / ostatnio edytowane / kolejność dodania); cyfry rzymskie 
  sortują się poprawnie
- Edycja wpisu po kliknięciu karty
- Eksport do TEI (`.txt`) i do JSON; import z JSON pozwala wznowić pracę

**Format danych:** JSON jest formatem nadrzędnym — zawiera komplet pól, 
a eksport TEI jest z niego generowany. Jeśli konwencja kodowania się zmieni, 
wystarczy zmodyfikować funkcję `exportTEI()`; danych nie trzeba wprowadzać 
ponownie.

```json
{
  "tom": "I",
  "rozdzial": "VII",
  "typ": "emendacja",
  "del": "czytanie odrzucone",
  "add": "czytanie przyjęte",
  "wits": ["KCodz", "rkps"],
  "note": "uzasadnienie decyzji edytorskiej"
}
```

**Dostosowanie do innego tekstu:** zmień stałe `TOMY` i `CHAPTERS` na początku 
sekcji `<script>`; sigla przekazów to elementy `.witness-chip` w kodzie HTML.

**Sposób użycia:** otwórz `index.html` w dowolnej nowoczesnej przeglądarce. 
Wczytaj `example/emendacje.json`, żeby zobaczyć edytor z przykładowymi danymi.

> **Uwaga:** dane przechowywane są w `localStorage` przeglądarki. Eksportuj 
> JSON regularnie — wyczyszczenie danych przeglądarki skasuje wpisy.

## Pliki przykładowe

Przykładowe pliki wejściowe i wyjściowe znajdują się w folderze `example/` 
każdego z narzędzi.

## Dodatkowe informacje

Interfejs html powstał przy pomocy AI - Claude (Anthropic). 

## Licencja

Licencja MIT

---

*Anna Mędrzecka-Stefańska | Pracownia Edycji i Monografii Cyfrowych — [nplp.pl](https://nplp.pl)*
