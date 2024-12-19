from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    first_name = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    role=db.Column(db.Enum('admin','user'),default='user')
    created_quizzes = db.relationship('Quiz', backref='creator', lazy=True)

class Quiz(db.Model):
    __tablename__ = 'quiz'
    quiz_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    quiz_name = db.Column(db.String(80), unique=True, nullable=False)
    quiz_description = db.Column(db.String(120), nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    

class Question(db.Model):
    __tablename__ = 'question'
    question_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question_content = db.Column(db.String(120), nullable=False)
    question_type = db.Column(db.Enum('mcq','short','tf'),default='mcq')
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.quiz_id'))
    options = db.Column(db.String(120), nullable=True)
    correct_answer = db.Column(db.String(120), nullable=False)
    explation = db.Column(db.String(120), nullable=True)

class QuizAttempt(db.Model):
    __tablename__ = 'quiz_attempt'
    attempt_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.quiz_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    score = db.Column(db.Integer, nullable=False)
    max_score = db.Column(db.Integer, nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)

class QuestionAttempt(db.Model):
    __tablename__ = 'question_attempt'
    question_attempt_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.question_id'))
    attempt_id = db.Column(db.Integer, db.ForeignKey('quiz_attempt.attempt_id'))
    user_answer = db.Column(db.String(120), nullable=False)
    is_correct = db.Column(db.Boolean(), nullable=False)

# class userFeedback(db.Model):
#     __tablename__ = 'user_feedback'
#     feedback_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
#     feedback_content = db.Column(db.String(120), nullable=False)
#     given_at = db.Column(db.DateTime, nullable=False)
    
    