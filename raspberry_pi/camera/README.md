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

# Resources

* [Picamera](https://picamera.readthedocs.io/)