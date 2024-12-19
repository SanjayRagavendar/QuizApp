from flask import Blueprint, request, render_template, redirect, url_for
from utils import admin_required
from flask_jwt_extended import verify_jwt_in_request, jwt_required,get_jwt_identity

frontend_bp = Blueprint('frontend', __name__)

@frontend_bp.route('/')
@jwt_required()
def index():
    return render_template('dashboard.html')

@frontend_bp.route('/login')
def loginpage():
    if verify_jwt_in_request(optional=True):
        return redirect('/')
    return render_template('login.html')


@frontend_bp.route('/register')
def registerpage():
    return render_template('register.html')

@frontend_bp.route('/attempt/<int:quiz>')
def attemptpage(quiz):
    return render_template('attempt.html',quiz_id=quiz)

@frontend_bp.route('/quiz_create')
@admin_required()
def quizcreatepage():
    return render_template('quiz_create.html')

@frontend_bp.route('/result')
def resultpage():
    return render_template('result.html')

@frontend_bp.route('/account')
@jwt_required()
def accountpage():
    user_id=get_jwt_identity()
    return render_template('account.html',user_id=user_id)

@frontend_bp.route('/logout')
def logout():
    return redirect(url_for('auth.logout'))