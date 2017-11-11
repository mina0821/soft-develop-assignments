#name: Mingnan Su
#macID: sum1

## @file lineADT.py
#  @title lineADT
#  @author Mingnan Su
#  @date 2/16/2017

from math import *
from pointADT import *

    
## @brief An ADT represents a line
class LineT:

    ## @brief Constructor for LineT
    #  @param pt one pointT at the end of the line
    #  @param pt2 another pointT at another end of the line
    def __init__(self,pt,pt2):
        self.__b = pt
        self.__e = pt2

    ## @brief returns the beginning point
    #  @return returns the beginning point of current line object
    def beg(self):
        return self.__b

    ## @brief returns the ending point
    #  @return returns the ending point of current line object
    def end(self):
        return self.__e

    ## @brief calculates the length of the line
    #  @return returns the length of the current line object
    def len(self):
        b = self.__b
        return b.dist(self.__e)

    ## @brief calculates the middle point of thel ine
    #  @return returns a PointT represents the middle point of the line
    def mdpt(self):
        b = self.__b
        e = self.__e
        xc = (b.xcrd() + e.xcrd()) / 2.0
        yc = (b.ycrd() + e.ycrd()) / 2.0
        return PointT(xc,yc)

    ## @brief rotate the line with given angle
    #  @param rad the angle given in radiance
    def rot(self,rad):
        self.__b.rot(rad)
        self.__e.rot(rad)

    ## @brief check if two object is equal
    def __eq__(self, other) : 
        return self.__dict__ == other.__dict__
