# What

Uses button to trigger event.

# How

## Bill of Material

* [Push button switch](https://www.google.com/search?q=mini+push+button+switch)
* Jumpwire

## Wiring

* One side => Ground (such as pin #9)
* The other side => GPIO pin (such as pin #12)

## Use in Python

1. Initializes GPIO pin

    ```python
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(PIN, GPIO.FALLING, callback=pressed)
    GPIO.add_event_detect(PIN, GPIO.RISING, callback=released)
    ```

1. Responds to button press

    ```python
    def pressed(channel):
        # do something...

    def release(channel):
        # do something...
    ```
