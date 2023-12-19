# this will require the IP webcam app from the playstore/appstore
# once the app is downloaded you will need the IP address given from the app and place it in our code below
import cv2
import numpy as np
url = "Your IP Address/video"
cp = cv2.VideoCapture(url)
while(True):
    camera, frame = cp.read()
    if frame is not None:
        cv2.imshow("Frame", frame)
    if (q := cv2.waitKey(1))==ord("q"):
        break
cv2.destroyAllWindows()
