"""


@author: fflores
"""
import vrep
import time


def go(clientID,Rmotor,RmotorB,Lmotor, LmotorB, rightSpeed, leftSpeed):
        rVelocity = rightSpeed;
        lVelocity = leftSpeed;
        vrep.simxSetJointTargetVelocity(clientID,Rmotor,rVelocity, vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetVelocity(clientID,RmotorB,rVelocity, vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetVelocity(clientID,Lmotor,lVelocity, vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetVelocity(clientID,LmotorB,lVelocity, vrep.simx_opmode_streaming)
        return;
        
def reverse(clientID,Rmotor,RmotorB,Lmotor, LmotorB, sec):
    go(clientID,Rmotor,RmotorB,Lmotor, LmotorB, -1, -1 )
    time.sleep(sec)
    return;
    

def turn(direction,clientID,Rmotor,RmotorB,Lmotor, LmotorB ):
    if direction == 'l':
        print('turning left')
        #reverse(clientID,Rmotor,RmotorB,Lmotor, LmotorB)
        #time.sleep(1)
        rSpeed = 1
        lSpeed = -1
        go(clientID,Rmotor,RmotorB,Lmotor, LmotorB, rSpeed, lSpeed)
        time.sleep(1.8)
        go(clientID,Rmotor,RmotorB,Lmotor, LmotorB,0,0)
    elif direction == 'r':
        print('turning right')
        #reverse(clientID,Rmotor,RmotorB,Lmotor, LmotorB)
        #time.sleep(1)
        rSpeed = -1
        lSpeed = 1
        go(clientID,Rmotor,RmotorB,Lmotor, LmotorB, rSpeed, lSpeed)
        time.sleep(1.)
        go(clientID,Rmotor,RmotorB,Lmotor, LmotorB,0,0)
    else:
        print('invalid direction. should be l or r.')
    return;

def seek(x,clientID,Rmotor,Lmotor):
#if target is centered on screen charge forward
    if abs(x-64/2) < 3:
        go(clientID,Rmotor,Rmotor,Lmotor, Lmotor, 5,5)
#if not realign
    elif x > 64/2:
        vrep.simxSetJointTargetVelocity(clientID, Lmotor,1,vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetVelocity(clientID, Rmotor,-1,vrep.simx_opmode_streaming)
    elif x < 64/2:
        vrep.simxSetJointTargetVelocity(clientID, Lmotor,-1,vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetVelocity(clientID, Rmotor,1,vrep.simx_opmode_streaming)
    return;
def avoid(x,clientID,Rmotor,Lmotor):
#if target is centered on screen charge forward
    if abs(x-64/2) < 12:
        vrep.simxSetJointTargetVelocity(clientID, Lmotor,1,vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetVelocity(clientID, Rmotor,-1,vrep.simx_opmode_streaming)

    return;
