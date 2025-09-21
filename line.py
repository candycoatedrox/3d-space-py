from point import *

class Line:

    def __init__(self, p: Point, v: Vector):
        # must be in 3d space
        if len(p) != 3:
            raise ValueError("base point must have 3 components")
        if len(v) != 3:
            raise ValueError("direction vector must have dimension 3")
        
        self.p = p
        self.v = v
    
    # p and v can be modified during runtime
    # these methods return accurate, up-to-date coordinates/components
    def x0(self):
        return self.p[0]
    def y0(self):
        return self.p[1]
    def z0(self):
        return self.p[2]
    
    def a(self):
        return self.v[0]
    def b(self):
        return self.v[1]
    def c(self):
        return self.v[2]
    
    def __cmp__(self, other):
        "Comparison, used to implement ==, <, etc."
        pass

    def __neg__(self):
        "Define unary negation with the - symbol."
        return self * -1

    def __add__(self, other):
        "Add two lines."
        pass

    def __sub__(self, other):
        "Subtract two lines."
        return self + (-other)
    
    def __mul__(self, other):
        "Multiply a line by a constant."
        pass
    
    def __truediv__(self, other):
        "Divide a line by a constant."
        pass

    def __radd__(self, other):
        "Add two lines, reflected version."
        return self + other

    def __rsub__(self, other):
        "Subtract two lines, reflected version."
        return -(self - other)
    
    def __rmul__(self, other):
        "Multiply a line by a constant, reflected version."
        return self * other
    
    def __iadd__(self, other):
        "Alter a line, adding another line to it."
        self = self + other
        return self

    def __isub__(self, other):
        "Alter a line, subtracting another line from it."
        self = self - other
        return self
    
    def __imul__(self, other):
        "Alter a line, multiplying it by by a constant."
        self = self * other
        return self
    
    def __itruediv__(self, other):
        "Alter a line, dividing it by by a constant."
        self = self / other
        return self
    
    def __str__(self):
        "Provide a basic string representation of a line."
        pass
    
    def __repr__(self):
        pass