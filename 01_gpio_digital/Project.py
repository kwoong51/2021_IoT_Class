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
LED_PIN2 = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)
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

def display2(number,number2):#7segment  2개의 숫자 출력하는 함수, 1초 대기 또한 포함
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
        print(val)
        if val == 0:    #스위치 누름 여부 확인 눌렀을때 0 누르지 않았을 때 1
            h, t =  Adafruit_DHT.read_retry(sensor, DHT_PIN)
            bull = 0.81 * t +0.01 * h + 46.3 #불쾌지수 계산
            if h is not None and t is not None:
                print(bull)
                if bull > 80: #불쾌지수 80 보다 클 때
                    pwm.ChangeFrequency(523)#음바꾸기
                    pwm.start(70)#피에조 부저 재생
                    GPIO.output(LED_PIN2, GPIO.HIGH)#led켜기
                    display2(math.floor(bull/10),math.floor(bull%10))#불쾌지수값의 소수점을 제외한 만큼의 값을 디스플레이에 출력 , 1초대기후 꺼짐
                    pwm.stop()#피에조 부저 끄기
                    GPIO.output(LED_PIN2, GPIO.LOW)#led끄기
                else: #80 이하일 때
                    pwm.ChangeFrequency(262)#음바꾸기
                    pwm.start(70)#피에조 부저 재생
                    GPIO.output(LED_PIN, GPIO.HIGH)#led켜기
                    display2(math.floor(bull/10),math.floor(bull%10))#불쾌지수값의 소수점 내림한 만큼의 값 디스플레이에 출력 , 1초대기후 꺼짐
                    pwm.stop()#피에조 끄기
                    GPIO.output(LED_PIN, GPIO.LOW)#led끄기
            else:
                print('Read Error')
            
finally:
    pwm.stop
    GPIO.cleanup()
    print('cleanup and exit')