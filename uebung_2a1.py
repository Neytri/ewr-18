#! /usr/bin/env python3
'''
• Speichern Sie den Quelltext ab. Testen Sie das Programm uber das Terminal.
• Stellen Sie sicher, dass Sie jeden Schritt verstehen und kommentieren Sie den
  Quellcode.
• Erweitern Sie das Quiz um das Uben weiterer Rechenarten (insb. modulo) und
  integrieren Sie eine selbstgewählte Statistik.
'''

# Bibliotheken importieren
import random
#import math

# Variablen mit zufallszahlen zuweisen
OPERANT1 = random.randint(1, 20)
OPERANT2 = random.randint(1, 20)
# rechenart bestimmen
OPERATOR = random.randint(1, 3)
# fehlermeldung
FALSCHE_ANTWORT = "Falsch. Versuchen Sie es noch einmal."

if OPERATOR == 1:       # Addition
    FRAGE = "Was ist " + str(OPERANT1) + " plus " + str(OPERANT2) + "?\n"
    ANTWORT = float(input(FRAGE))
    while not ((OPERANT1 + OPERANT2) == ANTWORT) and OPERATOR == 1:
        print(FALSCHE_ANTWORT)
        ANTWORT = float(input(FRAGE))

elif OPERATOR == 2:     # Subtraction
    FRAGE = "Was ist " + str(OPERANT1) + " minus " + str(OPERANT2) + "?\n"
    ANTWORT = float(input(FRAGE))
    while not ((OPERANT1 - OPERANT2) == ANTWORT) and OPERATOR == 2:
        print(FALSCHE_ANTWORT)
        ANTWORT = float(input(FRAGE))

elif OPERATOR == 3:     # Modulo
    FRAGE = "Was ist " + str(OPERANT1) + " modulo " + str(OPERANT2) + "?\n"
    ANTWORT = float(input(FRAGE))
    while not ((OPERANT1 % OPERANT2) == ANTWORT) and OPERATOR == 3:
        print(FALSCHE_ANTWORT)
        ANTWORT = float(input(FRAGE))

print("Korrekt.")
