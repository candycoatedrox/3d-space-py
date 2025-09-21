from rational import Rational, rat, ratOrInt
from vector import *
from point import *

class Line:

    def __init__(self, P: Point, v: Vector):
        # must be in 3d space
        if len(P) != 3:
            raise ValueError("base point must have 3 components")
        if len(v) != 3:
            raise ValueError("direction vector must have dimension 3")
        
        # base point and components
        self.P = P
        self.x0 = P.x()
        self.y0 = P.y()
        self.z0 = P.z()

        # direction vector and components
        self.v = v
        self.a = v[0]
        self.b = v[1]
        self.c = v[2]