'''
An initial script for testing Calypso ULP485 class
'''

from dbsensors.calypso import calypsoULP485
import time

#Create sensor
sensor = calypsoULP485.dbsensor('test', 1, 0)
sensor.connect('COM23')

#Measure
sensor.measure()
print(sensor)
time.sleep(1)
sensor.measure()
print(sensor)
time.sleep(1)
sensor.measure()
print(sensor)
time.sleep(1)

#Shutdown
sensor.comm.close()

