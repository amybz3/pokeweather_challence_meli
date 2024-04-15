from flask import jsonify, request
import requests

# 3.Obtener el Pokémon con nombre más largo de cierto tipo.
def get_pokemon_longest():
    type = request.args.get('type') #get query params type from url
    if not type:
        return jsonify({'error': 'Missing type parameter'}), 400
    
    pokeapi_url = f'https://pokeapi.co/api/v2/type/{type.lower()}'  
    response = requests.get(pokeapi_url)  #Call API
    
    if response.status_code == 200:
        data = response.json()
        pokemon_urls = [pokemon['pokemon']['url'] for pokemon in data['pokemon']]  #get array url of pokemons
        
        longest_pokemon_name = ''  #Initialize
        longest_pokemon_length = 0  #Initialize
        
        for url in pokemon_urls:
            pokemon_response = requests.get(url) #call API
            if pokemon_response.status_code == 200:
                pokemon_data = pokemon_response.json()
                pokemon_name = pokemon_data['name']
                if len(pokemon_name) > longest_pokemon_length:  #Ciclo for get first longest pokemon
                    longest_pokemon_length = len(pokemon_name)
                    longest_pokemon_name = pokemon_name
        
        if longest_pokemon_name:
            longest_pokemon = {'name': longest_pokemon_name, 'type': type}
            return jsonify(longest_pokemon)
        else:
            return jsonify({'error': 'No Pokémon found for the specified type'}), 404
    else:
        return jsonify({'error': 'Failed to fetch data from PokeAPI'}), 500
