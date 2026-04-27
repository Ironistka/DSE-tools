# Digital Scholarly Editing Tools

A collection of Python tools for processing textual variants 
and generating critical apparatus in TEI-compliant XML, 
developed for the TEI Panorama platform (tei.nplp.pl).

## Context

These tools were developed as part of the project:  
**Cyfrowa „Lalka": arcyedycja arcydzieła. Naukowa edycja 
cyfrowa „Lalki" Bolesława Prusa wraz z cyfrowym kompendium 
wiedzy o powieści**  
NPRH/DN/SP/0157/2024/14

The tools follow the TEI Panorama encoding guidelines. 
If you use a different TEI setup, you will need to adapt 
the output format to your own guidelines.

## Tools

### TEI app/rdg Processor (`tei-app-processor`)

Processes a register of textual variants and inserts 
TEI-compliant `<app>`/`<rdg>` critical apparatus 
into the base text.

**Input files:**
- `config.txt` — witness names and their normalized forms
- `odmiany.txt` — register of variants
- base text file (`.txt`)

**Output:**
- base text with `<app>` blocks inserted after each variant location

**Format of `odmiany.txt`:**

A plain text file containing the register of variants.
Each entry starts with a line number (`w. N`) and optionally 
a page number (`s. N`), followed by the base text and variants 
separated by `]`:
w. 1 base text] variant Witness
w. 4 base text] variant1 Witness1] variant2 Witness2, Witness3
s. 117 w. 6 base text] variant Witness

Entries spanning multiple lines are joined automatically.
Semicolons (`;`) can also be used as separators between variants.

**Format of `config.txt`:**

A plain text file mapping witness names to their canonical forms.
Each line: `witness_name = canonical_name`  
Useful for normalizing volume numbers (e.g. `L11 = L1`, `L12 = L1`).

**Output format:**
```xml
tekst bazowy<app>
    <rdg wit="Tekst edycji">tekst bazowy</rdg>
    <rdg wit="Świadek">wariant</rdg>
</app>
```

## Usage

### Google Colab
Open `procesor_app.ipynb` in Google Colab and run cells 
sequentially.

### Python
```bash
python procesor_app.py
```
Edit the file paths at the bottom of the script before running.

## Requirements

Python 3.x — no external libraries required.

## License

MIT License

## Authors

Anna Mędrzecka-Stefańska
Pracownia Edycji i Monografii Cyfrowych  
nplp.pl
