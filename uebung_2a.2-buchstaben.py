#! /usr/bin/env python3
'''
Man gibt ein Wort (eine Zeichenkette) ein und das Programm gibt aus,
wieviele Vokale dieses Wort enthaelt.
'''

wort = str(input('Sei so gut und Sag nur ein Wort: '))

vocaleKlein = wort.count('a') + wort.count('e') + wort.count('i') + wort.count('o') + wort.count('u')
vocaleGross = wort.count('A') + wort.count('E') + wort.count('I') + wort.count('O') + wort.count('U')
vocale = vocaleKlein + vocaleGross

print('In dem Wort sind ', vocale, " Vocale.")

