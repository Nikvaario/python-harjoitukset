# Ottaa ohjelmalle annetut luvut, ja palauttaa suorakulmion pinta-alana sekä piirinä lasketut ja pyöristetyt luvut
suorakulmioXStr = input("Anna suorakulmion kannan pituus (metreissä): ")
suorakulmioYStr = input("Anna suorakulmion korkeus (metreissä): ")
suorakulmioX = float(suorakulmioXStr)
suorakulmioY = float(suorakulmioYStr)

pintaAla = suorakulmioX * suorakulmioY
piiri = (suorakulmioY * 2) + (suorakulmioX * 2)

print("Suorakulmion pinta-ala on: "+str(round(pintaAla))+" neliömetriä.")
print("Suorakulmion piiri on: "+str(round(piiri))+" metriä.")