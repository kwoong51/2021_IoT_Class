from flask import Flask, render_template
import Adafruit_DHT
import json

sensor = Adafruit_DHT.DHT11
DHT_PIN = 23

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("dht11.html")

@app.route("/monitor")
def monitoring():
    try:
        h, t = Adafruit_DHT.read_retry(sensor, DHT_PIN)
        print(h,t)
        if h is not None and t is not None:
            data = {'humidity': h, 'temperature': t}
            print(data)
            return json.dumps(data)
        else:
            return 'Read Error'
    except Exception as e:
        print(e)

if __name__ == "__main__":
    app.run(host="0.0.0.0")