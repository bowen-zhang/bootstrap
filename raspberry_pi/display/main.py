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

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from luma.core.interface import serial
from luma.oled import device

ADDRESS = 0x3C
WIDTH = 128
HEIGHT = 64


def main():
  ser = serial.i2c(port=1, address=ADDRESS)
  dev = device.ssd1306(ser, width=WIDTH, height=HEIGHT, rotate=0, mode='RGB')
  image = Image.new(dev.mode, dev.size)
  draw = ImageDraw.Draw(image)

  font = ImageFont.truetype('RobotoMono-Regular.ttf', 11)
  draw.rectangle([1, 1, WIDTH - 2, HEIGHT - 2], fill='black', outline='white')
  draw.text((2, 2), 'Hello World!', font=font, fill='white')

  dev.display(image)

  time.sleep(5)


if __name__ == '__main__':
  main()