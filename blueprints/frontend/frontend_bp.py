from flask import Blueprint, request, render_template, redirect, url_for
from utils import admin_required
from flask_jwt_extended import verify_jwt_in_request, jwt_required,get_jwt_identity, get_jwt
from models import QuizAttempt

frontend_bp = Blueprint('frontend', __name__)

@frontend_bp.route('/')
@jwt_required()
def index():
    return render_template('dashboard.html', role = get_jwt()['role'])

@frontend_bp.route('/login')
def loginpage():
    if verify_jwt_in_request(optional=True):
        return redirect('/')
    return render_template('login.html')


@frontend_bp.route('/register')
def registerpage():
    return render_template('register.html')

@frontend_bp.route('/attempt/<int:quiz>')
@jwt_required()
def attemptpage(quiz):
    return render_template('attempt.html',quiz_id=quiz)

@frontend_bp.route('/quiz_create')
@admin_required()
def quizcreatepage():
    return render_template('quiz_create.html')

@frontend_bp.route('/account')
@jwt_required()
def accountpage():
    user_id=get_jwt_identity()
    return render_template('account.html',user_id=user_id)

@frontend_bp.route('/logout')
def logout():
    return redirect(url_for('auth.logout'))

@frontend_bp.route('/result/<int:attempt_id>')
@jwt_required()
def resultpage(attempt_id):
    attempt = QuizAttempt.query.filter_by(attempt_id=attempt_id).first()
    return render_template('result.html',score=attempt.score,max_score=attempt.max_score, quiz_id=attempt.quiz_id)

@frontend_bp.route('/admin',methods=['GET'])
@admin_required()
def adminpage():
    return render_template('admin_dasboard.html')

@frontend_bp.route('/admin/quiz/<int:quiz_id>')
@admin_required()
def quizdetailpage(quiz_id):
    print(quiz_id)
    return render_template('admin_questions.html',quiz_id=quiz_id)