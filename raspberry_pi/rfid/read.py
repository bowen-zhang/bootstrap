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

import pirc522
import sys

DEFAULT_KEY = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]


def main():
  # 1. Creates RFID instance.
  rfid = pirc522.RFID()
  last_uid = None
  while True:
    # 2. Detects tag.
    rfid.wait_for_tag()
    # 3. Requests current tag.
    error, tag_type = rfid.request()
    if error:
      last_uid = None
      continue
    # 4. Gets tag id.
    error, uid = rfid.anticoll()
    if error:
      last_uid = None
      continue
    # Skips if it is the same tag.
    if last_uid == uid:
      continue

    last_uid = uid
    print("UID: " + str(uid))

    # 5. elects current tag by id. (returns False if succeed)
    if rfid.select_tag(uid):
      print("Unable to select tag.")
      continue

    dump_data(rfid, uid)

    # 6. Stops crypto1 when done working.
    rfid.stop_crypto()

  # 7. Cleanup GPIO.
  rfid.cleanup()


def dump_data(rfid, uid):
  """Dumps all the data stored in specified tag.

  Args:
    rfid: pirc522.RFID instance.
    uid: id of the tag.
  """
  for sector in range(0, 16):
    if rfid.card_auth(rfid.auth_a, sector * 4, DEFAULT_KEY, uid):
      print('Unable to authenticate for sector %s.' % sector)
      return

    for block in range(0, 4):
      error, data = rfid.read(sector * 4 + block)
      if error:
        print('Unable to read sector %s block %s' % (sector, block))
        continue

      if block == 3:
        msg = ''  # sector trailer
      else:
        msg = ''.join([chr(x) for x in data]).strip('\0')
        print('S{0}B{1}: [{2}] - {3}'.format(sector, block, ' '.join(
            ['{:02X}'.format(x) for x in data]), msg))


if __name__ == '__main__':
  main()