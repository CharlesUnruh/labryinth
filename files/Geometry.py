import LinAlg as lin

class Circle(object):
    def __init__(self, x, y, Radius):
        self.x = x
        self.y = y
        self.Radius = Radius
        
class Rectangle:
    def __init__(self,right,top,left,bottom):
        self.right=right
        self.top=top
        self.left=left
        self.bottom=bottom

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
