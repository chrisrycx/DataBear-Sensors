'''
An initial script for testing UWSD-1 class
This is for the MDL, as I am having trouble getting it to work in office
'''

from dbsensors.dyacon import dyaconWSD1
import threading

#Create a lock object
testlock = threading.Lock()

#Create sensor
uwsd = dyaconWSD1.dbsensor('wsd',222,1)
uwsd.connect('/dev/ttyMAX3',testlock)

#Measure
uwsd.measure()

print(uwsd)