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
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = db.session.query(User).filter_by(email=email).first()

    if not user:
        return jsonify({'message': 'User not found'}), 404

    if not check_password_hash(user.password, password):
        return jsonify({'message': 'Incorrect password'}), 401

    try:
        additional_claims = {
            'name': user.first_name,
            'role': user.role,
        }
        access_token = create_access_token(identity=str(user.user_id), additional_claims=additional_claims)
    except Exception as e:
        return jsonify({'message': 'Error creating access token'}), 500

    response = jsonify({
        'message': 'Login successful',
    })
    set_access_cookies(response, access_token)
    return response

@auth_bp.route('/logout', methods=['GET'])
def logout():
    try:
        verify_jwt_in_request()
        response = redirect(url_for('frontend.loginpage'))
        unset_jwt_cookies(response)
        return response
    except Exception:
        return redirect(url_for('frontend.loginpage'))

