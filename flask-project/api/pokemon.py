from flask import request,jsonify,Response,current_app
from flask_restful import Resource
from flask_jwt_extended import jwt_required
import json


class Pokemon1(Resource):
    def get(self)-> Response:
        if 'id' in request.args:
            id = request.args.get('id')
            data = readJsonFile()
            res = None
            obj = json.loads(data)
            for i in obj:
                if i['Id'] == id:
                    res = i
            if(res is None):
                res = jsonify({"message" : "not found"})
                res.status_code = 404
            else:     
                res = jsonify(res)
                res.status_code = 200
            return res 

        elif 'name' in request.args:
            name = request.args.get('name').upper()
            data = readJsonFile()
            res = None
            obj = json.loads(data)
            for i in obj:
                if i['Name'].upper() == name:
                    res = i
            if(res is None):
                res = jsonify({"message" : "not found"})
                res.status_code = 404
            else:     
                res = jsonify(res)
                res.status_code = 200
            return res 

        elif 'type1' in request.args:
            if 'type2' in request.args:
                type1 = request.args.get('type1').upper()
                type2 = request.args.get('type2').upper()
                data = readJsonFile()
                res = None
                obj = json.loads(data)
                response = list()
                for i in obj:
                    if i['Type1'].upper() == type1 and i['Type2'].upper() == type2:
                        res = i
                        response.append(res)
                if(response==[]):
                    res = jsonify({"message" : "not found"})
                    res.status_code = 404
                else:     
                    res = jsonify(response)
                    res.status_code = 200
                return res
            else :
                type1 = request.args.get('type1').upper()
                data = readJsonFile()
                res = None
                obj = json.loads(data)
                response = list()
                for i in obj:
                    if i['Type1'].upper() == type1:
                        res = i
                        response.append(res)
                if(response==[]):
                    res = jsonify({"message" : "not found"})
                    res.status_code = 404
                else:     
                    res = jsonify(response)
                    res.status_code = 200
                return res
            
        elif 'type2' in request.args:
            type2 = request.args.get('type2').upper()
            data = readJsonFile()
            res = None
            obj = json.loads(data)
            response = list()
            for i in obj:
                if i['Type2'].upper() == type2:
                    res = i
                    response.append(res)
            if(response==[]):
                res = jsonify({"message" : "not found"})
                res.status_code = 404    
            else:     
                res = jsonify(response)
                res.status_code = 200
            return res
        else:        
            data = readJsonFile()
            res = None
            obj = json.loads(data)
            response = list()
            for i in obj:            
                res = i
                response.append(res)
            res = jsonify(response)
            res.status_code = 200      
            return res

    @jwt_required()
    def post(self)->Response:
        body = request.get_json()
        print(body)
        read = readJsonFile()
        obj = json.loads(read)
        data = list()
        for i in obj:
            data.append(i)
        
        if len(body) > 0:
            data.append(body)

        with open('pokemon.json','w') as outfile:
            json.dump(data, outfile)
            response = jsonify(data)
            response.status_code = 200
            return response
    
    @jwt_required()
    def put(self)->Response:
        body = request.get_json()
        key = body['key']
        read = readJsonFile()
        obj = json.loads(read)
        isSucess = False
        data = list()
        for i in obj:
            data.append(i)
            if i['Name'] == key:
                data.remove(i)
                isSucess = True

        del body['key']
        data.append(body)

        if isSucess is True:
            with open('pokemon.json','w') as outfile:
                json.dump(data, outfile)
                response = jsonify(data)
                response.status_code = 200
                return response
        else:
            return Response(status=404)
    

class  Pokemon2(Resource):

    @jwt_required()
    def delete(self,name: str)->Response:
        key = name
        read = readJsonFile()
        obj = json.loads(read)
        data = list()
        isSucess = False
        for i in obj:
            data.append(i)
            if i['Name'] == key:
                data.remove(i)
                isSucess = True

        with open('pokemon.json','w') as outfile:
            json.dump(data, outfile)

        if isSucess is True:
            response = jsonify(data)
            response.status_code = 200
            return response
        else:
            return Response(status=404)

def readJsonFile():
    with open('pokemon.json','r') as pokemon:
            data = pokemon.read()
    return data