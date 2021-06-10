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
pin = 12

def config():
    gp.setwarnings(False)
    gp.setmode(gp.BCM)
    gp.setup(pin, gp.OUT)
    gp.output(pin, gp.LOW)


# Funktion zum anschalten der Luefter
def switch_on():
    gp.output(pin, gp.HIGH)


# Funktion zum ausschalten der Luefter
def switch_off():
    gp.output(pin, gp.LOW)
