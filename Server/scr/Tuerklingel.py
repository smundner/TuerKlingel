#!/usr/bin/python3

from picamera import PiCamera
from time import sleep
from gpiozero import Button
from signal import pause
import socket


def init():
    global camera 
    camera = PiCamera()
    camera.resolution = (1024,768)
    camera.hflip = True
    camera.vflip = True
    camera.start_preview()
    sleep(2)

def takePic():
    global camera
    camera.capture('/var/www/html/foo.jpg')
    bs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bs.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    bs.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
    bs.sendto('Klingel1'.encode(),('<broadcast>',6000))

def main():
    init()
    tuerklingel_oben = Button(3)
    tuerklingel_oben.when_pressed = takePic
    print('Tuerklingel gestartet')
    pause()

if __name__ == '__main__':
    main()
