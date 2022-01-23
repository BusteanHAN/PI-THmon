#!/usr/bin/python
import sys
import Adafruit_DHT

from datetime import datetime

today = datetime.now()

humidity, temperature = Adafruit_DHT.read_retry(11, 17)

#print (f'Temp: {temperature} C  Humidity: {humidity} %')
with open(f'{today.strftime("%Y-%m-%d")}.txt', "a") as myfile:
    myfile.write(f'{today.strftime("%H-%M-%S")},{temperature},{humidity}\n')
