from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play')
def play():
    return render_template("play.html", phrase="hello", times=5)	# notice the 2 new named arguments!

@app.route('/play/<int:num>')
def play2(num):
    return render_template('play2.html', num = num)

@app.route('/play/<int:num>/<string:color>')
def play3(num, color):
    return render_template("play3.html",num = num, color = color)


if __name__=="__main__":
    app.run(debug=True)