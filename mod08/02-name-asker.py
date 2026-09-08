nimet = set()

def tarkistaNimi(syötettynimi, nimet):
    nimiLöytyy = False
    for nimi in nimet:
        if syötettynimi == nimi:
            nimiLöytyy = True

    if nimiLöytyy == True:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")


syötettyNimi = input("Syötä nimi tai lopeta ohjelma tyhjällä: ")
while syötettyNimi != "":
    if syötettyNimi == "": break
    else:
        tarkistaNimi(syötettyNimi, nimet)
        nimet.add(syötettyNimi)
        syötettyNimi = input("Syötä nimi tai lopeta ohjelma tyhjällä: ")

print("Tulostetaan kaikki syötetyt nimet")
for nimi in nimet:
    print(f"- {nimi}")