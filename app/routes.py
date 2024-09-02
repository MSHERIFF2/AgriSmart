from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from app.models import User, db, Quiz
from werkzeug.security import check_password_hash, generate_password_hash

main_routes = Blueprint('main', __name__)

@main_routes.route('/')
def home():
    return render_template('login.html')

@main_routes.route('/dashboard')
@login_required
def dashboard():
    quizzes = Quiz.query.all()
    return render_template('dashboard.html', quizzes=quizzes)

@main_routes.route('/create_quiz', methods=['GET', 'POST'])
@login_required
def create_quiz():
    if request.method == 'POST':
        name = request.form['quiz_name']
        questions = request.form['questions']
        new_quiz = Quiz(name=name, questions=questions)
        db.session.add(new_quiz)
        db.session.commit()
        return redirect(url_for('main.dashboard'))
    return render_template('create_quiz.html')

@main_routes.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('main.login'))
    return render_template('register.html')

@main_routes.route('/take_quiz/<int:quiz_id>', methods=['GET', 'POST'])
def take_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    if request.method == 'POST':
        user_answers = {key: value for key, value in request.form.items() if key.startswith('question_')}
        # Process answers
        # For example, check answers and store results
        return redirect(url_for('main.dashboard'))
    questions = quiz.questions
    return render_template('take_quiz.html', quiz=quiz, questions=questions)
@main_routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('main.dashboard'))
    return render_template('login.html')
@main_routes.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))


