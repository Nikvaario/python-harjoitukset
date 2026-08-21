# Ottaa ohjelmalle syötetyn sukupuolen ja hemoglobiinin, ja laskee onko henkilön hemoglobiiniarvo alhainen, normaali vai korkea.
sukupuoli = input("Anna biologinen sukupuolesi (M tai N): ")
hemoglobiini = float(input("Anna hemoglobiiniarvosi (g/l): "))

if sukupuoli == "M" and 134 < hemoglobiini < 195 or sukupuoli == "N" and 117 < hemoglobiini < 175:
    print("Hemoglobiiniarvosi on normaali.")
elif sukupuoli == "M" and hemoglobiini < 134 or sukupuoli == "N" and hemoglobiini < 117:
    print("Hemoglobiiniarvosi on alhainen.")
elif sukupuoli == "M" and hemoglobiini > 195 or sukupuoli == "N" and hemoglobiini > 175:
    print("Hemoglobiiniarvosi on korkea.")
else:
    print("Virheellinen sukupuoli syötetty. Hemoglobiinitasapainoa ei pystytty arvioimaan.")



    
    