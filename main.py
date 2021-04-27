# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import GPIO
import servo
import fan
import rgb
import pump
import bme680
import pcf8591
import kamera
import Display

import time

# Vergleichswerte
soil_moisture_check =  0       #Vergleichswert Bodenfeuchtigkeit
temperature_check = 22         #Vergleichswert Temperatur in °C
humidity_check = 50            #Vergleichswert Feuchtigkeit in %
irrigation_time = 15           #Bewässerungs Zeit in sek


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    servo.config()
    fan.config()
    GPIO.config()
    pump.config()
    kamera.config()

    while True :

        # Sensoren auslesen
        gas, humidity, pressure, temperature = bme680.get_data()
        soil_moisture = pcf8591.get_data()

        Display.set_data(soil_moisture, temperature, pressure, humidity)


        # Bodenfeuchtigkeit prüfen
        if soil_moisture <= soil_moisture_check :
            pump.switch_on()
            time.sleep(irrigation_time)
            pump.switch_off()

        # Temperatur & Luftfeuchtigkeit prüfen
        if (temperature >= temperature_check) | (humidity >= humidity_check):
            servo.switch_on()
            fan.switch_on()
            rgb.red()
        else:
            servo.switch_off()
            fan.switch_off()
            rgb.green()

        time.sleep(60)



