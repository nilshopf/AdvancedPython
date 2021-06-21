"""
 * ---------------------------------------------------------------------------------------------------------
 *		Version		:		1.0
 * ---------------------------------------------------------------------------------------------------------
 *
 *		Nutzen		:		Main Modul fuer Smartes Gewaechshaus
 *
 *		Modul		:		Advanced Python
 *
 *		Autoren		:		Merit Tienken
 *
 *		Sprache		:		Python
 *
 *
 *
 *	Date			Time	Name		Log		Modification
 *----------------------------------------------------------------------------------------------------------
 *25.05.2021        16:27   Nils Hopf   1       Hinzufuegen des Abschnitts "Website & Threads"
 *
 """

"""------------------------------INITIALISIERUNGSLISTE-----------------------------------"""
# Importieren vorgefertigter Module
from flask import Flask, render_template
import time
import threading

# Importieren eigener Module
import gpio
import fan
import rgb
import pump
import bme680
import pcf8591
import camera
import Display


# Startwerte fuer die Sensordaten
humidity = 0
pressure = 0
temperature = 0
soil_moisture = 0

# Vergleichswerte zum Kontrollieren der Messdaten
soil_moisture_check = 45    # Vergleichswert Bodenfeuchtigkeit in %
temperature_check = 26      # Vergleichswert Temperatur in °C
humidity_check = 80         # Vergleichswert Luftfeuchtigkeit in %
irrigation_time = 10        # Bewaesserungs Zeit in sek

ventilation_check = 0       # wird benoetigt, um den Luefter manuell zu steuern

"""------------------------------WEBSITE & THREADS-----------------------------------"""

# Befehle fuer Flask Webserver
app = Flask(__name__)
app.debug = False
app.use_reloader=False

# Erstmaliges auslesen der Sensordaten zum fuellen der Website
humidity, pressure, temperature = bme680.get_data()

# Festlegen der Website URL und der Funktion zum uebergeben der Daten an die Webseite
@app.route("/")
def hallo():
        return render_template("start.html", soil_moisture=soil_moisture, pressure=pressure, temperature=temperature,
                       humidity=humidity)

# Funktion zum auslagern des Webservern auf einen eigenen Thread
def flaskThread():
    app.run(host="192.168.178.63")


"""----------------------------------MAIN------------------------------------------"""

if __name__ == '__main__':

    #Thread fuer Webserver starten
    threading.Thread(target=flaskThread).start()

    # Module initialisieren
    rgb.green()
    fan.config()
    gpio.config()
    pump.config()
    camera.config()
    Display.config()

    while True:

        # Sensordaten auslesen
        humidity, pressure, temperature = bme680.get_data()
        soil_moisture = pcf8591.get_data()

        # Messwerte runden -zwei Nachkommastelle-
        humidity = round(humidity, 2)
        pressure = round(pressure, 2)
        temperature = round(temperature, 2)
        soil_moisture = round(soil_moisture, 2)

        # Moeglichkeit zur Ausgabe der Messdaten auf dem Terminal
        """
        print("\n\nDruck:", pressure, "\nLuftfeuchtigkeit:", humidity, "\nTemperatur:", temperature, "\nBodenfeuchtigkeit:",
              soil_moisture)
        """

        # Sensordaten an das Display senden
        Display.set_data(soil_moisture, humidity, pressure, temperature)

        # stuendliche Fotoaufnahme
        if time.localtime()[4] % 60 == 0:
            camera.picture()
            time.sleep(60)

        # Bodenfeuchtigkeit pruefen
        if soil_moisture <= soil_moisture_check:
            pump.switch_on()
            time.sleep(irrigation_time)
            pump.switch_off()
            time.sleep(20)

        # Temperatur & Luftfeuchtigkeit pruefen -> Luefter aktivieren
        if (temperature >= temperature_check) | (humidity >= humidity_check):
            fan.switch_on()
            rgb.red()
            ventilation_check = 1

        elif ventilation_check == 1:
            fan.switch_off()
            rgb.green()
            ventilation_check = 0


