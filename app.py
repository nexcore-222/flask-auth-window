from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import os
import bcrypt

app = Flask(__name__)
app.secret_key = 'qwerty' #You should change this to somethimg more secure :D
DATABASE = 'users.db'

#Initialization of the database
def init_db():
    if not os.path.exists(DATABASE):
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password BLOB)''')
        #Hash admin password
        password = b"admin"
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        #Send hashed password to database
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("admin", hashed))

        conn.commit()
        conn.close()

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password'].encode('utf-8')
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        #Fetch hashed password from database
        c.execute("SELECT password FROM users WHERE username=?", (username,))
        row = c.fetchone()
        conn.close()
        if row:
            hashed_password = row[0]
            if isinstance(hashed_password, str):
                hashed_password = hashed_password.encode('utf-8')
            #Compare passwords
            if bcrypt.checkpw(password, hashed_password):
                session['username'] = username
                return redirect(url_for('dashboard'))
            
        return render_template('login.html', error='Error: Invalid username or password')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return f"Welcome, {session['username']}!"
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

#Creation of the database and running the app in debug mode
if __name__ == '__main__':
    init_db()
    app.run(debug=True)
