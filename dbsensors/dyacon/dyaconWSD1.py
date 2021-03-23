'''
DataBear Sensor Class: Dyacon WSD-1 Sensor
'''

import datetime
import minimalmodbus as mm
from databear.errors import MeasureError, SensorConfigError
from databear.sensors import sensor

class dbsensor(sensor.BusSensor):
    hardware_settings = {
        'serial':'RS485',
        'duplex':'half',
        'resistors':1,
        'bias':1
    }
    measurements = [
        'speed',
        'speed_2min',
        'speed_10min',
        'direction',
        'direction_2min',
        'direction_10min',
        'gust',
        'gust_direction'
    ]
    units = {
        'speed':'m/s',
        'speed_2min':'m/s',
        'speed_10min':'m/s',
        'direction':'degrees',
        'direction_2min':'degrees',
        'direction_10min':'degrees',
        'gust':'m/s',
        'gust_direction':'degrees'
    }
    min_interval = 1  #Minimum interval that sensor can be polled
    uses_portlock = True
    registers = {
        'speed':201,
        'speed_2min':203,
        'speed_10min':205,
        'direction':202,
        'direction_2min':204,
        'direction_10min':206,
        'gust':207,
        'gust_direction':208
    }
    def connect(self,port,portlock):
        '''
        Create minimal modbus connection
        '''
        self.portlock=portlock
        if not self.connected:
            self.port = port
            self.comm = mm.Instrument(self.port,self.address)
            self.comm.serial.timeout = 0.3
            self.connected = True
    
    def readMeasure(self,starttime):
        '''
        Read in data using modbus
        '''
        fails = {} #keep track of measurement failures
        for measure in self.measurements:
            
            try:
                val = self.comm.read_register(self.registers[measure])
                val = val/10
                self.data[measure].append((starttime,val))

            except mm.NoResponseError as norsp:
                fails[measure] = 'No response from sensor'

            except:
                raise
                
        #Raise a measurement error if a fail is detected
        if len(fails)>0:
            failnames = list(fails.keys())
            raise MeasureError(self.name,failnames,fails)
    

    

    
