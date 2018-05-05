#! /usr/bin/env python3

'''
• Speichern Sie den Quelltext ab. Testen Sie das Programm uber das Terminal. ¨
• Stellen Sie sicher, dass Sie jeden Schritt verstehen und kommentieren Sie den
  Quellcode.
• Erweitern Sie das Quiz um das Uben weiterer Rechenarten (insb. modulo) und ¨
  integrieren Sie eine selbstgewählte Statistik.
'''

# Bibliotheken importieren
import random

# Variablen mit zufallszahlen zuweisen
operant1 = random.randint(1,20)
operant2 = random.randint(1,20)

# rechenart bestimmen
mod = random.randint(1,2)

# Fragestellung formulieren
if (mod == 1):
	frage = "Was ist " + str(operant1) + " plus " + str(operant2) + "?\n"
else:
	frage = "Was ist " + str(operant1) + " minus " + str(operant2) + "?\n"

# Antwort als eingabe vom Benutzer
antwort = float(input(frage))

while not ((operant1 + operant2) == antwort) and mod == 1:  # Überprüfung der Antwort
	print("Falsch. Versuchen Sie es noch einmal.")      # ... wenn antwort falsch
	antwort = float(input(frage))                       # ... neue eingabe erwarten
# print("Korrekt.")                                           # ... wenn antwort richtig: programm ende

while not ((operant1 - operant2) == antwort) and mod == 2:
	print("Falsch. Versuchen wie es noch einmal.")
	antwort = float(input(frage))
print("Korrekt.")
