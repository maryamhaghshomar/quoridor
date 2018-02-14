from flask import Flask, Blueprint
from flask_restful import  Api
from User import User
from Index import Index
from Auth import Auth
from Game import Game
from Join import Join
from Turn import Turn
from Score import Score

app = Flask(__name__)
api_bp = Blueprint('api', __name__)
api = Api(api_bp)


api.add_resource(Index, '/')
api.add_resource(User, '/user', '/user/<int:id>')
api.add_resource(Auth, '/auth')
api.add_resource(Game, '/game')
api.add_resource(Join, '/join')
api.add_resource(Turn, '/turn')
api.add_resource(Score, '/score')

app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run(debug=True)
