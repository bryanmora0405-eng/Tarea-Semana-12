# Sistema de Gestión de Biblioteca Digital
**Universidad Estatal Amazónica - Segundo Semestre**

Este proyecto es un sistema de gestión de biblioteca desarrollado en Python, aplicando una arquitectura estructurada por capas (modelos, servicios y punto de entrada) y los principios de la Programación Orientada a Objetos (POO).

## Estructura del Proyecto
El proyecto respeta la organización de carpetas solicitada para separar las responsabilidades del sistema:

* **modelos/**: Contiene las clases libro.py y usuario.py que representan las entidades de datos.
* **servicios/**: Contiene biblioteca_servicio.py, donde reside la lógica de negocio para préstamos, devoluciones y registros.
* **main.py**: Es el punto de arranque del programa que gestiona el menú interactivo en la consola.

## Requisitos Técnicos Implementados
Se han utilizado diversas colecciones de datos para cumplir con los requerimientos obligatorios de la asignatura:

1. **Tuplas**: Utilizadas en la clase Libro para almacenar el título y el autor de forma inmutable.
2. **Listas**: Utilizadas en la clase Usuario para gestionar la colección dinámica de libros prestados.
3. **Diccionarios**: Utilizados en la capa de servicios para el catálogo de libros, usando el ISBN como clave para búsquedas eficientes.
4. **Conjuntos (Sets)**: Utilizados para gestionar los IDs de usuario, garantizando que cada registro sea único y evitando duplicados.

## Funcionalidades
El sistema permite realizar las siguientes acciones a través de la interfaz de consola:
* Añadir y quitar libros del catálogo.
* Registrar y dar de baja usuarios.
* Gestionar préstamos y devoluciones de libros.
* Buscar libros por título, autor o categoría.
* Listar todos los libros prestados a un usuario específico.

## Instrucciones de Ejecución
Para ejecutar el programa, navega hasta la carpeta del proyecto en tu terminal y utiliza el comando:

python main.py
