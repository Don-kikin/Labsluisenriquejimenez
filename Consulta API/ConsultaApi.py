import requests

respuesta = requests.get("https://jsonplaceholder.typicode.com/posts/1")

publicacion = respuesta.json()
print(publicacion)
