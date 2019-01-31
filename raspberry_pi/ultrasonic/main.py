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

import sys
import time

from RPi import GPIO

TRIG = 20
ECHO = 21
SOUND_SPEED = 343  # m/s


def main():
  # 1. Initializes GPIO pins.
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(TRIG, GPIO.OUT)
  GPIO.setup(ECHO, GPIO.IN)
  GPIO.output(TRIG, False)
  print "Waiting For Sensor To Settle..."
  time.sleep(2)

  try:
    while True:
      # 2. Triggers pulse signal.
      GPIO.output(TRIG, True)
      time.sleep(0.00001)
      GPIO.output(TRIG, False)
      # 3. Waits for level raise on output.
      pulse_start = time.time()
      while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
      # 4. Waits for level drop on output.
      pulse_end = time.time()
      while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
      # 5. Calculate distance.
      pulse_duration = pulse_end - pulse_start
      distance = pulse_duration / 2.0 * SOUND_SPEED
      sys.stdout.write('\rDistance: {0:.2f}m   '.format(distance))
  finally:
    GPIO.cleanup()


if __name__ == '__main__':
  main()