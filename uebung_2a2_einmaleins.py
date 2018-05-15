#! /usr/bin/env python3
'''
Es wird eine Zahl zwischen 0 und 20 eingegeben. Das Programm gibt die
Einmaleins-Tabelle fur diese Zahl aus.
'''

TABELLENGROESSE = int(input("Wie weit hätten Sie gern die Tabelle: "))

for i in range(1, TABELLENGROESSE):
    print("{:3d} {:4d} {:5d}".format(i, i*i, i*i*i))

line = ""
n = TABELLENGROESSE

# tabelle zeichnen
for i in range(0, n + 1):
    line += "{:>3} |".format(i+1)
for i in range(0, n + 1):
    line += "----|"
for i in range(0, n + 1):
    line += "{:>3} |".format(i*i)

print(line)
