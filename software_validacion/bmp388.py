from time import time
import numpy as np
from file_logger import log_flight_info, log_error_msg





## time constants for each element
time_counter_barometer = 0
TIME_STEP_BAROMETER = 1*60
T1 = 60
T2 = 8000
T3 = 13000

## log key
BAROMETER_LK = 5

def simulated_sensor_reading(t0: float):

    simulation = time() - t0

    if 0 <= simulation < T1:  
        return 1013
    
    elif T1<= simulation < T2:  
        return 900
    
    elif T2 <= simulation < T3:  
        return 20
    
    else:  
        return "$"
    

PRESSURE_11 = 22.65
PRESSURE_25 = 2.488




def get_altitude_from_pressure(t0: float):

    t = time() - t0

    try:
        pressure = simulated_sensor_reading(t0)
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
            altitude = get_altitude_from_pressure(t0)
            pressure = simulated_sensor_reading(t0)
        except:
            altitude = "$"
            pressure = "$"
            log_error_msg("failed_barometer_reading") 

        info_arr = [BAROMETER_LK, altitude, pressure, t]

        log_flight_info(info_arr)

        time_counter_barometer += TIME_STEP_BAROMETER