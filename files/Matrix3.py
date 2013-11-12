from __future__ import division

import numbers
import numpy as np
import Vector3 as v3

class  Matrix3(object):
    def __init__(self, data):
        #data is a list or if the argument is empty Matrix3 creates the identity 
        if data is None:
            #11 is top left 33 is 
            self.m11 = 1.
            self.m12 = 0.
            self.m13 = 0.
            self.m21 = 0.
            self.m22 = 1.
            self.m23 = 0.
            self.m31 = 0.
            self.m32 = 0.
            self.m33 = 1.
        elif isinstance(data, Matrix3):
            self.m11 = data.m11
            self.m12 = data.m12
            self.m13 = data.m13
            self.m21 = data.m21
            self.m22 = data.m22
            self.m23 = data.m23
            self.m31 = data.m31
            self.m32 = data.m32
            self.m33 = data.m33
            
        elif isinstance(data, list):
            self.m11 = data[0]
            self.m12 = data[1]
            self.m13 = data[2]
            self.m21 = data[3]
            self.m22 = data[4]
            self.m23 = data[5]
            self.m31 = data[6]
            self.m32 = data[7]
            self.m33 = data[8]
        else:
            print("INVALID DATA ARG, MUST BE OF TYPE Matrix3, list, None")
    
    def __mul__(self, other):
        #standard matrix multiplication
        #matrix A * B = C returns a matrix
        #overloads *
        newData = [0,0,0,0,0,0,0,0,0]
        if isinstance(other,Matrix3):
            #Matrix3 * Matrix3
            newData[0] = (self.m11 * other.m11 +
                          self.m21 * other.m12 +
                          self.m31 * other.m13 )
            
            newData[1] = (self.m12 * other.m11 +
                          self.m22 * other.m12 +
                          self.m32 * other.m13 )

            newData[2] = (self.m13 * other.m11 +
                          self.m23 * other.m12 +
                          self.m33 * other.m13 )
            
            newData[3] = (self.m11 * other.m21 +
                          self.m21 * other.m22 +
                          self.m31 * other.m23 )

            newData[4] = (self.m12 * other.m21 +
                          self.m22 * other.m22 +
                          self.m32 * other.m23 )
            
            newData[5] = (self.m13 * other.m21 +
                          self.m23 * other.m22 +
                          self.m33 * other.m23 )
            
            newData[6] = (self.m11 * other.m31 +
                          self.m21 * other.m32 +
                          self.m31 * other.m33 )
            
            newData[7] = (self.m12 * other.m31 +
                          self.m22 * other.m32 +
                          self.m32 * other.m33 )
            
            newData[8] = (self.m13 * other.m31 +
                          self.m23 * other.m32 +
                          self.m33 * other.m33 )
            
            return Matrix3(newData)
        elif isinstance(other, v3.Vector3):
            return v3.Vector3(self.m11*other.x + self.m21*other.y + self.m31*other.z,
                           self.m12*other.x + self.m22*other.y + self.m32*other.z,
                           self.m13*other.x + self.m23*other.y + self.m33*other.z)

        elif isinstance(other, numbers.Number):
            return Matrix3([other*self.m11, other*self.m12, other*self.m13,
                    other*self.m21, other*self.m22, other*self.m23,
                    other*self.m31, other*self.m32, other*self.m33])

    def __rmul__(self,other):
        if isinstance(other, numbers.Number):
            return Matrix3([other*self.m11, other*self.m12, other*self.m13,
                    other*self.m21, other*self.m22, other*self.m23,
                    other*self.m31, other*self.m32, other*self.m33])
        else:
            print "Invalid Use of * operator"
            return 0;
    
    def __imul__(self, other):
        #standard matrix multiplication
        #matrix A *= B
        #or A = A * B
        #overloads *=

        if isinstance(other,Matrix3):
            #Matrix3 *= Matrix3
            tempM11 = (self.m11 * other.m11 +
                          self.m21 * other.m12 +
                          self.m31 * other.m13 )
            
            tempM12 = (self.m12 * other.m11 +
                          self.m22 * other.m12 +
                          self.m32 * other.m13 )

            tempM13 = (self.m13 * other.m11 +
                          self.m23 * other.m12 +
                          self.m33 * other.m13 )
            
            tempM21 = (self.m11 * other.m21 +
                          self.m21 * other.m22 +
                          self.m31 * other.m23 )

            tempM22 = (self.m12 * other.m21 +
                          self.m22 * other.m22 +
                          self.m32 * other.m23 )
            
            tempM23 = (self.m13 * other.m21 +
                          self.m23 * other.m22 +
                          self.m33 * other.m23 )
            
            tempM31 = (self.m11 * other.m31 +
                          self.m21 * other.m32 +
                          self.m31 * other.m33 )
            
            tempM32 = (self.m12 * other.m31 +
                          self.m22 * other.m32 +
                          self.m32 * other.m33 )
            
            tempM33 = (self.m13 * other.m31 +
                          self.m23 * other.m32 +
                          self.m33 * other.m33 )
            
            self.m11 = tempM11
            self.m12 = tempM12
            self.m13 = tempM13
            self.m21 = tempM21
            self.m22 = tempM22
            self.m23 = tempM23
            self.m31 = tempM31
            self.m32 = tempM32
            self.m33 = tempM33
            return self
        
        elif isinstance(other, numbers.Number):
            self.m11 *= other 
            self.m12 *= other
            self.m13 *= other
            self.m21 *= other
            self.m22 *= other
            self.m23 *= other
            self.m31 *= other
            self.m32 *= other
            self.m33 *= other
            return self
        
    def __add__(self, other):
        newData = [0,0,0,0,0,0,0,0,0,0]
        if isinstance(other, Matrix3):
            newData[0] = self.m11 + other.m11
            newData[1] = self.m12 + other.m12
            newData[2] = self.m13 + other.m13
            newData[3] = self.m21 + other.m21
            newData[4] = self.m22 + other.m22
            newData[5] = self.m23 + other.m23
            newData[6] = self.m31 + other.m31
            newData[7] = self.m32 + other.m32
            newData[8] = self.m33 + other.m33
            return Matrix3(newData)
        else:
            print "Invalid use of + operator"
            return 0
    
    def __iadd__(self,other):
        if isinstance(other,Matrix3):
            self.m11 += other.m11
            self.m12 += other.m12
            self.m13 += other.m13
            self.m21 += other.m21
            self.m22 += other.m22
            self.m23 += other.m23
            self.m31 += other.m31
            self.m32 += other.m32
            self.m33 += other.m33
            return self
        else:
            print "Invalid use of + operator"
            return 0
    
    def __sub__(self,other):
        newData = [0,0,0,0,0,0,0,0,0,0]
        if isinstance(other, Matrix3):
            newData[0] = self.m11 - other.m11
            newData[1] = self.m12 - other.m12
            newData[2] = self.m13 - other.m13
            newData[3] = self.m21 - other.m21
            newData[4] = self.m22 - other.m22
            newData[5] = self.m23 - other.m23
            newData[6] = self.m31 - other.m31
            newData[7] = self.m32 - other.m32
            newData[8] = self.m33 - other.m33
            return Matrix3(newData)
        else:
            print "Invalid use of - operator"
            return 0
        
    def __isub__(self,other):
        if isinstance(other,Matrix3):
            self.m11 -= other.m11
            self.m12 -= other.m12
            self.m13 -= other.m13
            self.m21 -= other.m21
            self.m22 -= other.m22
            self.m23 -= other.m23
            self.m31 -= other.m31
            self.m32 -= other.m32
            self.m33 -= other.m33
            return self
        else:
            print "Invalid use of - operator"
            return 0        

    def __neg__(self):
        return -1*self;
    
    def __div__(self,other):
        if isinstance(other,numbers.Number):
            return (1./other)*self
        else:
            print"invalid use of / operator"
            return 0
        
    def __idiv__(self,other):
        if isinstance(other,numbers.Number):
            self.m11 /= other 
            self.m12 /= other
            self.m13 /= other
            self.m21 /= other
            self.m22 /= other
            self.m23 /= other
            self.m31 /= other
            self.m32 /= other
            self.m33 /= other
            return self

        else:
            print"invalid use of / operator"
            return 0
                
    def Determinant(self):
        #this calculates the determinant.
        return (self.m11*(self.m22*self.m33 - self.m32*self.m23) -
                self.m21*(self.m12*self.m33 - self.m32*self.m13) +
                self.m31*(self.m12*self.m23 - self.m22*self.m13) ) 
    
    def Transpose(self):
        return Matrix3([self.m11,self.m21,self.m31,
                        self.m12,self.m22,self.m32,
                        self.m13,self.m23,self.m33])
    
    def SetTranspose(self):
        tempM11 = self.m11
        tempM12 = self.m21
        tempM13 = self.m31
        tempM21 = self.m12
        tempM22 = self.m22
        tempM23 = self.m32
        tempM31 = self.m13
        tempM32 = self.m23
        tempM33 = self.m33
        
        self.m11 = tempM11
        self.m12 = tempM12
        self.m13 = tempM13
        self.m21 = tempM21
        self.m22 = tempM22
        self.m23 = tempM23
        self.m31 = tempM31
        self.m32 = tempM32
        self.m33 = tempM33
        return self
    
    def Inverse(self):
        det = self.Determinant()
        if det == 0:
            print "Matrix is not invertable"
            return 0
        else:
            newData = [0,0,0,0,0,0,0,0,0]
            newData[0] = (self.m22*self.m33 - self.m32*self.m23)/det
            newData[1] = (self.m32*self.m13 - self.m12*self.m33)/det
            newData[2] = (self.m12*self.m23 - self.m22*self.m13)/det
            newData[3] = (self.m31*self.m23 - self.m21*self.m33)/det
            newData[4] = (self.m11*self.m33 - self.m31*self.m13)/det
            newData[5] = (self.m21*self.m13 - self.m11*self.m23)/det
            newData[6] = (self.m21*self.m32 - self.m31*self.m22)/det
            newData[7] = (self.m31*self.m12 - self.m11*self.m32)/det
            newData[8] = (self.m11*self.m22 - self.m21*self.m12)/det
            return Matrix3(newData)         
    
    
    def __str__(self):
        return '[{0}, {1}, {2}]\n[{3}, {4}, {5}]\n[{6}, {7}, {8}]'.format(
            self.m11, self.m21, self.m31, self.m12, self.m22, self.m32, self.m13,
            self.m23, self.m33)    


   

