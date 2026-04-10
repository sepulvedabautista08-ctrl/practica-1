import requests
url="https://pokeapi.co/api/v2/pokemon/pikachu"
respuesta=requests.get(url)
datos=respuesta.json()
print("nombre:", datos["name"])
print("altura:", datos["height"])
print("peso:", datos["weight"])