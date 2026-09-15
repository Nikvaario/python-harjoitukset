# Ohjelma luo uutta auto varten oman olion, joka sisältää sille oleellisia tietoja, jotka printataan käyttäjälle

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettuMatka = 0

auto = Auto("ABC-123", 142)
print(f"Uusi auto luotu rekisteritunnuksella {auto.rekisteritunnus}, jonka huippunopeus on {auto.huippunopeus}!")