from time import time

from file_logger import log_flight_info, log_error_msg




## time constants
time_counter_laser = 0
TIME_STEP_LASER = 5
T1 = 10
T2 = 170*60
T3 = 240*60

## log key
LASER_LK = 4

## other constants
DISTANCE_SEPARATION = 500 # mm

def simulated_sensor_reading(t0: float):

    simulation = time() - t0

    if 0 <= simulation < T1:  
        return "$"
    
    elif T1<= simulation < T2:  
        return 0
    
    elif T2 <= simulation < T3:  
        return 500
    
    else:  
        return 0





def is_separated(t0):
    try:
        distance = simulated_sensor_reading(t0)

        if distance >= DISTANCE_SEPARATION:
            return True
        else:
            return False

    except:
        return "$"


def log_laser_sensor(t0: float):

    global time_counter_laser, TIME_STEP_LASER, LASER_LK

    t = time() - t0

    ## laser sensors data
    if t > time_counter_laser:
        try:
            distance = simulated_sensor_reading(t0)
        except:
            distance= "$"
            log_error_msg("failed_laser_sensor_reading") 

        time_counter_laser += TIME_STEP_LASER

        if is_separated(t0)== True:
            info_arr = [LASER_LK, distance,"separated", t]
            log_flight_info(info_arr)
        else:
            info_arr = [LASER_LK, distance,"separation_not_confirmed", t]
            log_flight_info(info_arr)

            