# tkinter.py
import tkinter as tk
from tkinter import filedialog
from fajl_kezelo import fajlbeolvasas, fajlmentes
from main_belepes import karakterkonvertalas


class felulet:
    def __init__(self, root):
        self.root = root
        self.root.title("Szövegkonvertáló")

        self.text_content = tk.Text(self.root, wrap='word', width=60, height=10, background="lightgrey")
        self.text_content.pack(pady=10)

        self.load_button = tk.Button(self.root, text="Fájl betöltése", command=self.fajlbetoltes)
        self.load_button.pack(pady=5)

        self.file_path_label = tk.Label(self.root, text="Fájl elérési útvonala:")
        self.file_path_label.pack()

        self.encoding_var = tk.StringVar()
        self.encoding_var.set('utf-8')  # Kezdeti karakterkódolás beállítása

        self.encoding_label = tk.Label(self.root, text="Karakterkódolás:")
        self.encoding_label.pack()

        # Hozzáadott karakterkódolások
        self.encoding_options = ['utf-8', 'latin-1', 'utf-16', 'ISO-8859-1', 'cp1250', 'ascii', 'unicode_escape', 'ANSI']
        self.encoding_dropdown = tk.OptionMenu(self.root, self.encoding_var, *self.encoding_options)
        self.encoding_dropdown.pack(pady=5)

        self.save_button = tk.Button(self.root, text="Mentés", command=self.Szovegmentes)
        self.save_button.pack(pady=5)

    def fajlbetoltes(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            content = fajlbeolvasas(file_path)
            self.text_content.delete("1.0", tk.END)
            self.text_content.insert(tk.END, content)
            self.file_path_label.config(text=f"Fájl elérési útvonala: {file_path}")

    def TextKonvertalas(self):
        content = self.text_content.get("1.0", tk.END)
        target_encoding = self.encoding_var.get()
        converted_content = karakterkonvertalas(content, 'utf-8', target_encoding)
        if converted_content:
            self.text_content.delete("1.0", tk.END)
            self.text_content.insert(tk.END, converted_content.decode(target_encoding))

    def Szovegmentes(self):
        content = self.text_content.get("1.0", tk.END)
        target_encoding = self.encoding_var.get()
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            fajlmentes(file_path, content, encoding=target_encoding)
            print(f"A szöveg sikeresen mentve: {file_path}")
            self.file_path_label.config(text=f"Fájl elérési útvonala: {file_path}")


if __name__ == "__main__":
    root = tk.Tk()
    app = felulet(root)
    root.mainloop()