from flask_restful import Resource, reqparse
from sqlalchemy import desc
import db


class Score(Resource):
    def get(self):
        res = db.ses.query(db.User).order_by(desc(db.User.Score)).all()

        r = []


        id = 1
        for game in res:
            r.append({"username": game.Username, "score": game.Score,"id":id})
            id += 1

        return r
