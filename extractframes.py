import cv2
from time import sleep

cap = cv2.VideoCapture('video.mp4')
count = 0

ret, frame = cap.read()
while(ret):
    cv2.imwrite(f'frames/frame_{count}.png', frame) 
    count += 1
    ret, frame = cap.read()

cap.release()

