from endpoints import pokemon_type, pokemon_all_names, pokemon_all_types, pokemon_longest, pokemon_random, pokemon_random_letter
from flask import Flask

app = Flask(__name__)

app.add_url_rule('/pokemon/names', 'get_pokemon_all_names', pokemon_all_names.get_pokemon_all_names, methods=['GET'])
app.add_url_rule('/pokemon/types', 'get_pokemon_all_types', pokemon_all_types.get_pokemon_all_types, methods=['GET'])
app.add_url_rule('/pokemon/type', 'get_pokemon_type', pokemon_type.get_pokemon_type, methods=['GET'])
app.add_url_rule('/pokemon/random', 'get_pokemon_random', pokemon_random.get_pokemon_random, methods=['GET'])
app.add_url_rule('/pokemon/longest', 'get_pokemon_longest', pokemon_longest.get_pokemon_longest, methods=['GET'])
app.add_url_rule('/pokemon/random_letter', 'get_pokemon_random_letter', pokemon_random_letter.get_pokemon_random_letter, methods=['GET'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)