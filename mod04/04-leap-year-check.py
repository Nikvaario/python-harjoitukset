vuosi = (input("Anna vuosiluku: "))
vuosiNumero = int(vuosi) / 4
print(str(vuosiNumero))

if vuosiNumero.is_integer():
    print("Karkausvuosi")
else:
    print("Normaalivuosi")