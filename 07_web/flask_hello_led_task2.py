from flask import Flask, render_template
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
    return render_template("ledtask.html")

@app.route("/led/<op>/<color>")
def led_op(op, color):
    if op == "on":
        if color == "red":
            GPIO.output(LED_PIN, GPIO.HIGH)
            return "RED LED ON"
        elif color == "blue":
            GPIO.output(LED_PIN2, GPIO.HIGH)
            return "BLUE LED ON"
        else:
            return "Color Error"
    elif op == "off":
        if color == "red":
            GPIO.output(LED_PIN, GPIO.LOW)
            return "RED LED OFF"
        elif color == "blue":
            GPIO.output(LED_PIN2, GPIO.LOW)
            return "BLUE LED OFF"
        else:
            return "Color Error"
    else:
        return "URL Error"

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()