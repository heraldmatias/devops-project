from flask_restful import Resource
from flask_jwt_extended import create_access_token
from flask_pydantic import validate
from api.models.auth import LoginBody, LoginResponse


class ViewAuthUser(Resource):
    @validate()
    def post(self, body: LoginBody):
        application = body.application
        if application is None:
            return "Applicacion no existe", 404
        else:
            response = LoginResponse(
                token=create_access_token(identity=application))
            return response
