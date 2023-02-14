from flask import Flask, redirect, render_template,session,request
app = Flask(__name__)
app.secret_key = '123123'


# import statements, maybe some other routes
@app.route('/')
def index():
    session.clear()
    return render_template('index.html')


# our index route will handle rendering our form
@app.route('/submit', methods = ['POST'])
def submit():
# Here we properties to session to store the form inputs
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['dojo_timezone'] = request.form['dojo_timezone']
    session['current_stack'] = request.form['current_stack']
    session['comments'] = request.form['comments']
# Never render a template on a POST request.
# Instead we will redirect to route.
    print(session)
    return redirect('/user_survey')


# adding this method route to show user after submitting
@app.route('/user_survey')
def user_survey():
    return render_template('user_survey.html')


# app.run(debug=True) should be the very last statement! 
if __name__=="__main__":
    app.run(debug=True)