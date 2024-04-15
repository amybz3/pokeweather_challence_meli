from flask import jsonify, request
import requests

# 1. Obtener el tipo de un Pokémon (fuego, agua, tierra, aire, etc...) según su nombre.
def get_pokemon_type():
    pokemon_name = request.args.get('name') #get query params from url
    if not pokemon_name:
        return jsonify({'error': 'Missing Pokemon name parameter'}), 400

    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}'
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_data = response.json()
        types = [type['type']['name'] for type in pokemon_data['types']]
        return jsonify({'name': pokemon_name, 'types': types})
    else:
        return jsonify({'error': 'Pokemon not found'}), 404