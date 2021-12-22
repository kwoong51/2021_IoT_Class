import RPi.GPIO as GPIO
import Adafruit_DHT
import math
import time

SWITCH_PIN=2
LED_PIN = 4
SEGMENT_PINS = [6,7,8,9,10,11,12]
SEGMENT_PINS2 = [13,14,15,16,17,18,19]
BUZZER_PIN = 3
sensor = Adafruit_DHT.DHT11
DHT_PIN = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN, 1)

for segment in SEGMENT_PINS:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, GPIO.LOW)

for segment in SEGMENT_PINS2:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, GPIO.LOW)


data = [[1, 1, 1, 1, 1, 1, 0],  # 0
        [0, 1, 1, 0, 0, 0, 0],  # 1
        [1, 1, 0, 1, 1, 0, 1],  # 2
        [1, 1, 1, 1, 0, 0, 1],  # 3
        [0, 1, 1, 0, 0, 1, 1],  # 4
        [1, 0, 1, 1, 0, 1, 1],  # 5
        [1, 0, 1, 1, 1, 1, 1],  # 6
        [1, 1, 1, 0, 0, 0, 0],  # 7
        [1, 1, 1, 1, 1, 1, 1],  # 8
        [1, 1, 1, 0, 0, 1, 1]]  # 9

def display2(number,number2):
    for i in range(7):
        GPIO.output(SEGMENT_PINS2[i],data[number2][i])
        GPIO.output(SEGMENT_PINS[i],data[number][i])
        
        

    time.sleep(1)

    for i in range(7):
        GPIO.output(SEGMENT_PINS2[i], GPIO.LOW)
        GPIO.output(SEGMENT_PINS[i], GPIO.LOW)
        
try:
    while True:
        val = GPIO.input(SWITCH_PIN)
        if val == 0:
            h, t =  Adafruit_DHT.read_retry(sensor, DHT_PIN)
            bull = 0.81 * t +0.01 * h + 46.3
            if h is not None and t is not None:
                print(bull)
                if bull > 80:
                    pwm.start(30)
                    display2(math.floor(bull/10),math.floor(bull%10))
                    pwm.stop()
                else:
                    GPIO.output(LED_PIN, GPIO.HIGH)
                    display2(math.floor(bull/10),math.floor(bull%10))
                    GPIO.output(LED_PIN, GPIO.LOW)
            else:
                print('Read Error') 
            
finally:
    GPIO.cleanup()
    print('cleanup and exit')