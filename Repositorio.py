from github import Github

# Autenticación con un token de acceso personal
# Crea un token de acceso personal en GitHub y reemplázalo aquí
TOKEN = 'tu_token_de_acceso_personal'
g = Github(TOKEN)

# Obtén el usuario autenticado
user = g.get_user()

def listar_repositorios():
    print("Repositorios:")
    for repo in user.get_repos():
        print(f"- {repo.name}")

def crear_repositorio(nombre, descripcion='', privado=False):
    repo = user.create_repo(
        name=nombre,
        description=descripcion,
        private=privado
    )
    print(f"Repositorio '{nombre}' creado con éxito.")

def eliminar_repositorio(nombre):
    repo = user.get_repo(f"{user.login}/{nombre}")
    repo.delete()
    print(f"Repositorio '{nombre}' eliminado con éxito.")

def menu():
    while True:
        print("\n¿Qué desea hacer?")
        print("1. Listar repositorios")
        print("2. Crear repositorio")
        print("3. Eliminar repositorio")
        print("4. Salir")
        opcion = int(input("Elija una opción: "))

        if opcion == 1:
            listar_repositorios()
        elif opcion == 2:
            nombre = input("Ingrese el nombre del nuevo repositorio: ")
            descripcion = input("Ingrese la descripción del nuevo repositorio (opcional): ")
            privado = input("¿El repositorio será privado? (s/n): ").lower() == 's'
            crear_repositorio(nombre, descripcion, privado)
        elif opcion == 3:
            nombre = input("Ingrese el nombre del repositorio a eliminar: ")
            eliminar_repositorio(nombre)
        elif opcion == 4:
            break
        else:
            print("Opción inválida. Inténtelo de nuevo.")

if __name__ == "__main__":
    menu()
