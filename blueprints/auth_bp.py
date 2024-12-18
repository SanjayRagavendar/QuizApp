from flask import Blueprint, request, jsonify, redirect, url_for
from flask_jwt_extended import create_access_token, verify_jwt_in_request, get_jwt_identity, set_access_cookies, unset_jwt_cookies
from werkzeug.security import generate_password_hash, check_password_hash
from models import *

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    hashed_password = generate_password_hash(data['password'])
    user = User(username=data['username'], password=hashed_password, email=data['email'], first_name=data['first_name'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Invalid credentials'}), 401
    access_token = create_access_token(identity=user.user_id, additional_claims={'role': user.role, 'username': user.username})
    return jsonify(access_token=access_token), 201

@auth_bp.route('/logout', methods=['GET'])
def logout():
    response = redirect(url_for('frontend.loginpage'))
    unset_jwt_cookies(response)
    return response, 302
