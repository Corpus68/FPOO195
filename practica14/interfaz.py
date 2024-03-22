import tkinter as tk
from tkinter import messagebox, simpledialog
from cuenta import Cuenta

class AplicacionCaja(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Caja Popular")
        self.geometry("300x300")

        self.cuentas = {}  
        self.cuenta_actual = None  

        self.frame_cuenta = tk.Frame(self)
        self.frame_cuenta.pack(pady=10, anchor=tk.W)

        self.btn_seleccionar_cuenta = tk.Button(self.frame_cuenta, text="Seleccionar Cuenta", command=self.seleccionar_cuenta)
        self.btn_seleccionar_cuenta.pack(side=tk.LEFT)

        self.btn_registrar_cuenta = tk.Button(self.frame_cuenta, text="Registrar Nueva Cuenta", command=self.registrar_cuenta)
        self.btn_registrar_cuenta.pack(side=tk.LEFT)

        self.frame_saldo = tk.Frame(self)
        self.frame_saldo.pack(pady=10, anchor=tk.W)

        self.label_saldo = tk.Label(self.frame_saldo, text="Saldo disponible: ")
        self.label_saldo.pack(side=tk.LEFT)

        self.btn_consultar = tk.Button(self.frame_saldo, text="Consultar Saldo", command=self.consultar_saldo)
        self.btn_consultar.pack(side=tk.LEFT)

        self.frame_botones = tk.Frame(self)
        self.frame_botones.pack(pady=10, anchor=tk.W)

        self.btn_ingresar = tk.Button(self.frame_botones, text="Ingresar Efectivo", command=self.abrir_ventana_ingresar)
        self.btn_ingresar.grid(row=0, column=0, padx=5)

        self.btn_retirar = tk.Button(self.frame_botones, text="Retirar Efectivo", command=self.abrir_ventana_retirar)
        self.btn_retirar.grid(row=0, column=1, padx=5)

        self.btn_transferir = tk.Button(self.frame_botones, text="Transferir a otra cuenta", command=self.abrir_ventana_transferir)
        self.btn_transferir.grid(row=1, column=0, columnspan=2, pady=5)

    def seleccionar_cuenta(self):
        numero_cuenta = simpledialog.askinteger("Seleccionar Cuenta", "Ingrese el número de cuenta:")
        if numero_cuenta in self.cuentas:
            self.cuenta_actual = self.cuentas[numero_cuenta]
            messagebox.showinfo("Cuenta Seleccionada", f"Cuenta {numero_cuenta} seleccionada correctamente.")
        else:
            messagebox.showerror("Error", "Cuenta no encontrada.")

    def registrar_cuenta(self):
        numero_cuenta = simpledialog.askinteger("Registrar Cuenta", "Ingrese el número de la nueva cuenta:")
        if numero_cuenta not in self.cuentas:
            titular = simpledialog.askstring("Registrar Cuenta", "Ingrese el titular de la cuenta:")
            edad = simpledialog.askinteger("Registrar Cuenta", "Ingrese la edad del titular:")
            self.cuentas[numero_cuenta] = Cuenta(numero_cuenta, titular, edad)
            messagebox.showinfo("Cuenta Registrada", f"Cuenta {numero_cuenta} registrada exitosamente.")
        else:
            messagebox.showerror("Error", "Una cuenta con ese número ya existe.")

    def consultar_saldo(self):
        if self.cuenta_actual:
            saldo = self.cuenta_actual.consultar_saldo()
            messagebox.showinfo("Saldo", f"Su saldo disponible es: {saldo}")
        else:
            messagebox.showerror("Error", "No hay ninguna cuenta seleccionada.")

    def abrir_ventana_ingresar(self):
        if self.cuenta_actual:
            VentanaIngresar(self)
        else:
            messagebox.showerror("Error", "No hay ninguna cuenta seleccionada.")

    def abrir_ventana_retirar(self):
        if self.cuenta_actual:
            VentanaRetirar(self)
        else:
            messagebox.showerror("Error", "No hay ninguna cuenta seleccionada.")

    def abrir_ventana_transferir(self):
        if self.cuenta_actual:
            VentanaTransferir(self)
        else:
            messagebox.showerror("Error", "No hay ninguna cuenta seleccionada.")

class VentanaIngresar(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Ingresar Efectivo")
        self.geometry("200x120")

        self.label_cantidad = tk.Label(self, text="Ingrese la cantidad a depositar:")
        self.label_cantidad.pack(pady=5, anchor=tk.W)

        self.entry_cantidad = tk.Entry(self)
        self.entry_cantidad.pack(pady=5, anchor=tk.W)

        self.btn_ingresar = tk.Button(self, text="Ingresar", command=self.ingresar)
        self.btn_ingresar.pack(pady=5, anchor=tk.W)

    def ingresar(self):
        cantidad = float(self.entry_cantidad.get())
        self.parent.cuenta_actual.ingresar_efectivo(cantidad)
        messagebox.showinfo("Depósito Exitoso", "El efectivo ha sido depositado correctamente.")
        self.parent.consultar_saldo()
        self.destroy()

class VentanaRetirar(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Retirar Efectivo")
        self.geometry("200x120")

        self.label_cantidad = tk.Label(self, text="Ingrese la cantidad a retirar:")
        self.label_cantidad.pack(pady=5, anchor=tk.W)

        self.entry_cantidad = tk.Entry(self)
        self.entry_cantidad.pack(pady=5, anchor=tk.W)

        self.btn_retirar = tk.Button(self, text="Retirar", command=self.retirar)
        self.btn_retirar.pack(pady=5, anchor=tk.W)

    def retirar(self):
        cantidad = float(self.entry_cantidad.get())
        if self.parent.cuenta_actual.retirar_efectivo(cantidad):
            messagebox.showinfo("Retiro Exitoso", "El efectivo ha sido retirado correctamente.")
            self.parent.consultar_saldo()
            self.destroy()
        else:
            messagebox.showerror("Error", "Saldo insuficiente")

class VentanaTransferir(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Transferir a otra cuenta")
        self.geometry("250x150")

        self.label_numero_cuenta = tk.Label(self, text="Ingrese el número de cuenta destinataria:")
        self.label_numero_cuenta.pack(pady=5, anchor=tk.W)

        self.entry_numero_cuenta = tk.Entry(self)
        self.entry_numero_cuenta.pack(pady=5, anchor=tk.W)

        self.label_cantidad = tk.Label(self, text="Ingrese la cantidad a transferir:")
        self.label_cantidad.pack(pady=5, anchor=tk.W)

        self.entry_cantidad = tk.Entry(self)
        self.entry_cantidad.pack(pady=5, anchor=tk.W)

        self.btn_transferir = tk.Button(self, text="Transferir", command=self.transferir)
        self.btn_transferir.pack(pady=5, anchor=tk.W)

    def transferir(self):
        numero_cuenta_destinataria = int(self.entry_numero_cuenta.get())
        cantidad = float(self.entry_cantidad.get())
        if numero_cuenta_destinataria in self.parent.cuentas:
            cuenta_destinataria = self.parent.cuentas[numero_cuenta_destinataria]
            if self.parent.cuenta_actual.transferir_efectivo(cuenta_destinataria, cantidad):
                messagebox.showinfo("Transferencia Exitosa", "La cantidad ha sido transferida exitosamente.")
                self.parent.consultar_saldo()
                self.destroy()
            else:
                messagebox.showerror("Error", "Saldo insuficiente")
        else:
            messagebox.showerror("Error", "La cuenta destinataria no existe.")

if __name__ == "__main__":
    app = AplicacionCaja()
    app.mainloop()

