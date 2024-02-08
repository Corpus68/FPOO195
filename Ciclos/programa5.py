altura = int(input("Ingrese la altura del triángulo: "))
contador = 1
while contador <= altura:
    fila = 0
    while fila < altura - contador:
        print("", end='')
        fila +=1
    signos = contador
    while signos >=1:
        print(signos, end=' ')
        signos -= 2
    print()
    contador += 2
