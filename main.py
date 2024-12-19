from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager
from models import *

app = Flask(__name__)

# Database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# JWT config
app.config['JWT_SECRET_KEY'] = 'ajdfkjasdkjlfk!1203ASFD'
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_ACCESS_COOKIE_NAME'] = 'access_token'
app.config['JWT_COOKIE_CSRF_PROTECT'] = False
app.config['JWT_COOKIE_SECURE'] = False

# Initialize
db.init_app(app)
jwt = JWTManager(app)

from blueprints.auth_bp import auth_bp
from blueprints.frontend.frontend_bp import frontend_bp
from blueprints.admin_api import admin_api

app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(frontend_bp)
app.register_blueprint(admin_api, url_prefix='/api/admin')

if __name__ == '__main__':
    app.run(debug=True)