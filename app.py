from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import os
from flask_bcrypt import Bcrypt


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

@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template('dashboard.html', user=session['user'])
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

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
