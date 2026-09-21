class Huone:
    def __init__(self, nimi, ylös = "seinä", alas = "seinä", oikea = "seinä", vasen = "seinä"):
        self.nimi = nimi
        self.ylös = ylös 
        self.alas = alas
        self.oikea = oikea
        self.vasen = vasen

class Peli:
    def __init__(self, huoneet, nykyinen):
        self.huoneet = huoneet
        self.nykyinenHuone = nykyinen[0]
        self.pelaa()

    def pelaa(self):
        komento = input("Mihin suuntaan haluat liikkua (ylös, alas, oikea, vasen tai q lopettaaksesi liikkumisen ): ")
        while komento != 'q':
            if komento in {"ylös", "alas", "oikea", "vasen"}:
                #Yritetään siirtyä huoneesee
                pass
            else:
                #Yritä komentoa uudelleen
                pass

    def siirry(self, suunta):
        pass
huoneet = []

huone1 = Huone("Eteinen", ylös="Kellari", oikea="Keittiö", vasen="Olohuone")
huone2 = Huone("Keittiö", oikea="Eteinen")
huone3 = Huone("Kellari", alas="Eteinen")
huone4 = Huone("Olohuone", vasen="Eteinen")

huoneet.append(huone1)
huoneet.append(huone2)
huoneet.append(huone3)
huoneet.append(huone4)

peli = Peli(huoneet, huone1)