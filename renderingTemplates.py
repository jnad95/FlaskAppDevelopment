from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
@app.route('/home/<name>')
def hello(name=None):
	return render_template('hello.html', name=name)