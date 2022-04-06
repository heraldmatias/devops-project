from flask_restful import Resource


class HealthCheckResource(Resource):
    def get(self):
        return 'pong', 200
