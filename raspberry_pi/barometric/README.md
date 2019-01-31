# What

Measures ambient temperature and barometric pressure.

# How

## Bill of Material

* [BMP180 barometric sensor breakout](https://www.google.com/search?q=bmp180)
* Jumpwire

## Wiring

|BMP180 Sensor|Raspberry Pi|
|---|---|
|VCC|Pin #1 or #2: 3.3V or 5V|
|GND|Pin #6: Ground|
|SCL|Pin #5: GPIO 3/SCL|
|SDA|Pin #3: GPIO 2/SDA|

## Install dependencies

```shell
sudo apt-get install python-smbus
```

## Usage

```python
import barometric
sensor = barometric.BarometricSensor()
sensor.read()
sensor.temperature # in Celsuis
sensor.pressure # in Pa
```

See barometric.py for details.

# Resources

* [I2C](http://i2c.info/)