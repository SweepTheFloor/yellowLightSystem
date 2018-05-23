# CONTROL OF YELLOW LIGHT SYSTEM OF A CAR 
#   
#   By Bryan Beider
#   bb1643@nyu.edu
#   
#   This code sends signals to the arduino board light system via serial communication.
#   Input commands are sent from python
#   
#   NOTE: In Python 3.x the strings are Unicode by default. When sending data to Arduino, 
#   they have to be converted to bytes. This can be done by prefixing the string with b:
#   example-> serialObj.write(b'5') instead of serialObj.write('5') # prefix b is required
#   for Python 3.x, optional for Python 2.x. You can also use serialObj.write('5'.encode())

import serial
import time

#---------Yellow Light Stages-----------
# All yellow light stages will be blinking except for NO_LIGHTS
YELLOW_NO_LIGHTS  = '0'
YELLOW_ALL_FOUR   = '1'
YELLOW_RIGHT_SIDE = '2'
YELLOW_LEFT_SIDE  = '3'
YELLOW_REVERSE    = '4'


#------Initialize a serial object-------
try:
    yellowLights_arduino = serial.Serial("COM4", baudrate = 9600, timeout = 1)
except:
    print('Please check yellowLights_arduino COM port')
    
time.sleep(1)          # delay for quarter of a second since connection resets arduino board.


#------Turn on lights-------------    
while True:

    yellowLightStage = YELLOW_ALL_FOUR      #Choose light stage to send
        
    #The Arduino file prints:
    #   * What was sent/written from python 
    #   * The stage light executed
    #   * Confirmation of 'COMPLETE' when done
        
    arduinoData_printedToSerial = ''        # set data from arduino to empty
    data_received = False                   # data sent from python was it received by arduino? confirmation set to false
    
    while (arduinoData_printedToSerial != 'COMPLETE'):
        if not data_received : 
            yellowLights_arduino.write(yellowLightStage)                        # Send light stage from python only if data has not been received
        
        arduinoData_printedToSerial = yellowLights_arduino.readline()           # read what arduino printed to serial
        arduinoData_printedToSerial= arduinoData_printedToSerial.rstrip('\r\n') # readline adds an extra line by default so rstrip it  
        if arduinoData_printedToSerial:                                         # if what was read was different than '' then data was sent and received
            print(arduinoData_printedToSerial)                                        
            data_received = True
