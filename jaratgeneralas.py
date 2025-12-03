import random
from datetime import datetime, timedelta

def beolvas_lista(fajlnev):
    with open(fajlnev, "r", encoding="utf-8") as f:
        lista = [sor.strip() for sor in f.readlines() if sor.strip()]
    return lista

class Jarat:
    def __init__(self, nev, jaratszam, kapu, utasszam, ETD, RTD):
        self.nev = nev
        self.jaratszam = jaratszam
        self.kapu = kapu
        self.utasszam = utasszam
        self.ETD = ETD
        self.RTD = RTD

    def kiiras(self):
        # MEZŐK ELŐKÉSZÍTÉSE
        jarat_mezo = f"BUD-{self.nev}"          # pl. BUD-DEB (Debrecen)
        jaratszam_mezo = f"N8{self.jaratszam}"  # pl. N8123
        pax_mezo = f"239/{self.utasszam}"

        kapu = self.kapu
        etd = self.ETD
        rtd = self.RTD
        status = ""

        # CANCELLED
        if self.utasszam < 60:
            kapu = ""          # csak "Gate:" marad, szám nélkül
            rtd = ""           # csak "RTD:" marad, idő nélkül
            status = "CANCELLED"

        # OVERBOOKED
        elif self.utasszam > 239:
            status = "OVERBOOKED"

        # FIX SZÉLESSÉGEK AZ OSZLOPOKNAK
        return (
            f"{jarat_mezo:<30} | "   # járat név (BUD-XXX...), 30 karakter széles
            f"{jaratszam_mezo:<7} | "
            f"Gate: {kapu:<4} | "
            f"PAX: {pax_mezo:<11} | "
            f"ETD: {etd:<5} | "
            f"RTD: {rtd:<5} | "
            f"{status:<10}"
        )

def random_ido():
    base = datetime.now().replace(second=0, microsecond=0)
    etd = base + timedelta(minutes=random.randint(5, 300))
    rtd = etd + timedelta(minutes=random.randint(0, 30))
    return etd.strftime("%H:%M"), rtd.strftime("%H:%M")

def general_jaratok():
    
    schengen = beolvas_lista("schengen.txt")
    nonschengen = beolvas_lista("nonschengen.txt")  

    schengen_kivalasztott = random.sample(schengen, min(20, len(schengen)))
    nonschengen_kivalasztott = random.sample(nonschengen, min(20, len(nonschengen)))

    jaratok = []

    #(A kapuk)
    for dest in schengen_kivalasztott:
        jaratszam = random.randint(100, 999)
        kapu_szam = random.randint(1, 30)
        kapu = f"A{kapu_szam}"
        utasszam = random.randint(10, 260)
        etd, rtd = random_ido()
        jaratok.append(Jarat(dest, jaratszam, kapu, utasszam, etd, rtd))

    #(B kapuk)
    for dest in nonschengen_kivalasztott:
        jaratszam = random.randint(100, 999)
        kapu_szam = random.randint(1, 30)
        kapu = f"B{kapu_szam}"
        utasszam = random.randint(10, 260)
        etd, rtd = random_ido()
        jaratok.append(Jarat(dest, jaratszam, kapu, utasszam, etd, rtd))

    return jaratok

def jaratok_kiirasa():
    # Fejléc
    datum = datetime.now().strftime("%Y.%m.%d")
    print(f"JÁRATOK - {datum}")
    print("=" * 150)

    jaratok = general_jaratok()
    for j in jaratok:
        print(j.kiiras())
        
    print("=" * 150)
#if __name__ == "__main__":
   


