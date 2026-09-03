# Kysyy käyttäjältä käyttäjätunnut ja salasanaa. Mikäli molemmat menevät oikein, niin ohjelma suoritetaan.
# Mikäli jompikumpi tai molemmat on väärin, niin käyttäjänimeä ja salasanaa kysytään uudelleen maksimissaa viisi kertaa.
käyttäjä = ""
salasana = ""

käyttäjä=input("Syötä käyttäjätunnut: ")
salasana=input("Syötä salasana: ")

kertojaVäärin = 0
while käyttäjä != "python" or salasana != "rules":
    print("Käyttäjätunnus tai salasana ilmoitettu väärin. Kokeile uudestaan.")
    if kertojaVäärin == 5: break
    kertojaVäärin += 1
    käyttäjä=input("Syötä käyttäjätunnut: ")
    salasana=input("Syötä salasana: ")

if kertojaVäärin != 5:
    print("Tervetuloa")
else:
    print("Pääsy evätty")