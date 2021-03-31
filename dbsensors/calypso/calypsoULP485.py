'''
Databear Sensor Class for Calypso ULP 485
- Streaming sensor

Data Format: NMEA0183
- Example = $IIMWV,013,R,00.0,M,A*12
    -- First data value is direction, second is speed

Settings
- 1 sec measurement output
- 19200 baud
'''

import datetime
from databear.errors import MeasureError, SensorConfigError
from databear.sensors import sensor
import serial
import re

class dbsensor(sensor.Sensor):
    hardware_settings = {
        'serial':'RS485',
        'duplex':'half',
        'resistors':1,
        'bias':1
    }
    measurements = ['direction','speed']
    measurement_description = {
        'direction':'wind direction',
        'speed':'wind speed',
    } 
    units = {
        'direction':'degrees',
        'speed':'m/s'
    }
    min_interval = 1 #sec
    def __init__(self,name,sn,address):
        '''
        Create a new sensor
        '''
        super().__init__(name,sn,address)

        #Set up regular expression to decode stream of data
        self.data_re = re.compile(r'WV,(\d+),R,(\d+.\d),M')
    
    def connect(self,port):
        if not self.connected:
            self.port = port
            self.comm = serial.Serial(self.port,19200,timeout=0.5)
            #self.comm.reset_input_buffer()
            self.connected = True
        
    def measure(self):
        '''
        Read in data from port and parse to measurements
        '''
        dt = datetime.datetime.now()

        #Read in bytes from port
        dbytes = self.comm.in_waiting

        if dbytes > 0:
            rawdata = self.comm.read_until().decode('utf-8') 
            fails = {}

            #Parse measurements
            dataparse = re.findall(self.data_re,rawdata)

            if dataparse:
                #Extract data from match
                self.data['direction'].append((dt,int(dataparse[0][0])))
                self.data['speed'].append((dt,float(dataparse[0][1])))
            else:
                fails['speed'] = 'No data found'
                fails['direction'] = 'No data found'

            if fails:
                raise MeasureError(
                    self.name,
                    list(fails.keys()),
                    fails)