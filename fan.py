import RPi.GPIO as gp

#GPIO Pin
pin = 12

def config():
    gp.setwarnings(False)
    gp.setmode(gp.BCM)
    gp.setup(pin, gp.OUT)


def switch_on():
    gp.output(pin, gp.HIGH)


def switch_off():
    gp.output(pin, gp.LOW)
