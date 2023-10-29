# For Pi
import io
import socket
import struct
import time
import picamera
import py_rtmp_stream

# Create a socket connection between the Raspberry Pi and the Zoom RTMP server
stream = py_rtmp_stream.RTMPStream(
    url='rtmp://zoom.server.com/appname/streamname',
    width=640,
    height=480,
    fps=30,
    bitrate=500
)

try:
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        # Start a stream to the RTMP server
        camera.start_recording(stream, format='h264')
        while True:
            camera.wait_recording(1)
finally:
    camera.stop_recording()
    stream.close()
