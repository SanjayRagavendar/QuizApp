from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity
from models import db, User, Quiz
from utils import admin_required

admin_api = Blueprint('admin_api', __name__)

@admin_api.route('/quiz', methods=['GET','POST'])
@admin_required()
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
    
    if request.method == 'POST':
        data = request.json
        current_user = get_jwt_identity()
        quiz = Quiz(
            quiz_name=data['quiz_name'],
            quiz_description=data['quiz_description'],
            created_by=current_user
        )
        db.session.add(quiz)
        db.session.commit()
        return jsonify({'message': 'Quiz created successfully'}), 201