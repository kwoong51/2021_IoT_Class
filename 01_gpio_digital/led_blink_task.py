import RPi.GPIO as GPIO
import time

LED_PIN1=4
LED_PIN2=5
LED_PIN3=6
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)
GPIO.setup(LED_PIN3, GPIO.OUT)

GPIO.output(LED_PIN1, GPIO.HIGH)
print("red led on")
time.sleep(2)
GPIO.output(LED_PIN1, GPIO.LOW)
GPIO.output(LED_PIN2, GPIO.HIGH)
print("yellow led on")
time.sleep(2)
GPIO.output(LED_PIN2, GPIO.LOW)
GPIO.output(LED_PIN3, GPIO.HIGH)
print("green led on")
time.sleep(2)
GPIO.output(LED_PIN3, GPIO.LOW)
GPIO.cleanup()