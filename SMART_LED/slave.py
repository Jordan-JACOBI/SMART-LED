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
		
		# ATTRIBUTE SENSOR TOPICS
		self.sensor_topics = ["","","","","","","","","",""]
		self.define_sensor_topics()
		
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
		self.sensors.insert(SensorList.PIR.value, "PIR sensor")
		self.sensors.insert(SensorList.BRIGHTNESS.value, "Bright sensor")
	
	# ATTRIBUTION OF ALL SENSOR TOPICS
	def define_sensor_topics(self) :
		self.attribute_topic(SensorList.TEMPERATURE.value, topics.TEMPERATURE)
		self.attribute_topic(SensorList.HUMIDITY.value, topics.HUMIDITY)
		self.attribute_topic(SensorList.PIR.value, topics.PRESENCE)
		self.attribute_topic(SensorList.BRIGHTNESS.value, topics.BRIGHTNESS)
		
	# ATTRIBUTE A TOPIC TO A SENSOR
	def attribute_topic(self, sensor_id, topic) :
		full_topic = topics.format(topic, self.slave_address)
		self.sensor_topics.insert(sensor_id, full_topic)
	
	# GetTemperature from sensor
	def getTemperature(self) :
		return 19.4

	def sendTemperature(self) :
		self.client.publish(self.sensor_topics[SensorList.TEMPERATURE.value], self.getTemperature(), 1, False)
	
	# GET SENSOR VALUE
	def getValue(self, index) :
		print(self.sensors[index.value])
		return self.sensors[index.value].getValue()

	# SEND SENSOR VALUE OVER MQTT
	def sendValue(self, index) :
		self.client.publish(self.sensor_topics[index.value], self.getValue(index), 1, False)
