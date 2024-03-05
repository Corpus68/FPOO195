from tkinter import Tk  as tk 
from tkinter import Frame 
from tkinter import Button
from tkinter import messagebox

def mostrarmensajes():
    print(messagebox.showinfo('showinfo','Information'))
    print(messagebox.ERROR('showerror','ERROR'))
    print(messagebox.showwarning('showwaring','WARNING'))
    print(messagebox.askretrycancel(message="Desa continuar?",title="Soy el titulo"))

def addbtn():
    botonVerde.config(text="+")
    botonrosa = Button(seccion3, text="Nuevo", bg="#893C6A")
    botonrosa.configure(height=3, width=5)
    botonrosa.pack()

# Creamos la ventana
ventana = tk()  # Uso de POO creando objetos ventana
ventana.title("Practica 11")
ventana.geometry("600x400")

# Colocamos frames de la ventana
seccion1 = Frame(ventana, bg="black")
seccion1.pack(expand=True, fill='both')

seccion2 = Frame(ventana, bg="blue")
seccion2.pack(expand=True, fill='both')

seccion3 = Frame(ventana, bg="red")
seccion3.pack(expand=True, fill='both')

#3. Posicionar botones
#place
botonAzul= Button(seccion1, text="Azul", fg="#082359")
botonAzul.place(x=60, y=60, width=100, height= 30)

#grid
botonNegro= Button(seccion2, text= "Negro", fg="#FFFFFF", bg="#000000",command=mostrarmensajes)
botonNegro.configure(height=2,width=10)
botonNegro.grid(row=0,column=1)

botonAmarillo= Button(seccion2, text= "Amarillo", bg="#D9FF03",command=mostrarmensajes)
botonAmarillo.configure(height=2,width=10)
botonAmarillo.grid(row=1,column=2)

#pack
botonVerde= Button(seccion3, text= "Verde",fg="#FFFFFF", bg="#21E353",command=addbtn)
botonVerde.configure(height=2,width=10)
botonVerde.pack()

# Ejecuta
ventana.mainloop()
