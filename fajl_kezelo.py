# fajl_kezelo.py


import os
import chardet
def szoveg_mentese(szoveg, fajlnev):
    """Egy adott szöveg mentése egy txt fájlba."""
    with open(fajlnev, 'w', encoding='utf-8') as fajl:
        fajl.write(szoveg)

def karakterkodvaltas(fajlnev, uj_karakterkod):
    """Egy adott txt fájl karakterkészletének megváltoztatása."""
    try:
        with open(fajlnev, 'rb') as fajl_olvas:
            tartalom_bin = fajl_olvas.read()

        # Kódolás felismerése a chardet segítségével
        felismeres = chardet.detect(tartalom_bin)
        eredeti_kodolas = felismeres['encoding']

        # Szöveg dekódolása az eredeti kódolással
        tartalom = tartalom_bin.decode(eredeti_kodolas, errors='replace')

        with open(fajlnev, 'w', encoding=uj_karakterkod, errors='replace') as fajl_ir:
            fajl_ir.write(tartalom)

        return True
    except Exception as e:
        print(f"Hiba a karakterkészlet megváltoztatásakor: {e}")
        return False
