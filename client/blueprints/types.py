from flask import Blueprint, render_template, Flask, request
import json
import requests

types = Blueprint('types', __name__)

@types.route('/types')
def type():
    if 'type1' in request.args:
        type = request.args.get('type1')
        urlAPI = "http://localhost:8000/pokemon?type1={}".format(type)
    else:
        type = request.args.get('type2')
        urlAPI = "http://localhost:8000/pokemon?type2={}".format(type)

    dataPokemon = requests.get(urlAPI).json()

    allPokemon = list()

    for i in range(len(dataPokemon)):
        Id = dataPokemon[i]['Id']
        name = dataPokemon[i]['Name']
        type1 = dataPokemon[i]['Type1']
        type2 = dataPokemon[i]['Type2']
        url = dataPokemon[i]['Url']

        allPokemon.append({"Id":Id, "name":name, "type1":type1, "type2":type2, "url":url})
            
    return render_template("types.html", allPokemon=allPokemon, type=type)