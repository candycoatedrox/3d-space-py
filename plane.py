from line import *

def closestPoints(a, b) -> tuple[Point]:
    "Returns the closest points p and q on two objects in 3D space (points, lines, or planes)."

    # FIND TWO CLOSEST POINTS ON THE OBJECTS IF THEY AREN'T ALREADY POINTS HERE!!!!
    if isinstance(a, Point):
        p = a
        if isinstance(b, Point):
            q = b
        
        elif isinstance(b, Line):
            # FILL IN - POINT TO LINE
            pass
        
        elif isinstance(b, Plane):
            # FILL IN - POINT TO PLANE
            pass

        else:
            raise TypeError("object must be a point, line, or plane")
    
    elif isinstance(a, Line):
        if isinstance(b, Point):
            return closestPoints(b, a)

        elif isinstance(b, Line):
            # FILL IN - LINE TO LINE
            pass

        elif isinstance(b, Plane):
            # FILL IN - LINE TO PLANE
            pass

        else:
            raise TypeError("object must be a point, line, or plane")
    
    elif isinstance(a, Plane):
        if isinstance(b, Point):
            return closestPoints(b, a)

        elif isinstance(b, Line):
            return closestPoints(b, a)

        elif isinstance(b, Plane):
            # FILL IN - PLANE TO PLANE
            pass

        else:
            raise TypeError("object must be a point, line, or plane")
    
    else:
        raise TypeError("object must be a point, line, or plane")
    
    return (p, q)

def dist2(a, b):
    "Returns the distance between two objects in 3D space (points, lines, or planes), squared."

    # Determine p and q, the closest points on objects a and b respectively
    p, q = closestPoints(a, b)

    sum = 0
    for i in range(3):
        sum += (q[i] - p[i]) * (q[i] - p[i])
    return sum

def distance(a, b):
    "Returns the distance between two objects in 3D space (points, lines, or planes)."
    return math.sqrt(dist2(a, b))

class Plane:

    def __init__(self, p: Point, n: Vector):
        # must be in 3d space
        if len(p) != 3:
            raise ValueError("base point must have 3 components")
        if len(n) != 3:
            raise ValueError("direction vector must have dimension 3")
        
        self.p = p
        self.n = n

    # p and n can be modified during runtime
    # these methods return accurate, up-to-date coordinates/components
    def x0(self):
        return self.p[0]
    def y0(self):
        return self.p[1]
    def z0(self):
        return self.p[2]
    
    def a(self):
        return self.n[0]
    def b(self):
        return self.n[1]
    def c(self):
        return self.n[2]

    def __cmp__(self, other):
        "Comparison, used to implement ==, <, etc."
        pass

    def __neg__(self):
        "Define unary negation with the - symbol."
        return self * -1

    def __add__(self, other):
        "Add two planes."
        pass

    def __sub__(self, other):
        "Subtract two planes."
        return self + (-other)
    
    def __mul__(self, other):
        "Multiply a plane by a constant."
        pass
    
    def __truediv__(self, other):
        "Divide a plane by a constant."
        pass

    def __radd__(self, other):
        "Add two planes, reflected version."
        return self + other

    def __rsub__(self, other):
        "Subtract two planes, reflected version."
        return -(self - other)
    
    def __rmul__(self, other):
        "Multiply a plane by a constant, reflected version."
        return self * other
    
    def __iadd__(self, other):
        "Alter a plane, adding another plane to it."
        self = self + other
        return self

    def __isub__(self, other):
        "Alter a plane, subtracting another plane from it."
        self = self - other
        return self
    
    def __imul__(self, other):
        "Alter a plane, multiplying it by by a constant."
        self = self * other
        return self
    
    def __itruediv__(self, other):
        "Alter a plane, dividing it by by a constant."
        self = self / other
        return self
    
    def __str__(self):
        "Provide a basic string representation of a plane."
        pass
    
    def __repr__(self):
        pass