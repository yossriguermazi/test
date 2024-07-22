import awsgi
from flask import Flask
from flask_cors import CORS
from views.entreprise_view import Entrprise_bp


app = Flask(__name__)
app.register_blueprint(blueprint=Entrprise_bp)
cors = CORS(app)


def handler(event, context):
    return awsgi.response(app, event, context)


if __name__ == "__main__":
    handler(None, None)
