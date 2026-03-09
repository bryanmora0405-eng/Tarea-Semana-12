# modelos/libro.py

class Libro:
    """
    Clase que representa la entidad Libro.
    Se aplica encapsulamiento para proteger los datos del libro.
    """
    def __init__(self, titulo, autor, categoria, isbn):
        # REQUISITO: Uso de TUPLA para título y autor.
        # Las tuplas son inmutables, lo que asegura que la combinación 
        # título/autor no cambie accidentalmente.
        self.datos_inmutables = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"'{self.datos_inmutables[0]}' de {self.datos_inmutables[1]} (ISBN: {self.isbn})"