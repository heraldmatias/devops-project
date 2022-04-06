from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from api import (HealthCheckResource, BlackListsResource,
                 BlackListResource, ViewAuthUser)
from api.models import db


# Instancia de la aplicación en Flask
def create_app(config_filename):
    application = Flask(__name__)
    application.config.from_object(config_filename)
    return application


application = create_app('config.default_settings.Config')
app_context = application.app_context()
app_context.push()

db.init_app(application)
try:
    db.create_all()
except:
    pass

api = Api(application)

api.add_resource(HealthCheckResource, '/api/health-check/ping')
api.add_resource(ViewAuthUser, '/api/access-token')
api.add_resource(BlackListsResource, '/api/blacklists')
api.add_resource(BlackListResource, '/api/blacklists/<string:email>')

jwt = JWTManager(application)


def gunicorn():
    # Punto de arranque: gunicorn
    return application


# Punto de arranque: servidor de desarrollo
if __name__ == "__main__":
    application.run(
        host="0.0.0.0", port=5000, debug=True)
