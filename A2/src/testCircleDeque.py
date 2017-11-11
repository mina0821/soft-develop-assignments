#name: Mingnan Su
#macID: sum1

## @file testCircleDeque.py
#  @author Mingnan SU
#  @brief Test pointADT, lineADT, circleADT, deque
#  @date 2/18/2017

import unittest
from pointADT import *
from lineADT import *
from circleADTp import *
from deque import *

## @brief Tests all the other modules in current folder
class CircleDequeTests(unittest.TestCase):

    def setUp(self):
        #point sits at (0,1)
        self.pt = PointT(0,1)

        #line connected by (0,0) and (0,1)
        self.ln = LineT(PointT(0,0), self.pt)

        #Circle center at (0,1) have radius 1
        self.ci = CircleT(self.pt, 1)

        #Deque init
        Deq.init()
        self.c1 = CircleT(PointT(2,0), 1)
        self.c2 = CircleT(PointT(-3,0), 1)
        self.c3 = CircleT(PointT(0,-3), 1.5)

    def tearDown(self):
        self.pt = None
        self.ln = None
        self.ci = None
        Deq.init()
        self.c1 = None
        self.c2 = None
        self.c3 = None

    ## @brief Normal case - PointT xcrd return xc value
    def test_point_xcrd(self):
        self.assertTrue(self.pt.xcrd() == 0)

    ## @brief Normal case - PointT ycrd return yc value
    def test_point_ycrd(self):
        self.assertTrue(self.pt.ycrd() == 1)

    ## @brief Normal case - PointT dist return distance between two points
    def test_point_dist(self):
        pt2 = PointT(0,3)
        # Distance from point (0,1) to (0,3) should be 2
        self.assertAlmostEqual(self.pt.dist(pt2), 2.0)

    ## @brief Boundary case - PointT dist return 0 when two points overlap
    def test_point_dist_zero(self):
        pt2 = PointT(0,1)
        self.assertAlmostEqual(self.pt.dist(pt2), 0.0)

    ## @brief Normal case - PointT rot roates a point by given angle
    def test_point_rot(self):
        # point (0,1) rotates 90 degrees to left
        self.pt.rot(pi/2)
        # Now the point should sits at (-1,0)
        self.assertTrue(self.pt == PointT(-1,0))

    ## @brief Boundary case - PointT rot rotates 360 degree
    def test_point_rot_noChange(self):
        # rotate 360 degrees to left
        self.pt.rot(2*pi)
        self.assertTrue(self.pt == PointT(0,1))

    ## @brief Boundary case - PointT rot rotates 0 degree
    def test_point_rot_zero(self):
        # rotate 0 degrees to left
        self.pt.rot(0)
        self.assertTrue(self.pt == PointT(0,1))

    ## @brief Boundary case - PointT rot rotates negative degree
    def test_point_rot_neg(self):
        # rotate 90 degree to right
        self.pt.rot(-pi/2.0)
        self.assertTrue(self.pt == PointT(1,0))

    ## @brief Normal case - LineT beg returns beginning point
    def test_line_beg(self):
        self.assertTrue(self.ln.beg() == PointT(0,0))

    ## @brief Normal case - LineT end returns ending point
    def test_line_end(self):
        self.assertTrue(self.ln.end() == self.pt)

    ## @brief Normal case - LineT len returns the length of the line
    def test_line_len(self):
        # Length of the line from (0,0) to (0,1)
        self.assertAlmostEqual(self.ln.len(), 1.0)
        
    ## @brief Boundary case - LineT len return zero if two points connecting
    #                         the line is overlapped
    def test_line_len_zero(self):
        # Length of line from (0,1) to (0,1)
        self.assertAlmostEqual(LineT(self.pt,PointT(0,1)).len(), 0)

    ## @brief Normal case - LineT mdpt returns the middle point of the line
    def test_line_mdpt(self):
        # Middile point of the line from (0,0) to (0,1)
        self.assertTrue(self.ln.mdpt() == PointT(0,0.5))
        

    ## @brief Boundary case - LineT mdpt if two points are the same
    #                         (length of the line is zero)
    def test_line_mdpt_same(self):
        # Middle point of line from (0,1) to (0,1)
        test_line = LineT(self.pt, PointT(0,1))
        # First check if the length is zero
        self.assertTrue(test_line.len() == 0)
        # Check middle point
        self.assertTrue(test_line.mdpt() == self.pt) 

    ## @brief Normal case - LineT rot rotates a point by given angle
    def test_line_rot(self):
        # rotate 90 degrees to the left for the line from (0,0) to (0,1)
        self.ln.rot(pi/2)
        # Result line should be from (0,0) to (-1,0)
        self.assertTrue(self.ln == LineT(PointT(0,0), PointT(-1,0)))

    ## @brief Boundary case - LineT rot rotates 360 degrees to the left
    def test_line_rot_noChange(self):
        self.ln.rot(2*pi)
        self.assertTrue(self.ln == LineT(PointT(0,0), self.pt))

    ## @brief Boundary case - LineT rot rotates 0 degree
    def test_line_rot_zero(self):
        self.ln.rot(0)
        self.assertTrue(self.ln == LineT(PointT(0,0), self.pt))

    ## @brief Boundary case - LineT rot rotates negative degree
    def test_line_rot_neg(self):
        # rotate 90 degrees to the right
        self.ln.rot(-pi/2)
        # Result line should be from (0,0) to (1,0)
        self.assertTrue(self.ln == LineT(PointT(0,0), PointT(1,0)))

    ## @brief Normal case - CircleT cen return center point of the circle
    def test_circle_cen(self):
        self.assertTrue(self.ci.cen() == self.pt)

    ## @brief Normal case - CircleT rad return the radius of the circle
    def test_circle_rad(self):
        self.assertTrue(self.ci.rad() == 1)

    ## @brief Normal case - CircleT area return the area of the circle
    def test_circle_area(self):
        self.assertAlmostEqual(self.ci.area(), 3.1415926535)

    ## @brief Normal case - CircleT intersect test if two circle intersects
    def test_circle_intersect_yes(self):
        # self.circle centered at (0,1) have radius 1
        # intersect with circle centered at (0,0) with radius 1
        c_test = CircleT(PointT(0,0), 1)
        self.assertTrue(self.ci.intersect(c_test))

    ## @brief Normal case - CircleT intersect test if two circle intersects
    def test_circle_intersect_no(self):
        # self.circle centered at (0,1) have radius 1
        # does not intersect with circle centered at (-2,-2) with radius 1
        c_test = CircleT(PointT(-2,-2), 1)
        self.assertFalse(self.ci.intersect(c_test))

    ## @brief Boundary case - CircleT intersect test if two nested circles
    #                         (One circle is inside the another) intersects
    def test_circle_intersect_nested(self):
        # self.circle centered at (0,1) have radius 1
        # c_test with the same center but have radius 2
        c_test = CircleT(self.pt, 2)
        self.assertTrue(self.ci.intersect(c_test))

    ## @brief Boundary case - CircleT intersect test if two circles just
    #                         touches each other at boundary
    def test_circle_intersect_touch(self):
        # self.circle centered at (0,1) have radius 1
        # c_test centered at (0,-1) have radius 1
        c_test = CircleT( PointT(0,-1), 1 )
        self.assertTrue(self.ci.intersect(c_test))

    ## @brief Normal case - CircleT connection test if two center points connects
    def test_circle_connection(self):
        # self.circle centered at (0,1) have radius 1
        # c_test centered at (0,0) have radius 1
        c_test = CircleT( PointT(0,0), 1 )
        connect_line = self.ci.connection(c_test)
        self.assertTrue( connect_line == LineT(self.pt, PointT(0,0)))

    ## @brief Normal case - CircleT force Assume f(x) = x
    #                       Test the function c.force(f)
    def test_circle_force(self):
        func = lambda x: x**2
        test_func = self.ci.force(func)
        # self.circle centered at (0,1) have radius 1
        # c_test centered at (0,0) have radius 1
        c_test = CircleT( PointT(0,0), 1 )
        
        # test_func will take in c_test, mutiply the area of self.ci and c_test
        
        # The line connecting centers should be from (0,0) to (0,1)
        # So we easily knows the length of the connected line is 1
        # Then we get f(1) = 1**2 = 1

        #Final result should be pi*pi*1 = pi**2
        self.assertAlmostEqual(test_func(c_test), pi**2)

    ## @brief Normal case - Deque init check if Deq.s is empty list
    def test_deque_init(self):
        self.assertTrue(Deq.s == [])

    ## @brief Normal case - Deque pushBack pushes to the end
    def test_deque_pushBack(self):
        c1 = self.c1
        c2 = self.c2
        c3 = self.c3
        Deq.pushBack(c1)
        Deq.pushBack(c2)
        Deq.pushBack(c3)
        self.assertTrue(Deq.s == [c1,c2,c3])

    ## @brief Exception case - Deque pushBack cannot push to full deque
    def test_deque_pushBack_full(self):
        for _ in range(20):
            Deq.pushBack(self.c1)
            
        #Now the deque is full with 20 circles
        with self.assertRaises(FULL):
            Deq.pushBack(self.c1)

    ## @brief Normal case - Deque pushFront pushes to the front
    def test_deque_pushFront(self):
        c1 = self.c1
        c2 = self.c2
        c3 = self.c3
        Deq.pushFront(c1)
        Deq.pushFront(c2)
        Deq.pushFront(c3)
        self.assertTrue(Deq.s == [c3, c2, c1])

    ## @brief Exception case - Deque pushFront cannot push to full deque
    def test_deque_pushFront_full(self):
        for _ in range(20):
            Deq.pushFront(self.c1)

        #Now the deque is full with 20 circles
        with self.assertRaises(FULL):
            Deq.pushFront(self.c1)

    ## @brief Normal case - Deque popBack pops the last element
    def test_deque_popBack(self):
        c1 = self.c1
        c2 = self.c2
        c3 = self.c3
        Deq.pushFront(c1)
        Deq.pushFront(c2)
        Deq.pushFront(c3)
        Deq.popBack()
        #[c3, c2, c1] omit last element
        self.assertTrue(Deq.s == [c3, c2])

    ## @brief Exception case - Deque popBack cannot pop an empty deque
    def test_deque_popBack_empty(self):
        with self.assertRaises(EMPTY):
            Deq.popBack()

    ## @brief Normal case - Deque popFront pops the first element
    def test_deque_popFront(self):
        c1 = self.c1
        c2 = self.c2
        c3 = self.c3
        Deq.pushFront(c1)
        Deq.pushFront(c2)
        Deq.pushFront(c3)
        Deq.popFront()
        #[c3,c2,c1] omit first element
        self.assertTrue(Deq.s == [c2, c1])

    ## @brief Exception case - Deque popFront cannot pop an empty deque
    def test_deque_popFront_empty(self):
        with self.assertRaises(EMPTY):
            Deq.popFront()

    ## @brief Normal case - Deque back returns the last element
    def test_deque_back(self):
        c1 = self.c1
        c2 = self.c2
        c3 = self.c3
        Deq.pushBack(c1)
        Deq.pushBack(c2)
        Deq.pushBack(c3)
        # return the last element of [c1, c2, c3]
        self.assertTrue(Deq.back() == c3)

    ## @brief Exception case - Deque back cannot return with empty deque
    def test_deque_back_empty(self):
        with self.assertRaises(EMPTY):
            Deq.back()

    ## @brief Normal case - Deque front returns the first element
    def test_deque_front(self):
        c1 = self.c1
        c2 = self.c2
        c3 = self.c3
        Deq.pushBack(c1)
        Deq.pushBack(c2)
        Deq.pushBack(c3)
        # return the first element of [c1, c2, c3]
        self.assertTrue(Deq.front() == c1)

    ## @brief Exception case - Dequq front cannot return with empty deque
    def test_deque_front_empty(self):
        with self.assertRaises(EMPTY):
            Deq.front()

    ## @brief Normal case - Deque size return the size of the deque
    def test_deque_size(self):
        c1 = self.c1
        c2 = self.c2
        c3 = self.c3
        Deq.pushBack(c1)
        Deq.pushBack(c2)
        Deq.pushBack(c3)
        self.assertTrue(Deq.size() == 3)

    ## @brief Boundary case - Deque size is zero after initilazing
    def test_deque_size_zero(self):
        self.assertTrue(Deq.size() == 0)

    ## @brief Normal case - Deque disjoint test if all circles do not touches
    def test_deque_disjoint_true(self):
        c1 = self.c1
        c2 = self.c2
        c3 = self.c3
        Deq.pushBack(c1)
        Deq.pushBack(c2)
        Deq.pushBack(c3)
        #c1,c2,c3 all separated and donot intersects with each other
        self.assertTrue(Deq.disjoint())

    ## @brief Normal case - Deque disjoint test if one pair of circles touches
    def test_deque_disjoint_false(self):
        c1 = self.c1
        #c1 and c2 touches each other
        c2 = CircleT(PointT(0,0), 1)
        c3 = self.c3
        Deq.pushBack(c1)
        Deq.pushBack(c2)
        Deq.pushBack(c3)
        self.assertFalse(Deq.disjoint())

    ## @brief Boundary case - Deque disjoint with only one circle in the deque
    def test_deque_disjoint_one(self):
        c1 = self.c1
        Deq.pushBack(c1)
        #If there is only one circle in the deque,
        #   c1 do not have any chance touches any other circle,
        #   so result should be true
        self.assertTrue(Deq.disjoint())


    ## @brief Exception case - Deque disjoint cannot test with empty deque
    def test_deque_disjoint_empty(self):
        with self.assertRaises(EMPTY):
            Deq.disjoint()

    ## @brief Normal case - Deque sumFx calculates x-comp force acting on s[0]
    def test_deque_sumFx(self):
        c1 = self.c1        #Center (2,0) Radius 1
        c2 = self.c2        #Center (-3,0) Radius 1
        c3 = self.ci        #Center (0,1) Radius 1
        Deq.pushBack(c1)
        Deq.pushBack(c2)
        Deq.pushBack(c3)
        # Assume f(x) = x
        func = lambda x: x
        # According to the specification, the result should be
        #       Fx(f,c2,c1) + Fx(f,c3,c1)
        #
        # Calculating Fx(f,c1,c2)
        #           = xcomp(c1.force(f)(c2), c2, c1)
        #           = xcomp(pi*pi*5, c2, c1)
        #           = pi*pi*5*(-5/5)
        #           = - 5 * (pi ** 2)
        #
        # Calculating Fx(f,c1,c3)
        #           = xcomp(c1.force(f)(c3), c3, c1)
        #           = xcomp(pi*pi*sqrt(5), c3, c1)
        #           = pi*pi*sqrt(5)*(-2/sqrt(5))
        #           = - 2 * (pi ** 2)
        expected = -5*pi**2 + -2*pi**2
        self.assertAlmostEquals(Deq.sumFx(func), expected)

    ## @brief Exception case - Deque sumFx cannot evaluate with empty deque
    def test_deque_sumFx_empty(self):
        with self.assertRaises(EMPTY):
            Deq.sumFx(lambda x:x)

    ## @brief Normal case - Deque totalArea calculates the sum of area
    def test_deque_totalArea(self):
        c1 = self.c1        #Center (2,0) Radius 1
        c2 = self.c2        #Center (-3,0) Radius 1
        c3 = self.c3        #Center (0,-3) Radius 1.5
        Deq.pushBack(c1)
        Deq.pushBack(c2)
        Deq.pushBack(c3)
        # total area should be
        expected = pi + pi + pi*1.5**2
        self.assertAlmostEquals(Deq.totalArea(), expected)

    ## @brief Exception case - Deque totalArea cannot evaluate with empty deque
    def test_deque_totalArea_empty(self):
        with self.assertRaises(EMPTY):
            Deq.totalArea()

    ## @brief Normal case - Deque averageRadius calculates average value of radius
    def test_deque_averageRadius(self):
        c1 = self.c1        #Center (2,0) Radius 1
        c2 = self.c2        #Center (-3,0) Radius 1
        c3 = self.c3        #Center (0,-3) Radius 1.5
        Deq.pushBack(c1)
        Deq.pushBack(c2)
        Deq.pushBack(c3)
        # average radius should be
        expected = (1+1+1.5) / 3.0
        self.assertAlmostEquals(Deq.averageRadius(),expected)
    
    ## @brief Exception case - Deque averageRadius cannot evaluate with empty deque
    def test_deque_averageRadius_empty(self):
        with self.assertRaises(EMPTY):
            Deq.averageRadius()


if __name__ == '__main__':
    unittest.main()
