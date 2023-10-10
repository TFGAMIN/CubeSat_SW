from time import time

from file_logger import log_flight_info, log_error_msg

import board
import busio
import adafruit_ina260


## time constants
time_counter_ina = 0


## log keys
INA_LK = 1

## initialize i2c
i2c = busio.I2C(board.SCL, board.SDA)

## ina (PAYLOAD) setup 
ina1_adress = 0x40
ina1 = adafruit_ina260.INA260(i2c, i2c_address=ina1_adress)



def get_current_voltage_power_1():
    try:
        return ina1.current, ina1.voltage, ina1.power
    except:
        return "$", "$", "$"




def log_ina(t0: float):

    global time_counter_ina,  INA_LK

    t = time() - t0

    ## ina_data
    if t > time_counter_ina:

        t = time() - t0

        try:
            current, voltage, power = get_current_voltage_power_ina_1()
        except:
            current, voltage, power = "$", "$", "$"
            log_error_msg("failed_INA260_reading") 


        info_arr = [INA_LK, current, voltage, power, t]

        log_flight_info(info_arr)


