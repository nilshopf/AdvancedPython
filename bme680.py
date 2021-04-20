import board
import busio
import adafruit_bme680

def get_data():
    i2c = busio.I2C(board.SCL, board.SDA)
    sensor = adafruit_bme680.Adafruit_BME680_I2C(i2c)
    return sensor.gas, sensor.humidity, sensor.pressure, sensor.temperature