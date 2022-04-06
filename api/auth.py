from flask_restful import Resource
from flask import request
from flask_jwt_extended import create_access_token


class ViewAuthUser(Resource):
    def post(self):
        username = request.json.get("username")
        if username is None:
            return "El usuario no existe", 404
        else:
            access_token = create_access_token(identity=username)
            return {"token": access_token}
