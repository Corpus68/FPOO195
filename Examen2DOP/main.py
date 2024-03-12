import tkinter as tk
from tkinter import messagebox
from Estudiente import Estudiante

class InterfazEstudiante:
    def __init__(self, master):
        self.master = master
        self.master.title("Generador de matriculas estudiantil")
        
        self.label_nombre = tk.Label(master, text="Nombre del estudiante: ")
        self.label_nombre.grid(row=0, column= 0, padx= 5, pady= 5, sticky= 'w')
        self.entry_nombre = tk.Entry(master)
        self.entry_nombre.grid(row=0, column=1, padx= 5, pady= 5 )
        
        self.label_apellido_paterno = tk.Label(master, text="Apellido paterno: ")
        self.label_apellido_paterno.grid(row=1, column= 0, padx=5, pady=5, sticky='w')
        self.entry_apellido_paterno = tk.Entry(master)
        self.entry_apellido_paterno.grid(row=1, column=1, padx=5, pady=5)
        
        self.label_apellido_materno = tk.Label(master, text="Apellido materno: ")
        self.label_apellido_materno.grid(row=2, column=0, pady=5, padx=5, sticky='w')
        self.entry_apellido_materno = tk.Entry(master)
        self.entry_apellido_materno.grid(row=2, column=1, padx=5, pady=5)
        
        self.label_ano_nacimiento = tk.Label(master, text="Ano de nacimiento: ")
        self.label_ano_nacimiento.grid(row=3, column=0, padx=5, pady=5, sticky='w')
        self.entry_ano_nacimiento = tk.Entry(master)
        self.entry_ano_nacimiento.grid(row=3, column=1, padx=5, pady=5)
        
        self.label_carrera = tk.Label(master, text="Carrera:")
        self.label_carrera.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.entry_carrera = tk.Entry(master)
        self.entry_carrera.grid(row=4, column=1, padx=5, pady=5)
        
        self.btn_generar_matricula = tk.Button(master, text="Generar Matrícula", command=self.generar_matricula)
        self.btn_generar_matricula.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
        
    def generar_matricula(self):
        nombre = self.entry_nombre.get()
        apellido_paterno = self.entry_apellido_paterno.get()
        apellido_materno = self.entry_apellido_materno.get()
        ano_nacimiento = int(self.entry_ano_nacimiento.get())
        carrera = self.entry_carrera.get()
        
        estudiante = Estudiante(nombre, apellido_paterno, apellido_materno, ano_nacimiento, carrera)
        matricula = estudiante.generar_matricula()
        
        messagebox.showinfo("Matrícula", f"La matrícula es: {matricula}")

def main():
    root = tk.Tk()
    app = InterfazEstudiante(root)
    root.mainloop()

if __name__ == "__main__":
    main()
