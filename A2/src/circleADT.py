#name: Mingnan Su
#macID: sum1

## @file circleADT.py
#  @title circleADT
#  @author Mingnan Su
#  @date 2/17/2017

from math import *
from lineADT import *
from pointADT import *

## @brief an ADT represents a circle
class CircleT:

    ## @brief CircleT constructor
    #  @details Initializes a circleT object
    #           with a point in center and radius
    #  @param cin the center of the circle, type is PointT
    #  @param rin the radius of the circle
    def __init__ (self,cin,rin):
        self.__c = cin
        self.__r = rin

    ## @brief Gets the center of the circle
    #  @return Returns a PointT represents the center of the circle
    def cen(self):
        return self.__c

    ## @brief Gets the radiance of the circle
    #  @return Returns a real value represents the radius of the circle
    def rad(self):
        return self.__r

    ## @brief calculates the area of the cirlce
    #  @return Returns the area of the circle
    def area(self):
        return pi * (self.__r ** 2)

    ## @brief determines if the given circle intersects current circle object
    #  @details Select an arbitrary point inside the current circle, if there
    #           existed a point which is also insdie the given circle, this
    #           function will return true. Otherwise false. A point which just
    #           seats at the boundary of the circle is considered as "inside
    #           the circle".
    #  @param ci circle given to test
    #  @return Returns boolean variable: true if circles intersects; false if not
    def intersect(self,ci):
        c = self.__c
        dist = c.dist(ci.cen())
        maxRius = self.__r + ci.rad()
        return maxRius >= dist

    ## @brief draw a line between current circle object and given circle
    #  @param ci another circle provided to draw a line with
    #  @return Returns a LintT line which is the connection between two centers
    def connection(self,ci):
        return LineT(self.__c,ci.cen())

    ## @brief calculates the function of the force acting on current circle
    #         object from a given circle
    #  @details This function takes a function as input and output another
    #           function. Input function is used to parameterize the 
    #           gravitational law. The output function allows you to calculate
    #           the force acting on current circle object from given circle.
    #           Output function is taken a circle as input and output the force.
    #  @param f a function which takes in a real value and output a part of
    #           the force calculation
    #  @return Returns a function which can take another circle and output the force
    def force(self,f):
        area = self.area()
        return lambda x: area * x.area() * f(self.connection(x).len())

    ## @brief check if two object is equal
    def __eq__(self,other):
        return self.__dict__ == other.__dict__ 
