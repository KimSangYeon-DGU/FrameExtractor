import cv2
from time import sleep
filename = input('File name: ')
ext = input('Extension of file: ')
vCap = cv2.VideoCapture('./Video/'+'{}.{}'.format(filename, ext))

# Extract first frame and status
status, image = vCap.read() 
frameCnt = 0
while status:
    print('Processing...', end='\r') 
    sleep(0)

    # Save frame in target folder
    cv2.imwrite('./Frame/'+filename+'_{0:08d}.jpg'.format(frameCnt), image) 

    # Read next frame at the end
    status, image = vCap.read()
    frameCnt += 1
