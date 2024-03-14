import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()
    root.title("Artículos")

    def search_article():
        pass

    def add_article():
        pass

    def delete_article(id):
        print(f"Eliminar artículo ID: {id}")

    def modify_article(id):
        print(f"Modificar artículo ID: {id}")

    
    search_frame = ttk.Frame(root, padding="10")
    search_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

    search_label = ttk.Label(search_frame, text="Buscar artículo")
    search_label.pack(side=tk.LEFT)

    search_entry = ttk.Entry(search_frame, width=50)
    search_entry.pack(side=tk.LEFT, padx=10)

    search_button = ttk.Button(search_frame, text="BUSCAR", command=search_article)
    search_button.pack(side=tk.LEFT)

    list_frame = ttk.Frame(root, padding="10")
    list_frame.grid(row=1, column=0, sticky=(tk.W, tk.E))

    article_id = "01"
    article_name = "Artículo xxx"
    article_label = ttk.Label(list_frame, text=f"{article_id} {article_name}")
    article_label.grid(row=0, column=0, sticky=tk.W)

    delete_button = ttk.Button(list_frame, text="eliminar", command=lambda: delete_article(article_id))
    delete_button.grid(row=0, column=1)

    modify_button = ttk.Button(list_frame, text="Modificar", command=lambda: modify_article(article_id))
    modify_button.grid(row=0, column=2)

    add_frame = ttk.Frame(root, padding="10")
    add_frame.grid(row=2, column=0, sticky=(tk.W, tk.E))

    add_label = ttk.Label(add_frame, text="Ingresar Artículo nuevo")
    add_label.pack()

    name_label = ttk.Label(add_frame, text="Nombre del artículo")
    name_label.pack()

    name_entry = ttk.Entry(add_frame, width=50)
    name_entry.pack(pady=5)

    add_button = ttk.Button(add_frame, text="AGREGAR", command=add_article)
    add_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
