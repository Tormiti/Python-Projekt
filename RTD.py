import jaratgeneralas #importálás

def rtd_modositas():
    if jaratgeneralas.jaratok_tarol is None: #ellenőrzés.
        print("Nincs lista! Előbb generáld le a járatokat a 'Járatok' menüpontban.")
        input("ENTER a folytatáshoz...")
        return

    jaratok = jaratgeneralas.jaratok_tarol #betőltés.

    print(" RTD módosítás ")
    keresett = input("Add meg a járatszámot (pl. 123): ") #keresés.
    if keresett.startswith("N8"):
        keresett = keresett[2:]         #mivel mind N8 kezdődik Így elég 3 számra rá keresni.

    talalat = None
    for j in jaratok:
        if str(j.jaratszam) == keresett:        
            talalat = j
            break

    if talalat is None:
        print("Nincs ilyen járat!")
        input("ENTER a folytatáshoz...") 
        return

    print(f"Járat megtalálva: BUD-{talalat.nev} | N8{talalat.jaratszam}")
    print(f"Jelenlegi RTD: {talalat.RTD}")   #találat, informáciok


    uj_rtd = input("Add meg az új RTD időt (HH:MM): ") #megadás
    talalat.RTD = uj_rtd

    print("✔ RTD sikeresen módosítva!")
    input("ENTER a folytatáshoz...")
 #happy end
