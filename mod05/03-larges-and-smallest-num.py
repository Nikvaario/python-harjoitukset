# Ottaa ohjelmalle syötetyt luvut siihenmennessä, kunnes luvuksi annetaan tyhjä.
# Ohjelma tallentaa isoimman ja pienimmän syötetyt luvut, jotka palautetaan tyhjän luvun antaessa.
syötettyluku = input("Syötä ensimmäinen luku: ")

isoinLuku = float(syötettyluku)
pieninLuku = float(syötettyluku)
while (syötettyluku != ""):
    syötettyluku = input("Syötä uusi luku: ")

    if syötettyluku == "": break

    syötettylukuFloat = float(syötettyluku)
    if syötettylukuFloat < pieninLuku:
        pieninLuku = syötettylukuFloat
    elif syötettylukuFloat > isoinLuku:
        isoinLuku = syötettylukuFloat 

print("Laskeminen lopetetaan. Suurin syötetty luku oli "+str(isoinLuku)+" ja pienin "+str(pieninLuku))
