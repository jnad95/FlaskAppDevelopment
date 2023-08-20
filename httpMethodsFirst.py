from flask import request, Flask

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		return do_the_login()
	else:
		return show_the_login_form()

def do_the_login():
	return '<p> You can proceed with login</p>'

def show_the_login_form():
	return '<p> You cant proceed with login</p>'