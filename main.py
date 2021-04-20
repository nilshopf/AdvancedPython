import functions
import taster
# import luefter
import time
# import rgb
import servo
import kamera
import bme680


if __name__ == '__main__':
    #camera = kamera.config()
    #while True:
    #kamera.picture(camera)

    gas, humidity, pressure, temperature = bme680.get_data()
    print(gas)
    print(humidity)
    print(pressure)
    print(temperature)

