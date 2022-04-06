from flask_restful import Resource
from flask import request
from flask_jwt_extended import create_access_token


class ViewAuthUser(Resource):
    def post(self):
        application = request.json.get("application")
        if application is None:
            return "Applicacion no existe", 404
        else:
            access_token = create_access_token(identity=application)
            return {"token": access_token}
