from rational import Rational, rat, ratOrInt
from vector import *

class Point:

    def __init__(self, p: tuple):
        if len(p) != 3:
            raise ValueError("point must have 3 components")
        
        self.p = p
    
    def __getitem__(self, n: int):
        "Returns the nth coordinate of a point."
        if not(isinstance(n, int)):
            raise TypeError("coordinate indices must be integers or slices")
        if n >= 3 or n < -3:
            raise KeyError("coordinate index out of range")
        
        return self.p[n]
    
    def __setitem__(self, n: int, value):
        "Sets the nth coordinate of a point to the specified value."
        if not(isinstance(n, int)):
            raise TypeError("coordinate indices must be integers or slices")
        if n >= 3 or n < -3:
            raise KeyError("coordinate index out of range")
        
        self.p[n] = value
    
    # x, y, and z coordinates can be modified during runtime
    # these methods return accurate, up-to-date coordinates
    def x(self):
        return self[0]
    def y(self):
        return self[1]
    def z(self):
        return self[2]
    
    def __iter__(self):
        "Allows iteration through coordinates of a point."
        for i in range(3):
            yield self[i]