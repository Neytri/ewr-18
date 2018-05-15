#! /usr/bin/env python3
'''
Es wird eine Zahl zwischen 0 und 20 eingegeben. Das Programm gibt die
Einmaleins-Tabelle fur diese Zahl aus.
'''

TABELLENGROESSE = int(input("Wie weit hätten Sie gern die Tabelle: "))
LINE = ""
zahl = ""
### Stringformatierung durch str.format() und platzhaltern
#for i in range(1, TABELLENGROESSE):
#    print("{:3d} {:4d} {:5d}".format(i, i*i, i*i*i))
if TABELLENGROESSE > 20:
    TABELLENGROESSE = 20
print("20 ist das Maximum und wurde gesetzt.")

# tabelle zeichnen
for i in range(0, TABELLENGROESSE + 1):
    LINE += "{:4d} |".format(i)
    print(LINE)

for j in range(0, TABELLENGROESSE + 1):
    for k in range(0, TABELLENGROESSE +1):
        zahl += "{:4d} |".format(j*k)
    print(zahl)
