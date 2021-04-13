import functions
import taster
from gpiozero import LED, Butto

button = Button(2)

if __name__ == '__main__':

    while True:
        button.wait_for_press()
        print("Button pushed")
        led.on()
        button.wait_for_release()
        led.off()
