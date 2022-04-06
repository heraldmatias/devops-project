from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required
from api.models import db, BlackList, BlackListSchema


black_list_schema = BlackListSchema()


class BlackListsResource(Resource):
    @jwt_required()
    def post(self):
        ip_address = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
        new_black_list = BlackList(
            ip_address=ip_address,
            app_id=request.json['app_id'],
            email=request.json['email'],
            blocked_reason=request.json['blocked_reason']
        )
        db.session.add(new_black_list)
        db.session.commit()
        return black_list_schema.dump(new_black_list), 201


class BlackListResource(Resource):
    @jwt_required()
    def get(self, email):
        black_list = BlackList.query.filter(BlackList.email == email)
        return black_list_schema.dump(black_list[0]), 200
