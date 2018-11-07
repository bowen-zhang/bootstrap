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

import datetime
import flask
import picamera
import time

app = flask.Flask('my demo')
camera = None


@app.route('/image')
def capture_image():
  camera.hflip = False
  camera.vflip = False
  camera.rotation = 0  # 0,90,180,270
  camera.capture('image.jpg')
  return 'OK'


@app.route('/video')
def record_video():
  camera.start_recording(
      'video.h264', format='h264', resize=(640, 480), bitrate=1000000)
  for _ in range(10):
    now = datetime.datetime.now()
    camera.annotate_text = '{0} - {1: %Y/%b/%d %H:%M:%S}'.format('Room', now)
    time.sleep(1)
  camera.stop_recording()
  return 'OK'


@app.route('/stream')
def stream_video():
  return flask.Response(
      _stream_video(), mimetype='multipart/x-mixed-replace; boundary=frame')


def _stream_video():
  camera.resolution = (1024, 768)
  camera.framerate = 30
  camera.annotate_background = picamera.color.Color('#777777')

  stream = io.BytesIO()
  for _ in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
    stream.seek(0)
    data = stream.read()
    stream.seek(0)
    stream.truncate()

    yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + data + b'\r\n')

    now = datetime.datetime.now()
    camera.annotate_text = '{0} - {1: %Y/%m/%d %H:%M:%S}'.format('Room', now)


if __name__ == '__main__':
  global camera
  camera = picamera.PiCamera()
  app.run(host='0.0.0.0', port=8080, debug=True)