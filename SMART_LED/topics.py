# This file defines the different topics used in MQTT communications between master & slaves.
# These topics can be reused in a remote web interface.

# /!\ Topic names MUST NOT end or begin with a '/'
# Topic full syntax : RADIX/SLAVE_NUMBER/TOPIC

import re

# RADIX
RADIX = "ECAM/smart_led"

# SENSORS
TEMPERATURE = "sensors/temperature"
HUMIDITY = "sensors/humidity"
BRIGHTNESS = "sensors/brightness"
PRESENCE = "sensors/presence"

# COMMANDS
ON_OFF = "commands/on_off"
DIMMER = "commands/dimmer"

# ALARMS
ALARM_HIGH_TEMP = "alarms/high_temp"


###### TOPIC METHODS #####

# GET A FULL MQTT TOPIC NAME FROM THE RADIX, THE SPECIFIED TOPIC & THE SLAVE NUMBER
def format(topic, slave) :
	topic_full_name = RADIX + '/' + str(slave) + '/' + topic
	return topic_full_name

# GET A TOPIC & SLAVE NUMBER FROM THE FULL TOPIC NAME (if the radix matches)
def extract(topic_full_name) :
	# CHECK IF THE STRING BEGINS WITH THE RADIX
	if(topic_full_name.startswith(RADIX)) :
		# REMOVE THE RADIX AND THE '/' FROM THE STRING
		t = topic_full_name[len(RADIX)+1:]
		
		# GET SLAVE NUMBER
		try :
			# REGULAR EXPRESSION RETURNING ONLY THE FIRST DIGITS OF A STRING...
			slave = int(re.sub('([0-9]*).*', r'\1', t))
		except :
			slave = -1

		# ...AND THE OPPOSITE REMOVING THESE DIGITS
		t = re.sub('^[0-9]*', "", t)

		# REMOVE THE '/' BEFORE THE TOPIC NAME
		topic = t[1:]

		return topic, slave
	else :
		return "", -1
