import tkinter as tk
from tkinter import messagebox

def main():
    root = tk.Tk()
    root.title("Control de acceso")

    def submit_action():
        department = department_name_entry.get()
        password = password_entry.get()
        messagebox.showinfo("Login Attempt", f"Department: {department}\nPassword: {password}")

    tk.Label(root, text="Control de acceso", font=("Arial", 16)).pack(pady=(10, 5))
    tk.Label(root, text="Nombre de Usuario", font=("Arial", 12)).pack(pady=(5, 0))
    department_name_entry = tk.Entry(root, font=("Arial", 12))
    department_name_entry.pack(pady=(0, 5))
    tk.Label(root, text="Contraseña:", font=("Arial", 12)).pack(pady=(5, 0))
    password_entry = tk.Entry(root, show="*", font=("Arial", 12))
    password_entry.pack(pady=(0, 10))

    submit_button = tk.Button(root, text="ENVIAR", command=submit_action, font=("Arial", 12))
    submit_button.pack(pady=(5, 10))

    root.mainloop()

if __name__ == "__main__":
    main()
