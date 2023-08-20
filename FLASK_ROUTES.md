### Routes

`route()` decorator is used to bind a function to a URL
```
@app.route('/')
def index():
	return 'Index Page'

@app.route('/hello'):
def hello():
	return 'Hello, World'
```

------------------------------------------------------------
# Varible Rules
Variable Section could be added in the URL.
- function receives the args as `arg` if route is something like
@app.route('user/<arg>')
- To explicitly specify the type converter could be used.
ex:
```
@app.route('/user/<username>')
def show_user_profile(username):
	# show profile for that user
	return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
	# shows the post for the given id, id is an integer
	return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
	# show the subpath after /path/
	return f'Subpath {escape(subpath)}'
```

------------------------------------------------------------
### Converter Types
| Types  | Explaination                            |
|--------|-----------------------------------------|
| String | accepts any text without slash          |
| int    | accepts positive integers               |
| float  | accespts positive floating point values |
| path   | like string but also accept slashes     |
| uuid   | accepts UUID strings                    |
|--------------------------------------------------|

------------------------------------------------------------
### Unique URL / Redirection Behaviour
1. @app.route('/projects/') # similar to folder pathName
2. @app.route('/about')     # similar to file pathName

If url is access with trailing slash(/) -
	1. it is routed to '/projects/'
	2. it gives 404

If url is accessed without trailing slash(/) -
	1. it is redirected to '/projects/'
	2. it is routed to '/about'

------------------------------------------------------------
### URL binding

url_for is the function used to URL binding instead of manually binding it to a function. Here are the benefits -
1. Reversing is more descriptive than hard-coded URLs
2. Change URLs in one go instead of manually chaning all the places.
3. URL binding handles escaping of special chars transparently.
4. URL paths are always abosulte helps avoiding unexpected behabviour.
5. if your application is places outside URL root, it is handled properly.

Read about context(https://flask.palletsprojects.com/en/2.1.x/quickstart/#context-locals)

