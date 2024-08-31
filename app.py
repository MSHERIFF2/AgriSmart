from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import os
from flask_bcrypt import Bcrypt
from datetime import datetime



app = Flask(__name__)
app.secret_key = 'M08170205738$s'
bcrypt = Bcrypt(app)

#configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///quizbuzz.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)

#Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
#Define the Quiz model
class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    questions = db.relationship('Question', backref='quiz', lazy=True)
#Define the Question model
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(200), nullable=False)
    answer = db.Column(db.String(100), nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)

#Initialize the database (Run this once)
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('register.html')

@app.route('/create_quiz', methods=['GET' 'POST'])
def create_quiz():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form.get('description', '')
        new_quiz = Quiz(title=title, description=description)
        db.session.add(new_quiz)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('create_quiz.html')

@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        quizzes = Quiz.query.all()
        return render_template('dashboard.html', user=session['user'], quizzes=quizzes)
    else:
        return redirect(url_for('home'))

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    '''simple user authentication logic
    if username == 'admin' and password == 'password':
        session['user'] = username
        return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('home'))
    '''
    #Simple user authentication logic (to be repalced with database validation
    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        session['user'] = username
        return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('home'))

@app.route('/quiz/<int:quiz_id>', methods=['GET', 'POST'])
def take_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    if request.method == 'POST':
        #Logic to handle the submission of quiz answers
        answers = request.form.getlist('answers')
        score = 0
        for i, question in enumerate(quiz.questions):
            if i < len(answers) and answer[i].strip().lower() == question.answer.strip().lower():
                score += 1
        #store results in session or database
        session['score'] = score
        return redirect(url_for('quiz_results', quiz_id=quiz.id))
    return render_template('take_quiz.html', quiz=quiz)
@pp.route('/quiz/<int:quiz_id>/results')
def quiz_results(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    score = session.get('score', 0)
    total_questions = len(quiz.questions)
    return render_template('quiz_results.html', score=score, total_questions=total_questions, quiz=quiz)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
