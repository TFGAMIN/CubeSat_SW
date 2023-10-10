from time import time

from file_logger import log_flight_info, log_error_msg




## time constants
time_counter_ina = 0
TIME_STEP_INA = 1 #For the moment, don't needed
T1 = 60
T2 = 180*60
T3 = 240*60

## log keys
INA_LK = 1



def simulated_sensor_reading(t0: float):

    simulation = time() - t0

    if 0 <= simulation < T1:  
        return "$", "$", "$"
    
    elif T1 <= simulation < T2:  
        return 0,0,0
    
    elif T2 <= simulation < T3:  
        return 2,5,10
    
    else:  
        return 0,0,0




def log_ina(t0: float):

    global time_counter_ina, TIME_STEP_INA, INA_LK

    t = time() - t0

    ## ina_data
    if t > time_counter_ina:

        t = time() - t0

        try:
            current, voltage, power = simulated_sensor_reading(t0)
        except:
            current, voltage, power = "$", "$", "$"
            log_error_msg("failed_INA260_reading") 


        info_arr = [INA_LK, current, voltage, power, t]

        log_flight_info(info_arr)


