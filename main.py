# main.py
from modelos.libro import Libro
from modelos.usuario import Usuario
from servicios.biblioteca_servicio import BibliotecaServicio

def mostrar_menu():
    print("\n" + "="*30)
    print(" SISTEMA DE BIBLIOTECA - UEA")
    print("="*30)
    print("1. Añadir libro")
    print("2. Registrar usuario")
    print("3. Prestar libro")
    print("4. Listar libros prestados")
    print("5. Salir")
    return input("Seleccione una opción: ")

def ejecutar():
    servicio = BibliotecaServicio()
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            t = input("Título: "); a = input("Autor: ")
            c = input("Categoría: "); i = input("ISBN: ")
            servicio.añadir_libro(Libro(t, a, c, i))
            print("✔ Libro añadido.")
        elif opcion == "2":
            n = input("Nombre: "); id_u = input("ID: ")
            if servicio.registrar_usuario(Usuario(n, id_u)):
                print("✔ Usuario registrado.")
            else: print("✘ ID ya existe.")
        elif opcion == "3":
            isbn = input("ISBN: "); id_u = input("ID Usuario: ")
            if servicio.prestar_libro(isbn, id_u):
                print("✔ Préstamo exitoso.")
            else: print("✘ Error en datos.")
        elif opcion == "4":
            id_u = input("ID Usuario: ")
            user = servicio.usuarios_registrados.get(id_u)
            if user:
                for lib in user.libros_prestados: print(f"- {lib}")
            else: print("✘ No encontrado.")
        elif opcion == "5":
            break

if __name__ == "__main__":
    ejecutar()