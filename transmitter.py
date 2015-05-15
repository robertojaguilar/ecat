#!/usr/bin.python

import sys, time
import Adafruit_BBIO.ADC as ADC
import Adafruit_BMP.BMP085 as BMP085
from datetime import datetime
sys.path.insert(0, './libraries')
from Adafruit_HMC6352 import HMC6352

line = "0.0\n"
gyroPin = 'P9_35'
accelXPin = 'P9_36'
accelYPin = 'P9_38'
accelZPin = 'P9_40'

bmp = BMP085.BMP085()
hmc = HMC6352()

f = open('data.csv', 'w')

def setup():
	ADC.setup()
	f.write("Year; Month; Day; Hours; Minutes; Seconds; Compass; Gyroscope; Accel X; Accel Y; Accel Z; Altitude\n")


def loop():
	global line
	line = ""
	getTime()
	getHeading()
	getGyro()
	getAccel("P9_36")
	getAccel("P9_38")
	getAccel("P9_40")
	getAltitude()
	getTemp()
	print "*"
	f.write(line)

def getTime():
	global line
	now = datetime.now()
	line += str(now.year)+"; "
	line += str(now.month)+"; "
	line += str(now.day)+"; "
	line += str(now.hour)+"; "
	line += str(now.minute)+"; "
	line += str(now.second)+"; "

def getHeading():
	global line
	value = hmc.readData()
	line += str(value)+"; "

def getGyro():
	global line
	value = ADC.read(gyroPin)
	line += str(value)+"; "

def getAccel(axis):
	global line
	zeroOffset = 0.4584
	conversionFactor = 0.0917
	rawRead = ADC.read(axis)
	value = (rawRead - zeroOffset) / conversionFactor
	line += str(value)+"; "

def getAltitude():
	global line
	value = bmp.read_altitude()
	line += str(value)+"; "

def getTemp():
	global line
	value = bmp.read_temperature()
	line += str(value)+"\n"

setup()
while True:
	loop()

f.close()
