# IMPORT CUSTOM FILES
import slave
import master
import mqtt
from sensorlist import SensorList

# TEST SENSORLIST ENUM
print (repr(SensorList.IR))

# INIT SLAVE
s = slave.Slave(0)

# INIT MASTER
m = master.Master()

# PRINT TEMPERATURE
print(s.getTemperature())
s.sendTemperature()
s.getValue(SensorList.IR)

# CALLBACK FUNCTIONS
def on_message(client, userdata, msg):
	print("on_message function")
	print(msg.topic)
	print(msg.payload)
	if(int(msg.payload) == 2) :
		print("Equal to 2")
	else :
		print("Not equal to 2")

def on_connect(client, userdata, flags, rc):
	print("on_connect function")

# INIT MQTT
client = mqtt.MQTTClient()

# DEFINE CALLBACK FUNCTIONS
client.define_on_message(on_message)
client.define_on_connect(on_connect)

# MQTT FUNCTIONS
client.connect()
client.subscribe('ECAM/jordan', 0)
client.listen()


###### MAIN BEHAVIOUR ######
TEMPERATURE_THRESHOLD = 85
BRIGHTNESS_THRESHOLD = 1200

def behaviour_temperature(temperature, slave) :
	if(temperature >= TEMPERATURE_THRESHOLD) :
		# SEND ALARM
		m.sendAlarmHighTemp(temperature, slave)

def behaviour_brightness(brightness, slave) :
	if(brightness < BRIGHTNESS_THRESHOLD) :
		dimmer = (brightness - BRIGHTNESS_THRESHOLD)*100/BRIGHTNESS_THRESHOLD
		# SEND NEW INTENSITY
		m.sendDimmer(dimmer, slave)
	else :
		# SEND OFF COMMAND
		m.sendOnOff(False, slave)


###### MAIN CALLBACK #####

def on_message(client, userdata, msg) :
	topic_name, slave = topics.extract(msg.topic)

	if(topic_name == topics.TEMPERATURE) :
		behaviour_temperature(float(msg.payload), slave)

	if(topic_name == topics.BRIGHTNESS) :
		behaviour_brightness(float(msg.payload), slave)
	


