# What

Get location information via GPS module.

# How

## Bill of Material

* [NEO 6M GPS](https://www.google.com/search?q=neo-6m+gps&oq=neo-6m+gps&aqs=chrome..69i57j69i60j69i61l2.4145j0j4&sourceid=chrome&ie=UTF-8)
* Jumpwire

## Wiring

* VCC => 3.3V (such as pin #1)
* TX => RX (pin #10)
* RX => TX (pin #8)
* GND => Ground (such as pin #6)

## Setup

1. Turns off serial console

    Open /boot/cmdline.txt, delete "console=...".

1. Reboot

    ```shell
    sudo reboot
    ```

## Test

Places GPS module outside or near window to have sky in view.

```shell
stty -F /dev/ttyS0 9600
cat /dev/ttyS0
```
Messages should be printed continuously.

```shell
sudo apt-get install gpsd gpsd-clients
gpsd -S 4000 /dev/ttyS0
cgps :4000
```
Location data should be received and refreshed. 

## Get location in Python

1. Installs dependencies

    ```shell
    pip install pynmea2 pyserial --user
    ```

1. Reads message from serial device

    ```python
    ser = serial.Serial('/dev/ttyS0', 9600)
    reader = pynmea2.NMEAStreamReader()
    while True:
      data = ser.read(16).replace('\r', '')
      msgs = reader.next(data)
      for msg in msgs:
        # ...
    ```

1. Parses location data

    ```python
    if type(msg) == pynmea2.types.talker.RMC:
      msg.datetime        # UTC
      msg.latitude        # degree
      msg.longitude       # degree
      msg.true_course     # degree
      msg.spd_over_grnd   # knots
    elif type(msg) == pynmea2.types.talker.GGA:
      msg.altitude        # meter
    ```

# Resources

* [NMEA data](https://www.gpsinformation.org/dale/nmea.htm)