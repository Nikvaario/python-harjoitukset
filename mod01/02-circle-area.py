import math

# Ottaa ohjelmalle kirjoitetun desimaaliluvun, ja palauttaa ympyrän pinta-ala lasketun pyöristetyn luvun
sädeStr = input('Anna ympyrän säde (metreissä): ')
säde = float(sädeStr)
pintaAla = (säde * säde) * math.pi
print("Ympyrän pinta-ala on: "+str(round(pintaAla))+" neliömetriä.") 