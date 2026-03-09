# Sistema de Gestión de Biblioteca Digital 📚
**Universidad Estatal Amazónica - Segundo Semestre**

Este proyecto es un sistema de gestión de biblioteca desarrollado en Python, aplicando una **arquitectura estructurada por capas** (modelos, servicios y punto de entrada) y Programación Orientada a Objetos (POO).

## 🏗️ Estructura del Proyecto
El proyecto respeta la siguiente organización de carpetas:

* **`modelos/`**: Contiene las clases que representan entidades (`libro.py` y `usuario.py`).
* **`servicios/`**: Contiene la lógica del negocio (`biblioteca_servicio.py`).
* **`main.py`**: Punto de arranque del programa y menú interactivo.

## 🛠️ Requisitos Técnicos Implementados
Se han utilizado diversas colecciones de datos según los criterios de evaluación:

1.  **Tuplas**: Para almacenar título y autor de forma inmutable en el modelo Libro.
2.  **Listas**: Para gestionar los libros actualmente prestados a cada usuario.
3.  **Diccionarios**: Para el catálogo de libros, usando el **ISBN** como clave para búsquedas eficientes.
4.  **Conjuntos (Sets)**: Para garantizar que los IDs de usuario registrados sean únicos.

## 🚀 Funcionalidades Principales
El sistema permite realizar todas las operaciones requeridas:
* Añadir y quitar libros.
* Registrar y dar de baja usuarios.
* Realizar préstamos y devoluciones.
* Búsquedas por título, autor o categoría.
* Listar libros prestados por usuario.

## 💻 Ejecución
Navega a la carpeta del proyecto y ejecuta:
```bash
python main.py