from flask_restful import Resource, reqparse
import db

parser = reqparse.RequestParser()
parser.add_argument('username')
parser.add_argument('password')
parser.add_argument('email')


class User(Resource):
    def get(self, id=None):
        if id is not None:
            res = db.ses.query(db.User).filter(db.User.Id == id).first()
            if res is None:
                return {"ok": False}
            return {"username": res.Username, "email": res.Email, "score": res.Score}
        return {"ok": False}

    def post(self, id=None):
        args = parser.parse_args()
        if id is None and args.username is not "" and args.password is not "" and args.email is not "":
            user = db.User(Username=args.username, Password=args.password, Email=args.email, Score=0)
            db.ses.add(user)
            db.ses.commit()
            return {"ok":True,"username": user.Username, "email": user.Email, "score": user.Score}
        return {"ok": False}