import smbus
import time

address = 0x48
A0 = 0x40
"""
A1 = 0x41
A2 = 0x42
A3 = 0x43
bus = smbus.SMBus(1)
while True:
    bus.write_byte(address,A0)
    #value = bus.read_byte(address)
    for i in range(5):
        value = bus.read_byte(address)
        time.sleep(0.5)

    print("AOUT:%1.3f  " %(value*3.3/255))
"""


def get_data():
    bus = smbus.SMBus(1)
    for i in range(5):
        value = bus.read_byte(address)
        time.sleep(0.5)

    value = (value * 3.3 / 255)

#!TODO Umrechnung in Prozent
    #!Aktualisiert Werte nicht richtig
    value = value - 0.955
    value = (value / 1.265) * 100
    value = 100 - value
    return value
