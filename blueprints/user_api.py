from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity,jwt_required
from models import db, User, Question,Quiz

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
    return jsonify(user_data),200

@user_api.route('/quiz/<int:quiz_id>/questions',methods=['GET'])
@jwt_required()
def get_questions(quiz_id):
    questions=Question.query.filter_by(quiz_id=quiz_id).all()
    question_list=[]
    for question in questions:
        #options=question.option
        question_list.append({
            'question_id':question.question_id,
            'question_content':question.question_content,
            'question_type':question.question_type,
            'quiz_id':question.quiz_id,
            'options':question.options.split(','),
            'correct_answer':question.correct_answer,
            'explation':question.explation
        })
    return jsonify(question_list),200
