# Ottaa ohjelmalle syötetyn luvun, ja tarkistaa onko kyseessä alkuluku
# Jos luku on jaettavissa vain ykkösellä ja itsellään, niin ohjelma palauttaa TRUE

luku = int(input("Anna tarkistettava luku: "))
while luku <= 1:
    luku = int(input("Luku yksi tai sitä pienempi syötetty, syötä uusi luku: "))

jaetutLuvut = [] 
alkuluku = True

for i in range(luku):
    jaetutLuvut.append(luku / (i+1))

if jaetutLuvut[0] % 1 != 0:
    alkuluku = False

jaetutLuvut.remove(1)
jaetutLuvut.remove(luku)

for tarkastettava in range(luku-2):
    if (jaetutLuvut[tarkastettava].is_integer()):
        alkuluku=False

if alkuluku == True:
    print("Syötetty luku on alkuluku!")
else:
    print("Syötetty luku ei ole alkuluku!")
    