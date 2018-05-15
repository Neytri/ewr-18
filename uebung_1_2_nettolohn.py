#! /usr/bin/env python3
'''
Nettolohnberechnung Es sind folgende Angaben in Variablen gespeichert:
gearbeiteten Stunden im Monat StundeNETTO und Prozentsatz der Abgaben
fur Krankenversicherung und SozialABGABEN. Das Programm gibt Brutto-
und Nettolohn fur den Monat aus.
'''
ABGABEN = 0.51

STUNDENLOHN = float(input("Wie hoch ist ihr StundeNETTO: "))
GESAMTSTUNDEN = float(input("Gearbeitete Stunden in Monat: "))

BRUTTO = STUNDENLOHN * GESAMTSTUNDEN
NETTO = BRUTTO * ABGABEN

print("Brutto-Lohn:", round(BRUTTO))
print("Netto-Lohn: ", round(NETTO))
