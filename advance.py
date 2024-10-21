# this contains the minimum code required for hand tracking
import cv2 as cv
import mediapipe as mp
import time  # to chk the frame rate

cap=cv.VideoCapture(0)
hand=mp.solutions.hands
hands=hand.Hands()
draw=mp.solutions.drawing_utils # object use to draw points/line on hand

ptime=0
ctime=0

while(True):
    success,img=cap.read()
    imgrgb=cv.cvtColor(img,cv.COLOR_BGR2RGB) #bcz hands uses only rgb images
    res=hands.process(imgrgb)

    # extracting information from res
    #print(res.multi_hand_landmarks) # this will display some data if hand is there otherwise None
    if res.multi_hand_landmarks:
        # using for loop bcx if multiple hands are present then etract them one by one
        for han in res.multi_hand_landmarks: 
            draw.draw_landmarks(img,han,hand.HAND_CONNECTIONS) # to draw points do not use last parameter
            # to draw lines use last parameter
    # to calculate time and fps
    ctime=time.time()
    fps=1/(ctime-ptime)
    ptime=ctime
    # to display it on screen
    cv.putText(img,str(int(fps)),(10,70),cv.FONT_HERSHEY_COMPLEX,3,(255,0,255),2)
    
    cv.imshow('Frame',img)
    if(cv.waitKey(1) & 0xFF==ord('q')):
        break