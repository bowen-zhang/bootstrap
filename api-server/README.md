# What

Make an API server.

# How

## GET only

1. Imports Flask library.

    ```python
    import flask
    ```

1. Creates a Flask instance.

    ```python
    app = flask.Flask('my demo')
    ```

1. Creates a request handler method that returns response in string.

    ```python
    @app.route('/get-data')
    def handler():
        return 'my results'
    ```

1. Starts Flask app in main entry.

    ```python
    app.run(host='0.0.0.0', port=8080, debug=True)
    ```

## Restful APIs

1. Creates a handler class and derives from flask_restful.Resource).

    ```python
    class RestfulApiService(flask_restful.Resource):
        def get(self):
            return 'my results'

        def post(self):
            # do something
            return 'OK'
    ```

2. Creates api instance.

    ```python
    api = flask_restful.Api(app)
    ```

3. Adds handler class type and path mapping.

    ```python
    api.add_resource(RestfulApiService, '/restful/<string:user_id>')
    ```

# References

* [Flask](http://flask.pocoo.org/)
* [Flask-Restful](https://flask-restful.readthedocs.io/en/latest/index.html)
* [JsonPickle](http://jsonpickle.github.io/)
* [Postman](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=en)