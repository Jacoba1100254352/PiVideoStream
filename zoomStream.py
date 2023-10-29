# For Pi
import av
import picamera

container = av.open("rtmp://10.37.68.171/live/test")

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    stream = container.add_stream('vp9', rate=30)
    stream.width = camera.resolution[0]
    stream.height = camera.resolution[1]

    camera.start_recording(stream, format='vp9')
    while True:
        camera.wait_recording(1)

camera.stop_recording()
container.close()
