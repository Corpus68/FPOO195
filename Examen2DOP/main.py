import tkinter as tk
from tkinter import messagebox
from Estudiente import estudiante

class InterfazEstudiente:
    def __init__(self, master):
        self.master = master
        self.master.titulo("Generador de matriculas estudiantil")
        
        self.label_nombre = tk.Label(master, text="Nombre del estudiante: ")
        self.label_nombre.grid(row=0, column= 0, padx= 5, pady= 5, sticky= 'w')
        self.entry_nombre = tk.Entry(master)
        self.entry_nombre.grid(row=0, column=0, padx= 5, pady= 5 )
        
        self.label_apellido_paterno = tk.Label(master, text="Apellido paterno: ")
        self.label_apellido_paterno.grid(row=1, column= 0, padx=5, pady=5, sticky='w')
        self.entry_apellido_paterno = tk.Entry(master)
        self.entry_apellido_paterno.grid(row=1, column=0, padx=5, pady=5)
        
        self.label_apellido_materno = tk.Label(master, text="Apellido materno: ")
        self.label_apellido_materno.grid(row=2, column=0, pady=5)