# Ohjelma arpoo luvun 1-10 väliltä ja kysyy käyttäjältä lukuja, kunnes hän arvaa oikein arvotun luvun.
# Ohjelma neuvoo käyttäjää väärän luvun arvauksessa ja kertoo, oliko arvaus pieni vai suuri#
import random

arvottuLuku = random.randint(1,10)

arvattuLuku = int(input("Arvaa arvottu luku: "))

while arvattuLuku != arvottuLuku:
    if arvattuLuku < arvottuLuku:
        print("Liian pieni arvaus")
    elif arvattuLuku > arvottuLuku:
        print("Liian suuri arvaus")
    else:
        break

    arvattuLuku = int(input("Arvaa arvottu luku: "))

print("Oikein!")