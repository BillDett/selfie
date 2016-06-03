import RPi.GPIO as GPIO 
import time            
 
inPin = 2
GPIO.setmode(GPIO.BCM)  
GPIO.setup(inPin, GPIO.IN)
 
while True:              
	value = GPIO.input(inPin)
	if value != GPIO.HIGH:               
		print "PRESS!\n"
	time.sleep(0.2)
 
GPIO.cleanup()            

