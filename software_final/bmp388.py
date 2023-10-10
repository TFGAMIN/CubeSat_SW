from time import time
import numpy as np
from file_logger import log_flight_info, log_error_msg
from bmp388 import BMP388

try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

# Initialise the BMP388
bus = SMBus(1)
bmp388 = BMP388(i2c_dev=bus)


## time constants for each element
time_counter_barometer = 0
TIME_STEP_BAROMETER = 1*60

## log key
BAROMETER_LK = 5

## function to get the data from the barometer
def get_pressure():
    try:
        pressure = bmp388.get_pressure()
        return pressure
    except:
        return "$"
    

PRESSURE_11 = 22.65
PRESSURE_25 = 2.488




def get_altitude_from_pressure():

    try:
        pressure = get_pressure()
        #we divide by 10 to go from millibar to kilopascal
        pressure /= 10
 

        if (pressure > PRESSURE_11):
            T = (pressure/101.29)**(0.19026)*288.08 - 273.1
            h = (T - 15.04)/-6.49E-3

        elif ((pressure < PRESSURE_11) and (pressure > PRESSURE_25)):
            T = -56.46
            h = (np.log(pressure/22.65) - 1.73)/-1.57E-4

        else:
            T = (pressure/2.488)**(-0.087812)*216.6 - 273.1
            h = (T + 131.21)/2.99E-3

        #we get the height in meters
        return h
    
    except:
        pressure= "$"
        T= "$"
        h= "$"
        return "$"

def log_barometer(t0: float):

    global time_counter_barometer, TIME_STEP_BAROMETER, BAROMETER_LK

    t = time() - t0

    ## barometer data
    if t > time_counter_barometer:
        
        try:
            altitude = get_altitude_from_pressure()
            pressure = get_pressure()
        except:
            altitude = "$"
            pressure = "$" 
            log_error_msg("failed_barometer_reading") 

        info_arr = [BAROMETER_LK, altitude, pressure, t]

        log_flight_info(info_arr)

        time_counter_barometer += TIME_STEP_BAROMETER