import sensor

class IRSensor(sensor.Sensor) :

	# Define some constants from the datasheet
	DEVICE     = 0x23 # Default device I2C address
	POWER_DOWN = 0x00 # No active state
	POWER_ON   = 0x01 # Power on
	RESET      = 0x07 # Reset data register value

	# Start measurement at 4lx resolution. Time typically 16ms.
	CONTINUOUS_LOW_RES_MODE = 0x13
	# Start measurement at 1lx resolution. Time typically 120ms
	CONTINUOUS_HIGH_RES_MODE_1 = 0x10
	# Start measurement at 0.5lx resolution. Time typically 120ms
	CONTINUOUS_HIGH_RES_MODE_2 = 0x11
	# Start measurement at 1lx resolution. Time typically 120ms
	# Device is automatically set to Power Down after measurement.
	ONE_TIME_HIGH_RES_MODE_1 = 0x20
	# Start measurement at 0.5lx resolution. Time typically 120ms
	# Device is automatically set to Power Down after measurement.
	ONE_TIME_HIGH_RES_MODE_2 = 0x21
	# Start measurement at 1lx resolution. Time typically 120ms
	# Device is automatically set to Power Down after measurement.
	ONE_TIME_LOW_RES_MODE = 0x23

	def __init__(self) :
		pass

	def init(self) :
		pass

	def getValue(self) :
		return -1
