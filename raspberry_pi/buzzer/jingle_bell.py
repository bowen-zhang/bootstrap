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

import RPi.GPIO as GPIO
import time

PIN = 20


def on():
  GPIO.setup(PIN, GPIO.OUT)
  GPIO.output(PIN, GPIO.LOW)


def off():
  GPIO.setup(PIN, GPIO.IN)


def play():
  notes = 'eeeeeeegcde fffffeeeeddedg'
  beats = [
      1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
      2, 2
  ]
  tones = {
      'c': 0.001915,
      'd': 0.001700,
      'e': 0.001519,
      'f': 0.001432,
      'g': 0.001275,
      'a': 0.001136,
      'b': 0.001014,
      'C': 0.000956
  }
  tempo = 0.2
  for (note, beat) in zip(notes, beats):
    duration = beat * tempo
    if note == ' ':
      off()
      time.sleep(duration)
    else:
      tone = tones[note]
      i = 0
      while i < duration:
        on()
        time.sleep(tone)
        off()
        time.sleep(tone)
        i = i + tone * 2
      time.sleep(0.01)


def main():
  GPIO.setmode(GPIO.BCM)
  off()
  play()
  off()
  GPIO.cleanup()


if __name__ == '__main__':
  main()