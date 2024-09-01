# app.py
from flask import Flask, render_template, request, redirect, url_for
from extensions import db
from models import User, Quiz, Question

app = Flask(__name__)

# Configure your database URI here
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quizbuzz.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the Flask app
db.init_app(app)

# Create tables if they don't exist
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/take_quiz/<int:quiz_id>', methods=['GET', 'POST'])
def take_quiz(quiz_id):
    if request.method == 'POST':
        # Handle the form submission here
        return redirect(url_for('dashboard'))
    quiz = Quiz.query.get(quiz_id)
    return render_template('take_quiz.html', quiz=quiz)

if __name__ == '__main__':
    app.run(debug=True)
