import functions
import taster
# import luefter
import time
# import rgb
import servo


if __name__ == '__main__':

    p = servo.config()

try:
    while True:
        #p.ChangeDutyCycle(7.5)
        #"""
        servo.min(p)
        time.sleep(5)
        #servo.mid(p)
        #time.sleep(5)
        servo.max(p)
        time.sleep(5)
       # """
except KeyboardInterrupt:
        p.stop()

