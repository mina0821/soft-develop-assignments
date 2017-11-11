#Michael Balas
#400023244
import pointADT
import lineADT
import math
## @file circleADT.py
#  @title CircleADT
#  @author Michael Balas
#  @date 2/2/2017

## @brief This class represents a circle ADT. 
#  @details This class represents a circle ADT, with point cin (x, y)
#  defining the centre of the circle, and r defining its radius. 
class CircleT(object):

        ## @brief Constructor for CircleT
        #  @details Constructor accepts one point and a number (radius)
        #  to construct a circle.
        #  @param cin is a point (the centre of the circle).
        #  @param rin is any real number (represents the radius of the circle).
        def __init__(self, cin, rin):
                self.c = cin
                self.r = rin

        ## @brief Returns the centre of the circle
        #  @return The point located at the centre of the circle
        def cen(self):
                return self.c

        ## @brief Returns the radius of the circle
        #  @return The radius of the circle
        def rad(self):
                return self.r
        
        ## @brief Calculates the area of the circle
        #  @return The area of the circle
        def area(self):
                return math.pi*(self.r)**2
        
        ## @brief Determines whether the circle intersects another circle
        #  @details This function treats circles as filled objects: circles completely
        #  inside other circles are considered as intersecting, even though
        #  their edges do not cross.  The set of points in each circle
        #  includes the boundary (closed sets).
        #  @param ci Circle to test intersection with
        #  @return Returns true if the circles intersect; false if not         
        def intersect(self, ci):
                xDist = self.c.xc - ci.c.xcrd()
                yDist = self.c.yc - ci.c.ycrd()
                centerDist = math.sqrt(xDist ** 2 + yDist ** 2)
                rSum = self.r + ci.rad()
                return rSum >= centerDist

        ## @brief Creates a line between the centre of two circles
        #  @details This function constructs a line beginning at the centre of the
        #  first circle, and ending at the centre of the other circle.
        #  @param ci Circle to create connection with
        #  @return Returns a new LineT that connects the centre of both circles
        def connection(self, ci):
                return lineADT.LineT(self.c, ci.cen())

        ## @brief Determines the force between two circles given some parameterized
        #  gravitational law
        #  @details This functions calculates the force between two circles of unit
        #  thickness with a density of 1 (i.e. the mass is equal to the area). Any
        #  expression can be substituted for the gravitational law, f(r), or G/(r**2).
        #  @param f Function that parameterizes the gravitational law. Takes the distance
        #  between the centre of the circles and can apply expressions to it (e.g. multiply
        #  the universal gravitation constant, G, by the inverse of the squared distance between
        #  the circles).
        #  @return Returns the force between two circles 
        def force(self, f):
                return lambda x: self.area() * x.area() * f(self.connection(x).len())
