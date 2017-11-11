import math

class CircleT(object):
    ## @brief Creates a CircleT object and sets it's x/y-coordinates and radius.
    # @param x The x-coordinate of the center of the circle
    # @param y The y-coordinate of the center of the circle
    # @param r The radius of the circle
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    ## @brief Returns the x-coordinate of the given circle object
    # @param self The CircleT object itself
    # @return The x-coordinate of the circle
    def xcoord(self):
        return self.x

    ## @brief Returns the y-coordinate of the given circle object
    # @param self The CircleT object itself
    # @return The y-coordinate of the circle
    def ycoord(self):
        return self.y

    ## @brief Returns the radius of the given circle object
    # @param self The CircleT object itself
    # @return The radius of the circle
    def radius(self):
        return self.r
    
    ## @brief Returns the area of the given circle object
    # @param self The CircleT object itself
    # @return The area of the circle
    def area(self):
        return math.pi*self.r*self.r

    ## @brief Returns the circumference of the given circle object
    # @param self The CircleT object itself
    # @return The circumference of the circle
    def circumference(self):
        return 2*math.pi*self.r

    ## @brief Determines if the circle is inside a box
    # @param self The CircleT object itself
    # @param x0 The x-coordinate of the top left corner of the box
    # @param y0 The y-coordinate of the top left corner of the box
    # @param w The width of the box
    # @param h The height of the box
    # @return True if the circle is inside the box, and False if otherwise
    def insideBox(self, x0, y0, w, h):
        if (self.x > x0 and self.y > y0):
            if (self.x-self.r > x0 and self.x+self.r < x0+h and self.y-self.r > y0 and self.y+self.r < y0+w):
                return True
        else:
            return False

    ## @brief Determines if the circle intersects with another circle, including overlapping point on the border
    # @param self The CircleT object itself
    # @param c Another CircleT object
    # @return True if the circles intersect, and False if otherwise
    def intersect(self, c):
        totalRadius = self.r + c.r
        distance = math.sqrt(math.pow(self.x-c.x,2) + math.pow(self.y-c.y,2))
        if (distance > totalRadius):
            return False
        else:
            return True
        
    ## @brief Manipulates the size of the radius
    # @param self The CircleT object itself
    # @param c A number that the radius will be scaled by
    def scale(self, k):
        self.r = self.r*k

    ## @brief Manipulates the location of the circle
    # @param self The CircleT object itself
    # @param dx The horizontal shift of the circle
    # @param dy The vertical translation of the circle
    def translate(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
                
                

    
