class Serie:
    def __init__(self, titulo, genero, calificacion=0):
        self.titulo = titulo
        self.horas_estimadas = 10
        self.status = "Sin reproducir"
        self.genero = genero
        self.calificacion = calificacion
    
    def reproducir(self):
        return f"reproduciendo {self.titulo}"
    def agregar_a_mi_lista(self):
        return f"Agregado {self.titulo} a mi lista"
    def marcar_como_completada(self):
        self._status = "completado"
    def calificar(self, calificacion):
        self._calificacion = calificacion
    
    def get_titulo(self):
        return self.__titulo
    def get_horas_estimadas(self):
        return self.__horas_estimadas 
    def get_status(self):
        return self.status
    
    def get_calificacion(self):
        return self.calificacion