# Ottaa ohjelmalle syötetyt seinän mitat ja maalin neliömetrejä/litra luvun, ja laskee tarvittavan määrän maalia litroissa
# maalaamaan käyttäjän seinän.
seinänKorkeus = float(input("Anna seinän korkeus: "))
seinänLeveys = float(input("Anna seinän leveys: "))
maali_m2PerLitra = float (input("Kuinka monta neliömetriä voi maalata yhdellä litralla maaliasi?: "))

seinäPintaAla = seinänKorkeus * seinänLeveys
maalinTarve = seinäPintaAla / maali_m2PerLitra
print("Maalia tarvitaan seinän maalaamiseen "+str(maalinTarve)+" litraa.")