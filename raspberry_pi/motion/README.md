# What

Uses PIR motion sensor to detect movement.

# How

## Bill of Material

* [PIR motion sensor]

## Wiring

* VCC => 5V (such as pin #2)
* GND => Ground (such as pin #9)
* OUT => GPIO pin (such as pin #11)

## Usage

```python
def triggered(pin):
    has_motion = GPIO.input(pin)
    # ...

_PIN = [GPIO pin number]
GPIO.setmode(GPIO.BCM)
GPIO.setup(_PIN, GPIO.IN)
GPIO.add_event_detect(_PIN, GPIO.BOTH, callback=triggered)
```

# Resources

* [How PIRs work](https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor/how-pirs-work)