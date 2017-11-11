#name:Mingnan Su
#macID: sum1

import CircleADT
import Statistics

c1=CircleADT.CircleT(1,4,3)
c2=CircleADT.CircleT(-3,2,1)
c3=CircleADT.CircleT(-1,5,2)
c4=CircleADT.CircleT(4,-2,4)

#test CircleADT
print("Testing CircleADT ...")
print("The area of circle 1 should be around 28.27, ")
print("    the output is "+str(c1.area()))
print("The circumference of circle 2 should be around 6.28, ")
print("    the output is "+str(c2.circumference()))
print("We have a box, circle 2 should inside the box.")
print("    the output is "+str(c2.insideBox(-5,3,5,2)))
print("We have a box, circle 1 should outside the box.")
print("    the output is "+str(c1.insideBox(2,-3,100,100)))
print("circle 1 does not intersect circle 2.")
print("    the output is "+str(c1.intersect(c2)))
print("circle 1  intersect circle 3.")
print("    the output is "+str(c1.intersect(c3)))
print("Scale the radius of circle 1 by k=2.Now radius is 6.")
c1.scale(2)
print("    the output is "+str(c1.radius()))
print("Translate the center of circle 1 by (-1,-1).Now center should be (0,3)")
c1.translate(-1,-1)
print("    the output is "+str(c1.xcoord())+","+str(c1.ycoord()))

#test Statictics
c1.scale(0.5)
c1.translate(1,1)
print("\nTesting Statistics ...")
clist=[c1,c2,c3,c4]
print("The average of circles should be 2.5")
print("    the output is "+str(Statistics.average(clist)))
print("The standard deviation shoould be around 1.118")
print("    the output is "+str(Statistics.stdDev(clist)))
print("The ranked list should be [3,1,2,4]")
print("    the output is "+str(Statistics.rank(clist)))
