#! /usr/bin/env python3
'''
a) Schreiben Sie in Ihrem Python-Programm eine Funktion, die y in Abh¨angigkeit
   von Parametern t, v0 und g berechnet und zuruck gibt. ¨
   • Geben Sie für g einen default-Wert vor.
   • Berechnen Sie für fixierte v0, g; jedoch für verschiedene t
     (z.B. t = 0, 0.1, 0.2,. . . , 1.4) die Flughöhe y.
   • Erm¨oglichen Sie die Ubergabe einer Liste von Werten f ¨ ur ¨ t, fur die die Funktion ¨
     die zugeh¨origen y(t)-Werte berechnet und als Liste zuruck gibt. ¨
     Plotten Sie die Flugbahn des Balles.
   • Erm¨oglichen Sie zus¨atzlich die Eingabe von v0 als Liste und geben Sie die zugeh¨origen
     y-Werte in einer Liste von Listen zuruck. ¨
   • Zeichnen Sie nun die Flugbahn des Balles fur verschiedene ¨ v0 oder verschiedene g.
b) Wiederholen Sie die Teilaufgabe a) und erlauben nun die Ubergabe eines numpy- ¨
   arrays als Eingabe fur die Funktion. Geben Sie die berechneten Werte als passendes ¨
   numpy-array zuruck. Inwiefern vereinfachen sich die folgenden Schritte? 
'''
# ihr erstes programm
#
# y(t) = v0t - (1/2)gt²
# Y  = Höhe (gesucht y
# v0 = Anfangsgeschwindigkeit
# g  = Gravitationskonstante

v = 6
t = 0.6
g = 9.81

print(6 * 0.6 - 0.5 * 9.81 * 0.6**2) # original zum vergleich
print(v * t - 0.5 * g * t**2)
