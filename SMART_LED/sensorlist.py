from enum import Enum

# ENUM CLASS USED TO DEFINE CONSTANTS FOR SENSORS TO CALL GENERAL METHODS
# ex : getValue(sensorList.TEMPERATURE)
class SensorList(Enum) :
	TEMPERATURE = 0
	HUMIDITY = 1
	BRIGHTNESS = 2
	IR = 3
	PIR = 4
