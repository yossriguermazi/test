from flask import Flask
from flask_cors import CORS
from views.DemandePartenariat_view import  DeamndePartenaire_bp

app = Flask(__name__)
app.register_blueprint(DeamndePartenaire_bp)

CORS(app)

app.run(debug=True, host="0.0.0.0", port=5500)
