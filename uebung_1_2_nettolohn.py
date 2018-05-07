#! /usr/bin/env python3

# Nettolohnberechnung Es sind folgende Angaben in Variablen gespeichert:
# gearbeiteten Stunden im Monat Stundenlohn und Prozentsatz der Abgaben
# fur Krankenversicherung und Sozialabgaben. Das Programm gibt Brutto-
# und Nettolohn fur den Monat aus.

abgaben = 0.51

stundenlohn = float(input("Wie hoch ist ihr Stundenlohn: "))
gesamtstunden = float(input("Gearbeitete Stunden in Monat: "))

blohn = stundenlohn * gesamtstunden
nlohn = blohn * abgaben

print("Brutto-Lohn:", round(blohn))
print("Netto-Lohn: ", round(nlohn))
