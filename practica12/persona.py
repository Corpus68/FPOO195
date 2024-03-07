class Persona:
    def __init__(self, nombre, correo, contraseña):
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña

    def __str__(self):
        return f"Nombre: {self.nombre}, Correo: {self.correo}, Contraseña: {self.contraseña}"

    def validar(self, correo, contraseña):
        return self.correo == correo and self.contraseña == contraseña
