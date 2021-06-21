"""
 * ---------------------------------------------------------------------------------------------------------
 *		Version		:		1.0
 * ---------------------------------------------------------------------------------------------------------
 *
 *		Nutzen		:		Modul zum Arbeiten mit GPIO Pins und Interrupts
 *
 *		Modul		:		Advanced Python
 *
 *		Autor		:		Merit Tienken
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
import RPi.GPIO as GPIO
import camera


# GPIO Pin
camera_button = 19     # Pin vom Taster, um manuell Fotos aufzunehmen


# Taster fuer den manuelle Fotoaufnahme initialisieren
def config():
    GPIO.setmode(GPIO.BCM)  #GPIO Pin-Nummern ansprechen
    GPIO.setwarnings(False)

    GPIO.setup(camera_button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    GPIO.add_event_detect(camera_button, GPIO.RISING, callback=camera_Interrupt, bouncetime=200)


# Interrupt Service Routine zum ausloesen der Kamera
def camera_Interrupt(Channel):

    # Foto vom Gewaechshaus aufnehmen
    #camera.picture(camera)

    # print("Foto Aufgenommen!!")
