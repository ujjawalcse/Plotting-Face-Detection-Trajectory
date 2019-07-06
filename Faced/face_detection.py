import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
import time
from imutils.video import VideoStream
from imutils.video import FPS
from faced.detector import FaceDetector
from faced.utils import annotate_image
from datetime import datetime
face_detector = FaceDetector()

#-----------In Below code lines we are evaluating trajectory of face and noting x_centre and y_centre with respect to time
#-----------Here our frame rate is 30 frames/second so each frame is taking 1/30 second....This gives us an array like 0,1/30,2/30,3/30...........

print("----starting video stream-----")
vs=cv2.VideoCapture('input\\video1.mp4')
time.sleep(2.0)
thresh=0.5
x=[]
y=[]
t=[]
while(True):
	grabbed,frame=vs.read()
	if grabbed:
		rgb_img = cv2.cvtColor(frame.copy(), cv2.COLOR_BGR2RGB)
	else:
		break
	# Receives RGB numpy image (HxWxC) and
	# returns (x_center, y_center, width, height, prob) tuples. 
	bboxes = face_detector.predict(rgb_img, thresh)
	bboxes_list=list(bboxes)
	x.append(bboxes_list[0][0])
	y.append(bboxes_list[0][1])

	# Use this utils function to annotate the image.
	#ann_img = annotate_image(frame, bboxes)

	# Show the image
	#cv2.imshow("Frame",frame)
	key=cv2.waitKey(1) & 0xFF
	if key==ord("q"):
		cv2.destroyAllWindows()
		vs.stop()
		break

print(len(x))
print(len(y))
for i in range(len(x)):
	t.append(i/30)

print(len(t))

#-----------##In Below code lines we are plotting two graph-> first is x_centre vs time and second one is y_centre vs time
#-----------##These code lines are commented because we have saved the graph while running first time  

#plt.subplot(2,1,1)
#plt.plot(t, x, color='green', linestyle='dashed', linewidth = 1, marker='o', markerfacecolor='blue', markersize=3)
#plt.title('x_centre vs time')
#plt.subplot(2,1,2)
#plt.plot(t, y, color='red', linestyle='dashed', linewidth = 1, marker='o', markerfacecolor='blue', markersize=3)
#plt.title('y_centre vs time')
#plt.show()

######################################################################################################################
# ----------In Below code lines we moved a random face on the evaluated x and y and showing that face how it is moving with respect to time----------------- 
fourcc = cv2.VideoWriter_fourcc(*'MJPG') 
out = cv2.VideoWriter('output\\video1.avi', fourcc, 20.0, (1080, 1920))
img=cv2.imread('input\\human_face.jpg')
res_img=cv2.resize(img,(100,100))
img_data=[]
for i in range(len(x)):
	empty_img=np.full((1080,1920,3), 255, dtype=np.uint8)
	h,w,c = res_img.shape
	added_img=cv2.addWeighted(empty_img[int(y[i]-(h/2)):int(y[i]+(h/2)), int(x[i]-(w/2)):int(x[i]+(w/2))],0.9,res_img,0.1,0)
	empty_img[int(y[i]-(h/2)):int(y[i]+(h/2)), int(x[i]-(w/2)):int(x[i]+(w/2))] = added_img
	out.write(empty_img)
	cv2.imshow("Frame",empty_img)
	key=cv2.waitKey(1) & 0xFF
	if key==ord("q"):
		cv2.destroyAllWindows()
		vs.stop()
		break

    
out.release()





