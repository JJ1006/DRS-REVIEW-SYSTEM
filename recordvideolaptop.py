import numpy as np
import os
import cv2
import requests
import cv2
import imutils

url = "http://172.20.10.10:8080/shot.jpg"

filename = 'video.avi'
frames_per_second = 24.0
res = '720p'

# Set resolution for the video capture
# Function adapted from https://kirr.co/0l6qmh
def change_res(cap, width, height):
    cap.set(3, width)
    cap.set(4, height)

# Standard Video Dimensions Sizes
STD_DIMENSIONS =  {
    "480p": (640, 480),
    "720p": (1280, 720),
    "1080p": (1920, 1080),
    "4k": (3840, 2160),
}

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))


# grab resolution dimensions and set video capture to it.
def get_dims(cap, res='1080p'):
    width, height = STD_DIMENSIONS["480p"]
    if res in STD_DIMENSIONS:
        width,height = STD_DIMENSIONS[res]
    ## change the current caputre device
    ## to the resulting resolution
    change_res(cap, width, height)
    return width, height

# Video Encoding, might require additional installs
# Types of Codes: http://www.fourcc.org/codecs.php
VIDEO_TYPE = {
    '.avi': cv2.VideoWriter_fourcc(*'XVID'),
    '.mp4': cv2.VideoWriter_fourcc(*'H264')
}

def get_video_type(filename):
    while True:
	    img_resp = requests.get(url)
	    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
	    img = cv2.imdecode(img_arr, -1)
	    combined_window = imutils.resize(img, width=1200, height=1900)
	    cv2.imshow("Android_cam", combined_window)


	# Press Esc key to exit
	    if cv2.waitKey(1) == 27:
		    break

    filename, ext = os.path.splitext(filename)
    if ext in VIDEO_TYPE:
        return  VIDEO_TYPE[ext]
    return VIDEO_TYPE['avi']



cap = cv2.VideoCapture(0)
out = cv2.VideoWriter(filename, get_video_type(filename), 25, get_dims(cap, res))

while True:
    ret, frame = cap.read()
    out.write(frame)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
out.release()
cv2.destroyAllWindows()