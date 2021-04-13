from gpiozero import LED, Button
from time import sleep

def blinkt():
    led = LED(17)
    led.on()
    sleep(0.1)
    led.off()
    sleep(0.1)

def button():
    button = Button(2)