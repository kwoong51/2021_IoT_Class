from lcd import drivers
import datetime
import time
import time
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
PIN = 5

display = drivers.Lcd()

try:
    print('Writing to Display')
    while True:
        now = datetime.datetime.now()
        h, t =  Adafruit_DHT.read_retry(sensor, PIN)
        display.lcd_display_string(now.strftime("%x%X"),1)
        display.lcd_display_string(str(t) + "*C  " + str(h) + "%",2)
        time.sleep(0.5) 

    
finally:
    print("cleaning up")
    display.lcd_clear()