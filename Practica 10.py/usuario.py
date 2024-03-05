class usuario:
    def __init__(self, nombre, contrasena, correo, numero="", calle="", genero="", ciudad="", fecha=""):
        self.__nombre = nombre
        self.__contrasena = contrasena
        self.__correo = correo
        self.__numero = numero
        self.__calle = calle
        self.__genero = genero
        self.__ciudad = ciudad
        self.__fecha = fecha
    def get_nombre(self):
        return self.__nombre
    def get_contrasena(self):
        return self.__contrasena
    def get_correo(self):
        return self.__correo
    def get_numero(self):
        return self.__numero
    def set_numero(self, numero):
        self.__numero = numero
    def get_calle(self):
        return self.__calle
    def set_calle(self, calle):
        self.__calle = calle
    def get_fecha(self):
        return self.__fecha
    def set_feca(self, fecha):
        self
