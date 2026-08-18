import math


sädeStr = input('Anna ympyrän säde (metreissä): ')
säde = int(sädeStr)
pintaAla = (säde * säde) * math.pi
print("Ympyrän pinta-ala on: "+str(round(pintaAla))+" neliömetriä") 