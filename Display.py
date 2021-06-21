"""
 * ---------------------------------------------------------------------------------------------------------
 *		Version		:		1.0
 * ---------------------------------------------------------------------------------------------------------
 *
 *		Nutzen		:		Modul zum Arbeiten mit dem Nextion Display (NX3224T024)
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

import time
import serial
from binascii import unhexlify
import RPi.GPIO as GPIO

button = 25     # Pin vom Taster
state = 0       # Prueft, ob das Display aktiv oder inaktiv ist


def config():
    GPIO.setmode(GPIO.BCM)  # GPIO Pin-Nummern ansprechen
    GPIO.setwarnings(False)

    # Schalter fuer das Display initialisieren
    GPIO.setup(button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    GPIO.add_event_detect(button, GPIO.BOTH, callback=display_Interrupt, bouncetime = 200)


# Sensordaten fuer das Display vorbereiten und uebermitteln
def set_data(soil_moisture, humidity, pressure, temperature):
    global state

    # wenn das Display aktiv ist, werden die Sensor Daten 10sek aktiv gesendet
    if state == 1:
        time_reference = time.localtime()   # aktuelle Uhrzeit
        time_reference = ((int(time_reference.tm_sec)) + 10) % 60   # aktuelle Sekunden + 10s

        while time.localtime()[5] != time_reference:        # localtime()[5] == aktuelle sekunde
            # Sensordaten an das Display senden (gewuenschtes Textfeld auf dem Display + Uebermittelter text)
            # Bodenfeuchtigkeit
            send_data(txt_field="t2.txt=", msg= str(soil_moisture) + "%")
            # Luftfeuchtigkeit
            send_data(txt_field="t4.txt=", msg=str(humidity) + "%")
            # Druck
            send_data(txt_field="t8.txt=", msg=str(pressure) + "hPa")
            # Temperatur
            send_data(txt_field="t6.txt=", msg=str(temperature))


# Sensordaten an das Display senden
def send_data(txt_field, msg):

    ser = serial.Serial("/dev/serial0", 9600)  # UART Port mit Baudrate von 9600 erstellen
    my_string = 'FF'

    ser.write(str.encode(txt_field))
    ser.write(str.encode("\""))
    ser.write(str.encode(msg))
    ser.write(str.encode("\""))
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))

# Display Status setzen (aktiv/inaktiv)
def display_Interrupt(Channel):

    global state

    if state == 0:
        state = 1
    else:
        state = 0
    # print("INTERRUPT Display!")