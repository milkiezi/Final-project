from flask import Flask, request, render_template, jsonify
import os
import base64
import requests
from PIL import Image
from flask_sqlalchemy import SQLAlchemy
from blueprints.home import home
from blueprints.types import types
from blueprints.pokemon import pokemon
from blueprints.about import about
from blueprints.models import db
from blueprints.ml_model import TFModel

app = Flask(__name__)

app.config['SECRET_KEY'] = 'app-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()    

app.register_blueprint(home)
app.register_blueprint(types)
app.register_blueprint(pokemon)
app.register_blueprint(about)

UPLOAD_FOLDER = './static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

model = TFModel(model_dir='./ml-models/')
model.load()

@app.route('/predict', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file1' not in request.files:
            return 'there is no file1 in form!'
        file1 = request.files['file1']
        path = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename)
        file1.save(path)

        image_1 = Image.open(path)
        outputs = model.predict(image_1)

        pred_result = outputs['predictions'][0]['label']
        
        urlAPI = "http://localhost:8000/pokemon?name={}".format(pred_result)
        
        dataPokemon = requests.get(urlAPI).json()

        allPokemon = list()

        if dataPokemon:
            try:
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
            except KeyError:   
                name = "Unknown"
                type1 = "Unknown"
                type2 = "Unknown"
                total = "Unknown"
                hp = "Unknown"
                attack = "Unknown"
                defen = "Unknown"
                atk = "Unknown"
                de = "Unknown"
                speed = "Unknown"
                legen = "Unknown"
                url = "https://c.tenor.com/_4zuCogesXQAAAAj/person-man.gif"

            allPokemon.append({"name":name, "type1":type1, "type2":type2, "total":total, "hp":hp, "attack":attack, "defen":defen, "atk":atk, "de":de, "speed":speed, "legen":legen, "url":url})
                
        return render_template('predict.html',  allPokemon= allPokemon)
    else:
        return render_template('predict.html')

app.env="development"
app.run(debug=True)