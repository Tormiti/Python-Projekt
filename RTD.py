import jaratgeneralas #importálás

def  rtd_modositas():

    if jaratgeneralas.jaratok_tarol is None:
        print("Nincs nyomtatva minta :(, Generálj listát!")
        input("Folytatáshoz egy Enter-t")
        return 
    
    jaratok = jaratgeneralas.general_jaratok()
    

