import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()
    root.title("Solicitud de artículos")

    def add_to_cart():
        pass

    def view_cart():
        pass

    def complete_purchase():
        pass

    def verify_order_status():
        pass

    search_article_frame = ttk.Frame(root, padding="10")
    search_article_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

    tk.Label(search_article_frame, text="Buscar artículo:").grid(row=0, column=0)
    article_search_entry = tk.Entry(search_article_frame)
    article_search_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))
    add_to_cart_button = ttk.Button(search_article_frame, text="Agregar artículo", command=add_to_cart)
    add_to_cart_button.grid(row=0, column=2)

    cart_frame = ttk.Frame(root, padding="10")
    cart_frame.grid(row=1, column=0, sticky=(tk.W, tk.E))
    tk.Label(cart_frame, text="Carrito de compras").grid(row=0, column=0)
    for i in range(1, 4):
        tk.Label(cart_frame, text=f"{i}. Item").grid(row=i, column=0, sticky=(tk.W))
    view_cart_button = ttk.Button(cart_frame, text="Ver carrito", command=view_cart)
    view_cart_button.grid(row=4, column=0, sticky=(tk.W))

    purchase_button = ttk.Button(root, text="Realizar compra", command=complete_purchase)
    purchase_button.grid(row=2, column=0, sticky=(tk.W))

    order_status_button = ttk.Button(root, text="Verificar estatus de pedido", command=verify_order_status)
    order_status_button.grid(row=3, column=0, sticky=(tk.W))

    root.columnconfigure(0, weight=1)
    search_article_frame.columnconfigure(1, weight=1)

    root.mainloop()

if __name__ == "__main__":
    main()
