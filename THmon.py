#!/usr/bin/python
import sys
import Adafruit_DHT

from datetime import date

humidity, temperature = Adafruit_DHT.read_retry(11, 17)

#print (f'Temp: {temperature} C  Humidity: {humidity} %')
with open(f"{date.today()}.txt", "a") as myfile:
    myfile.write(f'{temperature},{humidity}')
