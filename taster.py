from gpiozero import LED
from time import sleep

led = LED(17)

def blinkt():
    led.on()
    sleep(1)
    led.off
    sleep(1)