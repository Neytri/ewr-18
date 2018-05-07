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
operant1 = random.randint(1, 20)
operant2 = random.randint(1, 20)
# rechenart bestimmen
operator = random.randint(1, 3)
# fehlermeldung
falsch = str("Falsch. Versuchen Sie es noch einmal.")

if(operator == 1):      # Addition
    Frage = "Was ist " + str(operant1) + " plus " + str(operant2) + "?\n"
    Antwort = float(input(Frage))
    while not ((operant1 + operant2) == Antwort) and operator == 1:
        print(falsch)
        Antwort = float(input(Frage))

elif(operator == 2):      # Subtraction
    Frage = "Was ist " + str(operant1) + " minus " + str(operant2) + "?\n"
    Antwort = float(input(Frage))
    while not ((operant1 - operant2) == Antwort) and operator == 2:
        print(falsch)
        Antwort = float(input(Frage))

elif(operator == 3):      # Modulo
    Frage = "Was ist " + str(operant1) + " modulo " + str(operant2) + "?\n"
    Antwort = float(input(Frage))
    while not ((operant1 % operant2) == Antwort) and operator == 3:
        print(falsch)
        Antwort = float(input(Frage))

print("Korrekt.")
