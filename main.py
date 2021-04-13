# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import time
import GPIO
def print_hi(name):
    print(f'Hello, {name}')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    GPIO.LED_init()

    while 1:
        GPIO.LED_ON()
        time.sleep(1.5)
        GPIO.LED_OFF()
        time.sleep(1.5)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
