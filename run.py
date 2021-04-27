from flask import Flask, render_template
import bme680
import kamera
from time import sleep
app = Flask(__name__)

camera = kamera.config()
date, time = kamera.picture(camera)

gas, humidity, pressure, temperature = bme680.get_data()
print(gas)
print(humidity)
print(pressure)
print(temperature)
print(date)
print(time)

# Route zu Funktion in der URL
@app.route("/")
def hallo():
    # können zusätzliche Parameter enthalten
        return render_template("start.html", gas=gas, pressure=pressure, temperature=temperature,
                               humidity=humidity)