from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("index1.html")

@app.route('/submit', methods= ['POST'])
def display_name():
    name = request.form['user_input']
    return f"Hi {name}. Welcome to the page."

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5001)