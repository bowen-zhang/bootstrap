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

import threading
import time

from RPi import GPIO

_PIN = 17
_MOTION_TIMEOUT_SEC = 8

timer = None


def triggered(pin):
  global timer

  if timer:
    timer.cancel()
    timer = None

  has_motion = GPIO.input(pin)
  if has_motion:
    print 'Motion detected.'
  else:
    timer = threading.Timer(_MOTION_TIMEOUT_SEC, motion_stopped)
    timer.start()


def motion_stopped():
  print 'Motion stopped.'


def main():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(_PIN, GPIO.IN)
  GPIO.add_event_detect(_PIN, GPIO.BOTH, callback=triggered)

  try:
    while True:
      time.sleep(1)
  finally:
    GPIO.remove_event_detect(_PIN)
    GPIO.cleanup()


if __name__ == '__main__':
  main()