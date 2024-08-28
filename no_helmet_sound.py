def nhs():
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
	for cnt in range(0,2):
		pwm.ChangeFrequency(659.2551)
		time.sleep(0.4)
		pwm.ChangeFrequency(440)
		time.sleep(0.4)

	pwm.ChangeDutyCycle(0.0)


	pwm.stop()
#
