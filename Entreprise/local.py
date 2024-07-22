from flask import Flask
from flask_cors import CORS
from views.entreprise_view import Entrprise_bp

app = Flask(__name__)
app.register_blueprint(Entrprise_bp)

CORS(app)

app.run(debug=True, host="0.0.0.0", port=3000)
