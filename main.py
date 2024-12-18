from flask import Flask, request, jsonify
from models import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'

db.init_app(app)

from blueprints.auth_bp import auth_bp
from blueprints.frontend.frontend_bp import frontend_bp

app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(frontend_bp)

if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)