from time import time
from file_logger import log_flight_info, log_error_msg


## time constants
time_counter_image = 0
TIME_STEP_IMAGE= 10

time_counter_video = 0
TIME_STEP_VIDEO = 1*60
VIDEO_DURATION = 10

## other constants
image_counter = 0
video_counter = 0


IMAGE_LK = 2
VIDEO_LK = 3


def take_caption(t0: float):

    
    global time_counter_image, TIME_STEP_IMAGE, image_counter
    
    current_time = time() - t0

    if current_time < time_counter_image:
        return

    try:

        log_image(t0)

        time_counter_image += TIME_STEP_IMAGE

        image_counter += 1

    except:
        log_error_msg("failed_camera_caption") 
        return 


def take_video(t0: float):

    
    global time_counter_video, TIME_STEP_VIDEO, video_counter

    current_time = time() - t0
    
    if current_time < time_counter_video:
        return

    try:
        log_video(t0)

        time_counter_video+= TIME_STEP_VIDEO

        video_counter += 1

    except:
        log_error_msg("failed_camera_video") 
        return 

def log_image(t0: float):

    t = time() - t0

    info_arr = [IMAGE_LK, "caption", t]

    log_flight_info(info_arr)



def log_video(t0: float):

    t = time() - t0

    info_arr = [VIDEO_LK, "video", t]

    log_flight_info(info_arr)
