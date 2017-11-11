#name:Mingnan Su
#macID: sum1

import math

class CircleT:
    x=0
    y=0
    r=0

    #constructor
    def __init__(self,x,y,r):
        self.x=x
        self.y=y
        self.r=r

    def xcoord(self):
        return self.x

    def ycoord(self):
        return self.y

    def radius(self):
        return self.r

    #return the area of the circle
    def area(self):
        return math.pi*self.r*self.r

    #return the circumference of the circle
    def circumference(self):
        return math.pi*self.r*2

    #a rectangle with left top point at (x0,y0)
    #width=w,height=h
    #determine if the circle is inside the box
    def insideBox(self,x0,y0,w,h):
        r=self.r
        x=self.x
        y=self.y
        #limit of x0
        posx=x-r
        #limit of y0
        posy=y+r
        #limit of width
        limtw=abs(posx-x0)+2*r
        #limit of height
        limth=abs(posy-y0)+2*r

        #check if the box statisfy all the limits
        if w>=limtw:
            if h>=limth:
                if x0<=posx:
                    if y0>=posy:
                        return True
        return False

    #determine if another circle is intersected with this one
    def intersect(self,c):
        #calculate the sum of two radius
        rds=self.r+c.r

        #calculate the distance between center
        xsq=(self.x-c.x)**2
        ysq=(self.y-c.y)**2
        dist=math.sqrt(xsq+ysq)

        #if they intersected, ditstance between center <= rds
        if dist<=rds:
            return True
        else:
            return False

    #scale the radius by k
    def scale(self, k):
        self.r=self.r*k

    #move the center of circle to (dx,dy)
    def translate(self,dx,dy):
        self.x=self.x+dx
        self.y=self.y+dy
        
