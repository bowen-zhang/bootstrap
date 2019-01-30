# What

Reads input from a rotary encoder.

![encoder](https://user-images.githubusercontent.com/9627471/51965900-c5a4aa80-241f-11e9-99db-542920f55506.jpg)

# How

## Parts

* [Rotary encoder](https://www.google.com/search?q=keyes+rotary+encoder)
* 5x M-F jumpwire


## Wiring

|Rotary encoder|Raspberry Pi|
|---|---|
|CLK|Pin #33: GPIO13|
|DT|Pin #35: GPIO19|
|SW|Pin #37: GPIO26|
|+|Pin #1: 3.3V|
|GND|Pin #6: Ground|

## Code

1. Detects press of rotary encoder knob:

   ```
   def _on_pressed(_):
     print('pressed')

   switch_pin = 26
   GPIO.setmode(GPIO.BCM)
   GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
   GPIO.add_event_detect(switch_pin, GPIO.FALLING, callback=_on_pressed)
   ```
   
   It may be necessary to filter repeated presses that occurred within short period (0.25 sec).

1. Detects CLK and DT signal:

   ```
   clk_pin = 13
   dt_pin = 19
   GPIO.setmode(GPIO.BCM)
   GPIO.setup(clk_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
   GPIO.setup(dt_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
   _clk_last_state = GPIO.input(clk_pin)
   _dt_last_state = GPIO.input(dt_pin)
   GPIO.add_event_detect(clk_pin, GPIO.BOTH, callback=_clk_callback)
   GPIO.add_event_detect(dt_pin, GPIO.BOTH, callback=_dt_callback)
   ```
   
1. Concludes rotation direction based on CLK/DT state and trigger order:

   ```
   def _clk_callback(channel):
     state = GPIO.input(channel)
     if _clk_last_state == state:
       return

     if state == 0 and _dt_last_state == 1:
       print('rotated counterclockwise.')
     _clk_last_state = state

   def _dt_callback(self, channel):
     state = GPIO.input(channel)
     if _dt_last_state == state:
       return

     if state == 0 and _clk_last_state == 1:
       print('rotated clockwise.')
     _dt_last_state = state   ```

# Reference

* [How does rotary encoder work](https://www.youtube.com/watch?v=v4BbSzJ-hz4)