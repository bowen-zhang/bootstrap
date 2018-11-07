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

import time

from RPi import GPIO

PIN = 21


def pressed(channel):
  print 'Button pressed.'


def released(channel):
  print 'Button released.'


def main():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.add_event_detect(PIN, GPIO.FALLING, callback=pressed)
  while True:
    time.sleep(1)


if __name__ == '__main__':
  main()