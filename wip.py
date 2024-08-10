import cv2 as cv
import json
import time

def load_settings(stream_object):
    with open('./config.json', 'r') as f:
        data = json.load(f)

    # loop settings entries
    stream_object.set(getattr(cv, 'CAP_PROP_AUTO_EXPOSURE'), 3)
    time.sleep(1)
    for prop, value in data.items():
        stream_object.set(getattr(cv, prop), float(value)) # getattr to retrieve constant int keys from cv
        print(str(prop) + ': ' + str(value))
        time.sleep(1)

def main(cam_index):
    # Detect video backend
    backendCheckStream = cv.VideoCapture(cam_index)
    videoBackendString = backendCheckStream.getBackendName()
    backendCheckStream.release()
    match videoBackendString:
        case 'AVFOUNDATION': videoBackendKey = cv.CAP_AVFOUNDATION
        case 'V4L2': videoBackendKey = cv.CAP_V4L2
        case _:
            videoBackendKey = cv.CAP_ANY   # ! if this happens then yikes, our settings won't get applied i think
            raise KeyError('Could not match video api key for {}'.format(videoBackendString))
    
    # Setup and warm up cameras
    stream = cv.VideoCapture(index=cam_index, apiPreference=videoBackendKey)
    time.sleep(1.5)
    load_settings(stream)
    
    while True:
        ret, img = stream.read()
        cv.imshow("input", img)

        key = cv.waitKey(1)
        if key == ord('r'):
            load_settings(stream)
        if key == ord('q'):
            break

main(0)