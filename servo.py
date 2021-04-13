import RPi.GPIO as gp
import time

servo = 18


def config():
    gp.setwarnings(False)
    gp.setmode(gp.BCM)
    gp.setup(servo, gp.OUT)

    p = gp.PWM(servo, 50)
    p.start(2.5)
    return p


def min(p):
    p.ChangeDutyCycle(2.5)


def mid(p):
    p.ChangeDutyCycle(7.5)


def max(p):
    p.ChangeDutyCycle(12.5)
