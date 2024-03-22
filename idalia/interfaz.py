import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
from cuenta import Cuenta
import json

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Caja Popular')
        self.geometry('300x300')

        self.cuentas = []
        self.numero_cuenta_actual = 1
        self.cuenta_seleccionada = tk.StringVar(self)
        self.cargar_cuentas()
        self.create_widgets()

    def create_widgets(self):
        tk.Button(self, text='Registrar Nueva Cuenta', command=self.registrar_cuenta).pack(pady=(10, 0))
        self.menu_cuentas = ttk.Combobox(self, textvariable=self.cuenta_seleccionada, state='readonly')
        self.menu_cuentas.pack(pady=10)
        self.actualizar_menu_cuentas()

        tk.Button(self, text='Consultar Saldo', command=self.consultar_saldo).pack(pady=5)
        tk.Button(self, text='Ingresar Efectivo', command=lambda: self.operacion_efectivo("ingreso")).pack(pady=5)
        tk.Button(self, text='Retirar Efectivo', command=lambda: self.operacion_efectivo("retiro")).pack(pady=5)
        tk.Button(self, text='Depositar a Otra Cuenta', command=self.depositar_a_otra_cuenta).pack(pady=5)

    def cargar_cuentas(self):
        try:
            with open('cuentas.json', 'r') as file:
                cuentas_data = json.load(file)
                for cuenta_data in cuentas_data:
                    cuenta = Cuenta(cuenta_data['numero_cuenta'], cuenta_data['titular'], cuenta_data['edad'], cuenta_data['saldo'])
                    self.cuentas.append(cuenta)
                    self.numero_cuenta_actual = max(self.numero_cuenta_actual, int(cuenta.numCuenta) + 1)
        except FileNotFoundError:
            pass

    def actualizar_menu_cuentas(self):
        cuentas_disponibles = [cuenta.numCuenta for cuenta in self.cuentas]
        self.menu_cuentas['values'] = cuentas_disponibles
        if cuentas_disponibles:
            self.menu_cuentas.current(0)
        else:
            self.cuenta_seleccionada.set('')

    def registrar_cuenta(self):
        titular = simpledialog.askstring("Titular", "Nombre del titular:")
        edad = simpledialog.askinteger("Edad", "Edad del titular:")
        saldo = simpledialog.askfloat("Saldo inicial", "Saldo inicial de la cuenta:")
        if titular and edad is not None and saldo is not None:
            numero_cuenta = str(self.numero_cuenta_actual).zfill(4)
            nueva_cuenta = Cuenta(numero_cuenta, titular, edad, saldo)
            self.cuentas.append(nueva_cuenta)
            self.numero_cuenta_actual += 1
            self.actualizar_menu_cuentas()
            messagebox.showinfo("Cuenta Registrada", f"La cuenta {numero_cuenta} ha sido registrada correctamente.")
            self.guardar_cuentas()
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")

    def obtener_cuenta_seleccionada(self):
        numero_cuenta = self.cuenta_seleccionada.get()
        for cuenta in self.cuentas:
            if cuenta.numCuenta == numero_cuenta:
                return cuenta
        return None

    def consultar_saldo(self):
        cuenta = self.obtener_cuenta_seleccionada()
        if cuenta:
            messagebox.showinfo("Saldo", cuenta.consultarSaldo())

    def operacion_efectivo(self, tipo):
        cuenta = self.obtener_cuenta_seleccionada()
        if cuenta:
            monto = simpledialog.askfloat("Monto", f"Ingresa el monto a {tipo}:")
            if monto is not None:
                if tipo == "ingreso":
                    resultado = cuenta.ingresarEfectivo(monto)
                else:  # retiro
                    resultado = cuenta.retirarEfectivo(monto)
                messagebox.showinfo("Resultado", resultado)
                self.guardar_cuentas()

    def depositar_a_otra_cuenta(self):
        cuenta_origen = self.obtener_cuenta_seleccionada()
        if cuenta_origen:
            numero_cuenta_destino = simpledialog.askstring("Cuenta Destino", "Número de cuenta destino:")
            cuenta_destino = next((c for c in self.cuentas if c.numCuenta == numero_cuenta_destino), None)
            if cuenta_destino:
                monto = simpledialog.askfloat("Monto", "Ingresa el monto a depositar:")
                if monto is not None:
                    resultado = cuenta_origen.depositarOtraCuenta(cuenta_destino, monto)
                    messagebox.showinfo("Resultado", resultado)
                    self.guardar_cuentas()
            else:
                messagebox.showerror("Error", "No se encontró la cuenta destino.")
        else:
            messagebox.showerror("Error", "No se ha seleccionado una cuenta de origen.")

    def guardar_cuentas(self):
        cuentas_data = [
            {
                'numero_cuenta': cuenta.numCuenta,
                'titular': cuenta.titular,
                'edad': cuenta.edad,
                'saldo': cuenta.saldo
            } for cuenta in self.cuentas
        ]
        with open('cuentas.json', 'w') as file:
            json.dump(cuentas_data, file)

if __name__ == "__main__":
    app = App()
    app.mainloop()
