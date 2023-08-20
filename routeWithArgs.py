from flask import Flask

app = Flask(__name__)

@app.route('/<name>')
def profile(name):
	return f'You have accessed profile of {name}'
	