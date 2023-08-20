from flask import Flask

app = Flask(__name__)

@app.route('/projects/')
def projects():
	return 'This is project page'

@app.route('/about')
def about():
	return 'This is about page'
	