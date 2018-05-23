# CONTROL OF YELLOW LIGHT SYSTEM OF A CAR 
#   
#   By Bryan Beider
#   bb1643@nyu.edu
#   
#   This code sends signals to the arduino board light system via serial communication.
#   Input commands are sent from python using the keyboard 
#   
#   NOTE: In Python 3.x the strings are Unicode by default. When sending data to Arduino, 
#   they have to be converted to bytes. This can be done by prefixing the string with b:
#   example-> serialObj.write(b'5') instead of serialObj.write('5') # prefix b is required
#   for Python 3.x, optional for Python 2.x. You can also use serialObj.write('5'.encode())

import serial
import time
import pygame
from pygame.locals import *

#******************************* GLOBAL CONSTANTS ********************************
#---------Yellow Light Stages-----------
# All yellow light stages will be blinking except for NO_LIGHTS
YELLOW_NO_LIGHTS  = '0'
YELLOW_ALL_FOUR   = '1'
YELLOW_RIGHT_SIDE = '2'
YELLOW_LEFT_SIDE  = '3'
YELLOW_REVERSE    = '4'


#******************************* END OF GLOBAL CONSTANTS ****************************
#******************************   MAIN CODE STARTS HERE ****************************

#--------Initialize Keyboard through Pygame ---------------------
pygame.init()                        #Initializes queue of keyboard inputs
pygame.display.set_mode((400,400))   #A window must be created in order for pygame to work

condition1True = 0                   #List of Bool variables based on keyboard inputs
condition2True = 0
condition3True = 0
condition4True = 0
condition5True = 0

#------Initialize a serial object-------
try:
    yellowLights_arduino = serial.Serial("COM4", baudrate = 9600, timeout = 1)
except:
    print('Please check yellowLights_arduino COM port')
    
time.sleep(1)          # delay for quarter of a second since connection resets arduino board.



#------Turn on lights-------------    
while True:

    #************************** READ KEYBOARD DATA ****************************
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a: condition1True = 1
            if event.key == pygame.K_v: condition2True = 1
            if event.key == pygame.K_e: condition3True = 1
            if event.key == pygame.K_f: condition4True = 1
            if event.key == pygame.K_r: condition5True = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a: condition1True = 0
            if event.key == pygame.K_v: condition2True = 0
            if event.key == pygame.K_e: condition3True = 0
            if event.key == pygame.K_f: condition4True = 0
            if event.key == pygame.K_r: condition5True = 0
 
    #************************** END OF KEYBOARD DATA ****************************
   

    if condition1True:
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


