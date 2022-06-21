# Importing all necessary libraries
import cv2
import os
from PIL import Image   
# Read the video from specified path

#Enter the path to your video here
cam = cv2.VideoCapture("./data/TestVideo.mp4")
  
try:
      
    # creating a folder named Frames
    if not os.path.exists('Frames'):
        os.makedirs('Frames')
  
# if not created then raise error
except OSError:
    print ('Error: Creating directory of data')
  
# frame
currentframe = 0
  
while(True):
      
    # reading from frame
    ret,frame = cam.read()
  
    if ret:
        # if video is still left continue creating images
        name = './Frames/frame' + str(currentframe) + '.jpg'
        print ('Creating...' + name)
  
        # writing the extracted images
        cv2.imwrite(name, frame)
  
        # increasing counter so that it will
        # show how many frames are created
        currentframe += 1
    else:
        break
  
# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()