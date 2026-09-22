import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 100
        self.kuljettuMatka = 0
        print(f"Luotu auto {self.rekisteritunnus} huippunopeudella {self.huippunopeus} km/h")

    # Vaihtaa auton nopeuden pyydettyyn lukuun
    def kiihdytä(self, nopeus):
        if nopeus >= 0:
            for i in range(nopeus):
                if self.nopeus < self.huippunopeus:
                    self.nopeus += 1
        else:
            self.nopeus += nopeus
            if self.nopeus < 0: self.nopeus = 0

    # Kulkee autolla annetun tuntimäärän verran omalla nopeudella
    def kulje(self, tuntimäärä):
        self.kuljettuMatka += self.nopeus * tuntimäärä

    # Antaa kilpailulle tiedon, mikäli
    def annaKuljettuAika(self, pituus):
        if self.kuljettuMatka < pituus: return False
        else: return True

    # Tulostaa auton tilastot kilpailussa tai sen päätyttyä
    def tulostaTilastoni(self, kilpailuOhi):
        if kilpailuOhi == False:
            if self.kuljettuMatka < 10000:
                print(f"Auto {self.rekisteritunnus} on liikkunut {self.kuljettuMatka} kilometria.")
            else:
                print(f"Auto {self.rekisteritunnus} on liikkunut {self.kuljettuMatka} kilometria ja on ylittänyt maaliviivan.")
        else:
            print(f"Auto {self.rekisteritunnus} liikkui {self.kuljettuMatka} kilometria, ja tuntinopeudeksi kisan päätyttyä jäi {self.huippunopeus} km/h")

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.kilpailuNimi = nimi
        self.pituus = pituus
        self.autot = autot
        print("---------------------------------------------------------------")
        print(f"Aloitetaan kilpailu {self.kilpailuNimi}, jonka pituus on {self.pituus} kilometria!")

    # Arpoo jokaiselle kilpailun autolle uuden tuntinopeuden ja liikuttaa niitä eteenpäin tunnilla
    def tunti_kuluu(self):
        for auto in self.autot:
                auto.kiihdytä(random.randint(-10, 15))
                auto.kulje(1)

    # Tulostaa jokaisen auton tilastot
    def tulosta_tilanne(self, tuntimäärä, kilpailuOhi):
        print("---------------------------------------------------------------")
        print(f"Autojen kuljettu pituus {tuntimäärä} tunnin jälkeen kisaa.")
        for auto in self.autot:
            auto.tulostaTilastoni(kilpailuOhi)

    # Tarkistaa, onko mikään auto ylittänyt maaliviivaa. Jos on, niin kilpailu päättyy. Muuten kilpailu jatkuu
    def kilpailu_ohi(self):
        lopetetaanKilpailu = False
        for auto in self.autot:
            if auto.annaKuljettuAika(self.pituus) == True:
                lopetetaanKilpailu = True
        return lopetetaanKilpailu

# Luo kaikki kilpailun autot
autot = []
for i in range(10):
    uusiAuto = Auto(f"ABC-{i+1}", random.randint(100, 200))
    autot.append(uusiAuto)

# Luo ja valmistelee kilpailun
kilpailu = Kilpailu("Suuri Romuralli", 8000, autot)
kilpailuPäättyy = False
tuntimäärä = 0

# Kilpailu
while kilpailuPäättyy != True:
    kilpailu.tunti_kuluu()
    tuntimäärä += 1

    if tuntimäärä % 10 == 0:
        kilpailu.tulosta_tilanne(tuntimäärä, False)
    
    kilpailuPäättyy = kilpailu.kilpailu_ohi()

print("---------------------------------------------------------------")
print(f"Kilpailu on päättynyt ja tässä on lopulliset tulokset {tuntimäärä} tunnin jälkeen.")
kilpailu.tulosta_tilanne(tuntimäärä, True)