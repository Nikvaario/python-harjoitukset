# Ohjelma luo uutta auto varten oman olion, joka sisältää sille oleellisia tietoja, jotka printataan käyttäjälle
# Autoa kiihdytetään metodilla, joka nostaa tai alentaa pyydetyllä määrällä auton nopeutta pitäen sen 0 ja "huippunopeus" muuttujan välillä

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettuMatka = 0

    def kiihdytä(self, nopeus):
        if nopeus >= 0:
            for i in range(nopeus):
                if self.nopeus < self.huippunopeus:
                    self.nopeus += 1
        else:
            self.nopeus += nopeus
            if self.nopeus < 0: self.nopeus = 0

        print(f"Auton nopeus: {self.nopeus} km/h")

auto = Auto("ABC-123", 142)
print(f"Uusi auto luotu rekisteritunnuksella {auto.rekisteritunnus}, jonka huippunopeus on {auto.huippunopeus}!")
auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)
auto.kiihdytä(-200)