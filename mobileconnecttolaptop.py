# Import essential libraries
import requests
import cv2
import numpy as np
import imutils

# Replace the below URL with your own. Make sure to add "/shot.jpg" at last.
url = "http://172.20.10.10:8080/shot.jpg"

# While loop to continuously fetching data from the Url
while True:
	img_resp = requests.get(url)
	img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
	img = cv2.imdecode(img_arr, -1)
	combined_window = imutils.resize(img, width=1200, height=1900)
	cv2.imshow("Android_cam", combined_window)

	# Press Esc key to exit
	if cv2.waitKey(1) == 27:
		break

cv2.destroyAllWindows()