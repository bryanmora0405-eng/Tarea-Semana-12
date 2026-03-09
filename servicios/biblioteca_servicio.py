# servicios/biblioteca_servicio.py

class BibliotecaServicio:
    """
    Capa de Servicio: Gestiona la lógica del negocio separada de la interfaz.
    """
    def __init__(self):
        # REQUISITO: DICCIONARIO para libros disponibles.
        # Clave: ISBN, Valor: Objeto Libro. Permite búsquedas instantáneas (O(1)).
        self.libros = {}
        
        # REQUISITO: CONJUNTO (SET) para IDs de usuario.
        # Los conjuntos no permiten duplicados, garantizando IDs únicos automáticamente.
        self.usuarios_registrados = {}
        self.ids_usuarios = set()

    def añadir_libro(self, libro):
        self.libros[libro.isbn] = libro

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.usuarios_registrados[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            return True
        return False

    def prestar_libro(self, isbn, id_usuario):
        # Lógica de préstamo: verifica existencia en el diccionario y el set
        if isbn in self.libros and id_usuario in self.usuarios_registrados:
            libro = self.libros.pop(isbn) # Se remueve del catálogo
            self.usuarios_registrados[id_usuario].libros_prestados.append(libro)
            return True
        return False

    def buscar_libros(self, criterio, valor):
        # Búsqueda flexible por atributos del modelo
        resultados = []
        for libro in self.libros.values():
            if valor.lower() in str(libro).lower():
                resultados.append(libro)
        return resultados