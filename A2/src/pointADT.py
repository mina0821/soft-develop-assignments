#name: Mingnan Su
#macID: sum1

from math import *
## @file pointADT.py
#  @title pointADT
#  @author Mingnan Su
#  @date 2/15/2017

## @brief An ADT represents a point in 2D graph
#  @details This class represents a point in 2D graph with (xc,yc)
#           coordinates the position in x-axis and y-axis

class PointT():
    
    ## @brief creates a point in 2-D graph with x and y coordinates
    #  @param x the value of x coordinate
    #  @param y the value of y coordinate
    def __init__(self,x,y):
        self.__xc = x
        self.__yc = y


    ## @brief return the x coordinates of given object
    #  @return Returns x coordinates of the point given
    def xcrd (self):
        return self.__xc


    ## @brief return the y coordinates of given object
    #  @return Returns y coordinates of the point given
    def ycrd (self):
        return self.__yc


    ## @brief calculate the distance between two points
    #  @param pt another pointT object
    #  @return the distance between pt and self
    def dist (self,pt):
        xcq = (self.__xc - pt.xcrd()) ** 2
        ycq = (self.__yc - pt.ycrd()) ** 2
        return sqrt(xcq + ycq)


    ## @brief rotate the point with given radius
    #  @param rad the radiance of the angle
    def rot(self,rad):
        ## @var a 2*2 Matrix represent by [ [row1] [row2] ]
        a = [ [cos(rad) , -sin(rad)] , [sin(rad) , cos(rad)] ]
        ## @var x 2*1 Matrix represent by [ row1 row2 ]
        x = [ self.__xc , self.__yc ]
        ## @var r Matrix result in a*x
        r = [ [b*c for b,c in zip(row,x)] for row in a]
        self.__xc = float(format(sum(r[0]),'.5f'))
        self.__yc = float(format(sum(r[1]),'.5f'))

    ## @brief check if two pointT object is equal
    def __eq__(self,other):
        return self.__dict__ == other.__dict__
