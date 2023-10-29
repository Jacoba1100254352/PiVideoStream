# For Pi
import io
import socket
import struct
import time
import picamera

# Create a socket connection between the Raspberry Pi and the computer
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('10.37.68.171', 8000))
connection = client_socket.makefile('wb')

try:
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        # Start a stream to the socket
        camera.start_recording(connection, format='h264')
        while True:
            camera.wait_recording(1)
finally:
    camera.stop_recording()
    connection.close()
    client_socket.close()
