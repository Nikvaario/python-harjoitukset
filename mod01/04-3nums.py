# Ottaa ohjelmalle kirjoitetut kolme lukua, ja palauttaa niiden summan, tulon ja keskiarvon
luku1 = int(input("Anna ensimmäinen numero (1/3): "))
luku2 = int(input("Anna toinen numero (2/3): "))
luku3 = int(input("Anna kolmas numero (3/3): "))

summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = (luku1 + luku2 + luku3) / 3

print("Lukujen summa on: "+str(summa))
print("Lukujen tulo on: "+str(tulo))
print("Lukujen keskiarvo on: "+str(keskiarvo))