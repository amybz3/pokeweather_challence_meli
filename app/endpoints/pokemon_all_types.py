from flask import jsonify, request
import requests

def get_pokemon_all_types():
    pokeapi_url = 'https://pokeapi.co/api/v2/type/' #URL to get of list type 
    response = requests.get(pokeapi_url)
    
    if response.status_code == 200:
        data = response.json()
        all_stop_types = [results['name'] for results in data['results']]
        return jsonify(all_stop_types)
    else:
        return jsonify({'error': 'Failed to fetch data from PokeAPI'}), 500

