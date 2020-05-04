import cv2
import time
import datetime
from datetime import timedelta

count = 0

t2=time.time()
cap = cv2.VideoCapture('2017_0505_010019_003.MP4')
cap.set(3,640);
cap.set(4,480);

if not cap.isOpened():
   print("Cam open failed");
   exit()	 	

print("Framing Begun")
try:
   while True:
      date=datetime.datetime.now()+timedelta(seconds=1)
      date=date.strftime("%m_%d_%Y_%H_%M_%S")				
      ret, frame = cap.read()
      if frame.all() == True:
         count += 1
      if count%60:
         filename = 'F:\FLUX\BBox-Label-Tool-master\Images\First\Photo' + '_' + str(count) + '_' + date + '.jpg' # create a folder name Img_Frme manually in the location#
         cv2.imwrite(filename, frame ,[int(cv2.IMWRITE_JPEG_QUALITY), 35])
         count += 1
except KeyboardInterrupt:
        print("Interrupted")
        exit()
        


