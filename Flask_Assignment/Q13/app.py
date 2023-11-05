from flask import Flask, render_template, request, redirect
from flask import flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sign-up', methods =['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        req = request.form

        username = req.get("username")
        email = req.get("email")
        password = req.get("password")

        #print(username, email, password)

        if not len(password) >= 8:
            flash("Password must be 8 character in length")
            return redirect(request.url)
        
        flash("Account Created")
        return redirect(request.url)

    return render_template('/sign_up.html')





if __name__ == '__main__':
    app.run(debug=True)