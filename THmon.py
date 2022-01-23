#!/usr/bin/python
import sys
import Adafruit_DHT
from datetime import datetime

humidity, temperature = Adafruit_DHT.read_retry(11, 17)
with open(f'/home/pi/PI-THmon/{datetime.now().strftime("%Y-%m-%d")}.txt', "a") as myfile:
    myfile.write(f'{datetime.now().strftime("%H-%M-%S")},{temperature},{humidity}\n')
