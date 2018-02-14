from flask_restful import Resource, reqparse
import db
import string
import random

parser = reqparse.RequestParser()
parser.add_argument('username')
parser.add_argument('password')
parser.add_argument('token')

alphabet = string.ascii_letters + string.digits


class Auth(Resource):

    def post(self):
        args = parser.parse_args()

        res = db.ses.query(db.User).filter(db.User.Username == args.username).first()

        if res:
            if res.Password == args.password:
                token = ''.join(random.SystemRandom().choice(alphabet) for i in range(10))
                t = db.Token(UserId=res.Id, Token=token)
                db.ses.add(t)
                db.ses.commit()
                return {"ok": True, "token": token}

        return {"ok": False}

    def delete(self):
        args = parser.parse_args()

        res = db.ses.query(db.Token).filter(db.Token.Token == args.token).first()

        if res:
            db.ses.delete(res)
            db.ses.commit()

        return {"ok": True}