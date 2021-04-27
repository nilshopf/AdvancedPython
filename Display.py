import struct
import time
import serial
from binascii import unhexlify
import RPi.GPIO as GPIO

button = 13
display = 18
state = 0;

def config():
   # ser = serial.Serial("/dev/serial0", 9600)  # Open port with baud rate

    GPIO.setmode(GPIO.BCM)  #GPIO Nummern ansprechen
    GPIO.setwarnings(False)

    # Display aktivieren
    GPIO.setup(display, GPIO.OUT)

    # Taster initialisieren
    GPIO.setup(button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    GPIO.add_event_detect(button, GPIO.RISING, callback=display_Interrupt, bouncetime = 200)


def set_data(gas, humidity, pressure, temperature):
    global state

    if state == 1:

        #Bodenfeuchtigkeit
        send_data(txtfeld="t2.txt=", msg= str(gas) + "%")
        #Temperatur
        send_data(txtfeld="t6.txt=", msg=str(humidity))
        # Druck
        send_data(txtfeld="t8.txt=", msg=str(pressure) + "hPa")
        #Luftfeuchtigkeit
        send_data(txtfeld="t4.txt=", msg=str(temperature) + "%")




def send_data(txtfeld, msg):
    ser = serial.Serial("/dev/serial0", 9600)  # Open port with baud rate

    my_string = 'FF'

    #ser.write(str.encode("t2.txt="))
    ser.write(str.encode(txtfeld))
    ser.write(str.encode("\""))
    #ser.write(str.encode("50%"))
    ser.write(str.encode(msg))
    ser.write(str.encode("\""))
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))

def display_Interrupt(Channel):

    global state

    print("Hallo")
    if state == 0:
        GPIO.output(display, GPIO.HIGH)
        state = 1
    else:
        GPIO.output(display, GPIO.LOW)
        state = 0