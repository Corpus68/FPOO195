from tkinter import *
from tkinter import ttk
import tkinter as tk 
from Controlador import *
from GeneradorPDF import *
import os

objControlador= Controlador ()
objPDF= GeneradorPDF()
def ejecutaInsert():
    objControlador.insertUsuario(var1.get(), var2.get(), var3.get())

def busUsuario():
    usuarioBD=objControlador.buscarUsuario(varBus.get())
    busqueda.delete("1.0", END)
    if usuarioBD == []:
        messagebox.showwarning("Nada", "No existe en base de datos")
    else:
        busqueda.insert(END, str(usuarioBD))
def ejecutaPDF():
    if varTitulo=="":
        messagebox.showwarning("Importante", "Escribe u nombre en el PDF SUBNORMAL")
    else:
        objPDF.add_page()
        objPDF.chapter_body()
        objPDF.output(varTitulo.get()+".pdf")
        rutaPDF = "C:/Users/dieco/OneDrive/Documentos/Fundamentos de programacion/FPOO195/TK-SQLITE/GeneradorPDF.py"+varTitulo.get()+".pdf"
        messagebox.showinfo("Archivo creado","PDF disponible en la carpeta")
        os.system(f"start {rutaPDF}")
        
def TreeView():
    global lista
    lista = ttk.Treeview(pestana3, columns=("Id", "Nombre", "Correo", "Contraseña"), show="headings")
    lista.heading("Id", text="ID") 
    lista.heading("Nombre", text="Nombre")
    lista.heading("Correo", text="Correo")
    lista.heading("Contraseña", text="Contraseña")
    lista.pack(fill=BOTH, expand=True)

def conUsuario():
    usuarios = objControlador.todosUsuarios()
    for i in lista.get_children():
        lista.delete(i)
    for usuario in usuarios:
        lista.insert("", END, values=usuario)
    
# 1 Crear la ventana
Ventana = Tk()
Ventana.title("CRUD de Usuarios")
Ventana.geometry("500x300")

# 2 Preparar el notebook para las pestañas
panel = ttk.Notebook(Ventana)
panel.pack(fill='both', expand="yes")

# 3 Definir las pestañas del notebook
pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)
pestana5 = ttk.Frame(panel)
pestana6 = ttk.Frame(panel)

# 4 Agregamos las pestañas 

panel.add(pestana1, text="Crear Usuario")
panel.add(pestana2, text="Buscar Usuario")
panel.add(pestana3, text="Consultar Usuario")
panel.add(pestana4, text="Editar Usuario")
panel.add(pestana5, text="Borrar Usuario")
panel.add(pestana6, text="Exportar un PDF")


# 5 Pestaña 1: Formulario de Insert 
Label (pestana1, text= "Registro de Usuarios", fg="blue", font=("Modern", 18)).pack()

var1= tk.StringVar()
Label(pestana1, text="Nombre").pack()
Entry(pestana1, textvariable=var1).pack()

var2= tk.StringVar()
Label(pestana1, text="Correo").pack()
Entry(pestana1, textvariable=var2).pack()

var3= tk.StringVar()
Label(pestana1, text="Contraseña").pack()
Entry(pestana1, textvariable=var3).pack()

Button(pestana1, text ="Guardar Usuario", command=ejecutaInsert).pack()

#6. Pestaña 1: Buscar usuario.

Label (pestana2, text= "Guardar Usuario", fg="red", font=("Mono", 18)).pack()
varBus= tk.StringVar()
Label(pestana2, text="Id: ").pack()
Entry(pestana2, textvariable=varBus).pack()
Button(pestana2, text ="Buscar Usuario", command=busUsuario).pack()
Label (pestana2, text= "Registrado: ", fg="blue", font=("Mono", 14)).pack()
busqueda = tk.Text(pestana2, height=5, width=52)
busqueda.pack()

#7. Pestaña 3: Consultar Usuario

Label(pestana3, text="Usuarios", fg ="blue", font=("Mono", 15)).pack()
TreeView()
Button(pestana3, text="Actualizar Lista de Usuarios", command=conUsuario).pack()

#Pestaña 6: exportar PDF
Label (pestana6, text= "Usuarios en PDF", fg="green", font=("Mono", 18)).pack()
varTitulo= tk.StringVar()
Label(pestana6, text="Escribe el titulo de tu archivo:  ").pack()
Entry(pestana6, textvariable=varTitulo).pack()

Button(pestana6, text="Crear PDF", command=ejecutaPDF).pack()
Ventana.mainloop()