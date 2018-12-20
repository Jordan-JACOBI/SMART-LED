import mqtt
import topics 
from sensorlist import SensorList

class Master :
	
	# CONSTRUCTOR
	def __init__(self) :
		# CREATE MQTT CLIENT
		self.client = mqtt.MQTTClient()
	
	# INIT MQTT COMMUNICATION
	def init(self) :
		# MQTT connection
		self.client.connect()
	
	# PRIVATE METHOD TO IMPLEMENT COMMANDS
	def sendCommand(self, topic, command) :
		self.client.publish(topic, command, 0, False)
		pass
	
##### COMMANDS #####

	# COMMAND TO ADJUST LED INTENSITY
	def sendDimmer(self, dim_intensity, slave) :
		topic = topics.format(topics.DIMMER, slave)
		self.sendCommand(topic, dim_intensity)

	# COMMAND TO SEND THE SIGNAL TO TURN ON/OFF THE LED
	def sendOnOff(self, on_off, slave) :
		topic = topics.format(topics.ON_OFF, slave)
		self.sendCommand(topic, on_off)

	# COMMAND TO SEND THE ALARM SIGNAL IF T° IS TOO HIGH
	def sendAlarmHighTemp(self, temp, slave) :
		topic = topics.format(topics.ALARM_HIGH_TEMP, slave)
		self.sendCommand(topic, temp)
