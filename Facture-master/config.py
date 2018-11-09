import uuid, json

class Config(object):
    SECRET_KEY = str(uuid.uuid4())
    with open('secrets.json') as json_file:
        secrets =  json.load(json_file)
        GOOGLE_CLIENT_ID = '718782038011-fdki0ma37m7keo9d30b00kdorcnqga9a.apps.googleusercontent.com'
        GOOGLE_CLIENT_SECRET = secrets['google_secret']

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/facture'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True
    ASSETS_DEBUG=True

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:@localhost/facture'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
