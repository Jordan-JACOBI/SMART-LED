import RPi.GPIO as GPIO
class PIR:
	gpioSensor=23

	def __init__(self):
		self.name = "Capteur  PIR"

	def getValue(self):
		GPIO.setmode(GPIO.BCM)
		sensor=self.gpioSensor
		GPIO.setup(sensor,GPIO.IN)
		if GPIO.input(sensor):
			return True
		return False
