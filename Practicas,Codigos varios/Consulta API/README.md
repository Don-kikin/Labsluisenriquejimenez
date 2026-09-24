# Consumo de API REST Básica en Python

Este script demuestra cómo realizar peticiones HTTP GET a una API REST pública utilizando el lenguaje Python y la librería de terceros `requests`. 

## Características

* Realiza una conexión a la API pública de prueba [JSONPlaceholder](https://jsonplaceholder.typicode.com/).
* Extrae el primer registro (`/posts/1`) simulando la obtención de un artículo o publicación de un blog.
* Convierte la respuesta de formato JSON a un diccionario nativo de Python para su posterior manipulación y visualización en consola.

## Requisitos Previos

* Python 3.x instalado en el sistema.
* Gestor de paquetes `pip` para la instalación de dependencias.

## Instalación

Dado que el código utiliza una librería que no pertenece a la biblioteca estándar de Python, es necesario instalarla antes de ejecutar el script.

1. Clona este repositorio o descarga el archivo `.py` en tu entorno local.
2. Abre una terminal en el directorio del proyecto.
3. Instala la dependencia necesaria ejecutando:

   ```bash
   pip install requests
