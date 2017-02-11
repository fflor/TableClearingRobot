# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 21:30:23 2016

@author: fflores
"""
import vrep
import cv2
import numpy as np

def seeJunk(clientID, handleCam):
    detected = False
    x = -1
    #get camera frame, rotate and convert from RGB to BGR
    errorCode, resolution, image=vrep.simxGetVisionSensorImage(clientID, handleCam, 0, vrep.simx_opmode_buffer)
    img = np.array(image, dtype = np.uint8)
    img.resize([resolution[0], resolution[1], 3])
    img = np.rot90(img,2)
    img = np.fliplr(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
	#convert to hsv and detect colors
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    low = np.array([49,50,50], dtype=np.uint8)
    high = np.array([80, 255, 255], dtype=np.uint8)
    mask = cv2.inRange(hsv, low, high)
    #Denoise mask and search for object center
    moments = cv2.moments(mask)
    area = moments['m00']
    if(area > 20):
        x = int(moments['m10']/moments['m00'])
        y = int(moments['m01']/moments['m00'])
        cv2.rectangle(img, (x, y), (x+2, y+2),(0,0,255), 2)
        print(x,y)
        detected = True

    cv2.imshow('Image', img)
    cv2.imshow('Mask', mask)
    esc = cv2.waitKey(5) & 0xFF
    if esc == 27:
        cv2.destroyAllWindows()
    print detected
    return detected, x;

def seeObstacle(clientID, handleCam):
    obstacle = False
    p = -1
    #get camera frame, rotate and convert from RGB to BGR
    errorCode, resolution, image=vrep.simxGetVisionSensorImage(clientID, handleCam, 0, vrep.simx_opmode_buffer)
    img = np.array(image, dtype = np.uint8)
    img.resize([resolution[0], resolution[1], 3])
    img = np.rot90(img,2)
    img = np.fliplr(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
	#convert to hsv and detect colors
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    low = np.array([150,116,105], dtype=np.uint8)
    high = np.array([185, 255, 185], dtype=np.uint8)
    mask = cv2.inRange(hsv, low, high)
    #Denoise mask and search for object center
    moments = cv2.moments(mask)
    area = moments['m00']
    if(area > 20):
        p = int(moments['m10']/moments['m00'])
        y = int(moments['m01']/moments['m00'])
        cv2.rectangle(img, (p, y), (p+2, y+2),(0,0,255), 2)
        print(p,y)
    cv2.imshow('Mask_obs', mask)
    #print obstacle
    return obstacle,p;
"""
"""