import mqtt
import topics
from sensorlist import SensorList

class Slave :

	# CONSTRUCTOR
	def __init__(self, slave_address) :
		self.address = slave_address

		# ATTRIBUTE SLAVES
		self.sensors = [0,0,0,0,0,0,0,0,0,0]
		self.define_sensors()

		# CREATE MQTT CLIENT
		self.client = mqtt.MQTTClient()

		# INIT DEVICE
		self.init()
	
	# Init MQTT & Sensors
	def init(self):
		# MQTT connection
		self.client.connect()
		
		# Sensor configuration
		for sensor in self.sensors :
			try :
				sensor.init()
			except :
				print("Failed to init :" + str(sensor))

	# ATTRIBUTION OF SENSORS
	def define_sensors(self) :
		self.sensors.insert(SensorList.TEMPERATURE.value, "Temp sensor")
		self.sensors.insert(SensorList.HUMIDITY.value, "Humidity sensor")
		self.sensors.insert(SensorList.IR.value, "IR sensor")
		self.sensors.insert(SensorList.BRIGHTNESS.value, "Bright sensor")


	# GetTemperature from sensor
	def getTemperature(self) :
		return 19.4

	def sendTemperature(self) :
		self.client.publish('ECAM/jordan', self.getTemperature(), 1, False)
	
	# GET SENSOR VALUE
	def getValue(self, index) :
		print(self.sensors[index.value])
		#return self.sensors[index].getValue()

	# SEND SENSOR VALUE OVER MQTT
	def sendValue(self, index) :
		pass
