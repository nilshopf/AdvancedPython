import RPi.GPIO as gp
import time

#GPIO Pin
servo1 = 16
servo2 = 20
servo3 = 21

#global
p1=0
p2=0
p3=0



def config():

    global p1
    global p2
    global p3

    gp.setwarnings(False)
    gp.setmode(gp.BCM)

    #Pins als Ausgang definieren
    gp.setup(servo1, gp.OUT)
    gp.setup(servo2, gp.OUT)
    gp.setup(servo3, gp.OUT)

    #PWM Pin definieren
    p1 = gp.PWM(servo1, 50)
    p2 = gp.PWM(servo2, 50)
    p3 = gp.PWM(servo3, 50)

    p1.start(2.5)
    p2.start(2.5)
    p3.start(2.5)



def switch_on():
    max(p1)
    max(p2)
    max(p3)

def switch_off():
    min(p1)
    min(p2)
    min(p3)

#
def min(p):
    p.ChangeDutyCycle(2.5)


def mid(p):
    p.ChangeDutyCycle(7.5)


def max(p):
    p.ChangeDutyCycle(12.5)
