from flask import Blueprint, render_template, Flask, request
import json
import requests

pokemon = Blueprint('pokemon', __name__)

@pokemon.route('/pokemon')
def pokemons():
    if 'id' in request.args:
        id = request.args.get('id')
    
    urlAPI = "http://localhost:8000/pokemon?id={}".format(id)
    
    dataPokemon = requests.get(urlAPI).json()

    allPokemon = list()
    if dataPokemon:
        Id = dataPokemon['Id']
        name = dataPokemon['Name']
        type1 = dataPokemon['Type1']
        type2 = dataPokemon['Type2']
        total = dataPokemon['Total']
        hp = dataPokemon['HP']
        attack = dataPokemon['Attack']
        defen = dataPokemon['Defense']
        atk = dataPokemon['Sp.Atk']
        de = dataPokemon['Sp.Def']
        speed = dataPokemon['Speed']
        legen = dataPokemon['Legendary']
        url = dataPokemon['Url']

        allPokemon.append({"Id":Id, "name":name, "type1":type1, "type2":type2, "total":total, "hp":hp, "attack":attack, "defen":defen, "atk":atk, "de":de, "speed":speed, "legen":legen, "url":url})
            
    return render_template("pokemon.html", allPokemon=allPokemon, type=type)