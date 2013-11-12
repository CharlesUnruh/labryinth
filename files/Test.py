import LinAlg as lin
import visual as vis
import numpy as np
R = 1./np.sqrt(2)

scaleMatrix = lin.Matrix3([2,0,0,0,2,0,0,0,1])
rotationMatrix = lin.Matrix3([R,R,0.,-R,R,0.,0.,0.,1.])
shiftMatrix = lin.Matrix3([1.,0.,0.,0.,1.,0.,0.,0.,1.])
a = lin.Vector3(0,0,0)
b = lin.Vector3(2,0,0)
c = lin.Vector3(2,2,0)
d = lin.Vector3(0,2,0)

a2 = rotationMatrix * a
b2 = rotationMatrix * b
c2 = rotationMatrix * c
d2 = rotationMatrix * d

#vis.curve(pos  = [(a.x,a.y,a.z),(b.x,b.y,b.z),(c.x,c.y,c.z),(d.x,d.y,d.z),(a.x,a.y,a.z)])
#vis.curve(pos  = [(a2.x,a2.y,a2.z),(b2.x,b2.y,b2.z),(c2.x,c2.y,c2.z),(d2.x,d2.y,d2.z),(a2.x,a2.y,a2.z)])
num = float(4)

v1 = lin.Vector3(1,2,3)
print v1
print v1.Norm()