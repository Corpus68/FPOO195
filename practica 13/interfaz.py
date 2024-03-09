import tkinter as tk
from tkinter import messagebox
from contraseña import generador

class Aplicacion:
    def __init__(self, master):
        self.master = master
        self.master.title ("Generador de contraseñas")
        self.contraseña_generador = generador()
        self.master.configure(bg = "blue")

        self.longitud = tk.IntVar(value=8)
        self.mayusculas = tk.BooleanVar()
        self.especiales = tk.BooleanVar()

        self.label_longitud = tk.Label(master, text="Longitud:")
        self.label_longitud.grid(row=0, column=0, padx=5, pady=5, sticky= "w")
        self.entry_longitud = tk.Entry(master, textvariable=self.longitud)
        self.entry_longitud.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        self.check_mayusculas = tk.Checkbutton(master, text="Incluir Mayúsculas", variable=self.mayusculas)
        self.check_mayusculas.grid(row=1, column=0, padx=5, pady=2, sticky= "w")

        self.check_especiales = tk.Checkbutton(master, text="Incluir Caracteres Especiales", variable=self.especiales)
        self.check_especiales.grid(row=2, column=0, padx=5, pady=5, sticky= "w")
        
        self.btn_generar = tk.Button(master, text="Generar contraseña", command=self.generar_contraseña)
        self.btn_generar.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="w")

        self.entrada_contraseña = tk.Entry(master, width=30)
        self.entrada_contraseña.grid(row=4, column=0, columnspan=2,padx=1,pady=5, sticky="w")
        self.btn_comprobar = tk.Button(master, text="Verificar fortaleza", command=self.comprobar_fortaleza)
        self.btn_comprobar.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky= "w")

    def generar_contraseña(self):
        longitud = self.longitud.get()
        mayusculas = self.longitud.get()
        especiales = self.especiales.get()
        
        self.contraseña_generador = generador(longitud, mayusculas, especiales)
        contraseña = self.contraseña_generador.generar()
        
        self.entrada_contraseña.delete(0,tk.END)
        self.entrada_contraseña.insert(0,contraseña)

    def comprobar_fortaleza(self):
        contraseña = self.entrada_contraseña.get()
        
        fortaleza = "DEBIL"
        if len(contraseña)>=8:
            if any(c.isupper() for c in contraseña) and any(c.islower() for c in contraseña) and any(c.isdigit() for c in contraseña):
                fortaleza = "Fuerte"
            elif len (contraseña)>=8:
                fortaleza = "Moderada"
            messagebox.showinfo("Fortaleza de contraseña", f"La fortaleza de la contraseña es: {fortaleza}")
def main():
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()
    
if __name__ == "__main__":
    main()
