negatiivinenSyöte = False
while negatiivinenSyöte == False:
    Syötettytuuma = int(input("Anna tumma: "))
    tuumaCm = Syötettytuuma * 2.54
    if tuumaCm < 0:
        negatiivinenSyöte = True-2
    else:
        print("Muutettu luku "+str(tuumaCm)+" cm on positiivinen, syötä uusi luku.")
print("muunnettu luku on negatiivinen, joten ohjelma lopetetaan.")

