import visual
import "RectangleClass"
class collidableBox:
    def __init__(self, pos=visual.vector(0,0,0), frame=None, length=1, width=1,
                    height = 1):
        self.geometry = visual.box(pos=pos, length=length, width=width, 
                                    height=height, frame=frame)
        self.collision = visual.shapes.rectangle(pos=pos, width=width,
                                    height=height, frame=frame)
