from flask_restful import Resource, reqparse
import db

parser = reqparse.RequestParser()
parser.add_argument('token')
parser.add_argument('game')


class Join(Resource):

    def post(self):
        args = parser.parse_args()
        UserId = db.ses.query(db.Token).filter(db.Token.Token == args.token).first().UserId
        Game = db.ses.query(db.Game).filter(db.Game.Id == args.game).first()

        if Game is not None and UserId is not None:
            game = db.Joine(UserId=UserId, GameId=Game.Id)
            db.ses.add(game)
            Game.Joined += 1
            db.ses.commit()
            return {"ok": True}

        return {"ok": False}
