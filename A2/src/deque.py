# Name:  Mingnan Su
# MacID: sum1

## @file deque.py
#  @title deque
#  @author Mingnan Su
#  @date 1/17/2017

from math import *
from circleADT import *

## @brief An abstract object that represents a double ended queue of circles
class Deq:


    ## @var MAX_SIZE Exported Constants
    MAX_SIZE = 20
    ## @var s state variables - sequence of CircleT
    s = []


    ## @brief Initialize a deque
    #  @details This method is assumed to be called before
    #           any access program
    @staticmethod
    def init():
        Deq.s = []


    ## @brief Add a circle at the end of the list
    #  @param c A CircleT waiting to be add
    #  @exception FULL throws if the deque is full
    @staticmethod
    def pushBack(c):
        s = Deq.s
        size = len(s)
        if size == Deq.MAX_SIZE:
            raise FULL("Maximum size exceeded")
        s = s + [c]
        Deq.s = s


    ## @brief Add a circle at the beginning of the list
    #  @param c A CircleT waiting to be add
    #  @exception FULL throws if the deque is full
    @staticmethod
    def pushFront(c):
        s = Deq.s
        size = len(s)
        if size == Deq.MAX_SIZE:
            raise FULL("Maximum size exceeded")
        s = [c] + s
        Deq.s = s


    ## @brief Delete a circle from the end
    #  @exception EMPTY throws if the deque is empty
    @staticmethod
    def popBack():
        s = Deq.s
        size = len(s)
        if size == 0:
            raise EMPTY("Deque is empty.")
        s = s[0 : size - 1]
        Deq.s = s


    ## @brief Delete a circle from the beginning
    #  @exception EMPTY throws if the deque is empty
    @staticmethod
    def popFront():
        s = Deq.s
        size = len(s)
        if size == 0:
            raise EMPTY("Deque is empty.")
        s = s[1 : size]
        Deq.s = s


    ## @brief Get the last circle in the deque
    #  @return Returns the last element in the deque
    #  @exception EMPTY throws if the deque is empty
    @staticmethod
    def back():
        s = Deq.s
        size = len(s)
        if size == 0:
            raise EMPTY("Deque is empty.")
        return s[size - 1]


    ## @brief Get the first circle in the deque
    #  @return Returns the first element in the deque
    #  @exception EMPTY throws if the deque is empty
    @staticmethod
    def front():
        s = Deq.s
        size = len(s)
        if size == 0:
            raise EMPTY("Deque is empty.")
        return s[0]


    ## @brief Get the length of the deque
    #  @reutrn Returns the size of the deque
    @staticmethod
    def size():
        s = Deq.s
        size = len(s)
        return size


    ## @brief Test if all the circle in the deque intersects with each other
    #  @details Retun true if all the circles in the deque does not interact
    #           with each other. Return false if there is one circle in the
    #           deque interact with another circle in the deque.
    #  @return Returns true if all the circle does not interact. False if one
    #          circle interact with another.
    #  @exception EMPTY throws if the deque is empty
    @staticmethod
    def disjoint():
        s = Deq.s
        size = len(s)
        if size == 0:
            raise EMPTY("Deque is empty.")
        ## @var r store a list of boolean - false means two arbitrary circle
        #         in the deque intersects each other
        r = [not i.intersect(j) for j in s for i in s if i != j]
        return reduce(lambda x, y: x and y, r, True)


    ## @brief Calulate the total force in x-direction on first circle
    #  @details This method first takes in a partial gravitational force
    #           function to calculate the force acting on first circle by another 
    #           circles in the deque (for example, s[0] and s[2]). Then the
    #           method calculates the x-comp force between two circles. This
    #           process continue untill we reach the end of the deque. The
    #           output is the sum of the x-comp force exerted by all circles
    #           in the deque on the first circle (s[0]).
    #  @param f a partial gravitational force function
    #  @return Returns the sum of the x-comp force acting on first circle
    #  @exception EMPTY throws if the deque is empty
    @staticmethod
    def sumFx(f):
        s = Deq.s
        size = len(s)
        if size == 0:
            raise EMPTY("Deque is empty.")
        c0 = s[0]
        ## @brief calculate the x-comp force between two circles
        #  @param c circle to be calculated
        #  @return Return the x-comp force acting on c0 by c
        def fx(c):
            force = c.force(f)(c0)
            line_len = float((c0.connection(c).len()))
            x_comp = (c.cen().xcrd() - c0.cen().xcrd()) / line_len
            return force * x_comp
        return reduce(lambda x,y: x+y, [fx(i) for i in s if i != c0], 0)
        

    
    ## @brief Calculate the total area of the circles in the deque
    #  @details This method returns the sum of all circles' area in deque.
    #           Overlap between circles is not considered in this case, which
    #           means the output generated maybe count for the area overlaped
    #           more than once.
    #  @return Returns total area of all circles in the deque
    #  @exception EMPTY throws if the deque is empty
    @staticmethod
    def totalArea():
        s = Deq.s
        size = len(s)
        if size == 0:
            raise EMPTY("Deque is empty.")
        ## @var r store the area of each circle in a list
        r = [c.area() for c in s]
        return reduce(lambda x, y: x+y, r, 0)


    ## @brief Calculate the average radius of circles in the deque
    #  @return Returns the average of all the circles' radius in the deque
    #  @exception EMPTY throws if the deque is empty
    @staticmethod
    def averageRadius():
        s = Deq.s
        size = len(s)
        if size == 0:
            raise EMPTY("Deque is empty.")
        return reduce(lambda x,y: x+y, [c.rad() for c in s], 0)/float(size)
        
        


## @brief raise exception when the sequence is full
class FULL(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return str(self.value)

## @brief raise exception when the sequence is empty
class EMPTY(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return str(self.value)
