#!/usr/bin.python

import sys, time
import Adafruit_BBIO.ADC as ADC
import Adafruit_BMP.BMP085 as BMP085
from datetime import datetime
sys.path.insert(0, './libraries')
from Adafruit_HMC6352 import HMC6352

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
	getTime()
	getHeading()
	getGyro()
	getAccel("P9_36")
	getAccel("P9_38")
	getAccel("P9_40")
	getAltitude()
	print "."

def getTime():
	now = datetime.now()
	storeData(now.year, "; ")
	storeData(now.month, "; ")
	storeData(now.day, "; ")
	storeData(now.hour, "; ")
	storeData(now.minute, "; ")
	storeData(now.second, "; ")


def getHeading():
	value = hmc.readData()
	storeData(value, "; ")


def getGyro():
	value = ADC.read(gyroPin)
	storeData(value, "; ")

def getAccel(axis):
	zeroOffset = 0.4584
	conversionFactor = 0.0917
	rawRead = ADC.read(axis)
	value = (rawRead - zeroOffset) / conversionFactor
	storeData(value, "; ")

def getAltitude():
	value = bmp.read_altitude()
	storeData(value, "\n")

def storeData(data, chr):
	f.write(str(data)+chr)
setup()
while True:
	loop()

f.close()
