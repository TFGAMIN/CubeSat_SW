from time import time
from file_logger import log_flight_info

# constants
time_to_transmit = 180*60
TRANSMISSION_DURATION = 60*60
is_generator_activated = False
transmission_done= False


# log key
GENERATOR_LK = 7



def transmission(t0: float):
    global is_generator_activated, transmission_done

    t = time() - t0

    if not transmission_done:
        if ((t > time_to_transmit) and (is_generator_activated == False)):
            is_generator_activated = True

        elif ((t > (time_to_transmit + TRANSMISSION_DURATION)) and (is_generator_activated == True)):
            is_generator_activated = False
            transmission_done = True
    

    if (is_generator_activated == True):

        info_arr = [GENERATOR_LK , "transmission_activated", t]

        log_flight_info(info_arr)

    else:

        info_arr = [GENERATOR_LK , "transmission_not_activated", t]

        log_flight_info(info_arr)
