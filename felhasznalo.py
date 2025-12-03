import menu

def felhasznalo():
    felhasznalo = "Bud156AB"
    jelszo = "BudAirport2025+"

    while True:
        print("BEJELENTKEZÉS")
        print("*" * 150)
        megadott_f = input("Felhasználó: ")
        megadott_j = input("Jelszó: ")

        if megadott_f == felhasznalo and megadott_j == jelszo:
            print("Sikeres bejelentkezés!")
            menu.menu()   
            break
        else:
            print("Hibás felhasználó vagy jelszó! Próbáld újra.\n")


if __name__ == "__main__":
    felhasznalo()