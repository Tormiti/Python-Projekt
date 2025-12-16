import random
from datetime import datetime, timedelta

jaratok_tarol = None


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
        
        jarat_megnevezes = f"BUD-{self.nev}"

        #basic
        alap = (
            f"{jarat_megnevezes:<35} | "
            f"N8{self.jaratszam:<4} | "
            f"Gate: {self.kapu:<5} | "
            f"PAX: 239/{self.utasszam:<3} | "
            f"ETD: {self.ETD} | "
            f"RTD: {self.RTD}"
        )

        status = ""

        # CANCELLED
        if self.utasszam < 60:
            alap = (
                f"{jarat_megnevezes:<35} | "
                f"N8{self.jaratszam:<4} | "
                f"Gate: {'-':<4} | "
                f"PAX: 239/{self.utasszam:<3} | "
                f"ETD: {self.ETD} | "
                f"RTD: {'-':<4}"
            )
            status = "CANCELLED"

        # OVERBOOKED
        elif self.utasszam > 239:
            status = "OVERBOOKED"

        
        return f"{alap} | {status}"


def general_jaratok():
    global jaratok_tarol
    if jaratok_tarol is not None:
        
        return jaratok_tarol

    schengen = beolvas_lista("schengen.txt")
    nonschengen = beolvas_lista("nonschengen.txt")

    schengen_kivalasztott = random.sample(schengen, min(20, len(schengen)))
    nonschengen_kivalasztott = random.sample(nonschengen, min(20, len(nonschengen)))

    jaratok = []

    
    base = datetime.now().replace(second=0, microsecond=0)
    lepes = timedelta(minutes=15)
    index = 0  

    # A KAPUK (Schengen)
    for dest in schengen_kivalasztott:
        jaratszam = random.randint(100, 999)
        kapu_szam = random.randint(1, 30)
        kapu = f"A{kapu_szam}"
        utasszam = random.randint(50, 260)

        etd_dt = base + index * lepes
        etd = etd_dt.strftime("%H:%M")
        rtd = "-"

        jaratok.append(Jarat(dest, jaratszam, kapu, utasszam, etd, rtd))
        index += 1

    # B KAPUK (Non-Schengen)
    for dest in nonschengen_kivalasztott:
        jaratszam = random.randint(100, 999)
        kapu_szam = random.randint(1, 30)
        kapu = f"B{kapu_szam}"
        utasszam = random.randint(10, 260)

        etd_dt = base + index * lepes
        etd = etd_dt.strftime("%H:%M")
        
        rtd = "-"

        jaratok.append(Jarat(dest, jaratszam, kapu, utasszam, etd, rtd))
        index += 1

    
    jaratok_tarol = jaratok
    return jaratok_tarol


def jaratok_kiirasa():
    datum = datetime.now().strftime("%Y.%m.%d")
    print(f"JÁRATOK - {datum}")
    print("=" * 120)

    jaratok = general_jaratok()
    for j in jaratok:
        print(j.kiiras())
print("=" * 120)


