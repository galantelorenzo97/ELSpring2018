#Import Libraries we will be using
import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import os
import sqlite3

#Assign GPIO pins
redPin = 27
tempPin = 17
buttonPin = 26

#Temp and Humidity Sensor
tempSensor = Adafruit_DHT.DHT11
#LED Variables--------------------------------------------------------
#Duration of each Blink
blinkDur = .1
#Number of times to Blink the LED
blinkTime = 7
#---------------------------------------------------------------------
#Initialize the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#SQLite setup
db = sqlite3.connect('./log/tempLog.db') #Create DB in RAM
cursor = db.cursor() #Get cursor
#cursor.execute('''CREATE TABLE tempRecord(time TEXT, temperature TEXT)''') 
#Create Temperature table

db.commit() #Commit Changes



def oneBlink(pin):
	GPIO.output(pin,True)
	time.sleep(blinkDur)
	GPIO.output(pin,False)
	time.sleep(blinkDur)

def readF(tempPin):
	humidity, temperature = Adafruit_DHT.read_retry(tempSensor, tempPin)
	temperature = temperature * 9/5.0 +32
	if humidity is not None and temperature is not None:
		tempFahr = '{0:0.1f}*F'.format(temperature)
	else:
		print('Error Reading Sensor')

	return tempFahr

try:

	with open("./log/templog.csv", "a") as log:

		while True:
			#input_state = GPIO.input(buttonPin)
			#if input_state == False:
			for i in range (blinkTime):
				oneBlink(redPin)

			time.sleep(5)
			data = readF(tempPin)
			#print(data)
			log.write("{0},{1}\n".format(time.strftime("%Y-%m-%d %H:%M:%S"),str(data)))
			timeNow = (time.strftime("%Y-%m-%d %H:%M:%S"))
			cursor.execute('''INSERT INTO tempRecord VALUES(?,?)''', (timeNow, str(data)))
			db.commit()
			all_rows = cursor.execute('''SELECT * FROM tempRecord''')
			os.system('clear')
			for row in all_rows:
				print('{0} : {1}'.format(str(row[0]), row[1],))
			#END


except KeyboardInterrupt:
	os.system('clear')
	print('Thanks for Blinking and Thinking!')
	GPIO.cleanup()
	db.close()
