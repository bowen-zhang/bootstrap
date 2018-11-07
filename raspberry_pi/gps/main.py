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

import logging
import pynmea2
import serial

MODE = ['', 'no fix', '2D fix', '3D fix']


def parse_message(msg):
  if type(msg) == pynmea2.types.talker.GLL:
    # Loran emulation
    pass
  elif type(msg) == pynmea2.types.talker.RMC:
    # Recommended minimum specific GPS/TRANSIT data
    print '{0}: lat={1:.3f}, lon={2:.3f}, direction={3}, speed={4}kts'.format(
        msg.datetime,
        msg.latitude,  # degree
        msg.longitude,  # degree
        msg.true_course,  # degree (True)
        msg.spd_over_grnd,  # knots
    )
  if type(msg) == pynmea2.types.talker.VTG:
    # Vector track and speed over ground
    pass
  elif type(msg) == pynmea2.types.talker.GGA:
    # fix data
    print 'alt={0}m'.format(msg.altitude)
  elif type(msg) == pynmea2.types.talker.GSA:
    # Satellite data
    print 'mode={0}'.format(MODE[int(msg.mode_fix_type)])
  elif type(msg) == pynmea2.types.talker.GSV:
    # Satellites in view
    pass


def main():
  ser = serial.Serial('/dev/ttyS0', 9600)
  reader = pynmea2.NMEAStreamReader()

  while True:
    data = ser.read(16).replace('\r', '')
    try:
      msgs = reader.next(data)
      for msg in msgs:
        parse_message(msg)
    except Exception as e:
      logging.warn(str(e))

  ser.close()


if __name__ == '__main__':
  main()
