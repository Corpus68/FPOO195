altura = int(input("Ingrese la altura del triángulo: "))

for i in range(1, altura + 1):
    numeros = list(range(i, 0, -1))
    fila = ''.join(map(str, numeros))
    print(fila)
