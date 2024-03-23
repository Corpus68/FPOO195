from tkinter import *
from tkinter import ttk
import tkinter as tk
from CONTROLADOR import *

objControlador= Controlador()
def ejecutarInsert():
    objControlador.insertUsuario(var1.get(),var2.get(),var3.get())


Ventana= Tk()
Ventana.title("CRUD de usuarios")
Ventana.geometry("500x300")

#2 preparar el notebook para pestañas
panel= ttk.Notebook(Ventana)
panel.pack(fill='both', expand='yes')

#3 definir las pestañas del nootbook
pestana1= ttk.Frame(panel)
pestana2= ttk.Frame(panel)
pestana3= ttk.Frame(panel)
pestana4= ttk.Frame(panel)
pestana5= ttk.Frame(panel)


#4 agregamos las pestañas
panel.add(pestana1,text="Crear usuario")
panel.add(pestana2,text="Buscar usuario")
panel.add(pestana3,text="Consultar usuario")
panel.add(pestana4,text="Editar usuario")
panel.add(pestana5,text="Eliminar usuario")

#5 Pestaña 1: Formuladrio de insert
Label(pestana1, text="Registro de usuaios", fg="blue", font=("Modern",18)).pack()

var1= tk.StringVar()
Label(pestana1, text="Nombre: ").pack()
Entry(pestana1, textvariable=var1).pack()

var2= tk.StringVar()
Label(pestana1, text="Correo: ").pack()
Entry(pestana1, textvariable=var2).pack()

var3= tk.StringVar()
Label(pestana1, text="Contraseña: ").pack()
Entry(pestana1, textvariable=var3).pack()

Button(pestana1, text= "Guardar usuario",command=ejecutarInsert).pack()
Ventana.mainloop()