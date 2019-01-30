# What

Use RFID scanner to read and write card / key fob for identification.
![rfid](https://user-images.githubusercontent.com/9627471/51960221-ef080b00-240c-11e9-9181-99f2a2d483cd.jpg)

# How

## Parts

* [MIFARE RC522 RFID Card Sensor Kit](https://www.google.com/search?q=RC522)

* 8x jumpwire

## Wiring

|RC522 Sensor|Raspberry Pi|
|---|---|
|SDA|Pin #24: GPIO8/CE0|
|SCK|Pin #23: GPIO11/SCKL|
|MOSI|Pin #19: GPIO10/MOSI|
|MISO|Pin #21: GPIO9/MISO|
|IRQ|Pin #18: GPIO24|
|GND|Pin #6: Ground|
|RST|Pin #22: GPIO25|
|3.3V|Pin #1: 3V3|


## Code

1. Install dependent libraries:

   ```
   pip install spidev pirc522 --user
   ```

1. Creates RFID instance:

   ```
   import pirc522
   rfid = pirc522.RFID()
   ```

1. Waits for detection of card / key fob:

   ```
   rfid.wait_for_tag()
   ```

1. Prepares to access the card / key fob:

   ```
   error, tag_type = rfid.request()
   if error:
     return
   error, uid = rfid.anticoll()
   if error:
     return
   error = not rfid.select_tag(uid)
   if error:
     return
   ```

1. Reads data stored on the card / key fob:

   ```
   address = sector * 4 + block
   default_key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
   error = not rfid.card_auth(rfid.auth_a, address, default_key, uid)
   if error:
     return
   error, data = rfid.read(address)
   ```

   `data` will be a 16-byte array.

1. Writes data to the card / key fob:

   ```
   data = [1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6]
   error = not rfid.write(address, data)
   if error:
     return
   ```

1. Cleasn up after access is done:

   ```
   rfid.stop_crypto()
   rfid.cleanup()
   ```

# Reference

* [Serial Peripheral Interface (SPI)](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi/all)
* [Datasheet](https://www.nxp.com/docs/en/data-sheet/MF1S50YYX_V1.pdf)
