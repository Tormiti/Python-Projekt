Python projekt – Járatkezelő rendszer
A projekt célja

A projekt célja egy egyszerű járatkezelő rendszer megvalósítása Python nyelven, amely külső fájlokból beolvasott adatok alapján járatokat generál, majd azokat strukturált formában megjeleníti a konzolon.

A program célja az objektumorientált programozás, modulhasználat, fájlkezelés és dátum/idő kezelés gyakorlása.

Használt technológiák és modulok

Programozási nyelv: Python 3

Felhasznált modulok:

random – véletlenszerű járatadatok generálásához

datetime – dátum és idő kezeléséhez

A projekt kizárólag a Python standard könyvtárát használja.

A program két szövegfájlból olvas be adatokat:

schengen.txt

Schengen-övezeten belüli célállomások listája.

nonschengen.txt

Schengen-övezeten kívüli célállomások listája.

A fájlok soronként egy célállomást tartalmaznak. Az üres sorokat a program figyelmen kívül hagyja.

A program felépítése
5.1 Globális változók

jaratok_tarol
A generált járatok listáját tárolja, hogy egy futtatás során ne történjen újragenerálás.

5.2 Függvények
beolvas_lista(fajlnev)

Feladata:

Beolvassa a megadott fájlt

Listát készít a nem üres sorokból

Visszatér a beolvasott adatokkal

general_jaratok()

Feladata:

Beolvassa a Schengen és Non-Schengen célállomásokat

Véletlenszerűen kiválaszt maximum 20–20 célállomást

Létrehozza a járatokat

15 perces időközökkel ETD időpontokat generál

Eltárolja az eredményt a jaratok_tarol változóban

jaratok_kiirasa()

Feladata:

Kiírja az aktuális dátumot

Kiírja a járatok listáját formázott módon a konzolra

5.3 Osztály: Jarat

A Jarat osztály egyetlen járat adatait reprezentálja.

Adattagok:

nev – célállomás neve

jaratszam – járatszám

kapu – indulási kapu

utasszam – utaslétszám

ETD – tervezett indulási idő

RTD – tényleges indulási idő

Metódus:

kiiras()
Formázott szöveget állít elő a járat adataiból, valamint kezeli a járat státuszát.

Státuszkezelés

A járatokhoz a következő státuszok tartozhatnak:

CANCELLED

Ha az utasszám kevesebb mint 60

A kapu és az RTD értéke ilyenkor "-"

OVERBOOKED

Ha az utasszám nagyobb mint 239

Ha egyik feltétel sem teljesül, a járat normál állapotú.

Kimenet

A program a járatokat a konzolra írja ki egységes formátumban, például:

BUD-Berlin | N8123 | Gate: A12 | PAX: 239/180 | ETD: 10:00 | RTD: - | 

A kimenet tartalmazza:

célállomást

járatszámot

kaput

utasszámot

ETD és RTD értékeket

státuszt (ha van)

Program futtatása

A program a következő módon futtatható:

python main.py

A futtatás feltétele, hogy a két bemeneti .txt fájl a programmal azonos mappában legyen.
