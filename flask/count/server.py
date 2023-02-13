from flask import Flask, redirect, render_template,session
app = Flask(__name__)
app.secret_key = '123123' # set a secret key for security purposes

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
    else:
        session['count'] += 1
    print(session)
    return render_template('index.html')

@app.route('/delete')
def delete():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)