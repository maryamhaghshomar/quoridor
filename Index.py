from flask_restful import Resource

class Index(Resource):
    def get(self):
        return 'this is Api Server For Quoridor Game - University Of Tehran CS-BP'
