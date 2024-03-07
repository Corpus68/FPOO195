import tkinter as tk
from tkinter import messagebox
from persona import Persona

class LoginApp:
    def __init__(self, usuarios):
        self.usuarios = usuarios

    def run(self):
        self.root = tk.Tk()
        self.root.title("Login")
        self.root.geometry("300x150")

        self.root.configure(bg="red")

        self.label_email = tk.Label(self.root, text="Correo:", bg="red", fg="white")
        self.label_email.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.entry_email = tk.Entry(self.root)
        self.entry_email.grid(row=0, column=1, padx=10, pady=10)

        self.label_password = tk.Label(self.root, text="Contraseña:", bg="red", fg="white")
        self.label_password.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.entry_password = tk.Entry(self.root, show="*")
        self.entry_password.grid(row=1, column=1, padx=10, pady=10)

        self.btn_login = tk.Button(self.root, text="Login", bg="blue", fg="white", command=self.validar_usuario)
        self.btn_login.grid(row=2, column=1, padx=10, pady=10, sticky="e")

        self.root.mainloop()

    def validar_usuario(self):
        email = self.entry_email.get()
        contraseña = self.entry_password.get()

        if not email or not contraseña:
            messagebox.showwarning("Error", "Por favor, complete todos los campos.")
            return

        for usuario in self.usuarios:
            if usuario.validar(email, contraseña):
                messagebox.showinfo("Bienvenido", f"Bienvenido, {usuario.nombre}!")
                self.root.destroy()
                return

        messagebox.showerror("Error", "Credenciales inválidas.")

if __name__ == "__main__":
    app = LoginApp([])
    app.run()
