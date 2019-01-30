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
  sector = int(raw_input('Sector:'))
  block = int(raw_input('Block:'))
  data = raw_input('Data:') + '\0' * 16
  data = [ord(x) for x in data][:16]

  # 1. Creates RFID instance.
  rfid = pirc522.RFID()
  last_uid = None
  # 2. Detects tag.
  rfid.wait_for_tag()
  # 3. Requests current tag.
  error, tag_type = rfid.request()
  if error:
    last_uid = None
    return
  # 4. Gets tag id.
  error, uid = rfid.anticoll()
  if error:
    last_uid = None
    return
  # Skips if it is the same tag.
  if last_uid == uid:
    return

  last_uid = uid
  print("UID: " + str(uid))

  # 5. elects current tag by id. (returns False if succeed)
  if rfid.select_tag(uid):
    print("Unable to select tag.")
    return

  # 6. Writes data to tag.
  if rfid.card_auth(rfid.auth_a, sector * 4, DEFAULT_KEY, uid):
    print('Unable to authenticate for sector %s.' % sector)
    return
  if rfid.write(sector * 4 + block, data):
    print('Unable to write to sector %s block %s' % (sector, block))
    return

  print('Write completed.')

  # 7. Stops crypto1 when done working.
  rfid.stop_crypto()

  # 8. Cleanup GPIO.
  rfid.cleanup()


if __name__ == '__main__':
  main()