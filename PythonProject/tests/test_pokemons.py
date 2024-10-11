import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
Token = '9eb1155fc97e8560e08862eaabdb659f'
Header = {'content-type' : 'application/json', 
          'trainer_token' : Token}
Trainer_id = '12438'

'''def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : Trainer_id})
    assert response.status_code == 200

def test_part_of_response():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : Trainer_id})
    assert response.json()["data"][0]["name"] == 'Бульбазавр'
    
@pytest.mark.parametrize('key, value', [('name', 'Бульбазавр'),('trainer_id', Trainer_id),('id', '83483')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : Trainer_id})
    assert response_parametrize.json()["data"][0][key] == value'''

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : Trainer_id})
    assert response.status_code == 200