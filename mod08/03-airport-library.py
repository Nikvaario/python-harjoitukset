# Ohjelma toimii käyttäjälle lentoasemien hakukoneena, johon käyttäjä voi lisätä tai hakea lentoasemia käyttäen niiden ICAO-koodia 
# Mikäli ohjelmalla haluaa hakea lentoasemaa, tulee valita "hae" komento jossa ohjelma kysyy ICAO-koodia hakeaksesen oikean lentokentän
# Mikäli ohjelmalle haluaa lisätä lentoaseman, tulee valita "uusi" komento jossa ohjelma kysyy lentokentän nimeä ja ICAO-koodia sen etsimistä varten 

lentoasemat = {"EFHK": "Helsinki-Vantaa",
              "EFRO": "Rovaniemi",
              "EFKT": "Kittilä",
              "EFOU": "Oulu",
              "EFTU": "Turku"}

def etsiLentoasema(koodi, lentoasemat):
    if koodi in lentoasemat:
        print(f"Lentoasema {lentoasemat[koodi]} löytynyt koodilla {koodi}")
    else: 
        print(f"Lentoasemaa ei löytynyt koodilla {koodi}")

def lisääLentoasema(lentoasemat, koodi, nimi):
    if koodi in lentoasemat:
        print(f"Koodilla {koodi} löytyy jo lentoasema nimeltä {nimi}")
    else:
        lentoasemat[koodi] = nimi

komento = input("Haluatko syöttää uuden lentoaseman (uusi), hakea lentoasemaa (hae) vai lopettaa ohjelman (lopeta): ")
while komento != "lopeta":
    if komento == "uusi":
        uusinimi = input("Kerro lentoaseman nimi: ")
        uusikoodi = input("Kerro lentoaseman ICAO-koodi: ")
        lisääLentoasema(lentoasemat, uusikoodi, uusinimi)
    if komento == "hae":
        haettavaAsema = input("Kerro haettavan lentoaseman ICAO-koodi: ")
        etsiLentoasema(haettavaAsema, lentoasemat)
    komento = input("Haluatko syöttää uuden lentoaseman (uusi), hakea lentoasemaa (hae) vai lopettaa ohjelman (lopeta): ")

print("Lopetetaan ohjelma.")


