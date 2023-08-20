### Rendering Templates

Flask provide `render_template()` to render html templates.
it takes template and args that needs to be passed to template.

```
from flask import render_template


@app.route('/home')
@app.route('/home/<name>')
def hello(name=None):
	return render_template(hello.html, name=name)
```

Flask will look for templates at `templates` folder
if your application is a 
 > module, this folder is next to that module. 
```
/application.py
/templates
    /hello.html
```
 > package it’s actually inside your package.
```
/application
    /__init__.py
    /templates
        /hello.html
```

Inside templates you also have access to 
1. objects
	> config, 
	> request, 
	> session,
	> g(https://flask.palletsprojects.com/en/2.1.x/quickstart/#id3)

2. functions - 
	> url_for()
	> get_flashed_messages()

Templates are useful if inheritance is used.
Template inheritance(https://flask.palletsprojects.com/en/2.1.x/patterns/templateinheritance/)
Using templates you can write certain page elements once and reuse them whenever required.
Additionally in templates, automatic escaping is enabled. You can mark certain elements as safe(skip escaping) by using Markup class(https://flask.palletsprojects.com/en/2.1.x/api/#flask.Markup) or by using `| safe` filter on template.

```
from markupsafe import Markup
Markup('<strong>Hello %s!<strong>') % '<blink>hacker</blink>')
Markup.escape('<blink>hacker</blink>')
Markup('<em>Marked up</em> &raquo; HTML').striptags()
```

SQLite3 with Flask(https://flask.palletsprojects.com/en/2.1.x/)patterns/sqlite3/