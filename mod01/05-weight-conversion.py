# Ottaa ohjelmalle kirjoitetut kolme lukua, ja palauttaa lukujen määrättyjen massojen mukaan
# kilogrammat ja ylijäämät grammat
lievieskät = float(input("Anna lievisköjen määrä: "))
naulat = float(input("Anna naulojen määrä: "))
luodit = float(input("Anna luotien määrä: " ))

luotiGrammat = 13.3 * luodit
naulaGrammat = 425.6 * luodit
lieviskäGrammat = 8512 * naulat

grammatYhteensä = luotiGrammat + naulaGrammat + lieviskäGrammat
kilogrammat = int(grammatYhteensä / 1000)
grammat = grammatYhteensä - (kilogrammat * 1000)

print("Massa nykymittojen mukaan: \n"+str(kilogrammat)+" kilogrammaa ja "+str(round(grammat, 2))+" grammaa.")
