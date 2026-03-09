# modelos/usuario.py

class Usuario:
    """
    Clase que representa a un usuario de la biblioteca.
    """
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        # REQUISITO: Uso de LISTA para libros prestados.
        # Se elige una lista porque el orden de préstamo importa y 
        # permite añadir/quitar elementos dinámicamente.
        self.libros_prestados = []

    def __str__(self):
        return f"Usuario: {self.nombre} [ID: {self.id_usuario}]"