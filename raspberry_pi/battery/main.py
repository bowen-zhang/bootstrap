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

from RPi import GPIO

LBO_PIN = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(LBO_PIN, GPIO.IN)
low_battery = (GPIO.input(LBO_PIN) == 0)
print('Battery level: {0}'.format('low' if low_battery else 'normal'))
