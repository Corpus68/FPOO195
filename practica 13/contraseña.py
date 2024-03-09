import string
import secrets

class generador:
    def __init__(self, longitud =8, mayusculas = True, especiales = False) :
        self.longitud = longitud
        self.mayusculas = mayusculas
        self.especiales = especiales
    
    def generar(self):
        mayusculas = string.ascii_uppercase if self.mayusculas else ''
        especiales = string.punctuation if self.especiales else ''
        caracteres = string.ascii_letters + string.digits + mayusculas + especiales
        contrasena = ''.join(secrets.choice(caracteres) for _ in range(self.longitud))

        return contrasena