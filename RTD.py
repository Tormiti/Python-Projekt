import jaratgeneralas #importálás

def  rtd_modositas():

    if jaratgeneralas.jaratok_tarol is None:
        print("Nincs nyomtatva minta :(, Generálj listát!")
        input("Folytatáshoz egy Enter-t")
        return 
    
    jaratok = jaratgeneralas.jaratok_tarol() 
    
print(" RTD módosítás ")
keresett = input("Add meg a járatszámot (pl. 123): ")

if keresett.startswith("N8"):
    keresett = keresett[2:]

talalat = None

for jarat in jaratok:
    if str(jarat.jaratszam) == keresett:
        talalat = jarat
        break


