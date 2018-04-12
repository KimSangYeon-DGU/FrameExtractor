import cv2
from time import sleep
filename = input('file name: ')
vidcap = cv2.VideoCapture('./Video/'+filename)
success,image = vidcap.read()
count = 0
success = True
while success:
    print('Processing...', end='\r') 
    sleep(0)
    cv2.imwrite('./Frame/frame_{0:08d}.jpg'.format(count), image)     # save frame as JPEG file      
    success,image = vidcap.read()
    count += 1
