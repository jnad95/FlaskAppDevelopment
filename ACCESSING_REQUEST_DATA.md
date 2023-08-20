### Accessing Request Data

Flask has a global Object for caputring request data know as `Request` Object(https://flask.palletsprojects.com/en/2.1.x/api/#flask.request)

## Context locals
When Flask starts its internal request handling it figures out that the current thread is the active context and binds the current application and the WSGI environments to that context (thread). It does that in an intelligent way so that one application can invoke another application without breaking.

```
from flask import Flask

with app.test_request_context('/home', method='POST'):
	# now you can do something with the request until the
	# end of the with block, such as basic assertions:
	assert request.path == '/hello'
	assert request.method == 'POST'
```

```
with app.request_context(environ):
	assert request.method == 'POST'
```

## Request object

```
from flask import request, Flask, render_template

app = Flask(__name__)

@app.route('/login', methods=['POST', 'GET'])
def login():
	error = None
	if request.method == 'POST':
		if valid_login(	request.form['username'],
						request.form['password']):
			return log_the_user_in(request.form['username'])
		else:
			error = 'Invalid username/password'
	# the code below is executed ifg the request method
	# was GET or the credentials were invalid
	return render_template('login.html', error=error)
```
