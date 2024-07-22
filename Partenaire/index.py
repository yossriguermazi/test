import awsgi
from flask import Flask
from flask_cors import CORS
from views.DemandePartenariat_view import DemandePartenariat_bp

app = Flask(__name__)
app.register_blueprint(blueprint=DemandePartenariat_bp)
cors = CORS(app)


def handler(event, context):
    return awsgi.response(app, event, context)


if __name__ == "__main__":
    handler(None, None)
