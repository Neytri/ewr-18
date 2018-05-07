#! /usr/bin/env python3

# Umfang berechnen für:
# - Dreieck
#     U = a+b+c
# - Viereck
#     U = 2a+2b
# - Kreis
#     U = 2 * pi + r

pi = 3.14159265358979323846

print("Welchen Umfang möchten Sie berechnen?")
print("(1) - Dreieck")
print("(2) - Viereck")
print("(3) - Kreis")
berechne = int(input("Nummer: "))

if berechne > 3:
    print("Bitte gib beim nächten Versuch eine Gültige ziffer an")
    print("Auf Wiedersehen.")
if berechne == 1:
    a = float(input("Wie lang ist die Seite 'a' in cm: "))
    b = float(input("Wie lang ist die Seite 'b' in cm: "))
    c = float(input("Wie lang ist die Seite 'c# in cm: "))
    U = a + b + c
    print("Der Umfang des Dreiecks beträgt:", round(U,2), "cm")
if berechne ==2:
    a = float(input("Wie lang ist die Seite 'a' in cm: "))
    b = float(input("Wie lang ist die Seite 'b' in cm: "))
    u = 2*(a+b)
    print("Der Umfang des Vierecks beträgt:", round(u,2), "cm")
if berechne == 3:
    r = float(input("Wie lang ist der Radius des Kreises in cm: "))
    U = 2 * pi * r
    print("Der Umfang des Kreises beträgt:", round(U,2), "cm")
