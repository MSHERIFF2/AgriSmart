from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from app.models import User, db, Quiz
from werkzeug.security import check_password_hash, generate_password_hash
from app.forms import LoginForm

main_routes = Blueprint('main', __name__)

@main_routes.route('/', methods=['GET', 'POST'])
def home():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('main.dashboard'))
    return render_template('login.html', form=form)

@main_routes.route('/dashboard')
@login_required
def dashboard():
    quizzes = Quiz.query.all()
    return render_template('dashboard.html', quizzes=quizzes)

@main_routes.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if current_user.is_authenticated:
        if current_user.is_admin:
            return redirect(url_for('admin_page'))
        else:
            return redirect(url_for('admin_login'))
    
    form = LoginForm()  # Assuming you have a form class for login
    
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            if user.is_admin:
                login_user(user)
                return redirect(url_for('admin_page'))
            else:
                flash('You are not authorized to access the admin section.')
                return redirect(url_for('login'))
    
    return render_template('admin_login.html', form=form)

@main_routes.route('/admin_page')
@login_required
def admin_page():
    if not current_user.is_admin:
        flash('You do not have permission to access this page.')
        return redirect(url_for('home'))

    return render_template('admin_page.html')

@main_routes.route('/admin_register', methods=['GET', 'POST'])
def admin_register():
    if request.method == 'POST':
        # You may want to include a verification step here
        # For example, checking a special admin code or invitation link
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        admin_code = request.form.get('admin_code')  # Example of an admin verification step

        # Verify the admin code (implement your own logic)
        if admin_code == 'M08170205738$s':
            new_admin = User(username=username, password=password, is_admin=True)
            db.session.add(new_admin)
            db.session.commit()
            return redirect(url_for('main.admin_login'))
        else:
            flash('Invalid admin code', 'danger')
    
    return render_template('admin_register.html')


@main_routes.route('/create_quiz', methods=['GET', 'POST'])
@login_required
def create_quiz():
     if not current_user.is_admin:
        flash('You do not have permission to create quizzes.')
        return redirect(url_for('dashboard'))
     
     if request.method == 'POST':
        quiz_title = request.form.get('title')
        quiz_description = request.form.get('description')
        question_texts = request.form.getlist('question_text')
        options_texts = request.form.getlist('option_text')
        correct_option_indices = request.form.getlist('correct_option')

        new_quiz = Quiz(title=quiz_title, description=quiz_description)
        db.session.add(new_quiz)
        db.session.commit()

        question_index = 0
        while question_index < len(question_texts):
            new_question = Question(text=question_texts[question_index], quiz_id=new_quiz.id)
            db.session.add(new_question)
            db.session.commit()

            option_start_index = question_index * 4
            for i in range(option_start_index, option_start_index + 4):
                if i < len(options_texts):
                    is_correct = str(i - option_start_index) == correct_option_indices[question_index]
                    new_option = Option(text=options_texts[i], is_correct=is_correct, question_id=new_question.id)
                    db.session.add(new_option)

            db.session.commit()
            question_index += 1

        flash('Quiz created successfully!')
        return redirect(url_for('dashboard'))

        return render_template('create_quiz.html')

@main_routes.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        new_user = User(username=username, password=password)
        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('main.admin_login'))
        except Exception as e:
            db.session.rollback()
            flash('Error registering user: {}'.format(str(e)), 'error')

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

@main_routes.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))


