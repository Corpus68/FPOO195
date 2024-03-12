import random
class Estudiante:
    ano_cursaso= 2024
    def __init__(self, nombre, apellido_paterno, apellido_materno, ano_nacimiento, carrera):
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.ano_nacimiento = ano_nacimiento
        self.carrera = carrera
    
    def generar_matricula(self):
        matricula = (
            self.carrera[:3].upper() +
            str(self.ano_cursaso)[-2:] +
            str(self.ano_nacimiento)[-2:] +
            self.nombre[0] +
            self.apellido_paterno[:3] +
            self.apellido_materno[:3] +
            ''.join(str(random.randint(0, 9)) for _ in range(3))
        )
        return matricula

    
        
        
    

        