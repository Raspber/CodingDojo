from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play')
def play():
    return render_template("play.html", phrase="hello", times=5)	# notice the 2 new named arguments!

@app.route('/play/<int:num>')
def play(num):
    return render_template('play2.html', num = num)



if __name__=="__main__":
    app.run(debug=True)