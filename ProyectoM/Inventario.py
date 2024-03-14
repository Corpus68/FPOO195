import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()
    root.title("Inventario de artículos")

    def search():
        pass

    def generate_report():
        pass

    # Search section
    search_frame = ttk.Frame(root, padding="10")
    search_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

    search_label = ttk.Label(search_frame, text="Artículos")
    search_label.pack(side=tk.LEFT)

    search_entry = ttk.Entry(search_frame, width=50)
    search_entry.pack(side=tk.LEFT, padx=10)

    search_button = ttk.Button(search_frame, text="BUSCAR", command=search)
    search_button.pack(side=tk.LEFT)

    # Article list section
    article_frame = ttk.Frame(root, padding="10")
    article_frame.grid(row=1, column=0, sticky=(tk.W, tk.E))

    article_list = tk.Listbox(article_frame, height=4)
    article_list.insert(1, "01 Artículo xxx")
    article_list.insert(2, "02 Artículo yyy")
    article_list.pack(fill=tk.BOTH, expand=True)

    # Graph section
    graph_frame = ttk.Frame(root, padding="10")
    graph_frame.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    graph_label = ttk.Label(graph_frame, text="Gráfica de Destacados")
    graph_label.pack()

    graph_canvas = tk.Canvas(graph_frame, bg="gray", height=150)
    graph_canvas.pack(fill=tk.BOTH, expand=True)

    # Reports section
    report_frame = ttk.Frame(root, padding="10")
    report_frame.grid(row=3, column=0, sticky=(tk.W, tk.E))

    reports_label = ttk.Label(report_frame, text="Reportes")
    reports_label.pack()

    report_buttons_frame = ttk.Frame(report_frame, padding="10")
    report_buttons_frame.pack(fill=tk.BOTH, expand=True)

    reports = [
        ("Todos los Artículos", generate_report),
        ("Pedidos por departamento", generate_report),
        ("Pedidos por fecha", generate_report)
    ]

    for text, command in reports:
        button = ttk.Button(report_buttons_frame, text=text, command=command)
        button.pack(fill=tk.X)

    root.mainloop()

if __name__ == "__main__":
    main()
