# Ohjelma kutsuu funktiota joka heittää kuuden luvun noppaa siihen asti, kunnes luku 6 on heitetty.
import random

def noppa():
    luku = random.randint(1,6)
    return luku

heitettyluku = noppa()
while heitettyluku != 6:
    print("Heitetty luku "+str(heitettyluku)+", yritetään uudestaan")
    heitettyluku = noppa()

print("Luku "+str(heitettyluku)+" heitetty!")