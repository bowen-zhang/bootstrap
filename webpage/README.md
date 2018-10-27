# What

Serves webpage on a machine for access from other machines in same network.

# How

## Basic Usage

1. Imports flask
    ```python
    import flask
    ```

1. Creates a Flask instance with arbitrary name as parameter.

    ```python
    app = flask.Flask('some name')
    ```

1. Call run() of Flask instance.

    ```python
    app.run(host='0.0.0.0', port=8080, debug=True)
    ```

    * host: by default, host = '127.0.0.1', meaning the web server is only
    accessible on local machine. To allow access from another machine in same
    network, set host = '0.0.0.0'.

    * debug: True allows run-time reloading whenever a file changes.

1. Put webpage under "static" directory.

    Any file under "static" directory can be accessed as:
    
    http://[ip]:[port]/static/[filename]

## Uses String Directly

```python
@app.route("/demo1")
def demo1():
  return "Demo1: Hello World!"
```

## Uses Template

1. Put templage html under "templates" directory.

    Variables can be accessed in html as:

    {{ variableName }}

1. Call flask.render_template.

    ```python
    @app.route('/demo2')
    @app.route('/demo2/<name>')
    def demo2(name='World'):
      return flask.render_template('template.html', name=name)
    ```

# References

* [Flask](http://flask.pocoo.org/)
