from usuario import Persona, RegistroUsuarios

def menu():
    print("\nMenu de opciones:")
    print("1. Registrar usuario")
    print("2. Mostrar usuarios registrados")
    print("3. Buscar usuario por correo electrónico")
    print("4. Eliminar usuario por correo electrónico")
    print("5. Editar información de usuario")
    print("6. Salir")

if __name__ == "__main__":
    registro = RegistroUsuarios()

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del usuario: ")
            correo = input("Ingrese el correo electrónico del usuario: ")
            contrasena = input("Ingrese la contraseña del usuario: ")
            numero = input("Ingrese el número telefónico del usuario: ")
            calle = input("Ingrese la calle del usuario: ")
            genero = input("Ingrese el género del usuario: ")
            ciudad = input("Ingrese la ciudad del usuario: ")
            fecha = input("Ingrese la fecha de registro del usuario (YYYY-MM-DD): ")

            nuevo_usuario = Persona(nombre, contrasena, correo, numero, calle, genero, ciudad, fecha)
            registro.agregar_usuario(nuevo_usuario)

        elif opcion == "2":
            registro.mostrar_usuarios()

        elif opcion == "3":
            correo_buscar = input("Ingrese el correo electrónico del usuario a buscar: ")
            registro.buscar_usuario(correo_buscar)

        elif opcion == "4":
            correo_eliminar = input("Ingrese el correo electrónico del usuario a eliminar: ")
            registro.eliminar_usuario(correo_eliminar)

        elif opcion == "5":
            correo_editar = input("Ingrese el correo electrónico del usuario a editar: ")
            registro.editar_usuario(correo_editar)

        elif opcion == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
