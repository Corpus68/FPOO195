numero = int(input("Ingresa un numero entero"))
cuenta_regresiva = []

for i in range (numero, -1, -1):
    cuenta_regresiva.append(str(i))
print(f"{cuenta_regresiva}")
