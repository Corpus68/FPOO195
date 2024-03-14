import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Pedidos")

def search_order():
    pass

def update_status():
    pass

search_frame = ttk.Frame(root, padding="10")
search_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

tk.Label(search_frame, text="Buscar pedido:").grid(row=0, column=0)
search_entry = tk.Entry(search_frame)
search_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

status_frame = ttk.Frame(root, padding="10")
status_frame.grid(row=0, column=1, sticky=(tk.W, tk.E))

tk.Label(status_frame, text="Status:").grid(row=0, column=0)
status_entry = tk.Entry(status_frame)
status_entry.grid(row=0, column=1)

update_button = ttk.Button(root, text="Notificar el status del pedido", command=update_status)
update_button.grid(row=1, column=0, columnspan=2)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
search_frame.columnconfigure(1, weight=1)
status_frame.columnconfigure(1, weight=1)

root.mainloop()
