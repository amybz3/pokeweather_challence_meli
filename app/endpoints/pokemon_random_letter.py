from flask import Flask, request, jsonify
import requests
import random

# 4. Obtener un Pokémon al azar que contenga alguna de las letras ‘I’,’A’,’M’ en su nombre y que sea del tipo específico más fuerte en
#base al clima actual de tu ciudad (ver referencia 1 y 2)
def get_pokemon_random_letter():
    letters = request.args.get('letter')
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')

    if not letters or not latitude or not longitude:
        return jsonify({'error': 'Missing required parameters'}), 400

    temperature = get_weather(latitude, longitude) #Call Service for Temperature ex: 13.4
    if temperature is None:
        return jsonify({'error': 'Failed to fetch weather data'}), 400

    strongest_type = get_strongest_type(temperature) #Validate elif for type strong: ex:normal
    if not strongest_type:
        return jsonify({'error': 'Unable to determine strongest type based on temperature'}), 400

    pokemon_list = get_pokemon_by_type(strongest_type) #Call service and get list pokemon name
    if not pokemon_list:
        return jsonify({'error': 'Failed to fetch Pokémon data or no Pokémon of this type'}), 400

    filtered_pokemon = [p for p in pokemon_list if any(letter.lower() in p for letter in letters)] #Filter by IAM Letter

    if not filtered_pokemon:
        return jsonify({'error': 'No Pokémon found that matches the criteria'}), 404

    random_pokemon_name = random.choice(filtered_pokemon) #Get a Random Pokemon by List
    return jsonify({'name': random_pokemon_name, 'type': strongest_type, 'letters': letters})

def get_weather(lat, lon):
    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m"
        response = requests.get(url)
        response.raise_for_status()  # Esto lanzará una excepción si el código de estado es 4xx o 5xx
        data = response.json()
        return data['current']['temperature_2m']
    except requests.RequestException as e:
        return None  # En caso de error, retorna None

def get_strongest_type(temperature):
    if temperature is None:
        return "unknown"  # Manejar caso donde la temperatura no esté disponible
    elif temperature >= 30:
        return "fire"
    elif temperature >= 20:
        return "rock"
    elif temperature >= 10:
        return "normal"
    elif temperature >= 0:
        return "water"
    else:
        return "ice"

def get_pokemon_by_type(pokemon_type):
    if not pokemon_type:
        return []  # Si no hay tipo, retorna lista vacía
    try:
        url = f"https://pokeapi.co/api/v2/type/{pokemon_type.lower()}"
        response = requests.get(url) #call service
        response.raise_for_status()
        data = response.json()
        return [pokemon['pokemon']['name'] for pokemon in data['pokemon']]
    except requests.RequestException as e:
        return []  # En caso de error, retorna lista vacía
