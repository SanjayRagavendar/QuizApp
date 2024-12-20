from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity
from models import db, User, Quiz, Question
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

@admin_api.route('/quiz/<int:quiz_id>', methods=['GET','PUT','DELETE'])
@admin_required()
def quiz_detail(quiz_id):
    quiz = Quiz.query.filter_by(quiz_id=quiz_id).first_or_404()
    if request.method == 'GET':
        return jsonify({
            'quiz_id': quiz.quiz_id,
            'quiz_name': quiz.quiz_name,
            'quiz_description': quiz.quiz_description,
            'created_by': quiz.creator.first_name
        }), 200
    
    if request.method == 'PUT':
        data = request.json
        quiz.quiz_name = data['quiz_name']
        quiz.quiz_description = data['quiz_description']
        db.session.commit()
        return jsonify({'message': 'Quiz updated successfully'}), 200
    
    if request.method == 'DELETE':
        quiz = Quiz.query.filter_by(quiz_id=quiz_id).first_or_404()
        Question.query.filter_by(quiz_id=quiz_id).delete()
        db.session.delete(quiz)
        db.session.commit()
        return jsonify({'message': 'Quiz deleted successfully'}), 200


@admin_api.route('/quiz/<int:quiz_id>/questions', methods=['GET','POST'])
# @admin_required()
def questions(quiz_id):
    if request.method == 'GET':
        questions = Question.query.filter_by(quiz_id=quiz_id).all()
        question_list = []
        for question in questions:
            question_list.append({
                'question_id': question.question_id,
                'question_content': question.question_content,
                'question_type': question.question_type,
                'quiz_id': question.quiz_id,
                'options': question.options.split(','),
                'correct_answer': question.correct_answer,
            })
        return jsonify(question_list), 200
    
    if request.method == 'POST':
        data = request.json
        print(data)
        question = Question(
            question_content=data['text'],
            question_type=data['answer']['type'],
            quiz_id=quiz_id,
            options=','.join(data['options']) if data['answer']['type'] == 'MCQ' else 'true,false' if data['answer']['type'] == 'truefalse' else '',
            correct_answer=data['answer']['correctAnswer'],
            
        )
        db.session.add(question)
        db.session.commit()
        return jsonify({'message': 'Question created successfully'}), 201