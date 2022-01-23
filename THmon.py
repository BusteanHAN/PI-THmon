#!/usr/bin/python
import sys
import Adafruit_DHT

from datetime import datetime

humidity, temperature = Adafruit_DHT.read_retry(11, 17)

#print (f'Temp: {temperature} C  Humidity: {humidity} %')
with open(f"{datetime.now().today()}.txt", "a") as myfile:
    myfile.write(f'{datetime.now.time()}{temperature},{humidity}\n')
