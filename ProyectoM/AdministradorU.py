import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()
    root.title("Administración de usuarios")

    def search_user():
        pass

    def modify_user(user_id):
        pass

    def delete_user(user_id):
        pass

    def add_user():
        pass

    search_frame = ttk.Frame(root, padding="10")
    search_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

    tk.Label(search_frame, text="Buscar usuario:").grid(row=0, column=0)
    search_entry = tk.Entry(search_frame)
    search_entry.grid(row=0, column=1)
    search_button = ttk.Button(search_frame, text="BUSCAR", command=search_user)
    search_button.grid(row=0, column=2)

    users_frame = ttk.Frame(root, padding="10")
    users_frame.grid(row=1, column=0, sticky=(tk.W, tk.E))

    tk.Label(users_frame, text="ID").grid(row=0, column=0)
    tk.Label(users_frame, text="Nombre de usuario").grid(row=0, column=1)
    tk.Label(users_frame, text="Acciones").grid(row=0, column=2, columnspan=2)

    for i in range(1, 4):
        ttk.Button(users_frame, text="modificar usuario", command=lambda id=i: modify_user(id)).grid(row=i, column=2)
        ttk.Button(users_frame, text="eliminar", command=lambda id=i: delete_user(id)).grid(row=i, column=3)

    new_user_frame = ttk.Frame(root, padding="10")
    new_user_frame.grid(row=2, column=0, sticky=(tk.W, tk.E))

    tk.Label(new_user_frame, text="Ingresar usuario Nuevo").grid(row=0, column=0, columnspan=2)

    tk.Label(new_user_frame, text="Nombre:").grid(row=1, column=0)
    name_entry = tk.Entry(new_user_frame)
    name_entry.grid(row=1, column=1)

    tk.Label(new_user_frame, text="Contraseña:").grid(row=2, column=0)
    password_entry = tk.Entry(new_user_frame, show="*")
    password_entry.grid(row=2, column=1)

    tk.Label(new_user_frame, text="Departamento:").grid(row=3, column=0)
    department_entry = tk.Entry(new_user_frame)
    department_entry.grid(row=3, column=1)

    add_button = ttk.Button(new_user_frame, text="AGREGAR", command=add_user)
    add_button.grid(row=4, column=1)

    root.columnconfigure(0, weight=1)
    for frame in (search_frame, users_frame, new_user_frame):
        frame.columnconfigure(1, weight=1)

    root.mainloop()

if __name__ == "__main__":
    main()
