from series import Serie

def main():
    titulo = input ("Ingrese el titulo de la serie: ")
    genero = input ("Ingrese el tipo de serie: ")
    serie1 = Serie (titulo, genero)
    
    print(f"Titulo de tu seire: {serie1.get_titulo()}")
    print(F"Estado de tu serie: {serie1.get_status}")
    
    print (serie1.reproducir())
    print (serie1.agregar_a_mi_lista())
    
    terminada = input ("Terminaste tu serie? SI O NO? ")
    
    if terminada.lower () == 'Si':
        serie1.marcar_como_completada()
        print(f"Serie terminada: {serie1.get_titulo()}")
        
    calificacion = int(input("Ingrese la calificacion de la serie (0-10) "))
    serie1.calificar(calificacion)
    print(f"Calificacion de {serie1.get_titulo}: ")
    
if __name__=="__main__":
    main
        
    
    