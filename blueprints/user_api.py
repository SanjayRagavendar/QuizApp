from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity,jwt_required
from models import db, User, Quiz

user_api=Blueprint('user_api',__name__)
@user_api.route('/quiz', methods=['GET'])
@jwt_required()
def quiz():
    if request.method == 'GET':
        quizzes = Quiz.query.all()
        quiz_list = []
        for quiz in quizzes:
            quiz_list.append({
                'quiz_id': quiz.quiz_id,
                'quiz_name': quiz.quiz_name,
                'quiz_description': quiz.quiz_description,
                'created_by': quiz.creator.first_name
            })
        return jsonify(quiz_list), 200

@user_api.route('/<int:user_id>',methods=['GET'])
@jwt_required()
def account_details(user_id):
    user=User.query.filter_by(user_id=user_id).first_or_404()
    user_data={
        'user_id':user.user_id,
        'first_name':user.first_name,
        'role':user.role,
        'email':user.email
    }