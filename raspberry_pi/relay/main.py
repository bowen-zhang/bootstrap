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


def init(pin):
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, GPIO.HIGH)


def toggle(pin):
  GPIO.output(pin, GPIO.LOW)
  time.sleep(0.3)
  GPIO.output(pin, GPIO.HIGH)


def off(pin):
  GPIO.output(pin, GPIO.LOW)


def on(pin):
  GPIO.output(pin, GPIO.HIGH)


def main():
  pin = 18
  init(pin)
  toggle(pin)


if __name__ == '__main__':
  main()
