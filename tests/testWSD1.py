'''
An initial script for testing WSD1 class
'''

from dbsensors.dyacon import dyaconWSD1
import threading

#Create a lock object
testlock = threading.Lock()

#Create sensor
wsd = dyaconWSD1.dyaconWSD1('wsd',222,1)
wsd.connect('COM23',testlock)

#Measure
wsd.measure()

print(wsd)