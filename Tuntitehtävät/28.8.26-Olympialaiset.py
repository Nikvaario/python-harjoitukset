# Ottaa ohjelmalle syötetyn vuosiluvun, ja tarkistaa onko kyseessä olympiavuosi eli onko vuosiluku jaollinen neljällä.
# Jos vuosiluku on jaollinen neljällä, niin palautetaan järjestäminen TRUE.
# Jos vuosiluku ei ole jaollinen neljällä, niin palautetaan järjestäminen FALSE.
# Jos vuosiluku on jaollinen neljällä mutta vuosiluvulla ei järjestetty poikkeuksesta, niin palautetaan järjestäminen FALSE + syy.
syötettyVuosi = int(input("Anna vuosi: "))

while syötettyVuosi < 1896:
    syötettyVuosi = int(input("Väärä vuosiluku syötetty! Syötä vuosiluku uudelleen (yli 1896): "))

vuosilukuJaettuna = syötettyVuosi / 4

if (vuosilukuJaettuna.is_integer()):
    if syötettyVuosi == 1916:
        print("Syötettynä vuonna olympialaisia ei järjestetty ensimmäisen maailmansodan takia.")
    elif syötettyVuosi == 1940 or syötettyVuosi == 1944:
        print("Syötettynä vuonna olympialaisia ei järjestetty toisen maailmansodan takia.")
    elif syötettyVuosi == 2020:
        print("Syötettynä vuonna olympialaiset järjestettiin poikkeuksellisesti vuonna 2021 koronavirus pandemian takia.")
    else:
        print("Syötettynä vuonna järjestettiin olympialaiset.")
else:
    print("Syötettynä vuonna ei järjestetty olympialaisia.")