import picamera


def capture_image():
  camera = picamera.PiCamera()
  camera.hflip = hflip
  camera.vflip = vflip
  camera.rotation = 0  # 0,90,180,270
  camera.start_preview()
  camera.capture('image.jpg')


if __name__ == '__main__':
  capture_image()