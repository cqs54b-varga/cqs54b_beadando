#tkinter_felulet.py
import tkinter as tk
from tkinter import filedialog
from fajl_kezelo import szoveg_mentese, karakterkodvaltas

class Fajlkezelo :
    def __init__(self, master):
        self.master = master
        master.title("Karakterkódolás")

        self.szoveg = tk.StringVar()
        self.szoveg.set("Ide írd a kívánt szöveget.")

        self.szoveg_input = tk.Entry(master, textvariable=self.szoveg, width=100, background="lightgrey" , )
        self.szoveg_input.pack(pady=10 )

        self.mentes_gomb = tk.Button(master, text="Szöveg mentése", command=self.szoveg_mentese)
        self.mentes_gomb.pack(pady=5)

        self.fajlvalaszto_gomb = tk.Button(master, text="Fájl kiválasztása", command=self.fajl_kivalasztasa)
        self.fajlvalaszto_gomb.pack(pady=5)

        self.kodvaltas_label = tk.Label(master, text="Válassz karakterkódot:")
        self.kodvaltas_label.pack(pady=5)

        self.karakterkod_valaszto = tk.StringVar()
        self.karakterkod_valaszto.set("utf-8")

        karakterkodok = ["utf-8", "ISO-8859-1", "windows-1252"]
        self.karakterkod_menu = tk.OptionMenu(master, self.karakterkod_valaszto, *karakterkodok)
        self.karakterkod_menu.pack(pady=5)

        self.kodvaltas_gomb = tk.Button(master, text="Karakterkódváltás", command=self.karakterkodvaltas)
        self.kodvaltas_gomb.pack(pady=5)

    def szoveg_mentese(self):
        szoveg = self.szoveg.get()
        fajlnev = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if fajlnev:
            szoveg_mentese(szoveg, fajlnev)
            tk.messagebox.showinfo("Mentés", f"A szöveg sikeresen el lett mentve a {fajlnev} fájlba.")

    def fajl_kivalasztasa(self):
        fajlnev = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if fajlnev:
            self.szoveg.set("")
            with open(fajlnev, 'r', encoding='utf-8') as fajl:
                self.szoveg.set(fajl.read())

    def karakterkodvaltas(self):
        fajlnev = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if fajlnev:
            uj_karakterkod = self.karakterkod_valaszto.get()
            if karakterkodvaltas(fajlnev, uj_karakterkod):
                tk.messagebox.showinfo("Karakterkódváltás", f"A {fajlnev} fájl karakterkódja megváltoztatva {uj_karakterkod}-re.")
            else:
                tk.messagebox.showerror("Hiba", "A karakterkódváltás sikertelen.")

if __name__ == "__main__":
    root = tk.Tk()
    app = Fajlkezelo(root)
    root.mainloop()