import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'b1a6a6ea6881b8f003a72e6a7ea5f11d'
HEADER = {'Content-Type' :'application/json','trainer_token': TOKEN}
body_create = {
    "name": "Булочка",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

body_name_pokemon = {
    "pokemon_id": "17081",
    "name": "Новый",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

body_pokebol = {
    "pokemon_id": "28500"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)


'''response_name_pokemon = requests.put(url= f'{URL}/pokemons', headers = HEADER,json= body_name_pokemon)
print(response_name_pokemon.text)'''


response_pokebol = requests.post(url= f'{URL}/trainers/add_pokeball', headers=HEADER, json= body_pokebol)
print(response_pokebol.text)


message = response_create.json['id']
print(message)