import RPi.GPIO as gp

pin = 17

def config():
    gp.setwarnings(False)
    gp.setmode(gp.BCM)
    gp.setup(pin, gp.OUT)


def on():
    gp.output(pin, gp.HIGH)


def off():
    gp.output(pin, gp.LOW)
