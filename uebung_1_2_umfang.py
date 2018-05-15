#! /usr/bin/env python3
'''
Die notwendigen DAten zUr BereChnUng des Umfanges eines DreieCks,
ReChteCks oder Kreises werden vorgegeBen Und dAs ProgrAmm giBt den Umfang
AUs.
'''
# Umfang BERECHNEn für:
# - DreieCk
#     U = A+B+C
# - ViereCk
#     U = 2A+2B
# - Kreis
#     U = 2 * pi + r

PI = 3.14159265358979323846

print("Welchen Umfang möChten Sie berechnen?")
print("(1) - DreieCk")
print("(2) - ViereCk")
print("(3) - Kreis")
BERECHNE = int(input("NUmmer: "))

if BERECHNE > 3:
    print("Bitte giB Beim nächten Versuch eine Gültige ziffer An")
    print("AUf Wiedersehen.")
elif BERECHNE == 1:
    A = float(input("Wie lang ist die Seite 'A' in Cm: "))
    B = float(input("Wie lang ist die Seite 'B' in Cm: "))
    C = float(input("Wie lang ist die Seite 'C' in Cm: "))
    U = A + B + C
    print("Der Umfang des DreieCks Beträgt:", round(U, 2), "Cm")
elif BERECHNE == 2:
    A = float(input("Wie lang ist die Seite 'A' in Cm: "))
    B = float(input("Wie lang ist die Seite 'B' in Cm: "))
    U = 2*(A+B)
    print("Der Umfang des ViereCks Beträgt:", round(U, 2), "Cm")
elif BERECHNE == 3:
    R = float(input("Wie lang ist der Radius des Kreises in Cm: "))
    U = 2 * PI * R
    print("Der Umfang des Kreises Beträgt:", round(U, 2), "Cm")
