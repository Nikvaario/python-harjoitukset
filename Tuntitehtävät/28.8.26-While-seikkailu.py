# Ohjelma käy läpi käyttäjän syöttämiä aseita, kunnes tietty oikea vaihtoehto on annettu
print("Maria oli rohkea ritari, joka joutui kaksintaisteluun. Ojentaen kätensä maagiseen taskuun, minkään aseen hän nappaisi sieltä?")
syötettyAse = input("Minkä aseen maria ottaa: ")

while syötettyAse != "miekka":
    syötettyAse = input("Tämä ase ei sovellu tähän taisteluun. Valitse toinen ase: ")    

print("Tämä ase soveltuu taisteluun. Kaksintaistelu alkakoon!")