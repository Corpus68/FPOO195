from tkinter import *
from tkinter import ttk
import tkinter as tk
from CONTROLADOR import *

objControlador= Controlador()
def ejecutarInsert():
    objControlador.insertUsuario(var1.get(),var2.get(),var3.get())

def busUsuario():
    usuarioBD=objControlador.buscarUsuario(varBus.get())
    # Limpiar el campo de texto antes de insertar el resultado nuevo
    resultado_text.delete("1.0", END)
    if usuarioBD == []:
        messagebox.showwarning("Nada", "Id no existe en BD")
    else:
        # Insertar el resultado en el campo de texto en vez de imprimirlo
        resultado_text.insert(END, str(usuarioBD))


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

#6. Pestaña 2: Buscar Usuario
Label (pestana2, text= "Guardar Usuario", fg="red", font=("Mono", 18)).pack()
varBus= tk.StringVar()
Label(pestana2, text="Id: ").pack()
Entry(pestana2, textvariable=varBus).pack()
Button(pestana2, text ="Buscar Usuario", command=busUsuario).pack()
Label (pestana2, text= "Registrado: ", fg="blue", font=("Mono", 15)).pack()
resultado_text = tk.Text(pestana2, height=5, width=52)
resultado_text.pack()




Ventana.mainloop()