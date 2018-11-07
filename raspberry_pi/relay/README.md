# What

Use relay switch to control high voltage switch, such as garage door opener,
irrigation valve (usually 24V), etc.

# How

## Parts

* [SunFounder 5V relay module](https://www.google.com/search?q=SunFounder+5v+relay+module)
    
    This relay module can control AC250V 10A, DC30V 10A.

* 4x jumpwire

## Wiring

1. VCC => 5V (such as pin #2)
2. GND => Ground (such as pin #6)
3. INT1 => GPIO port (such as pin #8)

## Code

1. Initialization.

    ```python
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    ```

1. Turns on.

    ```python
    GPIO.output(pin, GPIO.HIGH)
    ```

1. Turns off.
    ```python
    GPIO.output(pin, GPIO.LOW)
    ```

1. Toogles switch.

    ```python
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.3)
    GPIO.output(pin, GPIO.HIGH)
    ```

# Reference

## High vs Low Trigger

* High trigger: triggers (turns switch on) by low (5V) signal.
* Low trigger: triggers (turns switch on) by low (0V) signal.

There's no difference in power consumption.

## BCM vs BOARD GPIO modes

* BOARD: references by physical pin number.
* BCM: references by GPIO channel.