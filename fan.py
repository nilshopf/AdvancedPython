"""
 * ---------------------------------------------------------------------------------------------------------
 *		Version		:		1.0
 * ---------------------------------------------------------------------------------------------------------
 *
 *		Nutzen		:		Modul zum Arbeiten mit den beiden Lueftern
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
import RPi.GPIO as GPIO

#GPIO Pin
fan_pin = 12    # Pin der Luefter

# Luefter initialisieren
def config():
    GPIO.setmode(GPIO.BCM)               # GPIO Pin-Nummern ansprechen
    GPIO.setwarnings(False)

    GPIO.setup(fan_pin, GPIO.OUT)        # Luefter als Ausgang festlegen
    GPIO.output(fan_pin, GPIO.LOW)       # Initialzustand == Inaktiv


# Funktion zum anschalten der Luefter
def switch_on():
    GPIO.output(fan_pin, GPIO.HIGH)


# Funktion zum ausschalten der Luefter
def switch_off():
    GPIO.output(fan_pin, GPIO.LOW)
