from vector import *

def pointsToVec(p, q) -> Vector:
    "Returns the vector with initial point p and terminal point q."
    v = []
    for i in range(3):
        v.append(q[i] - p[i])
    
    return Vector(v)

def origin():
    "Returns the origin point (0, 0, 0)."
    return Point([0,0,0])

def tempDistance(p, q):
    pass

class Point:

    def __init__(self, p):
        if len(p) != 3:
            raise ValueError("point must have 3 components")
        
        if isinstance(p, list):
            self.p = p
        elif isinstance(p, tuple):
            pList = []
            for n in p:
                pList.append(n)
            self.p = pList
        elif isinstance(p, Vector):
            self.p = p.vector
        else:
            raise TypeError("point can only be created from a list, tuple, or vector")
    
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
    
    def vec(self):
        "Returns the point from the origin to a given point."
        return pointsToVec(origin(), self)
    
    def __cmp__(self, other):
        "Comparison, used to implement ==, <, etc."
        pass

    def __neg__(self):
        "Define unary negation with the - symbol."
        return self * -1

    def __add__(self, other):
        "Add two points."
        if not isinstance(other, Point):
            raise TypeError("undefined")
        
        sum = []
        for i in range(3):
            sum.append(self[i] + other[i])
        return Point(sum)

    def __sub__(self, other):
        "Subtract two points."
        return self + (-other)
    
    def __mul__(self, other):
        "Multiply a point by a constant."
        if not isScalar(other):
            raise TypeError("can only multiply a point by a constant")
        
        product = []
        for i in range(3):
            product.append(self[i] * other[i])
        return Point(product)
    
    def __truediv__(self, other):
        "Divide a point by a constant."
        if not isScalar(other):
            raise TypeError("can only divide a point by a constant")
        
        product = []
        for i in range(3):
            product.append(self[i] * other[i])
        return Point(product)

    def __radd__(self, other):
        "Add two points, reflected version."
        return self + other

    def __rsub__(self, other):
        "Subtract two points, reflected version."
        return -(self - other)
    
    def __rmul__(self, other):
        "Multiply a point by a constant, reflected version."
        return self * other
    
    def __iadd__(self, other):
        "Alter a point, adding another point to it."
        self = self + other
        return self

    def __isub__(self, other):
        "Alter a point, subtracting another point from it."
        self = self - other
        return self
    
    def __imul__(self, other):
        "Alter a point, multiplying it by by a constant."
        self = self * other
        return self
    
    def __itruediv__(self, other):
        "Alter a point, dividing it by by a constant."
        self = self / other
        return self
    
    def __str__(self):
        "Provide a basic string representation of a point."
        return(f'({self.x()}, {self.y()}, {self.z()})')
    
    def __repr__(self):
        return(f'({self.x()},{self.y()},{self.z()})')