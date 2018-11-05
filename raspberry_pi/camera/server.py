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

import camera
import flask

app = flask.Flask('my demo')
streamer = camera.VideoStreamer(camera.Camera())


@app.route('/video')
def stream_video():
  return flask.Response(
      _stream_video(), mimetype='multipart/x-mixed-replace; boundary=frame')


def _stream_video():
  with streamer.subscribe() as subscriber:
    for frame in subscriber:
      yield (b'--frame\r\n'
             b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)