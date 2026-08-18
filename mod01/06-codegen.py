import random

# Luo käyttäjälle kaksi numerokoodia: kolmelukuisen koodin 0-9 lukujen väliltä ja neljälukuisen koodin 1-6 lukujen väliltä
kolminumeroinenKoodi = []
nelinumeroinenKoodi = []

for x in range(3):
    kolminumeroinenKoodi.append(random.randint(0,9))

for x in range(4):
    nelinumeroinenKoodi.append(random.randint(1,6))

print ("Kolmenumeroinen koodi: "+str(kolminumeroinenKoodi[0])+str(kolminumeroinenKoodi[1])+str(kolminumeroinenKoodi[2]))
print ("Nelinumeroinen koodi: "+str(nelinumeroinenKoodi[0])+str(nelinumeroinenKoodi[1])+str(nelinumeroinenKoodi[2])
       +str(nelinumeroinenKoodi[3]))