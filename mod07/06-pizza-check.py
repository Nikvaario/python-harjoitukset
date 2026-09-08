# Otta ohjelmalle syötettyjen pitsojen hinnat sekä halkaisijat, ja laskee funktiolla niiden hinnan per neliömetri
# Ohjelma palauttaa käyttäjällä edullisemman vaihtoehdon kahden pitsan väliltä

import math

def laskePitsa(pitsa, hinta):
    arvo = 0
    pitsanPintaAla = (pitsa / 10 / 10) * math.pi
    arvo = round(hinta / pitsanPintaAla, 2)
    return arvo

pitsa1Hinta = float(input("Anna ensimmäisen pitsan hinta: "))
pitsa1Halkaisija = float(input("Anna ensimmäisen pitsan halkaisija (cm): "))
pitsa2Hinta = float(input("Anna toisen pitsan hinta: "))
pitsa2Halkaisija = float(input("Anna toisen pitsan halkaisija (cm): "))

pitsa1Arvo = laskePitsa(pitsa1Halkaisija, pitsa1Hinta)
pitsa2Arvo = laskePitsa(pitsa2Halkaisija, pitsa2Hinta)

print("Yhden neliömetrin hinta: Pitsa 1 - "+str(pitsa1Arvo)+" € ja Pitsa 2 - "+str(pitsa2Arvo)+" €")

if pitsa1Arvo < pitsa2Arvo:
    print("Pitsa 1 on edullisempi!")
elif pitsa1Arvo > pitsa2Arvo:
    print("Pitsa 2 on edullisempi!")
elif pitsa1Arvo == pitsa2Arvo:
    print("Pitsat ovat yhtä edullisia!")
