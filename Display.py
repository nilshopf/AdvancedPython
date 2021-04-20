import struct
import time
import serial
from binascii import unhexlify


def UART_init():
    ser = serial.Serial("/dev/serial0", 9600)  # Open port with baud rate


def Sensor_Data():
    var = 70
    #Bodenfeuchtigkeit
    UART_sendData(txtfeld="t2.txt=", msg= str(var) + "%")
    #Temperatur
    UART_sendData(txtfeld="t6.txt=", msg=str(var))
    # Druck
    UART_sendData(txtfeld="t8.txt=", msg=str(var) + "hPa")
    #Luftfeuchtigkeit
    UART_sendData(txtfeld="t4.txt=", msg=str(var) + "%")


def UART_sendData(txtfeld, msg):
    ser = serial.Serial("/dev/serial0", 9600)  # Open port with baud rate

    my_string = 'FF'

    #ser.write(str.encode("t2.txt="))
    ser.write(str.encode(txtfeld))
    ser.write(str.encode("\""))
    #ser.write(str.encode("50%"))
    ser.write(str.encode(msg))
    ser.write(str.encode("\""))
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))
    ser.write(unhexlify(my_string))

