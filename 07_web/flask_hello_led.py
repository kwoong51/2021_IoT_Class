from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)

LED_PIN = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

@app.route("/")
def hello_world():
    return '''
        <p>Hello, Flask!</p>
        <a href="/led/on">LED ON</a>
        <a href="/led/off">LED OFF</a>
    '''

@app.route("/led/<op>")
def led_op(op):
    print(op)
    if op == "on":
        GPIO.output(LED_PIN, GPIO.HIGH)
        return '''
            <p>LED ON</p>
            <a href="/">Go home</a>
        '''
    elif op == "off":
        GPIO.output(LED_PIN, GPIO.LOW)
        return '''
            <p>LED OFF</p>
            <a href="/">Go home</a>
        '''

if __name__ == "__main__":
    app.run(host="0.0.0.0")