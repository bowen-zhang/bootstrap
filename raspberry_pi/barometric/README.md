# What

Measures ambient temperature and barometric pressure.

# How

## Bill of Material

* [BMP180 barometric sensor breakout](https://www.google.com/search?q=bmp180)
* Jumpwire

## Wiring

* VCC => 5V (such as pin #2)
* GND => Ground (such as pin #6)
* SCL => Serial Clock (pin #5)
* SDA => Serial Data (pin #3)

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