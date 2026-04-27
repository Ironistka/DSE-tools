[🇵🇱 Wersja polska](README.pl.md)

# Digital Scholarly Editing Tools

A collection of Python tools for processing textual variants and generating 
critical apparatus in TEI-compliant XML, developed for the 
[TEI Panorama](https://tei.nplp.pl) platform.

> **Note:** These tools follow the TEI Panorama encoding guidelines. 
> If you use a different TEI setup, you will need to adapt the output 
> format to your own guidelines.

## Context

These tools were developed as part of the project:

**Cyfrowa „Lalka": arcyedycja arcydzieła. Naukowa edycja cyfrowa „Lalki" 
Bolesława Prusa wraz z cyfrowym kompendium wiedzy o powieści**  
NPRH/DN/SP/0157/2024/14

## Tools

### TEI app/rdg Processor (`tei-app-processor/`)

Processes a register of textual variants and inserts TEI-compliant 
`<app>`/`<rdg>` critical apparatus into the base text, directly after 
each base phrase.

**Output format:**
```xml
tekst bazowy<app>
    <rdg wit="Tekst edycji">tekst bazowy</rdg>
    <rdg wit="Świadek">wariant</rdg>
</app>
```

**Available as:**
- `procesor_app.ipynb` — Google Colab notebook
- `procesor_app.py` — standalone Python script
- `procesor_tei_app.html` — browser-based interface, no installation required

#### Input files

**`config.txt`** — maps witness names to their canonical forms.  
Useful for normalizing volume numbers (e.g. `L11 = L1`, `L12 = L1`).

```
rkps      = rkps
KCodz     = KCodz
L1        = L1
L11       = L1
L12       = L1
```

**`odmiany.txt`** — register of textual variants, one entry per line:

```
w. 1 tekst bazowy] wariant Świadek
w. 4 tekst] wariant1 Świadek1] wariant2 Świadek2, Świadek3
s. 117 w. 6 tekst] wariant Świadek1, Świadek2
```

Entries may span multiple lines — continuation lines are joined automatically.  
Groups of variants can be separated by `]` or `;`.

**Base text file** — plain text, no markup required.

#### Usage

**Google Colab:** open `procesor_app.ipynb` in Colab and run cells 
sequentially (`Shift+Enter`).

**Browser:** open `procesor_tei_app.html` in any modern browser. 
Upload the three input files, click the button, download the result. 
All processing happens locally — no data is sent to any server.

**Python:**
```bash
python procesor_app.py
```
Edit the file paths at the bottom of the script before running.

#### Requirements

Python 3.x — no external libraries required.

## Example files

Sample input and output files are available in the `example/` folder.

## Acknowledgements

The HTML interface was generated with AI assistance - Claude (Anthropic).


## License

MIT License

---

*Anna Mędrzecka-Stefańska / Pracownia Edycji i Monografii Cyfrowych — [nplp.pl](https://nplp.pl)*
