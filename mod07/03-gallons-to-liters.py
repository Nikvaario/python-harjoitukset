# Ottaa ohjelmalle syötetyn määrän yhdysvaltain nestegalloneja ja kutsuu funktiota muuntaakseen määrän litroiksi.
# Ohjelma laskee muunnoksia, kunnes negatiivinen luku syötetään

def muuntaja(gallonit):
    return 3.785 * gallonit

litrojaYhteensä = 0.0
syötettyGalloni = float(input("Syötä bensiini gallonien määrä: "))

while syötettyGalloni > 0:
    litrat = muuntaja(syötettyGalloni)
    litrojaYhteensä += litrat
    print("Muunnettu syötetty määrä litroihin: "+str(litrat)+" L")
    syötettyGalloni = float(input("Syötä uusi bensiini gallonien määrä: "))

print("Ohjelma lopetetaan, galloneita muunnettu litroiksi yhteensä: "+str(litrojaYhteensä)+" L")

