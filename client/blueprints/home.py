from flask import Blueprint, render_template, Flask, request
import json
import requests

home = Blueprint('home', __name__)

@home.route('/')
def index():
    urlAPI = "http://localhost:8000/pokemon"

    dataPokemon = requests.get(urlAPI).json()

    allPokemon = list()

    for i in range(len(dataPokemon)):
        Id = dataPokemon[i]['Id']
        name = dataPokemon[i]['Name']
        type1 = dataPokemon[i]['Type1']
        type2 = dataPokemon[i]['Type2']
        url = dataPokemon[i]['Url']

        allPokemon.append({"Id":Id, "name":name, "type1":type1, "type2":type2, "url":url})
            
    return render_template("home.html", allPokemon=allPokemon)