from flask import Flask, render_template, request, session, redirect, url_for
from flask_session import Session

app = Flask(__name__)

app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route('/')
def home():
    return render_template('index.html', user_data=session.get('user_data'))

@app.route('/login', methods=['POST'])
def login():
    user_data = request.form['user_data']
    session['user_data'] = user_data
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('user_data', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=5002)
