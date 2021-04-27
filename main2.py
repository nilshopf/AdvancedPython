

import GPIO
import time
import bme680
import Display

soil_moisture_check =  0       #Vergleichswert Bodenfeuchtigkeit
temperature_check = 22         #Vergleichswert Temperatur in °C
humidity_check = 50            #Vergleichswert Feuchtigkeit in %
irrigation_time = 15           #Bewässerungs Zeit in sek


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    GPIO.config()
    Display.config()

    while True:

        Display.set_data(soil_moisture_check, temperature_check, humidity_check, irrigation_time)
        # Sensoren auslesen
        #gas, humidity, pressure, temperature = bme680.get_data()
        #print("gas", gas, "\nLuftfeuchtigkeit:", humidity,"\nDruck:",  pressure, "\nTemperatur:", temperature)

