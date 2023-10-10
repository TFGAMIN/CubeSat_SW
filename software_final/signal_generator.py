import RPi.GPIO as GPIO
from time import time
from file_logger import log_flight_info


# constants
time_to_transmit = 180*60
TRANSMISSION_DURATION = 60*60
is_generator_activated = False
transmission_done= False

# log key
GENERATOR_LK = 7


# setup
PIN_GENERATOR = 25
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_GENERATOR, GPIO.OUT)
GPIO.output(PIN_GENERATOR, GPIO.LOW)


def activate_generator():
    GPIO.output(PIN_GENERATOR, True)


def deactivate_generator():
    GPIO.output(PIN_GENERATOR, False)


def transmission(t0: float):

    t = time() - t0

    if ((t > time_to_transmit) and (is_generator_activated == False)):

        activate_generator()
        is_generator_activated = True

    elif ((t > (time_to_transmit + TRANSMISSION_DURATION)) and (is_generator_activated == True)):

        deactivate_generator()
        is_generator_activated = False
    

    if (is_generator_activated == True):

        info_arr = [GENERATOR_LK , "transmission_activated", t]

        log_flight_info(info_arr)

    else:

        info_arr = [GENERATOR_LK , "transmission_not_activated", t]

        log_flight_info(info_arr)
