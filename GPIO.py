import RPi.GPIO as GPIO
import servo
import fan


#GPIO Pin
button = 25
state = 0


#Pumpe initialisieren
def config():
    GPIO.setmode(GPIO.BCM)  #GPIO Nummern ansprechen
    GPIO.setwarnings(False)

    #Taster initialisieren
    GPIO.setup(button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    GPIO.add_event_detect(button, GPIO.RISING, callback=fan_Interrupt, bouncetime = 200)



def fan_Interrupt(Channel):

    global state

    if state == 0:
        servo.switch_on()
        fan.switch_on()
        state = 1
    else:
        servo.switch_off()
        fan.switch_off()
        state = 0


