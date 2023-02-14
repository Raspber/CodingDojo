from flask import Flask, redirect, render_template, session,request
app = Flask(__name__)
app.secret_key = '123123'  # set a secret key for security purposes
import random

@app.route('/')
def index():
    if 'random_num' not in session:
        session['random_num'] = random.randint(1,100)
    print(session)
    return render_template('index.html')

@app.route('/guess', methods =['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    return redirect('/')

@app.route('/play_again')
def play_again():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
