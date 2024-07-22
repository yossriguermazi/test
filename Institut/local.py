from flask import Flask
from flask_cors import CORS
from views.institut_view import  Institut_bp

app = Flask(__name__)
app.register_blueprint(Institut_bp)

CORS(app)

app.run(debug=True, host="0.0.0.0", port=5000)
