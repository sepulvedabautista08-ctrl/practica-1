import requests
#importa una libreria para que el cliente haga solicitudes
url="https://pokeapi.co/api/v2/pokemon/pikachu"
#guarda la direccion web
respuesta=requests.get(url)
#hace la peticion a la url
datos=respuesta.json()
#datos esta guardando un json
print("nombre:", datos["name"])
#muestra el nombre
print("altura:", datos["height"])
#muestra la altura
print("peso:", datos["weight"])
#muestra el peso
print(respuesta)
#muestra la respuesta