
/*  CONTROL OF YELLOW LIGHT SYSTEM OF A CAR 
 *  
 *  By Bryan Beider
 *  bb1643@nyu.edu
 *  
 *  This code is controlled from the python script and it serves just as a platform
 *  to send signals to the arduino board light system from python. In the python script
 *  you will find conditions as to when a signal is sent according to sensor readings.
 *  
 *  Note: All yellow light stages will be blinking and the delayed time between on and off
 *  is set by "delayed_time" 
 *  
 *  Terminology (seen from the driver's seat)
 *  _FR : Front Right 
 *  _FL : Front Left 
 *  _BR : Back Right 
 *  _BL : Back Left
 *  
 *  Hardware: 
 *  Active low relays are being used therefore LOW = ON and HIGH = OFF
*/

//----RELAYS ARE ACTIVE LOW THEREFORE: -------
const bool ON  = LOW;
const bool OFF = HIGH;


//---------Yellow Light Stages-----------
// All yellow light stages will be blinking except for NO_LIGHTS
const char YELLOW_NO_LIGHTS  = '0';
const char YELLOW_ALL_FOUR   = '1';
const char YELLOW_RIGHT_SIDE = '2';
const char YELLOW_LEFT_SIDE  = '3';
const char YELLOW_REVERSE    = '4';
char yellowLightStage;  //Variable to read yello light stage sent trhrough serial communication 


//--------Relay Pin Numbers-------------
const int relayPin_FR =  2;      
const int relayPin_FL =  3;      
const int relayPin_BR =  4;      
const int relayPin_BL =  5;  


//--------Time Delay Between Blinks-------
const int delayed_time = 800; //milliseconds

void setup() {
  // initialize the relay pins as an output:
  pinMode(relayPin_FR, OUTPUT);
  pinMode(relayPin_FL, OUTPUT);
  pinMode(relayPin_BR, OUTPUT);
  pinMode(relayPin_BL, OUTPUT);

  // initialize relays to off
  digitalWrite(relayPin_FR, OFF); 
  digitalWrite(relayPin_FL, OFF);
  digitalWrite(relayPin_BR, OFF);
  digitalWrite(relayPin_BL, OFF);
  
  // initialize serial communication
  Serial.begin(9600);
}


void loop() {
  if(Serial.available() > 0) {
      yellowLightStage = Serial.read();         //Since commands are sent continously
      Serial.println(yellowLightStage);
      
      if (yellowLightStage == YELLOW_NO_LIGHTS) {
        digitalWrite(relayPin_FR, OFF);
        digitalWrite(relayPin_FL, OFF);
        digitalWrite(relayPin_BR, OFF);
        digitalWrite(relayPin_BL, OFF);
        Serial.println("YELLOW_NO_LIGHTS");
      }
      
      if (yellowLightStage == YELLOW_ALL_FOUR) {
        digitalWrite(relayPin_FR, ON);
        digitalWrite(relayPin_FL, ON);
        digitalWrite(relayPin_BR, ON);
        digitalWrite(relayPin_BL, ON);
        delay(delayed_time);  //milliseconds
        digitalWrite(relayPin_FR, OFF);
        digitalWrite(relayPin_FL, OFF);
        digitalWrite(relayPin_BR, OFF);
        digitalWrite(relayPin_BL, OFF);
        delay(delayed_time);
        Serial.println("YELLOW_ALL_FOUR");
        
      }

      if (yellowLightStage == YELLOW_RIGHT_SIDE) {
        digitalWrite(relayPin_FR, ON);
        digitalWrite(relayPin_BR, ON);
        delay(delayed_time);  //milliseconds
        digitalWrite(relayPin_FR, OFF);
        digitalWrite(relayPin_BR, OFF);
        delay(delayed_time);
        Serial.println("YELLOW_RIGHT_SIDE");
      }

      if (yellowLightStage == YELLOW_LEFT_SIDE) {
        digitalWrite(relayPin_FL, ON);
        digitalWrite(relayPin_BL, ON);
        delay(delayed_time);  //milliseconds
        digitalWrite(relayPin_FL, OFF);
        digitalWrite(relayPin_BL, OFF);
        delay(delayed_time);
        Serial.println("YELLOW_LEFT_SIDE");
      }
      
      if (yellowLightStage == YELLOW_REVERSE) {     
        digitalWrite(relayPin_BR, ON);
        digitalWrite(relayPin_BL, ON);
        delay(delayed_time);  //milliseconds
        digitalWrite(relayPin_BR, OFF);
        digitalWrite(relayPin_BL, OFF);
        delay(delayed_time);
        Serial.println("YELLOW_REVERSE");
      }
        
        Serial.println("COMPLETE"); //COMPLETE INDICATOR
        Serial.flush();
        
  }
}
