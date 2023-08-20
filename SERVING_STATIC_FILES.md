### Serving Static files

Create a folder with name `static`, to make it available at `/static`

To generate URLs for static files, use the special 'static' endpoint name:

```
url_for('static', filename='style.css')
```

The file has to be stored on the filesystem as static/style.css.