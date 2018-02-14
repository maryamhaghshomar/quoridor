from flask_restful import Resource, reqparse
import db

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('num')
parser.add_argument('token')


class Game(Resource):
    def get(self, id=None):
        if id is not None:
            res = db.ses.query(db.Game).filter(db.Game.Id == id).first()
            if res is None:
                return {"ok": False}
            return {"name": res.Name, "num": res.Num, "joined": res.Joined}
        else:
            res = db.ses.query(db.Game).all()

            r = []

            for game in res:
                r.append({"name": game.Name, "num": game.Num, "joined": game.Joined,"id":game.Id})

            return r

    def post(self, id=None):
        args = parser.parse_args()
        UserId = db.ses.query(db.Token).filter(db.Token.Token == args.token).first().UserId

        if id is None and UserId is not None:
            game = db.Game(Name=args.name, Num=args.num, Joined=1,Turn=0,Board="",Wall="")
            db.ses.add(game)
            db.ses.commit()
            joine = db.Joine(UserId=UserId, GameId=game.Id)
            db.ses.add(joine)
            db.ses.commit()
            return {"ok":True,"name": game.Name, "num": game.Num, "joined": game.Joined}

        return {"ok": False}
