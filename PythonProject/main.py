import requests

URL = 'https://api.pokemonbattle.ru/v2'
Token = '9eb1155fc97e8560e08862eaabdb659f'
Header = {'content-type' : 'application/json', 
          'trainer_token' : Token}

body_registration = {
    "trainer_token": Token,
    "email": "marqussweizy@gmail.com",
    "password": "Qwerty12345"
}
body_confirmation = {
    "trainer_token": Token
}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}
body_put = {
    "pokemon_id": "83483",
    "name": "TOKYO",
    "photo_id": 13
}
body_pokeball = {
    "pokemon_id": "83483"
}

'''response = requests.post(url = f'{URL}/trainers/reg', headers = Header, json = body_registration)
print(response.text)'''

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = Header, json = body_confirmation)
print(response_confirmation.text)'''

'''response_create = requests.post(url = f'{URL}/pokemons', headers = Header, json = body_create)
print(response_create.text)

message = response_create.json()['message']
print(message)'''

'''response_put = requests.put(url = f'{URL}/pokemons', headers = Header, json = body_put)
print(response_put.text)'''

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = Header, json = body_pokeball)
print(response_pokeball.text)