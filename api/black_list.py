from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required
from db.models import db, BlackList, BlackListSchema
from flask_pydantic import validate
from api.models.black_list import BlackEmailBody

black_list_schema = BlackListSchema()


class BlackListsResource(Resource):
    @jwt_required()
    @validate()
    def post(self, body: BlackEmailBody):
        ip_address = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
        new_black_list = BlackList(
            ip_address=ip_address,
            **dict(body)
        )
        db.session.add(new_black_list)
        db.session.commit()
        return black_list_schema.dump(new_black_list), 201


class BlackListResource(Resource):
    @jwt_required()
    def get(self, email):
        black_list = BlackList.query.filter(BlackList.email == email)
        if black_list.count():
            return black_list_schema.dump(black_list[0]), 200

        return None, 404
