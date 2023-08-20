### HOW TO RUN

## To run the app use `flask` or `python -m flask`
*Before running, set environment variable `FLASK_APP` to tell what to run.
```
export FLASK_APP=minimalApp
flask run
```

----------------------------------------------------

From @link: https://flask.palletsprojects.com/en/2.1.x/quickstart/

```
Application Discovery Behavior

As a shortcut, if the file is named app.py or wsgi.py, you don’t have to set the FLASK_APP environment variable. See Command Line Interface(https://flask.palletsprojects.com/en/2.1.x/cli/) for more details.
```

----------------------------------------------------

## Flask in Development Mode
To enable all development features, set the FLASK_ENV environment variable to development before calling flask run.
```
export FLASK_ENV_development
flask run
```