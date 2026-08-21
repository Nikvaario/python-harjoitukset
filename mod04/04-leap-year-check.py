# Ottaa ohjelmalle ilmoitetun vuosiluvun ja laskee onko kyseessä karkausvuosi.
# Jos vuosi on jaollinen neljällä tai 100 sekä 400, kyseessä on karkausvuosi.
vuosi = (input("Anna vuosiluku: "))
lukuJaettuna4 = int(vuosi) / 4
lukuJaettuna100 = int(vuosi) / 100
lukuJaettuna400 = int(vuosi) / 400

if lukuJaettuna100.is_integer():
    if lukuJaettuna400.is_integer():
        print("Ilmoittamasi vuosiluku on karkausvuosi.")
    else:
        print("Ilmoittamasi vuoliluku ei ole karkausvuosi.")
elif lukuJaettuna4.is_integer():
    print("Ilmoittamasi vuosiluku on karkausvuosi.")
else:
    print("Ilmoittamasi vuoliluku ei ole karkausvuosi.")