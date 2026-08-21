# Ottaa ohjelmalle syötetyn hyttiluokan ja tulostaa käyttäjälle kuvauksen hyttiluokasta, jos sellainen on olemassa
hyttiluokka = input("Anna hyttisi luokka: ")

if(hyttiluokka == "LUX"):
    print("Hyttiluokkasi on parvekkeellinen hytti yläkannella.")
elif(hyttiluokka == "A"):
    print("Hyttiluokkasi on ikkunallinen hytti autokannen yläpuolella.")
elif(hyttiluokka == "B"):
    print("Hyttiluokkasi on ikkunaton hytti autokannen yläpuolella.")
elif(hyttiluokka == "C"):
    print("Hyttiluokkasi on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")
    