"""
 * ---------------------------------------------------------------------------------------------------------
 *		Version		:		1.0
 * ---------------------------------------------------------------------------------------------------------
 *
 *		Nutzen		:		Modul zum Arbeiten mit der Kamera des Raspberry Pis und zum abspeichern der Bilder
 *
 *		Modul		:		Advanced Python
 *
 *		Autor		:		Nils Hopf
 *
 *		Sprache		:		Python
 *
 *
 *
 *	Date			Time	Name		Log		Modification
 *----------------------------------------------------------------------------------------------------------
 *
 *
 """
from picamera import PiCamera
from time import sleep
from datetime import datetime
from pathlib import Path
import os
import shutil

camera = 0

# Funktion zum einrichten der Kamera
def config():
    global camera
    camera = PiCamera()
    

# Funktion zum Aufnehmen und Abspeichern eines Bildes
def picture():

    global camera
    # Ermitteln des aktuellen Datums und der Uhrzeit
    a = datetime.now()
    time = str(a.hour)+":"+str(a.minute)+":"+str(a.second)
    date = str(a.year)+"-"+str(a.month)+"-"+str(a.day)

    # Pruefen ob Ordner mit aktuellem Datum bereits erstellt wurde
    if os.path.exists('/home/pi/Desktop/AdvancedPython/%s' % date):

        # Aufnehmen des Bildes
        camera.start_preview()
        sleep(5)
        camera.capture('/home/pi/Desktop/AdvancedPython/%s/%s.jpg' % (date, time))

        #Bilder verschieben fuer Flask
        src = '/home/pi/Desktop/AdvancedPython/%s/%s.jpg' % (date, time)
        shutil.copy(src, '/home/pi/Desktop/AdvancedPython/static')

        #Bilder umbenennen fuer Flask
        dst = '/home/pi/Desktop/AdvancedPython/static/%s.jpg' % (time)
        newname = '/home/pi/Desktop/AdvancedPython/static/latest.jpg'
        os.rename(dst, newname)
        camera.stop_preview()
    else:
        # Erstellen des neuen Ordners
        path = Path("/home/pi/Desktop/AdvancedPython/%s" % date)
        path.mkdir(parents=True, exist_ok=True)

        #Aufnehmen des Bildes
        camera.start_preview()
        sleep(5)
        camera.capture('/home/pi/Desktop/AdvancedPython/%s/%s.jpg' % (date, time))

        # Bilder verschieben fuer Flask
        src = '/home/pi/Desktop/AdvancedPython/%s/%s.jpg' % (date, time)
        shutil.copy(src, '/home/pi/Desktop/AdvancedPython/static')

        # Bilder umbenennen fuer Flask
        dst = '/home/pi/Desktop/AdvancedPython/static/%s.jpg' % (time)
        newname = '/home/pi/Desktop/AdvancedPython/static/latest.jpg'
        os.rename(dst, newname)
        camera.stop_preview()
