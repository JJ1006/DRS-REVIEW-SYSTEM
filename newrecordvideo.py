import cv2
import numpy as np
import requests
import imutils

# This will return video from the first webcam on your computer.
url = "http://26.68.128.52:8080/shot.jpg"

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640,480))

# loop runs if capturing has been initialized.
while(True):
	img_resp = requests.get(url)
	img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
	img = cv2.imdecode(img_arr, -1)
	combined_window = imutils.resize(img, width=1200, height=1900)
	out.write(img_arr)
	cv2.imshow("Android_cam", combined_window)
	
	# Wait for 'a' key to stop the program
	if cv2.waitKey(1) & 0xFF == ord('a'):
		break

# Close the window / Release webcam
url.release()

# After we release our webcam, we also release the output
out.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()