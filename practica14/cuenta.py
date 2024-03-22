class Cuenta:
    def __init__(self, numero_cuenta=0, titular="Sin titular", edad=0):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.edad = edad
        self.saldo = 0

    def consultar_saldo(self):
        return self.saldo

    def ingresar_efectivo(self, cantidad):
        self.saldo += cantidad

    def retirar_efectivo(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            return True
        else:
            return False

    def transferir_efectivo(self, otra_cuenta, cantidad):
        if self.retirar_efectivo(cantidad):
            otra_cuenta.ingresar_efectivo(cantidad)
            return True
        else:
            return False
