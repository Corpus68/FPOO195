def calcular(sin_iva, iva=21):
    factura = sin_iva * (1 + iva / 100)
    return factura

if __name__ == "__main__":
    sin_iva = float(input("Ingrese la cantidad sin IVA: "))

    porcentaje = input("Ingrese el porcentaje de IVA personalizado (si no ingresa, se aplicará el 21% por defecto): ")
    if porcentaje:
        porcentaje = float(porcentaje)
        total = calcular(sin_iva, porcentaje)
        print(f"Total de la factura con {porcentaje}% de IVA: {total}")
    else:
        totaliva = calcular(sin_iva)
        print(f"Total de la factura con 21% de IVA: {totaliva}")
    