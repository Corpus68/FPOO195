numero = int(input("Ingresa un numero entero: "))
def collatz (numero):
    serie=[numero]
    while numero !=1:
        if numero % 2 == 0:
            numero = numero // 2
        else:
            numero = numero * 3 + 1
        serie.append(numero)
    return serie
serie = collatz (numero)
print("Serie collat del numero", numero, ":", serie)