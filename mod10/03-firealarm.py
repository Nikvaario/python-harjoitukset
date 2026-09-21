# Ohjelma luo taloon hissejä, joita voi liikuttaa itseään pyydettyyn kerrokseen kunnes käyttäjä lopettaa ohjelman.
# Ohjelma valitsee myös satunnaisen luvun käyttöjä hisseille, jonka jälkeen palohälytin syttyy ja jokainen hissi kutsutaan alinpaan kerroseen.

import random

class Hissi:
    def __init__(self, alinKerros, ylinKerros):
        self.alinKerros = alinKerros
        self.ylinKerros = ylinKerros
        self.nykyinenKerros = alinKerros

    # Siirtää hissin pyydettyyn kerrokseen
    def siirry_kerrokseen(self, kerros):
        while self.nykyinenKerros != kerros:
            if self.nykyinenKerros < kerros:
                self.kerros_ylös()
            else:
                self.kerros_alas()
        print(f"Hissi on pysähtynyt kerrokseen {self.nykyinenKerros}")

    # Nostaa nykyinenKerros muuttujaa yhdellä
    def kerros_ylös(self):
        if self.nykyinenKerros + 1 <= self.ylinKerros:
            self.nykyinenKerros += 1
            print(f"Nykyinen kerros: {self.nykyinenKerros}")

    # Laskee nykyinenKerros muuttujaa yhdellä
    def kerros_alas(self):
        if self.nykyinenKerros - 1 >= self.alinKerros:
            self.nykyinenKerros -= 1
            print(f"Nykyinen kerros: {self.nykyinenKerros}")

class Talo:
    def __init__(self, hissienMäärä):
        self.hissit = []
        self.alinKerros = 1
        self.ylinKerros = 10
        self.palohälytysAjastin = random.randint(4, 6)
        for hissi in range(hissienMäärä):
            self.hissit.append(Hissi(self.alinKerros, self.ylinKerros))
        self.aja_hissiä()

    # Ohjaa luotuja hissejä ohjelmalle syötettyjen komentojen mukaisesti
    def aja_hissiä(self):
        while self.palohälytysAjastin != 0:
            hissi = int(input(f"Anna hissin numero mitä haluat liikuttaa. (1 - {len(self.hissit)}): "))
            while hissi == 0 or hissi > len(self.hissit):
                hissi = int(input(f"Viallinen hissinumero syötetty. Kokeile uudestaan (1 - {len(self.hissit)}): "))

            kerros = int(input(f"Mihin kerrokseen haluat siirtyä? ( {self.alinKerros} - {self.ylinKerros} ): "))
            while kerros < self.alinKerros or kerros > self.ylinKerros:
                kerros = int(input(f"Viallinen kerros syötetty. Kokeile uudestaan ( {self.alinKerros} - {self.ylinKerros} ): "))

            self.hissit[hissi - 1].siirry_kerrokseen(kerros)

            self.palohälytysAjastin -= 1
        self.palohälytys()

    # Kutsuu jokaisen hissin alimpaan kerrokseen
    def palohälytys(self):
        print("Rakennuksessa on palohälytys! Jokainen hissi kutsutaan pohjakerrokseen.")
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(1)

talo = Talo(3)