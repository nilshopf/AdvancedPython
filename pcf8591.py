"""
 * ---------------------------------------------------------------------------------------------------------
 *		Version		:		1.0
 * ---------------------------------------------------------------------------------------------------------
 *
 *		Nutzen		:		Modul fuer den PCF8591 (AD/DA Wandler mit I2C) zum Arbeiten mit Bodenfeuchtigkeitssensor
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
import smbus
import time

address = 0x48 # I2C Adresse des Wandlers
A2 = 0x42 # Register Adresse mit dem Wert an Analogpin 2


# Funktion zum erhalten des Spannungswertes
def get_data():
    bus = smbus.SMBus(1)
    bus.write_byte(address, A2)

    # mehrmaliges Auslesen, weil sonst gleiche Werte ermittelt werden
    for i in range(5):
        value = bus.read_byte(address)
        time.sleep(0.5)

    value = (value * 3.3 / 255)

    # Umrechnung der Spannungswerte in Prozent
    value = value - 0.955
    value = (value / 1.265) * 100
    value = 100 - value
    return value
