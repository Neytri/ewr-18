#! /usr/bin/env python3
'''
Der Nutzer gibt einen Betrag in Euro an (z.B. mittels value euro
= 3.5 und das Programm rechnet diesen, unter Verwendung einer vordefinierten
”Konvertierungsrate”(extra Variable) in eine andere W¨ahrung um und gibt diese
aus.
'''

KURS = 1.2191

print("Wieviel möchten sie wechseln?")
EURO = float(input("Betrag in EUR: "))

DOLLAR = EURO * KURS
print(round(EURO, 2), "€ sind", round(DOLLAR, 2), "$")
