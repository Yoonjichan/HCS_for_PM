def posound():
	
	import RPi.GPIO as GPIO
	import time

	buzzer=12

	GPIO.setmode(GPIO.BCM)

	GPIO.setup(buzzer, GPIO.OUT)
	GPIO.setwarnings(False)

	#buzzer
	pwm = GPIO.PWM(buzzer,1)

	#pwm = GPIO.PWM(buzzer,523.2511)
	pwm.start(50.0)
	for cnt in range(0,1):
		pwm.ChangeFrequency(698.4565)
		time.sleep(0.26)
		pwm.ChangeFrequency(523.2511)
		time.sleep(0.26)
		pwm.ChangeFrequency(391.9954)
		time.sleep(0.26)
		pwm.ChangeFrequency(830.6094)
		time.sleep(0.46)

	pwm.ChangeDutyCycle(0.0)


	pwm.stop()
#
