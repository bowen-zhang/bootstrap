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
import flask_oauth
import functools

#GOOGLE_CLIENT_ID = '[client id]'
#GOOGLE_CLIENT_SECRET = '[secret]'
GOOGLE_CLIENT_ID = '466493781521-u3duaojirc4ifiind9lq7p3h8c91vb51.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = '3jD2fPtLy0VEgX0EYCrg57Dx'

REDIRECT_URI = '/oauth2callback'

app = flask.Flask(__name__)
app.secret_key = "__somthing__"

oauth = flask_oauth.OAuth()
google = oauth.remote_app(
    'google',
    base_url='https://www.google.com/accounts/',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    request_token_url=None,
    request_token_params={
        'scope': 'https://www.googleapis.com/auth/userinfo.email',
        'response_type': 'code'
    },
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_method='POST',
    access_token_params={'grant_type': 'authorization_code'},
    consumer_key=GOOGLE_CLIENT_ID,
    consumer_secret=GOOGLE_CLIENT_SECRET)


def authorized_only(f):
  @functools.wraps(f)  # to preserve __name__, __doc__, __module__
  def wrapper(*args, **kwargs):
    access_token = flask.session.get('access_token')
    if access_token is None:
      return flask.redirect(flask.url_for('login'))
    else:
      return f(*args, **kwargs)

  return wrapper


@app.route('/')
@authorized_only
def index():
  return 'This is a secret message.'


@app.route('/login')
def login():
  callback = flask.url_for('authorized', _external=True)
  return google.authorize(callback=callback)


@app.route(REDIRECT_URI)
@google.authorized_handler
def authorized(resp):
  access_token = resp['access_token']
  user = google.get(url='userinfo', token=(token, '')).data
  flask.session['access_token'] = access_token, ''
  return flask.redirect(flask.url_for('index'))


@google.tokengetter
def get_access_token():
  return flask.session.get('access_token')


if __name__ == '__main__':
  app.run(debug=True)