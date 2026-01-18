import jaratgeneralas

def rtd_modositas():
    if jaratgeneralas.jaratok_tarol is None:
        print("❌ Nincs lista! Előbb generáld le a járatokat a 'Járatok' menüpontban.")
        input("ENTER a folytatáshoz...")
        return

    jaratok = jaratgeneralas.jaratok_tarol

    print("\n=== RTD módosítás ===")
    keresett = input("Add meg a járatszámot (pl. 123 vagy N8123): ")

    if keresett.startswith("N8"):
        keresett = keresett[2:]

    talalat = None
    for j in jaratok:
        if str(j.jaratszam) == keresett:
            talalat = j
            break

    if talalat is None:
        print("❌ Nincs ilyen járat!")
        input("ENTER a folytatáshoz...")
        return

    print(f"Járat megtalálva: BUD-{talalat.nev} | N8{talalat.jaratszam}")
    print(f"Jelenlegi RTD: {talalat.RTD}")

    uj_rtd = input("Add meg az új RTD időt (HH:MM): ")
    talalat.RTD = uj_rtd

    print("✔ RTD sikeresen módosítva!")
    input("ENTER a folytatáshoz...")

