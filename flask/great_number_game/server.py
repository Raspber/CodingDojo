from flask import Flask, redirect, render_template, session, random
app = Flask(__name__)
app.secret_key = '123123'  # set a secret key for security purposes
random.randint(1, 100)

@app.route('/')
def index():
    session = random.randint(1,100)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
