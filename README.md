# Varga László CQS54B Szkript nyelvek beadandó
Beadandó leírása: A feladatom az volt hogy a bekért sz 


3 Modulom:
- fajl_kezelo              Modul felelős a fájlkezelésért, beleértve a szöveges tartalom beolvasását, kódolását és mentését.
- kodolas                  Modul tartalmazza a karakterkódolás konverziójáért felelős függvényeket.
- tkinter_felulet          modul kezeli a grafikus felhasználói felületet és az eseményeket.




fajl_kezelo.py:

A read_file függvény a megadott fájl elérési útvonalról beolvassa a szöveget és visszaadja azt.
A save_file függvény a megadott fájl elérési útvonalon menti el a szöveget a megadott karakterkódolással.
Ez a modul felelős a fájlkezelésért.


kodolas.py:

A convert_encoding függvény a megadott szöveget átkonvertálja a forrás karakterkódolásról a cél karakterkódolásra, és a konvertált szöveget adja vissza.
Ez a modul a karakterkódolás konverziójáért felel.


tkinter.py:

Az TextConverterApp osztály a tkinter modult használva létrehoz egy grafikus felhasználói felületet (GUI-t) egy szövegkonvertáló alkalmazáshoz.
Az osztályban van egy szöveges mező (text_content), egy "Fájl betöltése" gomb (load_button), egy címke a fájl elérési útvonalához (file_path_label), egy legördülő menü a karakterkódolás kiválasztásához (encoding_dropdown), és egy "Mentés" gomb (save_button).
Az load_file metódus betölt egy szövegfájlt a kiválasztott fájl elérési útvonallal, és megjeleníti a szöveget a szöveges mezőben.
A convert_text metódus megváltoztatja a szöveg karakterkódolását a kiválasztott karakterkódolásra.
A save_text metódus menti a szöveget a kiválasztott karakterkódolással a kiválasztott fájl elérési útvonalon.
Az alkalmazás használ eseménykezelést, például a gombokra kattintást és a fájl kiválasztását.
