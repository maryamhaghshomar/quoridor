from flask_restful import Resource, reqparse
import db

parser = reqparse.RequestParser()
parser.add_argument('game')


class Turn(Resource):

    def post(self, id=None):
        args = parser.parse_args()
        if id is None:
            res = db.ses.query(db.Game).filter(db.Game.Id == args.game).first()

            if res is not None:
                return {"turn":res.Turn}
