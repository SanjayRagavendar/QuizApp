from flask import Blueprint, request, render_template
from utils import admin_required, custom_jwt_required


frontend_bp = Blueprint('frontend', __name__)

@frontend_bp.route('/')
@custom_jwt_required()
def index():
    return render_template('dashboard.html')

@frontend_bp.route('/login')
def loginpage():
    return render_template('login.html')


@frontend_bp.route('/register')
def registerpage():
    return render_template('register.html')

