class RegistroUsuarios:
    def __init__(self):
        self.usuarios = []

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print("Usuario registrado exitosamente.")

    def mostrar_usuarios(self):
        if self.usuarios:
            print("Lista de usuarios registrados:")
            for usuario in self.usuarios:
                print(f"Nombre: {usuario.get_nombre()}, Correo: {usuario.get_correo()}")
                # Agregar otros detalles según sea necesario
        else:
            print("No hay usuarios registrados.")

    def buscar_usuario(self, correo):
        for usuario in self.usuarios:
            if usuario.get_correo() == correo:
                print("Usuario encontrado:")
                print(f"Nombre: {usuario.get_nombre()}, Correo: {usuario.get_correo()}")
                return
        print("Usuario no encontrado.")

    def eliminar_usuario(self, correo):
        for usuario in self.usuarios:
            if usuario.get_correo() == correo:
                self.usuarios.remove(usuario)
                print("Usuario eliminado exitosamente.")
                return
        print("Usuario no encontrado.")

    def editar_usuario(self, correo):
        for usuario in self.usuarios:
            if usuario.get_correo() == correo:
                print("Editar información del usuario:")
                usuario.set_nombre(input("Nuevo nombre: "))
                usuario.set_numero(input("Nuevo número: "))
                usuario.set_calle(input("Nueva calle: "))
                usuario.set_genero(input("Nuevo género: "))
                usuario.set_ciudad(input("Nueva ciudad: "))
                usuario.set_fecha(input("Nueva fecha de registro (YYYY-MM-DD): "))
                print("Usuario editado exitosamente.")
                return
        print("Usuario no encontrado.")