# Ottaa ohjelmalle syötetyn kuukauden luvun ja palauttaa käyttäjälle sen vuodenajan
vuodenajat = "talvi", "talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy"

kuukausi = int(input("Anna valitsemasi kuukauden numero kuukausijärjestyksessä: "))
kuukaudenVuodenaika = vuodenajat[kuukausi - 1]
print(f"Valitseman kuukauden vuodenaika on {kuukaudenVuodenaika}!")