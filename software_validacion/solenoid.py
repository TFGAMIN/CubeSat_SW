from time import time
from file_logger import log_flight_info


# constants and variables
time_to_deploy = 170*60
DEPLOY_PULSE_DURATION = 2
is_solenoid_activated = False
TIME_TO_CHECK_SEPARATION = 5*60

# log key
MECHANISM_LK = 6



def deploy(t0: float):
    global time_to_deploy, DEPLOY_PULSE_DURATION, is_solenoid_activated, TIME_TO_CHECK_SEPARATION

    t = time() - t0

    if ((t > time_to_deploy) and (is_solenoid_activated == False)):

        is_solenoid_activated = True

    elif ((t > (time_to_deploy + DEPLOY_PULSE_DURATION)) and (is_solenoid_activated == True)):

        is_solenoid_activated = False
        time_to_deploy = t + TIME_TO_CHECK_SEPARATION

    if (is_solenoid_activated == True):

        info_arr = [MECHANISM_LK, "solenoid_activated", t]

        log_flight_info(info_arr)

    else:

        info_arr = [MECHANISM_LK, "solenoid_not_activated", t]

        log_flight_info(info_arr)
