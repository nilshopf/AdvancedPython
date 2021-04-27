import RPi.GPIO as GPIO

Counter = 0
status = 0

#LED's initialisieren
def GPIO_init():
    GPIO.setmode(GPIO.BCM)  #GPIO Nummern ansprechen
    GPIO.setwarnings(False)

    #LED initialisieren
    GPIO.setup(21, GPIO.OUT)

    #Taster initialisieren
    GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    GPIO.add_event_detect(24, GPIO.RISING, callback=Interrupt, bouncetime = 200)

def LED_ON():
    GPIO.output(21, GPIO.HIGH)

def LED_OFF():
    GPIO.output(21, GPIO.LOW)

def Interrupt(Channel):
    global Counter
    global status
    Counter = Counter + 1
    print ("Counter " + str(Counter))

    if status == 0:
        LED_ON()
        status = 1
    else:
        LED_OFF()
        status = 0





