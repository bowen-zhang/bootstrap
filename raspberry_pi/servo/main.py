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
import wiringpi

PIN = 18


def main():
  # 1. Uses GPIO naming
  wiringpi.wiringPiSetupGpio()

  # 2. Sets GPIO pin to be a PWM output
  wiringpi.pinMode(PIN, wiringpi.GPIO.PWM_OUTPUT)

  # 3. Sets the PWM mode to mark:space mode
  wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

  # 4. Sets pulse frequency to 50Hz for servo.
  # Raspberry Pi PWM base clock is 19.2MHz.
  # Pulse frequency = base / clock / range
  wiringpi.pwmSetClock(192)
  wiringpi.pwmSetRange(2000)

  while True:
    x = int(raw_input('50-250?'))
    # 5. Sets pulse width.
    wiringpi.pwmWrite(PIN, x)
    # 6. Waits until it moves to position (it takes 0.1s per 60 degree).
    time.sleep(0.5)
    # 7. Turns off servo to save energy and avoid jittering.
    wiringpi.pwmWrite(PIN, 0)


if __name__ == '__main__':
  main()