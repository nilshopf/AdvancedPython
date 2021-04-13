from picamera import PiCamera
from time import sleep
from datetime import datetime
from pathlib import Path
import os

def config():
    camera = PiCamera()
    return camera

def preview(camera):
    camera.start_preview()
    sleep(5)
    camera.stop_preview()

def picture(camera):
    a = datetime.now()
    time = str(a.hour)+":"+str(a.minute)+":"+str(a.second)
    date = str(a.year)+"-"+str(a.month)+"-"+str(a.day)

    if os.path.exists('/home/pi/Desktop/AdvancedPython/%s' % date):
        camera.start_preview()
        sleep(5)
        camera.capture('/home/pi/Desktop/AdvancedPython/%s/%s.jpg' % (date, time))
        camera.stop_preview()
    else:
        path = Path("/home/pi/Desktop/AdvancedPython/%s" % date)
        path.mkdir(parents=True, exist_ok=True)
        camera.start_preview()
        sleep(5)
        camera.capture('/home/pi/Desktop/AdvancedPython/%s/%s.jpg' % (date, time))
        camera.stop_preview()