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
import flask_restful
import jsonpickle

app = flask.Flask('my demo')


class Data(object):
  def __init__(self):
    self.value = 1
    self.message = 'Hello World!'


@app.route('/simple/get-string')
def _get_string():
  return 'OK!'


class SimpleApiService(object):
  def __init__(self, app):
    app.add_url_rule('/simple/get-json', view_func=self._get_json)

  def _get_json(self):
    data = Data()
    return flask.Response(
        response=jsonpickle.encode(data),
        status=200,
        mimetype='application/json')


class RestfulApiService(flask_restful.Resource):
  _users = {}

  def get(self, user_id):
    if user_id in self._users:
      return self._users[user_id]
    else:
      return -1

  def post(self, user_id):
    self._users[user_id] = flask.request.form['data']
    return 'OK'


if __name__ == '__main__':
  simple_api_service = SimpleApiService(app)
  api = flask_restful.Api(app)
  api.add_resource(RestfulApiService, '/restful/<string:user_id>')
  app.run(host='0.0.0.0', port=8080, debug=True)