from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'M08170205738$s'
bcrypt = Bcrypt(app)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quizbuzz.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Import models and forms
from models import User, Quiz, Question
from forms import RegisterForm, LoginForm, QuizForm, QuestionForm

# Initialize the database (Run this once)
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        session['user'] = username
        return redirect(url_for('dashboard'))
    flash('Invalid credentials, please try again.', 'danger')
    return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        quizzes = Quiz.query.all()
        return render_template('dashboard.html', user=session['user'], quizzes=quizzes)
    return redirect(url_for('home'))

@app.route('/create_quiz', methods=['GET', 'POST'])
def create_quiz():
    form = QuizForm()
    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        new_quiz = Quiz(title=title, description=description)
        db.session.add(new_quiz)
        db.session.commit()
        flash('Quiz created successfully!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('create_quiz.html', form=form)

@app.route('/quiz/<int:quiz_id>')
def view_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    return render_template('view_quiz.html', quiz=quiz)

@app.route('/quiz/<int:quiz_id>/add_question', methods=['GET', 'POST'])
def add_question(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    form = QuestionForm()
    if form.validate_on_submit():
        question_text = form.question_text.data
        answer = form.answer.data
        new_question = Question(question_text=question_text, answer=answer, quiz_id=quiz.id)
        db.session.add(new_question)
        db.session.commit()
        flash('Question added successfully!', 'success')
        return redirect(url_for('view_quiz', quiz_id=quiz.id))
    return render_template('add_question.html', form=form, quiz=quiz)

@app.route('/quiz/<int:quiz_id>', methods=['GET', 'POST'])
def take_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    if request.method == 'POST':
        answers = request.form.getlist('answers')
        score = 0
        for i, question in enumerate(quiz.questions):
            if i < len(answers) and answers[i].strip().lower() == question.answer.strip().lower():
                score += 1
        session['score'] = score
        return redirect(url_for('quiz_results', quiz_id=quiz.id))
    return render_template('take_quiz.html', quiz=quiz)

@app.route('/quiz/<int:quiz_id>/results')
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
