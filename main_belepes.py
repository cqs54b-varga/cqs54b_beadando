# main_belepes.py
from fajl_kezelo import szoveg_mentese, karakterkodvaltas

# Például szöveg mentése
szoveg = "Ez egy példa szöveg."
fajlnev = "pelda_fajl.txt"
szoveg_mentese(szoveg, fajlnev)

# Például karakterkészlet megváltoztatása
uj_karakterkod = 'ISO-8859-1'  # Példa: Latin-1 karakterkészlet
if karakterkodvaltas(fajlnev, uj_karakterkod):
    print(f"A {fajlnev} fájl karakterkódja megváltoztatva {uj_karakterkod}-re.")
else:
    print(f"A karakterkódváltás sikertelen.")