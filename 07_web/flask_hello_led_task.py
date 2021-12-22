from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)

LED_PIN = 2
LED_PIN2 = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN2, GPIO.OUT)

@app.route("/")
def hello_world():
    return '''
        <p>Hello, Flask!</p>
        <p><a href="/led/on/red">RED LED ON</a>
        <a href="/led/off/red">RED LED OFF</a></p>
        <p><a href="/led/on/blue">BLUE LED ON</a>
        <a href="/led/off/blue">BLUE LED OFF</a></p>
    '''

@app.route("/led/<op>/<color>")
def led_op(op, color):
    if op == "on":
        if color == "red":
            GPIO.output(LED_PIN, GPIO.HIGH)
            return '''
                <p>RED LED ON</p>
                <a href="/">Go home</a>
            '''
        elif color == "blue":
            GPIO.output(LED_PIN2, GPIO.HIGH)
            return '''
                <p>BLUE LED ON</p>
                <a href="/">Go home</a>
            '''
    elif op == "off":
        if color == "red":
            GPIO.output(LED_PIN, GPIO.LOW)
            return '''
                <p>RED LED OFF</p>
                <a href="/">Go home</a>
            '''
        elif color == "blue":
            GPIO.output(LED_PIN2, GPIO.LOW)
            return '''
                <p>BLUE LED OFF</p>
                <a href="/">Go home</a>
            '''

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()