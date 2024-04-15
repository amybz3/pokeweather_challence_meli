from flask import jsonify, request
import requests
import random

# 2 Obtener un Pokémon al azar de un tipo en específico.
def get_pokemon_random():
    pokemon_type = request.args.get('type')    #get query params type from url
    if not pokemon_type:
        return jsonify({'error': 'Missing Pokemon type parameter'}), 400

    url = f'https://pokeapi.co/api/v2/type/{pokemon_type.lower()}'
    response = requests.get(url)          #call API
    if response.status_code == 200:
        type_data = response.json() #convert json
        all_pokemon = [pokemon['pokemon']['name'] for pokemon in type_data['pokemon']] #return array pokemons->pokemon->name
        random_pokemon = random.choice(all_pokemon) #choice a random pokemon from list 
        return jsonify({'type': pokemon_type, 'random_pokemon': random_pokemon})
    else:
        return jsonify({'error': 'Type not found'}), 404