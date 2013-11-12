import numbers
import Matrix3 as m3
import numpy as np

class Vector3(object):
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        
    def __add__(self,other):
        if isinstance(other,Vector3):
            return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            print"invalid use of + operator" 

    def __iadd__(self,other):
        if isinstance(other,Vector3):
            self.x += other.x
            self.y += other.y
            self.z += other.z
            return self
        else:
            print "invalid use of + operator"
            return 0
        
    def __mul__(self,other):
        if isinstance(other, numbers.Number):
            return Vector3(self.x * other, self.y * other, self.z * other)
        else:
            print "invalid use of * operator"
            return 0
    
    def __imul__(self,other):
        if isinstance(other, numbers.Number):
            self.x *= other
            self.y *= other
            self.z *= other
            return self
        else:
            print "invalid use of * operator"
    
    def __rmul__(self,other):
        if isinstance(other, m3.Matrix3):
            return Vector3(other.m11*self.x + other.m21*self.y + other.m31*self.z,
                           other.m12*self.x + other.m22*self.y + other.m32*self.z,
                           other.m13*self.x + other.m23*self.y + other.m33*self.z)
        
        elif isinstance(other, numbers.Number):
            return Vector3(self.x * other, self.y * other, self.z * other)
        else:
            print"invalid use of * operator"
            return 0;
    def __div__(self,other):
        if isinstance(other,numbers.Number):
            return Vector3(self.x/other, self.y/other, self.z/other)
        else:
            print "invalid use of / operator"
            
    def __idiv__(self,other):
        if isinstance(other,numbers.Number):
            self.x /= other
            self.y /= other
            self.z /= other
            return self
        else:
            print "invalid use of / operator"
            return 0
        
    def __sub__(self, other):
        if isinstance(other, Vector3):
            return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            print "invalid use of the - operator"
            return 0
        
    def __isub__(self,other):
        if isinstance(other, Vector3):
            self.x -= other.x
            self.y -= other.y
            self.z -= other.z
            return self
        else:
            print "invalid use of - operator"
            return 0
        
    def __neg__(self):
        return -1.*self
    
    def __str__(self):
        return '[{0}, {1}, {2}]'.format(self.x, self.y, self.z)

    def Mag(self):
        return np.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
    
    def Norm(self):
        mag = self.Mag()
        return Vector3(self.x/mag, self.y/mag, self.z/mag)
