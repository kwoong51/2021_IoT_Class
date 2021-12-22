import picamera
import time

path = '/home/pi/src5/06_multimedia'

camera = picamera.PiCamera()

try:
    camera.resolution = (640, 480)
    camera.start_preview()
    while(True):
        print('photo : 1, video : 2, exit : 9')
        a = input()
        if (a == '1'):
            now_str = time.strftime("%Y%m%d_%H%M%S")
            camera.capture('%s/photo%s.jpg' % (path, now_str))
        elif (a == '2'):
            now_str = time.strftime("%Y%m%d_%H%M%S")
            camera.start_recording('%s/video%s.h264' % (path, now_str))
            input('press enter to stop')
            camera.stop_recording
        elif (a == '9'):
            break
finally:
    camera.stop_preview()