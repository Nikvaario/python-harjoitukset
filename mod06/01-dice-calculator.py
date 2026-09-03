# Ottaa ohjelmalle syötetyn määrän heitettäviä noppia ja palauttaa lasketun summan
import random

noppienMäärä = int(input("Anna heitettävien noppemien määrä: "))
noppienLuvut = []
noppiaLaskettu = 0
noppienSumma = 0

for noppa in range(noppienMäärä):
    noppienLuvut.append(random.randint(1,6))
    noppienSumma += noppienLuvut[noppiaLaskettu]
    noppiaLaskettu += 1

print("Noppien summa on: "+str(noppienSumma))


