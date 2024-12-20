from flask import Flask, request, jsonify, redirect, url_for, send_from_directory
from flask_jwt_extended import JWTManager, unset_jwt_cookies
from datetime import timedelta
from models import *
from urllib.parse import urlparse

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
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=10)

# Initialize
db.init_app(app)
jwt = JWTManager(app)

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    response = redirect(url_for('frontend.loginpage'))
    unset_jwt_cookies(response)
    return response, 302

@jwt.invalid_token_loader
def invalid_token_callback(error):
    response = redirect(url_for('frontend.loginpage'))
    unset_jwt_cookies(response)
    return response, 302

@jwt.unauthorized_loader
def missing_token_callback(error):
    response = redirect(url_for('frontend.loginpage'))
    unset_jwt_cookies(response)
    return response, 302

from blueprints.auth_bp import auth_bp
from blueprints.frontend.frontend_bp import frontend_bp
from blueprints.admin_api import admin_api
from blueprints.user_api import user_api

app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(frontend_bp)
app.register_blueprint(admin_api, url_prefix='/api/admin')
app.register_blueprint(user_api, url_prefix='/api/user')


@app.route('/favicon.ico', methods=['GET'])
def favicon():
    return send_from_directory('static', 'images/favicon.ico')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)