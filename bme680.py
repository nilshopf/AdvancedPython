"""
 * ---------------------------------------------------------------------------------------------------------
 *		Version		:		1.0
 * ---------------------------------------------------------------------------------------------------------
 *
 *		Nutzen		:		Modul zum Arbeiten mit dem Sensor BME-680
 *
 *		Modul		:		Advanced Python
 *
 *		Autor		:		Nils Hopf
 *
 *		Sprache		:		Python
 *
 *
 *
 *	Date			Time	Name		Log		Modification
 *----------------------------------------------------------------------------------------------------------
 *
 *
 """
import board
import busio
import adafruit_bme680

# Funktion zum Erhalten der Sensordaten
def get_data():
    i2c = busio.I2C(board.SCL, board.SDA) # Erstellen eines Objektes zum Nutzen des I2C Busses
    sensor = adafruit_bme680.Adafruit_BME680_I2C(i2c) # Erstellen eines Objektes unseren Sensors inklusive der Daten
    return sensor.humidity, sensor.pressure, sensor.temperature # Rueckgabe der aktuellen Sensordaten