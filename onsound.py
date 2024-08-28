import RPi.GPIO as GPIO
import time

buzzer=12

GPIO.setmode(GPIO.BCM)

GPIO.setup(buzzer, GPIO.OUT)
GPIO.setwarnings(False)

#buzzer
pwm = GPIO.PWM(buzzer,1)
pwm.start(60.0)
#time.sleep(1.5)

for cnt in range(0,1):
	pwm.ChangeFrequency(1194.508)
	time.sleep(0.3)
	pwm.ChangeFrequency(882.3275)
	time.sleep(0.3)
	pwm.ChangeFrequency(709.9888)
	time.sleep(0.4)
	pwm.ChangeFrequency(550.2540)
	time.sleep(0.15)
	pwm.ChangeFrequency(1194.508)
	time.sleep(0.3)
	pwm.ChangeFrequency(882.3275)
	time.sleep(0.4)

pwm.ChangeDutyCycle(0.0)


pwm.stop()
