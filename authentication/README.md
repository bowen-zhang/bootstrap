# What

Authenticates http request handlers using Google OAuth.

# How

1. Creates OAuth client id.

    1. Logins at console.cloud.google.com

    1. Goes to "APIs & Services" => "Credentials".

    1. Clicks "Create Credentials", select "OAuth Client ID"

    1. Selects "Web application".

    1. Adds "http://localhost:5000" to Authorized javascript origins".

    1. Adds "http://localhost:5000/oauth2callback" to "Authorized redirect URIs".

    1. "Save"

    1. Copy client id and client secret.

1. Create Oauth app.

    ```python
    app = flask.Flask(__name__)
    app.secret_key = "__somthing__"

    oauth = client.OAuth(app)
    google = oauth.remote_app(
        'google',
        consumer_key="[client id]",
        consumer_secret="[client secret]",
        request_token_params={
            'scope': 'email',
        },
        base_url='https://www.googleapis.com/oauth2/v1/',
        request_token_url=None,
        access_token_method='POST',
        access_token_url='https://accounts.google.com/o/oauth2/token',
        authorize_url='https://accounts.google.com/o/oauth2/auth',
    )
    ```

1. Authentication.

    For each Flask route that requires authentication, add the following at the
    beginning of the handler method:

    ```python
    access_token = flask.session.get('access_token')
    if access_token is None:
      callback = flask.url_for('authorized', _external=True)
      return google.authorize(callback=callback)
    ```

1. Authorization.

    In authentication callback method, retrieves user info to check if user is
    authorized.

    ```python
    @app.route('/oauth2callback')
    def authorized():
      resp = google.authorized_response()
      access_token = resp['access_token']
      user = google.get('userinfo', token=(access_token, '')).data
      if user['email'] == '[email of authorized user]':
        flask.session['access_token'] = access_token, ''
        return flask.redirect(flask.url_for('index'))
      else:
        return 'Not authorized'
    ```

# Example Code

To run example code:

1. Gets client secret.

    Download Oauth client id json file from Google Cloud console, save as
    "client_secret.json" in same directory.

1. Creates authorized user list.

    Creates "authorized_users.txt" in same directory, add emails of all authorized
    users in it, one per line.

1. Runs.

    ```shell
    make init
    make run
    ```

# Resources

* [flask-oauthlib](https://github.com/lepture/flask-oauthlib)