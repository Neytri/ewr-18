#! /usr/bin/env python3
'''
Man gibt ein Wort (eine Zeichenkette) ein und das Programm gibt aus,
wieviele Vokale dieses Wort enthaelt.
'''

WORT = str(input('Sei so gut und Sag nur ein Wort: '))
ANZAHL_VOKALE = 0

### Alte (einfache) Variante
# VOKALE_KLEIN = WORT.count('a') + WORT.count('e') + WORT.count('i') + \
#               WORT.count('o') + WORT.count('u')
# VOKALE_GROSS = WORT.count('A') + WORT.count('E') + WORT.count('I') + \
#               WORT.count('O') + WORT.count('U')
# ANZAHL_VOKALE = VOKALE_KLEIN + VOKALE_GROSS

for ZEICHEN in WORT:
    if ZEICHEN in "aeiouAEIOU":
        ANZAHL_VOKALE += 1

print('In dem Wort sind ', ANZAHL_VOKALE, " Vokale.")
