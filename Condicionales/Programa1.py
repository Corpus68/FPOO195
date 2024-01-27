contraseña = "12345"

ingresa = input("Ingrese la contraseña: ")

if ingresa.lower() == contraseña.lower():
    print("La contraseña es correcta")
else:
    print("La contraseña es incorrecta.")
