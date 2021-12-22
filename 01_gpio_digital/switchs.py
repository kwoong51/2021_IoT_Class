import RPi.GPIO as GPIO

RED_PIN = 13
SWITCH_RED = 21

YELLOW_PIN = 6
SWITCH_YELLOW = 20

GREEN_PIN = 5
SWITCH_GREEN = 16

GPIO.setmode(GPIO.BCM)

GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(SWITCH_RED, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(YELLOW_PIN, GPIO.OUT)
GPIO.setup(SWITCH_YELLOW, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(SWITCH_GREEN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:

        val_R = GPIO.input(SWITCH_RED)
        val_Y = GPIO.input(SWITCH_YELLOW)
        val_G = GPIO.input(SWITCH_GREEN)

        print(val_R)
        GPIO.output(RED_PIN, val_R)


        print(val_Y)
        GPIO.output(YELLOW_PIN, val_Y) 


        print(val_G)
        GPIO.output(GREEN_PIN, val_G) 

finally:
    GPIO.cleanup()
    print('cleanup and exit')