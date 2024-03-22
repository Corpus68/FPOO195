class Cuenta:
    def __init__(self, numCuenta, titular, edad, saldo):
        self.numCuenta = numCuenta
        self.titular = titular
        self.edad = edad
        self.saldo = saldo

    def consultarSaldo(self):
        return f"La cuenta No {self.numCuenta} tiene un saldo actual de : ${self.saldo}"

    def ingresarEfectivo(self, cantidad):
        self.saldo += cantidad
        return f"Se han depositado ${cantidad}. Tu saldo actual es ${self.saldo}"

    def retirarEfectivo(self, cantidad):
        if cantidad > self.saldo:
            return "Fondos insuficientes."
        else:
            self.saldo -= cantidad
            return f"Se retiró ${cantidad}. Su saldo actual es ${self.saldo}"

    def depositarOtraCuenta(self, cuentaDestino, cantidad):
        if cantidad > self.saldo:
            return "Fondos insuficientes."
        else:
            self.saldo -= cantidad
            cuentaDestino.saldo += cantidad
            return f"Se transfirieron ${cantidad} a la cuenta {cuentaDestino.numCuenta}. Su saldo actual es ${self.saldo}"
