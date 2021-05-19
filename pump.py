import RPi.GPIO as GPIO

# GPIO Pin
pumpe = 6


# Pumpe initialisieren
def config():
    GPIO.setmode(GPIO.BCM)  # GPIO Nummern ansprechen
    GPIO.setwarnings(False)

    # Pumpe initialisieren
    GPIO.setup(pumpe, GPIO.OUT)
    switch_off()


def switch_on():
    GPIO.output(pumpe, GPIO.HIGH)


def switch_off():
    GPIO.output(pumpe, GPIO.LOW)
