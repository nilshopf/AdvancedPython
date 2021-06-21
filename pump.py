"""
 * ---------------------------------------------------------------------------------------------------------
 *		Version		:		1.0
 * ---------------------------------------------------------------------------------------------------------
 *
 *		Nutzen		:		Modul zum Arbeiten mit der Pumpe zur Bewässerung
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

# GPIO Pin
pump_pin = 6    # Pin von der Pumpe


# Pumpe initialisieren
def config():
    GPIO.setmode(GPIO.BCM)          # GPIO Pin-Nummern ansprechen
    GPIO.setwarnings(False)

    GPIO.setup(pump_pin, GPIO.OUT)  # Pumpe als Ausgang festlegen
    switch_off()                    # initaialzustand == Deaktiv


def switch_on():
    GPIO.output(pump_pin, GPIO.HIGH)


def switch_off():
    GPIO.output(pump_pin, GPIO.LOW)
