# Ottaa ohjelmalle syötetyt viisi kaupunkia ja palauttaa ne annetussa järjestyksessä käyttäjälle
kaupungit = []
for kaupunki in range(5):
    kaupungit.append(input("Syötä kaupunki numero "+str(kaupunki+1)+": "))

print("Kaupungit järjestyksessä:")
for kaupunki in kaupungit:
    print(kaupunki)