# Ohjelma tulosaa kirjan ja lehden tiedot. Molemmat ovat aliluokkia Julkaisu luokalle, joka sisältää niiden nimen

class Julkaisu():
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, sivut, kirjoittaja):
        self.sivut = sivut
        self.kirjoittaja = kirjoittaja
        super().__init__(nimi)

    # Tulostaa kirjan kaikki tiedot
    def tulosta_tiedot(self):
        print(f"Kirja {self.nimi} julkaistu, jonka kirjailija on {self.kirjoittaja}. Kirjassa on {self.sivut} sivua.")
        pass

class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        self.päätoimittaja = päätoimittaja
        super().__init__(nimi)

    # Tulostaa lehden kaikki tiedot
    def tulosta_tiedot(self):
        print(f"Lehti {self.nimi} julkaistu, jonka päätoimittaja on {self.päätoimittaja}.")
        pass

lehti = Lehti("Aku Ankka", "Aki Hyyppä")
kirja = Kirja("Hytti n:o 6", 200, "Rosa Liksom")

lehti.tulosta_tiedot()
kirja.tulosta_tiedot()