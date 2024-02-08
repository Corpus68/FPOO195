saldo = 0

while True:
    entrada = input("Ingrese movimiento y cantidad (por ejemplo, 'D 1000'): ")
    if not entrada:
        break
    movimiento, cantidad = entrada.split()
    
    try:
        numero = float(cantidad.replace(',', '.'))  # Convertir a flotante
        if movimiento.upper() == 'D':
            saldo += numero
        elif movimiento.upper() == 'R':
            saldo -= numero
        else:
            print("Movimiento no válido. Use 'D' para depósito y 'R' para retiro.")
    except ValueError:
        print("Cantidad no válida. Ingrese un número válido.")

print(f"\nSaldo total $: {saldo}")

