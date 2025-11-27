def menu():
    while True:
        print("\n=== Főmenü ===")
        print("1. Járatok")
        print("2. RTD")
        print("3. Keresés")
        print("4. Kilépés")

        valasztas = input("Válassz egy menüpontot (1-4): ")

        if valasztas == "1":
            print("➡ Járatok menüpont kiválasztva.")
            # Ide jöhet majd a Járatok funkciója
        elif valasztas == "2":
            print("➡ RTD menüpont kiválasztva.")
            # Ide jöhet az RTD beíró funkció
        elif valasztas == "3":
            print("➡ Keresés menüpont kiválasztva.")
            # Ide jöhet a kereső funkció
        elif valasztas == "4":
            print("Kilépés...")
            break
        else:
            print("Érvénytelen választás, próbáld újra!")



