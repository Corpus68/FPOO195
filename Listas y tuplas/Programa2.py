import random
def generar_lista():
    return tuple(random.randint(10,20) for _ in range(30))

def contar (tupla):
    conteo = {}
    for elemento in tupla:
        if elemento in conteo:
            conteo[elemento] += 1
        else:
            conteo[elemento] = 1
    return conteo

def eliminar (tupla):
    return tuple(set(tupla))

def remplazar (tupla):
    conteo = contar(tupla)
    nueva_tupla = []
    for elemento in tupla:
        if conteo[elemento]>1:
            nueva_tupla.append(0)
            conteo[elemento] -=1
        else:
            nueva_tupla.append(elemento)
    return

def reemplazar_repetidos(tupla):
    conteo = contar(tupla)
    nueva_tupla = []
    for elemento in tupla:
        if conteo[elemento] > 1:
            nueva_tupla.append(0)
            conteo[elemento] -= 1
        else:
            nueva_tupla.append(elemento)
    return tuple(nueva_tupla)

# Función principal
def main():
    tupla = generar_lista()
    print("Tupla generada:", tupla)

    opcion = input("Selecciona una opción:\n"
                   "a. Contar número repetidos\n"
                   "b. Eliminar número repetidos\n"
                   "c. Reemplazar los repetidos con 0\n"
                   "Opción: ")

    if opcion == 'a':
        conteo = contar(tupla)
        print("Conteo de números repetidos:")
        for numero, cantidad in conteo.items():
            print(f"Número {numero}: {cantidad} veces")

    elif opcion == 'b':
        tupla_sin_repetidos = eliminar(tupla)
        print("Tupla sin números repetidos:", tupla_sin_repetidos)

    elif opcion == 'c':
        tupla_reemplazada = reemplazar_repetidos(tupla)
        print("Tupla con números repetidos reemplazados por 0:", tupla_reemplazada)

    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()

