# Ottaa ohjelmalle syötetyt luvut ja palauttaa niiden summan kutsumalla funktiota

def summa(luvut):
    lukujenSumma = 0
    for luku in luvut:
        lukujenSumma += luku
    print("Lukujen summa: "+str(lukujenSumma))

luvut = []
syötettyLuku = int(input("Syötä ensimmäinen luku laskettavaksi: "))
luvut.append(syötettyLuku)

while syötettyLuku != "":
    syötettyLuku = input("Syötä seuraava luku laskettavaksi tai aloita laskeminen tyhjällä: ")
    if syötettyLuku == "": break
    else:
        luvut.append(int(syötettyLuku))

summa(luvut)
