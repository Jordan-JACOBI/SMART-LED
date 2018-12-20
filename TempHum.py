# If planning to use wiringpi, uncomment the line below
# import wiringpi

# SMBUS is limited to 1 slave
import smbus
import time

class TempHum():

	bus = smbus.SMBus(1)
# Configure HTC1080 address : 100 0000
	address = 0x40

# Configure 0x02 to both acquire temperature & humidity with 11-bit & 8-bit resolution
# 0001 0110 0000 0000
	config = 0x1600


	def __init__(self):
        	self.name = "temperature and humidity sensor"


	def getValue(self):
		self.bus.write_byte_data(self.address, 0x02, self.config)
		time.sleep(0.1)

		self.bus.write_byte(self.address, 0x02)
		time.sleep(0.1)
		conf0=self.bus.read_byte(self.address)
		time.sleep(0.1)
		conf1=self.bus.read_byte(self.address)
		time.sleep(0.1)

	# Trigger the measurement : write 0x00
		self.bus.write_byte(self.address, 0x00)
		time.sleep(0.1)


	# Read from 0x00 & 0x01 (2-byte registers)
		temp0=self.bus.read_byte(self.address)
		time.sleep(0.1)
		temp1=self.bus.read_byte(self.address)
		time.sleep(0.1)


		self.bus.write_byte(self.address, 0x01)
		time.sleep(0.1)
		humidity0=self.bus.read_byte(self.address)
		time.sleep(0.1)
		humidity1=self.bus.read_byte(self.address)
		time.sleep(0.1)

		temperature = (float(temp0) / float(pow(2,8)))*165 - 40
		humidity = (float(humidity0) / float(pow(2,8)))*100
		return temperature , humidity

