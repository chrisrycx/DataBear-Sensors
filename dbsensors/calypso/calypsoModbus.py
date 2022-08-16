'''
Testing Calypso Modbus functionality
- Should work the same as WSD-1
'''

import minimalmodbus as mm

uwsd = mm.Instrument('COM11',1, debug=True)
#uwsd.close_port_after_each_call = True  #This didn't make a difference

test = uwsd.read_registers(201,2)

print(test)