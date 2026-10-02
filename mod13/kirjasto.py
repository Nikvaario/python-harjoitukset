class Julkaisu():
    def __init__(self, nimi):
        self.nimi = nimi
        self.onkoLainassa = False

class Kirja(Julkaisu):
    def __init__(self, nimi, sivut, kirjoittaja):
        self.sivut = sivut
        self.kirjoittaja = kirjoittaja
        super().__init__(nimi)

    # Tulostaa kirjan kaikki tiedot
    def tulosta_tiedot(self):
        return f"Kirja {self.nimi} julkaistu, jonka kirjailija on {self.kirjoittaja}. Kirjassa on {self.sivut} sivua. | onko kirja lainassa: {self.onkoLainassa}"

class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        self.päätoimittaja = päätoimittaja
        super().__init__(nimi)

    # Tulostaa lehden kaikki tiedot
    def tulosta_tiedot(self):
        return f"Lehti {self.nimi} julkaistu, jonka päätoimittaja on {self.päätoimittaja}. | onko kirja lainassa: {self.onkoLainassa}"

lehti = Lehti("Aku Ankka", "Aki Hyyppä")
kirja = Kirja("Hytti n:o 6", 200, "Rosa Liksom")

with open("kirjasto.txt", "w") as tiedosto:
    tiedosto.write(f"{lehti.tulosta_tiedot()}\n")
    tiedosto.write(f"{kirja.tulosta_tiedot()}\n")

with open("kirjasto.txt", "r") as tiedosto:
    data = tiedosto.read()
    print(data)