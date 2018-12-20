import paho.mqtt.client as mqtt

class MQTTClient :

	def __init__(self) :
		self.client = mqtt.Client()
		self.hostname = '127.0.0.1' 
		self.port = 1883
	
	def connect(self) :
		self.client.connect(self.hostname, self.port)
	
	def publish(self, topic, data, qos, retain) :
		self.client.publish(topic, data, qos, retain)

	def subscribe(self) :
		self.client.subscribe()
	
	def subscribe(self, topic, qos) :
		self.client.subscribe(topic, qos)
	
	def listen(self) :
		self.client.loop_forever()

	def define_on_connect(self, function) :
		self.client.on_connect = function

	def define_on_message(self, function) :
		self.client.on_message = function

	#def on_message(client, userdata, msg) :	
	#def on_connect(client, userdata, flags, rc):
