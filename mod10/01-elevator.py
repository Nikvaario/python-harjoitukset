# Ohjelma luo hissin, jota liikuttaa itseään pyydettyyn kerrokseen käyttäen molemmille suunnille tehtyjä funktioita.

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

hissi = Hissi(1, 10)
hissi.siirry_kerrokseen(6)
hissi.siirry_kerrokseen(1)