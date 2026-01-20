import jaratgeneralas

def keres():
    if jaratgeneralas.jaratok_tarol is None:
        print("Nincs járatlista! Előbb generáld le a járatokat a 'Járatok' menüpontban.")
        input("ENTER a folytatáshoz...")
        return

    jaratok = jaratgeneralas.jaratok_tarol

    print("\n=== Járat keresés ===")
    print("Kereshetsz: járatszámra, kapura, városra, ETD-re, RTD-re")
    keresett = input("Add meg a keresett értéket: ").strip().lower()

    # ha N8-al kezdődik akkor off (levagjuk h lehessen N8 nelkul is keresni)
    if keresett.startswith("n8"):
        keresett = keresett[2:]

    talalatok = []

    for j in jaratok:
        if (
            keresett in str(j.jaratszam).lower()
            or keresett in j.kapu.lower()
            or keresett in j.nev.lower()
            or keresett in j.ETD.lower()
            or keresett in j.RTD.lower()
        ):
            talalatok.append(j)

    if not talalatok:
        print("\n Nincs találat.")
    else:
        print("\n Találatok:")
        print("=" * 120)
        for j in talalatok:
            print(j.kiiras())
        print("=" * 120)

    input("ENTER a folytatáshoz...")
