# What

Drives a servo to move to specific position.
![servo](https://user-images.githubusercontent.com/9627471/51963623-0fd65d80-2419-11e9-931e-8dc8299bb7f3.jpg)

# How

## Parts

* [SG92R Servo](https://www.google.com/search?q=SG92R)
* 3x M-F jumpwire


## Wiring

|SG92R Servo|Raspberry Pi|
|---|---|
|Yellow wire|Pin #12: GPIO18|
|Red wire|Pin #4: 5V|
|Black/brown wire|Pin #6: Ground|

## Code

1. Install dependent libraries:

   ```
   pip install wiringpi --user
   ```

1. Initialize wiringpi:

   ```
   wiringpi.wiringPiSetupGpio()
   ```
   
1. Sets GPIO pin as PWM output:

   ```
   wiringpi.pinMode(PIN, wiringpi.GPIO.PWM_OUTPUT)
   ```
   
1. Sets PWM mode to mark:space mode:

   ```
   wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
   ```

1. Sets pulse frequency to 50Hz for servo.

   Pulse frequency = base frequency / clock / range
   Raspberry Pi PWM base frequency is 19.2MHz. To get 50Hz pulse frequency, we choose
   clock=192 and range=2000.
  
   ```
   wiringpi.pwmSetClock(192)
   wiringpi.pwmSetRange(2000)
   ```

1. Sets pulse width (0.5ms - 2.5ms, or a value within 50-250).

   ```
   PIN = 18
   wiringpi.pwmWrite(PIN, value)
   ```
   
1. Gives enough time for servo to complete rotation, then turns off servo.

   A powered on servo consumes power and may jitter for a while as it tries to reach precise position but can't due to various error. Turning it off stops the jitter and noise.
   
    ```
    wiringpi.pwmWrite(PIN, 0)
    ```

# Reference

* [Wiringpi](http://wiringpi.com/)
* [DC Motor vs Servo vs Step Motor](https://www.modmypi.com/blog/whats-the-difference-between-dc-servo-stepper-motors)
* [Datasheet](http://www.wecl.com.hk/distribution/PDF/Robotics_IoT/58-01-9024.pdf)
