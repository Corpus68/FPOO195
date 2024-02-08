import math

def area_circulo(radio):
    return math.pi * radio ** 2

def volumen_cilindro(radio, altura):
    area_base = area_circulo(radio)
    return area_base * altura

def main():
    radio_circulo = float(input("Ingrese el valor del radio del círculo: "))
    altura_cilindro = float(input("Ingrese el valor de la altura del cilindro: "))

    area_circulo_result = area_circulo(radio_circulo)
    volumen_cilindro_result = volumen_cilindro(radio_circulo, altura_cilindro)

    print(f"Area del circulo: {area_circulo_result}")
    print(f"Volumen del cilindro: {volumen_cilindro_result}")

main()
