#! /usr/bin/env python3

kurs = 1.2191

print("Wieviel möchten sie wechseln?")
euro = float(input("Betrag in EUR: "))

dollar = euro * kurs
print(round(euro,2), "€ sind", round(dollar,2), "$")
