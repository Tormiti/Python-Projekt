import sys
import jaratgeneralas  

def menu():
    while True:
        print("\n=== Főmenü ===")
        print("1. Járatok")
        print("2. RTD")
        print("3. Keresés")
        print("4. Kilépés")

        valasztas = input("Válassz egy menüpontot (1-4): ")

        if valasztas == "1":
            print("➡ Járatok menüpont kiválasztva...")
            print()
            jaratgeneralas.jaratok_kiirasa()
            input("\nNyomj ENTER-t a folytatáshoz...")
        elif valasztas == "2":
            print("➡ RTD menüpont kiválasztva.")
            import RTD
            RTD.rtd_modositas()
        elif valasztas == "3":                
            print("➡ Keresés menüpont kiválasztva.")
            # Ide majd jöhet a kereső funkció
        elif valasztas == "4":
            print("Kilépés...")
            sys.exit() #exit- vagy break-el a világért nem akart kilépni

            
            
        else:
            print("Érvénytelen választás, próbáld újra!")



