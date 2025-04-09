import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '28e2d72f80803839fd0a42f1dd868bf9'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}  
body_create = {
    "name": "Кристалик",
    "photo_id": 225
}

body_create = {
    "pokemon_id": "283409",
    "name": "New Name",
    "photo_id": 2
}

body_create = {
    "pokemon_id": "283409"
}

'''response_create = requests.post(url = f'{URL}/pokemons',headers = HEADER, json = body_create)
print(response_create.text)'''

'''pokemon_id = response_create.json()['id']
print(pokemon_id)'''

'''response_create = requests.put(url = f'{URL}/pokemons',headers = HEADER, json = body_create)
print(response_create.text)'''


response_create = requests.post(url = f'{URL}/trainers/add_pokeball',headers = HEADER, json = body_create)
print(response_create.text)


