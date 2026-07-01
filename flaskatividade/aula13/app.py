import os
from flask import Flask
from models import db
from controllers import dashboard_bp, locadora_bp

from dados_iniciais import popular_dados
from controllers import dashboard_bp, locadora_bp, api_v1_bp

app = Flask(__name__, template_folder="views/templates")

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(BASE_DIR, "banco_locadora.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(dashboard_bp)
app.register_blueprint(locadora_bp)
app.register_blueprint(api_v1_bp)

if __name__ == "__main__":
    with app.app_context():
        db.create_all() 
        popular_dados()
        
    app.run(debug=True)