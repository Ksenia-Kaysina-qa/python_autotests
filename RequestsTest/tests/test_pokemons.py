import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'b1a6a6ea6881b8f003a72e6a7ea5f11d'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '2695'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params= {'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params= {'trainer_id': TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'Полкан'  

    
'''@pytest.mark.parametrize('key, value', [{'name', 'Хруст3'},{'trainer_id', TRAINER_ID},{'id', '26876'}])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/pokemons', params= {'trainer_id': TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value'''
