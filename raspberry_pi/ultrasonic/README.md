# What

Uses ultrasound sensor to detect distance to object in front.

![ultrasound](https://user-images.githubusercontent.com/9627471/52034632-b1bf7e00-24dd-11e9-8405-1ca07185089a.jpg)

# How

## Parts

* [HC-SR04 ultrasound sensor](https://www.google.com/search?q=hc-sr04)
* 1x 1KΩ resistor
* 1x 2KΩ resistor
* jumpwires


## Wiring

|Ultrasound Sensor|Raspberry Pi|
|---|---|
|VCC|Pin #2: 5V|
|TRIG|Pin #38: GPIO20|
|ECHO|<pre>             /=> 2KΩ resistor => Pin #39: Ground<br>=> 1KΩ resistor<br>             \\=> Pin 40: GPIO21</pre>|
|GND|Pin #6: Ground|

## Code

1. Initializes GPIO pins.

   ```
   GPIO.setmode(GPIO.BCM)
   GPIO.setup(TRIG, GPIO.OUT)
   GPIO.setup(ECHO, GPIO.IN)
   ```

1. Ensures TRIG pin starts with low level.
   ```
   GPIO.output(TRIG, False)
   time.sleep(2)
   ```

1. Triggers pulse signal.

   Pulse signal duration needs to be at least 10μs.

   ```
   GPIO.output(TRIG, True)
   time.sleep(0.00001)
   GPIO.output(TRIG, False)
   
1. Waits for ECHO level to raise, measure high level duration.

   ```
   pulse_start = time.time()
   while GPIO.input(ECHO) == 0:
     pulse_start = time.time()
   pulse_end = time.time()
   while GPIO.input(ECHO) == 1:
     pulse_end = time.time()
   pulse_duration = pulse_end - pulse_start
   ```
   
1. Calculates distance to object in front.
   
   ```
   SOUND_SPEED = 343 # m/second
   distance = pulse_duration / 2.0 * SOUND_SPEED
   ```
   
1. Cleans up GPIO.

   ```
   GPIO.cleanup()
   ```

# Reference

* [Datasheet](https://www.mouser.com/ds/2/813/HCSR04-1022824.pdf)
