from tkinter import messagebox
import sqlite3
import bcrypt 

class Controlador:
    def conexion(self):
        try:
            conex = sqlite3.connect("C:/Users/dieco/OneDrive/Documentos/Fundamentos de programacion/FPOO195/TK-SQLITE/db195.db")
            print("Conectado")
            return conex
        except sqlite3.OperationalError:
            print("No se pudo concetar")
    def encriptapass(self, cont):
        passPlana = cont
        passPlana =passPlana.encode()
        sal = bcrypt.gensalt()
        passHash = bcrypt.hashpw(passPlana, sal)
        return passHash
    
    def insertUsuario(self, nom,corr, cont):
        conexion= self.conexion()

        if(nom == "" or corr == "" or cont==""):
            messagebox.showwarning("Cuidado", "Inputs vacios" )
            conexion.close()

        else:
            cursor =conexion.cursor()
            conH=self.encriptapass(cont)
            datos = (nom, corr, conH)
            sqlInsert= "insert into tbUsuarios(nombre, correo, contra) values(?, ?,?)"

            cursor.execute (sqlInsert, datos)
            conexion.commit()
            conexion.close()
            messagebox.showinfo("Exito", "Exito")

    def buscarUsuario(self,id):
        conex= self.conexion()
        
        if(id== ''):
            messagebox.showwarning("Cuidado","Inputs vacios no sea tibio")
            conex.close()
        else:
            try:
                cursor = conex.cursor()
                sqlSelect= "select * from tbUsuarios where id="+id
                cursor.execute(sqlSelect)
                usuario= cursor.fetchall()
                conex.close()
                return usuario       
            except sqlite3.OperationalError:
                print("No se pudo ejecutar la busqueda")
    
    def todosUsuarios(self):
        conex= self.conexion()
        try:
            cursor= conex.cursor()
            cursor.execute("SELECT *FROM tbUsuarios")
            usuarios = cursor.fetchall()
            conex.close()
            return usuarios
        except sqlite3.OperationalError as e:
            messagebox.showerror("Error", f"No existe: {e}")
            return []
        
        



