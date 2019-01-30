import time

from RPi import GPIO


class PushSwitch(object):
  """Class for any switch that can be pressed."""

  _IGNORE_THRESHOLD = 0.25  # seconds

  def __init__(self, switch_pin, switch_callback):
    self._last_press = time.time()
    self._switch_callback = switch_callback
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(switch_pin, GPIO.FALLING, callback=self._on_pressed)

  def _on_pressed(self, channel):
    interval = time.time() - self._last_press
    if interval > self._IGNORE_THRESHOLD:
      self._switch_callback()
    self._last_press = time.time()


class RotaryEncoder(PushSwitch):
  """Class for pushable single rotary encoder."""

  def __init__(self, clk_pin, dt_pin, switch_pin, rotation_callback,
               switch_callback):
    super(RotaryEncoder, self).__init__(
        switch_pin=switch_pin, switch_callback=switch_callback)
    self._rotation_callback = rotation_callback
    self._counter = 0
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(clk_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(dt_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    self._clk_last_state = GPIO.input(clk_pin)
    self._dt_last_state = GPIO.input(dt_pin)
    GPIO.add_event_detect(clk_pin, GPIO.BOTH, callback=self._clk_callback)
    GPIO.add_event_detect(dt_pin, GPIO.BOTH, callback=self._dt_callback)

  def reset(self):
    self._counter = 0

  def _clk_callback(self, channel):
    state = GPIO.input(channel)
    if self._clk_last_state == state:
      return

    if state == 0 and self._dt_last_state == 1:
      self._counter -= 1
      self._rotation_callback(self._counter)
    self._clk_last_state = state

  def _dt_callback(self, channel):
    state = GPIO.input(channel)
    if self._dt_last_state == state:
      return

    if state == 0 and self._clk_last_state == 1:
      self._counter += 1
      self._rotation_callback(self._counter)
    self._dt_last_state = state


def _on_rotation(value):
  print('value={0}'.format(value))


def _on_pressed():
  print('pressed')


def main():
  RotaryEncoder(
      clk_pin=13,
      dt_pin=19,
      switch_pin=26,
      rotation_callback=_on_rotation,
      switch_callback=_on_pressed)
  while True:
    time.sleep(1)


if __name__ == '__main__':
  main()