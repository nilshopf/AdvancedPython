from gpiozero import RGBLED

led = RGBLED(red=17, green=27, blue=22)


# Red = Mosi; Green = Miso; Blue SCLK
# Last Pin on VCC
# 1k resistors in front of each color

def red():
    led.color = (0, 1, 1)


def green():
    led.color = (1, 0, 1)


def yellow():
    led.color = (0, 0, 1)


def blue():
    led.color = (1, 1, 0)
