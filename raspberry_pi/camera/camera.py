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
import io
import picamera
import threading
import time


class Camera(object):
  def __init__(self):
    self._camera = None

  @property
  def camera(self):
    if not self._camera:
      self._camera = picamera.PiCamera()
    return self._camera


class VideoStreamer(object):
  _TIMEOUT_SEC = 10

  def __init__(self, camera):
    self._camera = camera
    self._thread = None
    self._subscribers = {}
    self._frame = None
    self._stop_time = time.time()

  def subscribe(self):
    subscriber = _VideoFrameIterator(self)
    self._subscribers[subscriber] = threading.Event()
    return subscriber

  def unsubscribe(self, subscriber):
    del self._subscribers[subscriber]
    if not self._subscribers:
      self._stop_time = time.time()

  def get_frame(self, subscriber):
    self._stop_time = time.time() + VideoStreamer._TIMEOUT_SEC
    if not self._thread:
      self._ready_events = []
      self._thread = threading.Thread(target=self._run)
      self._thread.daemon = True
      self._thread.start()

    event = self._subscribers[subscriber]
    event.wait()
    event.clear()
    return self._frame

  def _init_camera(self):
    self._camera.camera.resolution = (1024, 768)
    self._camera.camera.framerate = 30
    self._camera.camera.annotate_background = picamera.color.Color('#777777')
    return self._camera.camera

  def _run(self):
    with self._init_camera() as camera:
      stream = io.BytesIO()
      for _ in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
        if time.time() > self._stop_time:
          break
        stream.seek(0)
        data = stream.read()
        stream.seek(0)
        stream.truncate()

        self._frame = data
        for event in self._subscribers.values():
          event.set()

        now = datetime.datetime.now()
        camera.annotate_text = '{0} - {1: %Y/%m/%d %H:%M:%S}'.format(
            'Room', now)

    self._thread = None


class _VideoFrameIterator(object):
  def __init__(self, streamer):
    self._streamer = streamer

  def __enter__(self):
    return self

  def __exit__(self, type, value, traceback):
    self._streamer.unsubscribe(self)

  def __iter__(self):
    return self

  def next(self):
    return self._streamer.get_frame(self)
