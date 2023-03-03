from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', username='username')

@app.route('/login', methods=['POST'])
def authenticate():
    username = request.form['username']
    password = request.form['password']

    # Perform authentication logic here
    if username == 'username' and password == 'password':
        # Redirect to dashboard if authentication succeeds
        return redirect(url_for('dashboard'))

    # Otherwise, show error message
    return render_template('login.html', error='Invalid username or password.')
