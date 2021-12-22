import time
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
PIN = 5

try:
    while True:
        h, t =  Adafruit_DHT.read_retry(sensor, PIN)
        if h is not None and t is not None:
            print(f"Temperature={t:.1f}C, Humidity={h:.1f}%")
        else:
            print('Read Error') 
        time.sleep(0.1)

finally:
    print("Bye")