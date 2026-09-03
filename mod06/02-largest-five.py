# Ottaa ohjelmalle syötetyt luvut ja palauttaa käyttäjälle viisi suurinta syötetty lukua
luvut = []

luku = input("Syötä ensimmäinen luku: ")
while luku != "":
    luvut.append(int(luku))
    luku = input("Syötä seuraava luku tai lopeta laskeminen jättämällä tyhjäksi: ")

luvut.sort()
luvut.sort(reverse=True)
print("Viisi suurinta lukua on: "+str(luvut[0:5]))