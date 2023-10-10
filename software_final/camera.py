from time import time
from picamera import PiCamera
from file_logger import log_flight_info, log_error_msg


## time constants
time_counter_image = 0
TIME_STEP_IMAGE= 20*60

time_counter_video = 0
TIME_STEP_VIDEO = 20*60
VIDEO_DURATION = 10

## other constants
image_counter = 0
video_counter = 0

IMAGE_RESOLUTION_H = 1280
IMAGE_RESOLUTION_V = 720

IMAGE_LK = 2
VIDEO_LK = 3


## camera setup
camera = PiCamera()
camera.resolution = (IMAGE_RESOLUTION_H, IMAGE_RESOLUTION_V)


def take_caption(t0: float):

    
    global time_counter_image, TIME_STEP_IMAGE, image_counter

    file_name = "images/img_" + str(image_counter) + ".jpg"
    
    current_time = time() - t0

    if current_time < time_counter_image:
        return

    try:
        camera.capture(file_name)

        log_image(t0)

        time_counter_image += TIME_STEP_IMAGE

        image_counter += 1

    except:
        log_error_msg("failed_camera_caption") 
        return 


def take_video(t0: float):

    
    global time_counter_video, TIME_STEP_VIDEO, video_counter

    file_name = "videos/video_" + str(video_counter) + ".h264"

    current_time = time() - t0
    
    if current_time < time_counter_video:
        return

    try:
        camera.start_recording(file_name)
        camera.wait_recording(VIDEO_DURATION)
        camera.stop_recording()

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
