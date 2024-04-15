from flask import jsonify, request
import requests

def get_pokemon_all_names():
    pokeapi_url = 'https://pokeapi.co/api/v2/pokemon/?limit=1000'  # URL to get of Pokemon list
    response = requests.get(pokeapi_url)  #To save value in variable with response to the service call from Pokeapi
    if response.status_code == 200:       #evaluate if has a status code is 200 ok success
        data = response.json()             #to save the respond json in data
        all_pokemon_names = [result['name'] for result in data['results']]  #iterate of array results, get the name and save in variable
        return jsonify(all_pokemon_names)  #return the list pokemon names with format json
    else:
        return jsonify({'error': 'Failed to fetch data from PokeAPI'})
