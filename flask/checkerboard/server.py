from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<int:x>')
def single_parameter(x):
    return render_template('x.html', x = x)

@app.route('/<int:x>/<int:y>')
def two_parameters(x, y):
    return render_template('xy.html', x = x, y = y)

@app.route('/<int:x>/<int:y>/<string:x_color>/<string:y_color>')
def multi(x, y, x_color, y_color):
    return render_template('multi.html', x = x, y = y, x_color = x_color, y_color = y_color)

if __name__=="__main__":
    app.run(debug=True) 