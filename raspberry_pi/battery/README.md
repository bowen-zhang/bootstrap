# What

Powers Raspberry Pi with a battery/UPS.

![powerboost](https://user-images.githubusercontent.com/9627471/52037302-7aec6680-24e3-11e9-8b55-5a6b767ccad9.jpg)
![battery](https://user-images.githubusercontent.com/9627471/52037305-7c1d9380-24e3-11e9-82d5-155aedcf06ac.jpg)

# How

## Parts

* [PowerBoost 1000 Charger](https://www.adafruit.com/product/2465)
* [LiPo 3.7V Battery](https://www.google.com/search?q=lipo+3.7v+battery)
* [SPDT switch](https://www.google.com/search?q=1p2t+spdt+switch)
* Male USB to Male Micro-USB Cable
* jumpwires


## Wiring

|PowerBoost 1000 Charger|Raspberry Pi|Switch|
|---|---|---|
|USB|||
|BAT|||
|VS||Left pin|
|EN||Middle pin|
|GND||Right pin|
|LBO|Pin #40: GPIO21||
|GND|Pin #6: GND||
|5V|Pin #4: 5V||

## Code

1. To detects low battery level:

   ```
   from RPi import GPIO
   LBO_PIN = 21
   GPIO.setmode(GPIO.BCM)
   GPIO.setup(LBO_PIN, GPIO.IN)
   low_battery = (GPIO.input(LBO_PIN) == 0)
   ```

# Reference

* [LiPo vs Li-Ion battery](http://blog.ravpower.com/2017/06/lithium-ion-vs-lithium-polymer-batteries/)
* [Switch basics](https://learn.sparkfun.com/tutorials/switch-basics/all)
