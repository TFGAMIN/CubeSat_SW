from time import time, sleep
from ina260 import log_ina
from bmp388 import log_barometer
from laser_sensor import log_laser_sensor
from camera import take_caption, take_video
from solenoid import deploy
from signal_generator import transmission


## get initial time
t0 = time()
tstep = 5

while True:

    log_ina(t0)
    
    take_caption(t0)

    take_video(t0)

    log_laser_sensor(t0)

    log_barometer(t0)

    deploy(t0)
    
    transmission(t0)
    
    sleep(tstep)