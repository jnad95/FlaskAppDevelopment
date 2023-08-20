from flask import Flask

'''
Instance of Flask which takes `Name of the module or package` as
first args. This is needed so that Flask knows where to look for
resources such as templates and static files
'''
app = Flask(__name__)

'''
Route decorator tells which function should be trigger
when this route is visited.
'''
@app.route("/")
def hello_world():
	'''
	This function returns what needs to be sent back to
	browser. default content type is HTML.
	'''
	return "<p>Hello, World!</p>"
