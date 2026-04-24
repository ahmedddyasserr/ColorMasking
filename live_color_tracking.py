import numpy as np
import cv2 as cv


live_lower1 = np.array([0, 140, 140])
live_upper1= np.array([10, 255, 255])
live_lower2 = np.array([170, 140, 140])
live_upper2= np.array([180, 255, 255])
#capture through default webcam
webcam=cv.VideoCapture(0)

 

#continous loop until pressing q button 
 
while True:
  _, frame = webcam.read()
  frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
  live_mask1 = cv.inRange(frame_hsv, live_lower1, live_upper1)
  live_mask2 = cv.inRange(frame_hsv, live_lower2, live_upper2)
  live_mask = cv.bitwise_or(live_mask1, live_mask2)

  live_kernel= np.ones((5,5),np.uint8)

  #live_dilation = cv.dilate(live_mask,live_kernel,iterations = 1)
  live_res= cv.bitwise_and(frame,frame, mask= live_mask)

  contours, heirarchy = cv.findContours(live_mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

  for pic , contour in enumerate(contours):
    area= cv.contourArea(contour)
    if(area>300):
      x,y,w,h = cv.boundingRect(contour)
      frame = cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
      cv.putText(frame, "Red", (x, y), cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255))	

  if cv.waitKey(10) & 0xFF == ord('q'):
    webcam.release()
    cv.destroyAllWindows()
    break
  cv.imshow("Live Color Tracking", frame)
   