from time import time

from file_logger import log_flight_info, log_error_msg

import VL53L0X


## time constants
time_counter_laser = 0
TIME_STEP_LASER = 5

## log key
LASER_LK = 4

## other constants
DISTANCE_SEPARATION = 500 # mm



## initialize sensor obj
SENSOR_I2C_ADDRESS = 0x29
sensor1=VL53L0X.VL53L0X(i2c_bus=1, i2c_address=SENSOR_I2C_ADDRESS)


def get_laser_sensor_distance():

    ## obtain distance
    try:
        distance = sensor1.get_distance()
    except:
        distance = "$"

    return distance


def is_separated():
    try:
        distance = get_laser_sensor_distance()

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
            distance = get_laser_sensor_distance()
        except:
            distance= "$"
            log_error_msg("failed_laser_sensor_reading") 

        time_counter_laser += TIME_STEP_LASER

        if is_separated()== True:
            info_arr = [LASER_LK, distance,"separated", t]
            log_flight_info(info_arr)
        else:
            info_arr = [LASER_LK, distance,"separation_not_confirmed", t]
            log_flight_info(info_arr)

            