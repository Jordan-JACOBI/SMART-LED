# If planning to use wiringpi, uncomment the line below
# import wiringpi

# SMBUS is limited to 1 slave
import smbus
import time

try :

	bus = smbus.SMBus(1)
	print "I2C bus connected"
	time.sleep(1)
except:
	print "Can't connect to the I2C bus 1"

# Init I2C communication
# Setup bitrate (default=100kHz)

# Configure HTC1080 address : 100 0000
address = 0x40

# Configure 0x02 to both acquire temperature & humidity with 11-bit & 8-bit resolution
# 0001 0110 0000 0000
config = 0x1600
bus.write_byte_data(address, 0x02, config)
time.sleep(0.1)

bus.write_byte(address, 0x02)
time.sleep(0.1)
conf0=bus.read_byte(address)
time.sleep(0.1)
conf1=bus.read_byte(address)
time.sleep(0.1)

print conf0
print conf1

# Trigger the measurement : write 0x00
bus.write_byte(address, 0x00)
time.sleep(0.1)


# Read from 0x00 & 0x01 (2-byte registers)
temp0=bus.read_byte(address)
time.sleep(0.1)
temp1=bus.read_byte(address)
time.sleep(0.1)


bus.write_byte(address, 0x01)
time.sleep(0.1)
humidity0=bus.read_byte(address)
time.sleep(0.1)
humidity1=bus.read_byte(address)
time.sleep(0.1)

temperature = (float(temp0) / float(pow(2,8)))*165 - 40
humidity = (float(humidity0) / float(pow(2,8)))*100
print temp0
print temp1
print humidity0
print humidity1
print temperature
print humidity
