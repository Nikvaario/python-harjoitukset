while True:
    try:
        luku1 = int(input("Anna ensimmäinen luku: "))
        break
    except ValueError:
        print("Merkkijono syötetty, kokeile uudestaan.")

while True:
    try:
        luku2 = int(input("Anna toinen luku: "))
        break
    except ValueError:
        print("Merkkijono syötetty, kokeile uudestaan.")

while True:
    try:
        jakolasku = luku1 / luku2
        print(f"Jakolaskun tulon on: {jakolasku}")
        break
    except ZeroDivisionError:
        print("Luvulla 0 ei voi jakaa, kokeile uudestaan.")
        luku2 = int(input("Anna toinen luku: "))
