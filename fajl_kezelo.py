# fajl_kezelo.py


import os
def szoveg_mentese(szoveg, fajlnev):
    """Egy adott szöveg mentése egy txt fájlba."""
    with open(fajlnev, 'w', encoding='utf-8') as fajl:
        fajl.write(szoveg)


def karakterkodvaltas(fajlnev, uj_karakterkod):
    """Egy adott txt fájl karakterkészletének megváltoztatása."""
    try:
        with open(fajlnev, 'r', encoding='utf-8') as fajl_olvas:
            tartalom = fajl_olvas.read()

        with open(fajlnev, 'w', encoding=uj_karakterkod) as fajl_ir:
            fajl_ir.write(tartalom)

        return True
    except Exception as e:
        print(f"Hiba a karakterkészlet megváltoztatásakor: {e}")
        return False