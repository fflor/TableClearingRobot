# -*- coding: utf-8 -*-
"""


@author: fflores
"""


"""
define sensor functions for threads to use
"""
import vrep

import tableBot_move


def checkFrontSensor(clientID,handleRightMotor, handleRightMotorB,handleLeftMotor,handleLeftMotorB, targetVelocity,handleProximitySensor):
#while (vrep.simxGetConnectionId(clientID)!=-1):
    returnCodeF,detectionStateF,detectedPointF,detectedObjectHandleF,detectedSurfaceNormalVectorF=vrep.simxReadProximitySensor(clientID,handleProximitySensor,vrep.simx_opmode_streaming)   
    if detectionStateF == False:
        while detectionStateF == False and vrep.simxGetConnectionId(clientID)!=-1:
            #back up
            print "detectionStateF ", detectionStateF, " backing up"
            tableBot_move.reverse(clientID,handleRightMotor, handleRightMotorB,handleLeftMotor,handleLeftMotorB,2)
            returnCodeF,detectionStateF,detectedPointF,detectedObjectHandleF,detectedSurfaceNormalVectorF=vrep.simxReadProximitySensor(clientID,handleProximitySensor,vrep.simx_opmode_buffer)
            print "detectionStateF ", detectionStateF, " beep"
            #turn left
        tableBot_move.turn('l', clientID,handleRightMotor, handleRightMotorB,handleLeftMotor,handleLeftMotorB)
        tableBot_move.go(clientID,handleRightMotor, handleRightMotorB,handleLeftMotor,handleLeftMotorB, targetVelocity, targetVelocity)
    return;
    
def checkRightSensor(clientID,handleRightMotor, handleRightMotorB,handleLeftMotor,handleLeftMotorB, targetVelocity,handleRightSensor):
# while (vrep.simxGetConnectionId(clientID)!=-1):
    returnCodeR,detectionStateR,detectedPointR,detectedObjectHandleR,detectedSurfaceNormalVectorR=vrep.simxReadProximitySensor(clientID,handleRightSensor,vrep.simx_opmode_streaming)   
#if detectionStateR == False:
    while detectionStateR == False and vrep.simxGetConnectionId(clientID)!=-1:
        #back up
        tableBot_move.reverse(clientID, handleRightMotor, handleRightMotorB, handleLeftMotor, handleLeftMotorB, 1)
        #turn left
        print 'detectionStateR: ', detectionStateR
        tableBot_move.turn('l', clientID,handleRightMotor, handleRightMotorB,handleLeftMotor,handleLeftMotorB)
        tableBot_move.go(clientID,handleRightMotor, handleRightMotorB,handleLeftMotor,handleLeftMotorB, targetVelocity, targetVelocity)
        returnCodeR,detectionStateR,detectedPointR,detectedObjectHandleR,detectedSurfaceNormalVectorR=vrep.simxReadProximitySensor(clientID,handleRightSensor,vrep.simx_opmode_buffer)
    print 'detectionStateR: ', detectionStateR
    return;
    
def checkLeftSensor(clientID,handleRightMotor, handleRightMotorB,handleLeftMotor,handleLeftMotorB, targetVelocity,handleLeftSensor):
#while (vrep.simxGetConnectionId(clientID)!=-1):
    returnCodeL,detectionStateL,detectedPointL,detectedObjectHandleL,detectedSurfaceNormalVectorL=vrep.simxReadProximitySensor(clientID,handleLeftSensor,vrep.simx_opmode_streaming)   
         #if detectionStateL == False:
    while detectionStateL == False and vrep.simxGetConnectionId(clientID)!=-1:
        #backup
        tableBot_move.reverse(clientID, handleRightMotor, handleRightMotorB, handleLeftMotor, handleLeftMotorB, 1)

                 #turn right
        print 'detectionStateL: ', detectionStateL
        tableBot_move.turn('r', clientID,handleRightMotor, handleRightMotorB,handleLeftMotor,handleLeftMotorB)
        tableBot_move.go(clientID,handleRightMotor, handleRightMotorB,handleLeftMotor,handleLeftMotorB, targetVelocity, targetVelocity)
        returnCodeL,detectionStateL,detectedPointL,detectedObjectHandleL,detectedSurfaceNormalVectorL=vrep.simxReadProximitySensor(clientID,handleLeftSensor,vrep.simx_opmode_buffer)
    print 'detectionStateL: ', detectionStateL
    return;