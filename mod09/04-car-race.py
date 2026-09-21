import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 100
        self.kuljettuMatka = 0
        print(f"Luotu auto {self.rekisteritunnus} huippunopeudella {self.huippunopeus} km/h")

    def kiihdytä(self, nopeus):
        if nopeus >= 0:
            for i in range(nopeus):
                if self.nopeus < self.huippunopeus:
                    self.nopeus += 1
        else:
            self.nopeus += nopeus
            if self.nopeus < 0: self.nopeus = 0

    def kulje(self, tuntimäärä):
        self.kuljettuMatka += self.nopeus * tuntimäärä

    def annaKuljettuAika(self):
        if self.kuljettuMatka < 10000:
            print(f"Auto {self.rekisteritunnus} on liikkunut {self.kuljettuMatka} kilometria.")
            return False
        else:
            print(f"Auto {self.rekisteritunnus} on liikkunut {self.kuljettuMatka} kilometria ja on ylittänyt maaliviivan.")
            return True

    def tulostaTilastoni(self):
        print(f"Auto {self.rekisteritunnus} liikkui {self.kuljettuMatka} kilometria, ja tuntinopeudeksi kisan päätyttyä jäi {self.huippunopeus}.")

def tarkistaKuljetutMatkat(autot):
    lopetetaanKilpailu = False
    for auto in autot:
        if auto.annaKuljettuAika() == True:
            lopetetaanKilpailu = True
    return lopetetaanKilpailu

autot = []

for i in range(10):
    uusiAuto = Auto(f"ABC-{i+1}", random.randint(100, 200))
    autot.append(uusiAuto)

kilpailuPäättyy = tarkistaKuljetutMatkat(autot)
tuntimäärä = 0

while kilpailuPäättyy != True:
    print("---------------------------------------------------------------")
    print(f"Autojen kuljettu pituus {tuntimäärä + 1} tunnin jälkeen kisaa.")
    for auto in autot:
        auto.kiihdytä(random.randint(-10, 15))
        auto.kulje(1)
    tuntimäärä += 1
    kilpailuPäättyy = tarkistaKuljetutMatkat(autot)

print("---------------------------------------------------------------")
print(f"Kilpailu on päättynyt ja tässä on lopulliset tulokset {tuntimäärä} tunnin jälkeen.")
for auto in autot:
    auto.tulostaTilastoni()


