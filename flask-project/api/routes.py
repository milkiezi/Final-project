from flask_restful import Api

from api.pokemon import Pokemon1, Pokemon2
from api.authentication import TokenApi,RefreshToken

def create_route(api: Api):

    api.add_resource(TokenApi,'/auth/token')
    api.add_resource(RefreshToken,'/auth/token/refresh')

    api.add_resource(Pokemon1, '/pokemon')
    api.add_resource(Pokemon2, '/pokemon/delete/<name>')
    