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
import fan


# GPIO Pin
fan_button = 19     # Pin vom Taster, um die Luefter manuell zu aktivieren/deaktivieren
state = 0           # Prueft, ob der Luefter aktiv oder inaktiv ist



# Taster fuer den Luefter initialisieren
def config():
    GPIO.setmode(GPIO.BCM)  #GPIO Pin-Nummern ansprechen
    GPIO.setwarnings(False)

    GPIO.setup(fan_button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    GPIO.add_event_detect(fan_button, GPIO.RISING, callback=fan_Interrupt, bouncetime=200)


# Interrupt Service Routine zum aktivieren der Luefter bei Tastendruck
def fan_Interrupt(Channel):
    global state

    # prueft ob Luefter bereits laufen
    if state == 0:
        #print("Lüfter ON")
        fan.switch_on()
        state = 1
    else:
        #print("Lüfter OFF")
        fan.switch_off()
        state = 0


