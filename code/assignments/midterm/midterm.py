#!/usr/bin/python

#Import Libraries we will be using
import RPi.GPIO as GPIO
import time
import os
import sqlite3
import sys

#Assign GPIO pins
TRIG = 23
ECHO = 24

#Set door distance
OpenMaximumDist = 15
#Set Initial Door Sate
doorOpen = False
#---------------------------------------------------------------------
#Initialize the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

#SQLite setup
db = sqlite3.connect('./doorLog/doorLog.db')
cursor = db.cursor() #Get cursor
db.commit() #Commit Changes

#Stabilize sensor
GPIO.output(TRIG, False)
print "Stabilizing..."
time.sleep(3)
print "Sensor stabilized!"

def logToDatabase(doorState):
	timeStamp = (time.strftime("%Y-%m-%d %H:%M:%S"))
	cursor.execute('''INSERT INTO doorLog VALUES(?,?)''', (timeStamp, doorState))
	db.commit()

def getDistance():
	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)

	while GPIO.input(ECHO)==0:
		pulse_start = time.time()

	while GPIO.input(ECHO)==1:
		pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start
	distance = pulse_duration * 17150
	distance = round(distance, 2)
	return distance


try:
	while True:
     		if not doorOpen:
			dist = getDistance()
			if dist < 15.0:
				print("Door opened")
				logToDatabase("open")
				doorOpen = True
				time.sleep(5)
				continue
		if doorOpen:
			dist = getDistance()
			if dist > 15.0:
				print("Door closed")
				logToDatabase("closed")
				doorOpen = False
				time.sleep(5)
				continue
		time.sleep(5)

except db.Error, e:
	print "Error %s:" %e.args[0]
	sys.exit(1)

except KeyboardInterrupt:
	GPIO.cleanup()
	db.close()
	print('Clean exit')

