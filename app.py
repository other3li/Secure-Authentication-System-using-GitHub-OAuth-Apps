from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL
from flask_session import Session
import bcrypt
import os
import re
from dotenv import load_dotenv
from authlib.integrations.flask_client import OAuth
from functools import wraps

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'fallback-secret-key')

# Database configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = os.getenv('DB_PASSWORD', '')
app.config['MYSQL_DB'] = 'github_task2'
app.config['SESSION_TYPE'] = 'filesystem'

# Initialize extensions
mysql = MySQL(app)
Session(app)

# Initialize OAuth
oauth = OAuth(app)

# Register GitHub OAuth
github = oauth.register(
    name='github',
    client_id=os.getenv('GITHUB_CLIENT_ID'),
    client_secret=os.getenv('GITHUB_CLIENT_SECRET'),
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize',
    api_base_url='https://api.github.com/',
    client_kwargs={'scope': 'user:email'},
)

# ==================== Helper Functions ====================

def is_password_strong(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[!@#$%^&*()_+]", password):
        return False
    return True

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('You must be logged in to access this page.', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# ==================== Routes ====================

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username_or_email = request.form['username_or_email']
        password = request.form['password']

        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM users WHERE username = %s OR email = %s', (username_or_email, username_or_email))
        user = cursor.fetchone()
        cursor.close()

        if user and bcrypt.checkpw(password.encode('utf-8'), user[3].encode('utf-8')):
            session['user_id'] = user[0]
            session['username'] = user[1]

            cursor = mysql.connection.cursor()
            cursor.execute('INSERT INTO login_logs (user_id, ip_address) VALUES (%s, %s)', (user[0], request.remote_addr))
            mysql.connection.commit()
            cursor.close()

            flash('Login successful!', 'success')
            return redirect(url_for('home'))

        flash('Invalid username or password', 'danger')
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if not is_password_strong(password):
            flash('Password must contain: 8+ chars, 1 uppercase, 1 lowercase, 1 number, 1 special char', 'danger')
            return redirect(url_for('signup'))

        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        cursor = mysql.connection.cursor()
        try:
            cursor.execute(
                'INSERT INTO users (username, email, password_hash, auth_method) VALUES (%s, %s, %s, %s)',
                (username, email, hashed_pw, 'manual')
            )
            mysql.connection.commit()
            flash('Account created successfully! Please login.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            mysql.connection.rollback()
            flash('Username or email already exists', 'danger')
        finally:
            cursor.close()

    return render_template('signup.html')

@app.route('/login/github')
def github_login():
    callback_url = url_for('github_callback', _external=True)
    return github.authorize_redirect(callback_url)

@app.route('/login/github/callback')
def github_callback():
    cursor = None
    try:
        token = github.authorize_access_token()
        if not token:
            flash('GitHub authorization failed', 'danger')
            return redirect(url_for('login'))

        resp = github.get('user')
        if resp.status_code != 200:
            flash('Failed to fetch user data from GitHub', 'danger')
            return redirect(url_for('login'))

        user_info = resp.json()
        github_id = str(user_info['id'])
        email = user_info.get('email')
        if not email:
            email = f"{user_info['login']}@users.noreply.github.com"

        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM users WHERE github_id = %s', (github_id,))
        user = cursor.fetchone()

        if not user:
            cursor.execute(
                'INSERT INTO users (username, email, github_id, auth_method) VALUES (%s, %s, %s, %s)',
                (user_info['login'], email, github_id, 'github')
            )
            mysql.connection.commit()
            user_id = cursor.lastrowid
        else:
            user_id = user[0]

        session['user_id'] = user_id
        session['username'] = user_info['login']
        flash('Login successful via GitHub!', 'success')
        return redirect(url_for('home'))

    except Exception as e:
        flash(f'GitHub login error: {str(e)}', 'danger')
        return redirect(url_for('login'))
    finally:
        if cursor:
            cursor.close()

@app.route('/home')
@login_required
def home():
    return render_template('home.html', username=session['username'])

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out successfully', 'success')
    return redirect(url_for('login'))

# ==================== Run the Server ====================

if __name__ == '__main__':
    app.run(debug=True, port=8000)
