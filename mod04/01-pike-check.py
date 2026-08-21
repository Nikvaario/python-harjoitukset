# Ottaa ohjelmalle annetun kuhan pituuden ja antaa sen perusteella päätöksen, täytyykö kuha palauttaa takaisin järveen vai ei.
# Jos kuhan pituus on 37 cm tai enemmän, sen voi pyydystää. Jos kuhan pituus on alle 37cm, se täytyy vapauttaa järveen.
kuhaPituus = float(input("Kirjoita kuhan pituus: "))
if kuhaPituus < 37: 
   print("Pyydystämäsi kuha on alamittainen, vapautan hänet takaisin järveen!")
   puuttuvaPituus = 37 - kuhaPituus
   print("Pyydystämäsi kuha on "+str(puuttuvaPituus)+" cm liian lyhyt (Alin sallittu pituus 37cm)")
else:
    print("Kuhan pyydystäminen sallittu!")