# What

Show text and graphic on small OLED display.

# How

## Bill of Material

* [SSD1306 OLED display](https://www.google.com/search?q=ssd1306)
* Jumpwire

## Wiring

* VCC => 3.3V (such as pin #1)
* Gnd => Ground (such as pin #9)
* SCL => Serial clock (pin #5)
* SDA => Serial data (pin #3)

## Setup

```shell
sudo apt-get install libjpeg-dev zlib1g-dev -y
pip install luma.core luma.oled --user
```

## Display in Python

1. Downloads font.

    1. Goes to https://fonts.google.com

    1. Selects a font.

    1. Download font.

    1. Unzip to get .ttf file and place in same directory as python code.

1. Creates device instance.

    ```python
    from luma.core.interface import serial
    from luma.oled import device

    ser = serial.i2c(port=1, address=0x3c)
    device = device.ssd1306(ser, width=128, height=64, rotate=0, mode='RGB')
    ```

1. Draws content.

    ```python
    from PIL import Image
    from PIL import ImageDraw
    from PIL import ImageFont

    image = Image.new(device.mode, device.size)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('RobotoMono-Regular.ttf', 11)
    draw.text((2, 2), 'Hello World!', font=font, fill=color)
    draw.rectangle([1, 1, 128 - 2, 64 - 2], fill=fill, outline=outline)
    ```

1. Renders to display.

    ```python
    device.display(image)
    ```

# Resources

* [PIL](https://pillow.readthedocs.io)