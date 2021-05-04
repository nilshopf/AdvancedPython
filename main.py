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
soil_moisture_check = 50       #Vergleichswert Bodenfeuchtigkeit in %
temperature_check = 24         #Vergleichswert Temperatur in °C
humidity_check = 60            #Vergleichswert Luftfeuchtigkeit in %
irrigation_time = 15           #Bewässerungs Zeit in sek

ventilation_check = 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    servo.config()
    fan.config()
    GPIO.config()
    pump.config()
    #kamera.config()
    Display.config()

    while True :

        # Sensoren auslesen
        gas, humidity, pressure, temperature = bme680.get_data()
        soil_moisture = pcf8591.get_data()

        print("\n\ngas:", gas, "\nLuftfeuchtigkeit:", humidity, "\nTemperatur:", temperature, "\nBodenfeuchtigkeit:", soil_moisture)

        Display.set_data(soil_moisture, temperature, pressure, humidity)

        # stündliche Fotoaufnahme
        if time.localtime()[4] % 60 == 0:
            kamera.picture()

        # Bodenfeuchtigkeit prüfen
        if soil_moisture <= soil_moisture_check:
            pump.switch_on()
            time.sleep(irrigation_time)
            pump.switch_off()

        # Temperatur & Luftfeuchtigkeit prüfen
        if (temperature >= temperature_check) | (humidity >= humidity_check):
            servo.switch_on()
            fan.switch_on()
            rgb.red()
            ventilation_check = 1

        elif ventilation_check == 1:
            servo.switch_off()
            fan.switch_off()
            rgb.green()






