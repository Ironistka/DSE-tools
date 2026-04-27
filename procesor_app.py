# -*- coding: utf-8 -*-
"""
Procesor odmian tekstowych — format TEI app/rdg
=================================================
Wczytuje rejestr odmian i wstawia aparaty krytyczne <app>/<rdg>
bezpośrednio za frazą bazową w tekście wejściowym.
Pliki wejściowe:
  config.txt   — mapowanie nazw przekazów na formy kanoniczne
  odmiany.txt  — rejestr odmian
  tekst.txt    — czysty tekst wejściowy

Plik wyjściowy:
  output.txt   — tekst z wstawionym kodowaniem odmian

Format odmiany.txt:
  w. 1 tekst bazowy] wariant Przekaz
  w. 4 tekst] wariant1 Przekaz1] wariant2 Przekaz2, Przekaz3
  s. 117 w. 6 tekst] wariant Przekaz

Format config.txt:
  rkps      = rkps
  KCodz     = KCodz
  L1        = L1
  L11       = L1
  L12       = L1
"""

import re
import os

import re
import io


def load_config(text):
    config = {}
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if '=' in line:
            k, v = line.split('=', 1)
            config[k.strip()] = v.strip()
    return config


def parse_variant_group(text, config):
    text = text.rstrip(',;').strip()
    all_names = set(config.keys())
    name_pat = '(?:' + '|'.join(
    re.escape(n) for n in sorted(all_names, key=len, reverse=True)
    ) + ')'
    pattern = r'\s+(' + name_pat + r'(?:\s*,\s*' + name_pat + r')*)\s*$'
    m = re.search(pattern, text)
    if not m:
        return text.strip(), []
    variant_text = text[:m.start()].strip()
    witnesses = []
    for w in re.split(r'\s*,\s*', m.group(1)):
        norm = config.get(w.strip())
        if norm and norm not in witnesses:
            witnesses.append(norm)
    return variant_text, witnesses


def parse_odmiany(text, config):
    text = text.replace('...', '\u2026')
    entry_pat = re.compile(
        r'^(?:s\.\s+[\d\-\u2013\u2014]+\s+)?w\.\s+[\d\-\u2013\u2014]+\s+'
    )
    match_pat = re.compile(
        r'^(?:s\.\s+[\d\-\u2013\u2014]+\s+)?w\.\s+([\d\-\u2013\u2014]+)\s+(.*?)\]\s*(.+)$'
    )
    joined = []
    current = None
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            if current:
                joined.append(current)
                current = None
            continue
        if entry_pat.match(line):
            if current:
                joined.append(current)
            current = line
        elif current:
            current = current + ' ' + line
    if current:
        joined.append(current)

    entries = []
    for line in joined:
        m = match_pat.match(line)
        if not m:
            continue
        nr_wersu = m.group(1)
        tekst_edycji    = m.group(2).strip()
        reszta    = m.group(3).strip()
        odmiany = []
        for g in re.split(r'[;\]]', reszta):
            g = g.strip()
            if not g:
                continue
            vtext, wits = parse_variant_group(g, config)
            if wits:
                odmiany.append((vtext, wits))
        if odmiany:
            entries.append({'nr_wersu': nr_wersu, 'tekst_edycji': tekst_edycji, 'odmiany': odmiany})
        else:
            print('UWAGA: w. ' + nr_wersu + ' -- nie rozpoznano przekazów: ' + tekst_edycji)
    return entries


def build_app(tekst_edycji, odmiany):
    lines = ['<app>']
    lines.append('\t<rdg wit="Tekst edycji">' + tekst_edycji + '</rdg>')
    for vtext, wits in odmiany:
        wit_str = ', '.join(wits)
        lines.append('\t<rdg wit="' + wit_str + '">' + vtext + '</rdg>')
    lines.append('</app>')
    return '\n'.join(lines)


def process(config_text, odmiany_text, input_text):
    config = load_config(config_text)

    entries = parse_odmiany(odmiany_text, config)
    original = input_text
    text_out = original
    report   = []

    for entry in entries:
        tekst_edycji     = entry['tekst_edycji']
        nr_wersu  = entry['nr_wersu']
        odmiany = entry['odmiany']

        occ = original.count(tekst_edycji)
        if occ == 0:
            report.append('NIEZNALEZIONY w. ' + nr_wersu + ': ' + tekst_edycji)
            continue
        if occ > 1:
            report.append('DUPLIKAT w. ' + nr_wersu + ': ' + tekst_edycji
                          + ' (' + str(occ) + ' wystąpień, oznaczono wszystkie)')

        app_block = build_app(tekst_edycji, odmiany)
        text_out = text_out.replace(tekst_edycji, tekst_edycji + app_block)

    return text_out, report


# ============================================================
#  Uruchomienie — dostosuj nazwy plików
# ============================================================

if __name__ == '__main__':
    config_text  = open('config.txt',  encoding='utf-8').read()
    odmiany_text = open('odmiany.txt', encoding='utf-8').read()
    input_text   = open('tekst.txt',   encoding='utf-8').read()

    text_out, report = process(config_text, odmiany_text, input_text)

    os.makedirs('output', exist_ok=True)
    with open('output/output.txt', 'w', encoding='utf-8') as f:
        f.write(text_out)

    print('\n=== RAPORT ===')
    if report:
        for r in report:
            print(r)
    else:
        print('Brak problemów — wszystkie warianty znalezione.')

    print('\nZapisano: output/output.txt')
