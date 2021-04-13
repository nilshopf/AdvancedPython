import RPi.GPIO as GPIO

#LED's initialisieren
def LED_init():
    GPIO.setmode(GPIO.BCM)  #GPIO Nummern ansprechen
    GPIO.setup(21, GPIO.OUT)


def LED_ON():
    GPIO.output(21, GPIO.HIGH)

def LED_OFF():
    GPIO.output(21, GPIO.LOW)