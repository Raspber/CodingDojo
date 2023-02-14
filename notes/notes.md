STATIC FILES

<!-- linking a css style sheet -->
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/my_style.css') }}">

<!-- linking a javascript file -->
<script type="text/javascript" src="{{ url_for('static', filename='js/my_script.js') }}"></script>

<!-- linking an image -->
<img src="{{ url_for('static', filename='img/my_img.png') }}">


SERVER.PY FILE

from flask import Flask, render_template,request,redirect,session
app = Flask(__name__)
app.secret_key = '123'

# our index route will handle rendering our form

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")

# Here we add two properties to session to store the name and email
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect('/show')
    
# adding this method route to show user after submitting
@app.route('/show')
def show_user():
    return render_template('show.html')


# app.run(debug=True) should be the very last statement! 
if __name__ == "__main__":
    app.run(debug=True)