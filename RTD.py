import jaratgeneralas #importálás

def  rtd_modositas():

    if jaratgeneralas.jaratok_tarol is None:
        print("Nincs nyomtatva minta :(, Generálj listát!")
        input("Folytatáshoz egy Enter-t")
        return 
    
jaratok = jaratgeneralas.jaratok_tarol
    
print(" RTD módosítás ")
keresett = input("Add meg a járatszámot (pl. 123): ")

if keresett.startswith("N8"):
    keresett = keresett[2:]

talalat = None

if keresett.startswith("N8"):
    keresett = keresett[2:] 
    talalat = None 
    for j in jaratok: 
        if str(j.jaratszam) == keresett:
             talalat = j 
             break
if talalat is None:
    print('Nincs ilyen járat!')
    input('ENTER')

print(f"Járat megtalálva: BUD-{talalat.nev} | N8{talalat.jaratszam}") 
print(f"Jelenlegi RTD: {talalat.RTD}")

uj_rtd = input("Add meg az új RTD időt (HH:MM): ")
talalat.RTD = uj_rtd 
print("✔ RTD sikeresen módosítva!") 
input("ENTER a folytatáshoz...")



