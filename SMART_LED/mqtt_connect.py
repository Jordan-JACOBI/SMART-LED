#IMPORT UART MODULES
import Adafruit_BBIO.UART as UART
import serial

#IMPORT MQTT MODULE
import paho.mqtt.client as mqtt

#DEFINE MQTT HOST PARAMETERS
hostname = "172.17.4.39"
port = 1883

#DEFINE TOPICS
topic_acquisition = "ECAM/Vinci1/1F04/BBB/in/acquisition"
topic_awake = "ECAM/Vinci1/1F04/PIC/in/awake"
topic_timesleep = "ECAM/Vinci1/1F04/PIC/in/timesleep"
topic_readtime = "ECAM/Vinci1/1F04/BBB/in/readtime"
topic_temp = "ECAM:Vinci1/sensor/temperature"

#SUBSCRIBE
def subscribe():
	client.subscribe(topic_temp, 0)

#DEFINE CALLBACK FUNCTIONS
def on_message(client, userdata, msg):
	print("Message received :")
	print(msg.topic+" "+str(msg.payload))
	#add send to DB

def on_connect(client, userdata, flags, rc):
	print("Connected")
	subscribe()


#SETUP THE CLIENT
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

#INITIATE THE MQTT CONNECTION
client.connect(hostname, port)

#ALLOW THE CLIENT TO LISTEN FOREVER
client.loop_forever()


#UART.setup("UART1")
