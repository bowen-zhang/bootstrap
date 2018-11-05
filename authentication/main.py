# Copyright 2018 Bowen Zhang
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import flask
import functools
import json

from flask_oauthlib import client

REDIRECT_URI = '/oauth2callback'

with open('authorized_users.txt') as f:
  authorized_users = f.readlines()
with open('client_secret.json') as f:
  config = json.loads(f.read())

app = flask.Flask(__name__)
app.secret_key = "__somthing__"

oauth = client.OAuth(app)
google = oauth.remote_app(
    'google',
    consumer_key=config['web']['client_id'],
    consumer_secret=config['web']['client_secret'],
    request_token_params={
        'scope': 'email',
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)


def authorized_only(f):
  @functools.wraps(f)  # to preserve __name__, __doc__, __module__
  def wrapper(*args, **kwargs):
    access_token = flask.session.get('access_token')
    if access_token is None:
      callback = flask.url_for('authorized', _external=True)
      return google.authorize(callback=callback)
    else:
      return f(*args, **kwargs)

  return wrapper


@app.route(REDIRECT_URI)
def authorized():
  resp = google.authorized_response()
  access_token = resp['access_token']
  user = google.get('userinfo', token=(access_token, '')).data
  if user['email'] in authorized_users:
    flask.session['access_token'] = access_token, ''
    flask.session['user'] = user
    return flask.redirect(flask.url_for('index'))
  else:
    return 'Not authorized'


@app.route('/')
@authorized_only
def index():
  return flask.jsonify(flask.session.get('user'))


if __name__ == '__main__':
  app.run(debug=True)