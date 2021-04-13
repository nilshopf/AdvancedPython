import functions
import taster
# import luefter
import time
# import rgb
import servo
import kamera


if __name__ == '__main__':
    camera = kamera.config()
    #while True:
    kamera.picture(camera)
