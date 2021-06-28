'''
UART communication on Raspberry Pi using Python
Крч, я в будущем, слушай внимательно
В raspi-config на врубить serial 
Так что не забудь
Peace
'''
import serial
from time import sleep

ser = serial.Serial ("/dev/ttyS0", 9600)    #Open port with baud rate
while True:
    received_data = ser.read()              #read serial port
    sleep(0.03)
    data_left = ser.inWaiting()             #check for remaining byte
    received_data += ser.read(data_left)
    print (received_data)                   #print received data
    ser.write(received_data)                #transmit data serially