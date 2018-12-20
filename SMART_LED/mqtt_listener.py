#IMPORT CUSTOM FILES
import topics
import cloud_backup

#CONNECT TO SQL
db_cursor = cloud_backup.sql_init()

#IMPORT UART MODULES
import Adafruit_BBIO.UART as UART
import serial

#IMPORT MQTT MODULE
import paho.mqtt.client as mqtt

#SUBSCRIBE
def subscribe():
	client.subscribe(topics.temperature, 0)
	client.subscribe(topics.acquisition, 0)
	client.subscribe(topics.awake, 0)
	client.subscribe(topics.timesleep, 0)
	client.subscribe(topics.readtime, 0)

#DEFINE CALLBACK FUNCTIONS
def on_message(client, userdata, msg):
	#JUST A TEST
	print("Message received :")
	print(msg.topic+" "+str(msg.payload))
	
	#INTERNAL LOGIC
	if msg.topic == topics.acquisition :
		with open("cfg/acquisition", "wb") as cfg_acquisition :
			cfg_acquisition.write(msg.payload)
			cfg_acquisition.flush()
		cfg_acquisition.close()

	if msg.topic == topics.awake :
		with open("cfg/awake", "wb") as cfg_awake :
			cfg_awake.write(msg.payload)
		cfg_awake.close()

	if msg.topic == topics.timesleep :
		with open("cfg/timesleep", "wb") as cfg_timesleep :
			cfg_timesleep.write(msg.payload)
		cfg_timesleep.close()

	if msg.topic == topics.readtime :
		with open("cfg/readtime", "wb") as cfg_readtime :
			cfg_readtime.write(msg.payload)
		cfg_readtime.close()

	if msg.topic == topics.temperature :
		# print("TEMPERATURE !")

		#CLOUD BACKUP TO DATABASE
		cloud_backup.save(msg.topic, msg.payload, db_cursor)


def on_connect(client, userdata, flags, rc):
	print("Connected")
	subscribe()

#SETUP THE CLIENT
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

#INITIATE THE MQTT CONNECTION
with open("cfg/mqtt/hostname", "r") as cfg_hostname :
	hostname =str(cfg_hostname.read())
cfg_hostname.close()

with open("cfg/mqtt/port", "r") as cfg_port :
	port = cfg_port.read()
cfg_port.close()

client.connect(hostname, 1883)

#ALLOW THE CLIENT TO LISTEN FOREVER
client.loop_forever()
