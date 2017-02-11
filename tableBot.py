# -*- coding: utf-8 -*-
"""
main robot script
"""
import sys
import time
import cv2
import tableBot_move as tb_m
import tableBot_sensors as tb_s
import tableBot_vision as tb_v

try:
    import vrep
except:
    print ('--------------------------------------------------------------')
    print ('"vrep.py" could not be imported. This means very probably that')
    print ('either "vrep.py" or the remoteApi library could not be found.')
    print ('Make sure both are in the same folder as this file,')
    print ('or appropriately adjust the file "vrep.py"')
    print ('--------------------------------------------------------------')
    print ('')
vrep.simxFinish(-1) # just in case, close all opened connections
clientID=vrep.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to V-REP
if clientID!=-1:
    print ('Connected to remote API server')
else:
    print('Connection unsucessful. Exiting program.')
    sys.exit('Exited due to connection failure.')
     
"""
    obtain the handles for the robots motors and sensors
"""
errorCode,handleRightMotor = vrep.simxGetObjectHandle(clientID,'Tablebot_rightMotor',vrep.simx_opmode_blocking)
errorCode,handleRightMotorB = vrep.simxGetObjectHandle(clientID,'Tablebot_rightMotorB',vrep.simx_opmode_blocking)
errorCode,handleLeftMotor = vrep.simxGetObjectHandle(clientID,'Tablebot_leftMotor',vrep.simx_opmode_blocking)
errorCode,handleLeftMotorB = vrep.simxGetObjectHandle(clientID,'Tablebot_leftMotorB',vrep.simx_opmode_blocking)
errorCode,handleProximitySensor = vrep.simxGetObjectHandle(clientID,'Proximity_sensor',vrep.simx_opmode_blocking)
errorCode,handleLeftSensor = vrep.simxGetObjectHandle(clientID,'Left_sensor',vrep.simx_opmode_blocking)
errorCode,handleRightSensor = vrep.simxGetObjectHandle(clientID,'Right_sensor',vrep.simx_opmode_blocking)
errorCode,handleCam = vrep.simxGetObjectHandle(clientID, 'TableBot_cam', vrep.simx_opmode_oneshot_wait)
   
#Initilaize the buffer
errorCode,resolution,image = vrep.simxGetVisionSensorImage(clientID, handleCam, 0, vrep.simx_opmode_streaming)
returnCodeL,detectionStateL,detectedPointL,detectedObjectHandleL,detectedSurfaceNormalVectorL=vrep.simxReadProximitySensor(clientID,handleLeftSensor,vrep.simx_opmode_streaming)   
returnCodeR,detectionStateR,detectedPointR,detectedObjectHandleR,detectedSurfaceNormalVectorR=vrep.simxReadProximitySensor(clientID,handleRightSensor,vrep.simx_opmode_streaming)   
returnCodeF,detectionStateF,detectedPointF,detectedObjectHandleF,detectedSurfaceNormalVectorF=vrep.simxReadProximitySensor(clientID,handleProximitySensor,vrep.simx_opmode_streaming)   
time.sleep(1)


"""
    start the motors and move the robot at the target velocity
"""
targetVelocity = 3
tb_m.go(clientID,handleRightMotor, handleRightMotorB,handleLeftMotor,handleLeftMotorB, targetVelocity, targetVelocity)

while (vrep.simxGetConnectionId(clientID)!=-1):
    #print vrep.simxGetConnectionId(clientID)
    tb_s.checkFrontSensor(clientID,handleRightMotor, handleRightMotorB,handleLeftMotor,handleLeftMotorB, targetVelocity,handleProximitySensor)
    tb_s.checkRightSensor(clientID,handleRightMotor, handleRightMotorB,handleLeftMotor,handleLeftMotorB, targetVelocity,handleRightSensor)
    tb_s.checkLeftSensor(clientID,handleRightMotor, handleRightMotorB,handleLeftMotor,handleLeftMotorB, targetVelocity,handleLeftSensor)
    detected,x = tb_v.seeJunk(clientID,handleCam)
    obstacle,p = tb_v.seeObstacle(clientID,handleCam)
    if(detected):
        tb_m.seek(x,clientID,handleRightMotor,handleLeftMotor)
    elif(obstacle):
        tb_m.avoid(p,clientID,handleRightMotor,handleLeftMotor)
    else:
         tb_m.turn('l', clientID,handleRightMotor, handleRightMotorB,handleLeftMotor,handleLeftMotorB)
    #tb_m.go(clientID,handleRightMotor, handleRightMotorB,handleLeftMotor,handleLeftMotorB, targetVelocity, targetVelocity)

#stop at the end of the simulation
targetVelocity = 0
tb_m.go(clientID,handleRightMotor, handleRightMotorB,handleLeftMotor,handleLeftMotorB, targetVelocity, targetVelocity)
cv2.destroyAllWindows()
vrep.simxFinish(-1) # close all opened connection