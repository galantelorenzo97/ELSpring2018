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

#Initiate ultrasound bursts using 10us pulse
GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)

def logToDatabase(doorState)
	timeStamp = time.time()
	cursor.execute('''INSERT INTO doorLog VALUES(?,?)''', (timeStamp, doorState))
	db.commit()

def getDistance()
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
				logToDatabase("open")
				doorOpen = True
				time.sleep(5)
				continue
		if doorOpen:
			dist = getDistance()
			if dist > 15.0:
				logToDatabase("closed")
				doorOpen = False
				time.sleep(5)
				continue
		time.sleep(5)

#Since the timeStamp is only set when the direction is determined and both sensors are triggered we use that as the condition to write our data:
#		if timeStamp:
#			db.commit()
#			all_rows = cursor.execute('''SELECT * FROM peopleLog''')
#			os.system('clear')
#			for row in all_rows:
#				print('{0} : {1} : {2}'.format(str(row[0]), row[1], str(row[2])))







except db.Error, e:
	print "Error %s:" %e.args[0]
	sys.exit(1)

except KeyboardInterrupt:
GPIO.cleanup()
       db.close()
       print('Clean exit')
