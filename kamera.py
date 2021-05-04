from picamera import PiCamera
from time import sleep
from datetime import datetime
from pathlib import Path
import os
import shutil

def config():

    return camera

def preview(camera):
    camera.start_preview()
    sleep(5)
    camera.stop_preview()

def picture():
    camera = PiCamera()
    a = datetime.now()
    time = str(a.hour)+":"+str(a.minute)+":"+str(a.second)
    date = str(a.year)+"-"+str(a.month)+"-"+str(a.day)

    if os.path.exists('/home/pi/Desktop/AdvancedPython/%s' % date):
        camera.start_preview()
        sleep(5)
        #Bild in Ordner speichern
        camera.capture('/home/pi/Desktop/AdvancedPython/%s/%s.jpg' % (date, time))

        #Bilder verschieben für Flask
        src = '/home/pi/Desktop/AdvancedPython/%s/%s.jpg' % (date, time)
        shutil.copy(src, '/home/pi/Desktop/AdvancedPython/static')

        #Bilder umbenennen für Flask
        dst = '/home/pi/Desktop/AdvancedPython/static/%s.jpg' % (time)
        newname = '/home/pi/Desktop/AdvancedPython/static/latest.jpg'
        os.rename(dst, newname)
        camera.stop_preview()
    else:
        path = Path("/home/pi/Desktop/AdvancedPython/%s" % date)
        path.mkdir(parents=True, exist_ok=True)
        camera.start_preview()
        sleep(5)
        camera.capture('/home/pi/Desktop/AdvancedPython/%s/%s.jpg' % (date, time))
        src = '/home/pi/Desktop/AdvancedPython/%s/%s.jpg' % (date, time)
        shutil.copy(src, '/home/pi/Desktop/AdvancedPython/static')
        dst = '/home/pi/Desktop/AdvancedPython/static/%s.jpg' % (time)
        newname = '/home/pi/Desktop/AdvancedPython/static/latest.jpg'
        os.rename(dst, newname)
        camera.stop_preview()

    return date, time