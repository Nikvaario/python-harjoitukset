# Ottaa ohjelmalle syötetyt esineet ja lisää ne olioon, josta ohjelman lopettaessa tulostetaan jokainen esine sekä valmiiksi annetut loitsut
# Kun käyttäjä syöttää ohjelmalle esineen, niin sille arvotaan myös satunnainen laatu
import random

class Inventaario:
    def __init__(self, loitsut):
        self.reppu = {}
        self.loitsut = ["Meteoriittisade", "Tulipallo"]
        self.loitsut.extend(loitsut)

    def lisääTavara(self, nimi, laatu):
        self.reppu[nimi] = laatu

    def tulostaReppu(self):
        print("Reppusi sisältää seuraavat esineet:")

        for esine in self.reppu:
            print("- "+self.reppu[esine], esine)

def arvoLaatu():
    arvot = "Huono", "Tavallinen", "Hyvä", "Erinomainen"
    laatu = arvot[random.randint(0, 3)]
    return laatu
    
lisättävätLoitsut = ["Myrkkypilvi", "Hiljaiset Askeleet"]
inventaario = Inventaario(lisättävätLoitsut)

esine = input("Syötä reppuun tavara tai lopeta syöttämällä tyhjä: ")
while esine != "":
    inventaario.lisääTavara(esine, arvoLaatu())
    esine = input("Syötä reppuun tavara tai lopeta syöttämällä tyhjä: ")

inventaario.tulostaReppu()
print(f"Pelaaja osaa seuraavat loitsut: {inventaario.loitsut}")