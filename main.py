# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import time

import GPIO
import function


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # LED und Taster initialisieren
    GPIO.GPIO_init()
    # Timer für die Camera aktievieren
    function.Timer_Camera()

    while 1:
        #Prüfen ob ein neuer Timer benötigt wird
        function.NeedNewTimer()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
