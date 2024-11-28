from flask import Flask, render_template, request, redirect, url_for, session
import re
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
from transformers import pipeline

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Use an environment variable in production

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='manager',
    database='summarylogin'
)

mycursor = mydb.cursor(dictionary=True)

# Initialize the summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        
        mycursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        account = mycursor.fetchone()
        
        if account and check_password_hash(account['password'], password):
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            return redirect(url_for('index'))
        else:
            msg = 'Incorrect username/password!'
    
    return render_template('login.html', msg=msg)

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/index', methods=['GET', 'POST'])
def index():
    if not session.get('loggedin'):
        return redirect(url_for('login'))
    
    summary_text = ""
    
    if request.method == 'POST':
        text_to_summarize = request.form.get("article", "")
        if text_to_summarize:
            summary_text = summarizer(text_to_summarize, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
    
    return render_template('index.html', summary=summary_text)

@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')

        if not username or not password or not email:
            msg = 'Please fill out the form!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        else:
            mycursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
            account = mycursor.fetchone()
            
            if account:
                msg = 'Account already exists!'
            else:
                hashed_password = generate_password_hash(password)
                mycursor.execute('INSERT INTO accounts (username, password, email) VALUES (%s, %s, %s)', 
                                 (username, hashed_password, email))
                mydb.commit()
                msg = 'You have successfully registered! You can now log in.'
    
    return render_template('register.html', msg=msg)

if __name__ == '__main__':
    app.run(debug=True)