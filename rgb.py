"""
 * ---------------------------------------------------------------------------------------------------------
 *		Version		:		1.0
 * ---------------------------------------------------------------------------------------------------------
 *
 *		Nutzen		:		Modul zum Arbeiten mit der RGB LED
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
from gpiozero import RGBLED

# Festlegen der Pins fuer die RGB
led = RGBLED(red=17, green=27, blue=22)
# Red = Mosi; Green = Miso; Blue SCLK

# Funktion um die Farbe der RGB auf rot zu stellen
def red():
    led.color = (0, 1, 1)

# Funktion um die Farbe der RGB auf gruen zu stellen
def green():
    led.color = (1, 0, 1)
