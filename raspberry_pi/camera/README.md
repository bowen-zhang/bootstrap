# What

Capture image from camera on Raspberry Pi.

# How

## Test Camera

```shell
raspistill -o ~/image.jpg
```

## Capture Image in Python

```python
import picamera
camera = picamera.PiCamera()
camera.start_preview()
camera.capture('image.jpg')
```

## Capture Video in Python

```python
camera.start_recording(
    'video.h264', format='h264', resize=(640, 480), bitrate=1000000)
time.sleep(10)
camera.stop_recording()
```

# Resources

* [Picamera API](https://picamera.readthedocs.io/)
* [Raspberry Pi Cameras](https://www.waveshare.com/product/modules/cameras/raspberry-pi-camera.htm)