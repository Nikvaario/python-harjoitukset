# Ottaa ohjelmalle syötetyn nopan ja kutsuu funktiota joka heittää kyseistä lukumäärän noppaa siihen asti, kunnes nopan suurin luku on heitetty.
import random

def noppa(korkeinLuku):
    luku = random.randint(1,korkeinLuku)
    return luku

nopanKorkeinLuku = int(input("Syötä nopan korkein luku: "))

heitettyluku = noppa(nopanKorkeinLuku)
while heitettyluku != nopanKorkeinLuku:
    print("Heitetty luku "+str(heitettyluku)+", yritetään uudestaan")
    heitettyluku = noppa(nopanKorkeinLuku)

print("Luku "+str(heitettyluku)+" heitetty!")