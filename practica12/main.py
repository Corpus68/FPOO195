from persona import Persona
from login import LoginApp

class MainApp:
    def __init__(self):
        self.usuarios = []

    def mostrar_menu(self):
        while True:
            print("1. Registrar usuario")
            print("2. Editar usuario")
            print("3. Eliminar usuario")
            print("4. Iniciar sesión")
            print("5. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.registrar_usuario()
            elif opcion == "2":
                self.editar_usuario()
            elif opcion == "3":
                self.eliminar_usuario()
            elif opcion == "4":
                login_app = LoginApp(self.usuarios)
                login_app.run()
            elif opcion == "5":
                break
            else:
                print("Opción no válida")

    def registrar_usuario(self):
        nombre = input("Ingrese el nombre: ")
        correo = input("Ingrese el correo: ")
        contraseña = input("Ingrese la contraseña: ")

        nuevo_usuario = Persona(nombre, correo, contraseña)
        self.usuarios.append(nuevo_usuario)
        print("Usuario registrado exitosamente!")

def main():
    app = MainApp()
    app.mostrar_menu()

if __name__ == "__main__":
    main()
