# Tulostaa while-loopissa 1-1000 lukujen väliltä aina kolmella jaettavan luvun.
jaettavaluku = 1;

print("Tulosetetaan luvut, jotka on jaollisia kolmella väliltä 1-1000")
while jaettavaluku < 1000:
    if jaettavaluku % 3 == 0:
        print(jaettavaluku)
    jaettavaluku += 1
print("Luvut tulostettu")