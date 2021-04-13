import functions
import taster
import luefter
import time

if __name__ == '__main__':
    luefter.config()

    while True:
        luefter.on()
        time.sleep(10)
        luefter.off()
        time.sleep(10)
