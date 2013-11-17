import LinAlg as lin
# import visual as vis
import numpy as np
# theta = np.pi/6
# phi = np.pi/3
#Rx = lin.Matrix3([1,0,0,0,np.cos(theta),-np.sin(theta),0,np.sin(theta),np.cos(theta)])
#Ry = lin.Matrix3([np.cos(phi),0,np.sin(phi),0,1,0,-np.sin(phi),0,np.cos(phi)])
# 
# 
# F = lin.Vector3(0,0,-1)
# 
# print Rx * F
# print Rx * Ry
# print Ry * F

from visual import *
#box = box()
theta = 0
phi = 0
dt = 0.001
f1 = frame()
print f1.up
scene.auroscale = False
ball = sphere(pos = (0,0,0),radius = 0.5, color = color.red, frame = f1)
table = box(pos = (0,0,-1),axis = (1,0,0), length = 30, height = 30, width = 1, material = materials.wood, frame = f1)
#origin = sphere(radius = 0.75, color = color.green)
def keyInput(evt):
    global theta
    global phi
    if evt.key == 'up':
        theta += 0.01
    if evt.key == 'down':
        theta -=0.01
    if evt.key == 'left':
        phi +=0.01
    if evt.key == 'right':
        phi -= 0.01
scene.bind('keydown',keyInput)
frameAxis = lin.Vector3(f1.axis.x, f1.axis.y, f1.axis.z)
frameUp = lin.Vector3(f1.up.x,f1.up.y,f1.up.z)
t = 0
tmax = 10
while (True):
    rate(1e20/dt)
    Rx = lin.Matrix3([1,0,0,0,np.cos(theta),-np.sin(theta),0,np.sin(theta),np.cos(theta)])
    Ry = lin.Matrix3([np.cos(phi),0,np.sin(phi),0,1,0,-np.sin(phi),0,np.cos(phi)])
    R = Rx*Ry * lin.Vector3(0,0,9.8)
    ball.pos.x += R.x * dt
    ball.pos.y += R.y * dt
    newAxis = Rx * Ry * frameAxis
    newUp = Rx * Ry * frameUp
    f1.axis = vector(newAxis.x, newAxis.y, newAxis.z)
    f1.up = vector(newUp.x,newUp.y,newUp.z)
    #print f1.pos
    t+=dt