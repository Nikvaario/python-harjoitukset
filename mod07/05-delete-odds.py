# Ottaa ohjelmalle syötetyt luvut ja palauttaa käyttäjälle listan luvuista sekä listan luvuista, jotka ei ole parittomia

def poistaParittomat(luvut):
    tarkistettavaLuku = 0
    parillisetLuvut = []
    print("Kaikki syötetyt luvut: "+str(luvut))

    for luku in luvut:
        tarkistettavaLuku = float(luku)
        tarkistettavaLuku = tarkistettavaLuku / 2

        if tarkistettavaLuku.is_integer(): 
            tarkistettavaLuku = tarkistettavaLuku * 2
            parillisetLuvut.append(int(tarkistettavaLuku))

    parillisetLuvut.sort()
    print("Syötetyistä luvuista parilliset luvut: "+str(parillisetLuvut))

syötetytLuvut = []
luku = input("Syötä ensimmäinen luku: ")
syötetytLuvut.append(int(luku))

while luku != "":
    luku = input("Syötä seuraava luku tai lopeta ohjelma tyhjällä: ")
    if luku == "": break
    else:
        syötetytLuvut.append(int(luku))

poistaParittomat(syötetytLuvut)
        