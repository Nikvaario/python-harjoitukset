# Luo kahden tyyppisen auton väliltä ajoneuvoja, ja kulkee pyydytän määrän tunteja niiden huippunopeuksilla sekä laskee resurssienkulutuksen.
# Autoa kiihdytetään metodilla, joka nostaa tai alentaa pyydetyllä määrällä auton nopeutta pitäen sen 0 ja "huippunopeus" muuttujan välillä.
# Autolla kuljetaan metodilla, joka nostaa kuljetun matkan määrää käyttäen auton nopeuden ja annettua tuntimäärään tuloa.

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, ):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettuMatka = 0
        self.käytetytResurssit = 0

    # Vaihtaa auton nopeuden pyydettyyn lukuun
    def kiihdytä(self, nopeus):
        if nopeus >= 0:
            for i in range(nopeus):
                if self.nopeus < self.huippunopeus:
                    self.nopeus += 1
        else:
            self.nopeus += nopeus
            if self.nopeus < 0: self.nopeus = 0

        print(f"Auton nopeus: {self.nopeus} km/h")

    # Kulkee autolla annetun tuntimäärän verran omalla nopeudella
    def kulje(self, tuntimäärä):
        self.kuljettuMatka += self.nopeus * tuntimäärä

        print(f"Autolla {self.rekisteritunnus} kuljettu matka {tuntimäärä} tunnin jälkeen on {self.kuljettuMatka} kilometria")

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

    # Suorittaa yliluokan Kulje funktion ja laskee oman resurssienkulutuksen
    def kulje(self, tuntimäärä):
        super().kulje(tuntimäärä)
        self.käytetytResurssit += self.akkukapasiteetti * tuntimäärä
        print(f"Auto on kuluttanut {self.käytetytResurssit} verran kilowatteja sähköä.")

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankinKoko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankinKoko = bensatankinKoko

    # Suorittaa yliluokan Kulje funktion ja laskee oman resurssienkulutuksen
    def kulje(self, tuntimäärä):
        super().kulje(tuntimäärä)
        self.käytetytResurssit += self.kuljettuMatka / 100
        print(f"Auto on kuluttanut {self.käytetytResurssit} litraa bensaa.")

sähköauto = Sähköauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sähköauto.kiihdytä(sähköauto.huippunopeus)
polttomoottoriauto.kiihdytä(polttomoottoriauto.huippunopeus)
sähköauto.kulje(3)
polttomoottoriauto.kulje(3)