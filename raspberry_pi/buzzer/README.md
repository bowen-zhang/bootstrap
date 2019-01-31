# What

Makes simple sound using an active buzzer.

![buzzer](https://user-images.githubusercontent.com/9627471/52039830-6e1f4100-24ea-11e9-8fc5-29775062f765.jpg)


# How

## Parts

* [Active buzzer](https://www.sunfounder.com/active-buzzer-module.html)
* jumpwires


## Wiring

|Buzzer|Raspberry Pi|
|---|---|
|SIG|Pin #38: GPIO20|
|VCC|Pin #4: 5V|
|GND|Pin #6: Ground|

## Code

1. Initializes GPIO.

   ```
   GPIO.setmode(GPIO.BCM)
   ```
   
1. To start beeping:

   ```
   GPIO.setup(PIN, GPIO.OUT)
   GPIO.output(PIN, GPIO.LOW)
   ```
   
1. To stop beeping:

   ```
   GPIO.setup(PIN, GPIO.IN)
   ```
   
   Note: by simply setting output to GPIO.HIGH, the buzzer will still make a noise sound. To eliminate the noise, change the PIN to input.

# Reference

* [Active vs passive buzzer](https://electronics.stackexchange.com/questions/224374/active-vs-passive-buzzer)
