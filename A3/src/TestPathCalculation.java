package src;

import static org.junit.Assert.*;

import static org.hamcrest.CoreMatchers.*;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;


public class TestPathCalculation {
	private static PointT pt;
	private static PointT pt2;
	private static PointT pt3;
	private static RegionT region;
	
	@Before
	public void setUp(){
		
		//define two points
		try {
			pt = new PointT(0,0);
			pt2 = new PointT(4,0);
			pt3 = new PointT(4,8);
		} catch (InvalidPointException e) {
			// TODO Auto-generated catch block
			System.out.println(e.error());
		}
		
		//define a region
		try {
			region = new RegionT(pt,3,4);
		} catch (InvalidRegionException e) {
			System.out.println(e.error());
		}
		
	}

	//test PointT.java
	@Test
	public void testPointT() {
		//test constructor exceptions
		try {
			PointT test = new PointT(181,160);
			Assert.fail("Expected exception to be thrown");
		} catch (InvalidPointException e) {
			assertThat(e.error(),containsString("Invalid point"));
		}
	}
	
	//test RegionT.java
	@Test
	public void testRegionT(){
		//test constructor exceptions
		try {
			RegionT reg = new RegionT(pt,3,161);
			Assert.fail("Expected exception to be thrown");
		} catch (InvalidRegionException e) {
			assertThat(e.error(),containsString("Invalid region"));
		}
		
		//test pointInRegion
		assertTrue(region.pointInRegion(pt3));
	}
	
	//test GenericList.java
	@Test
	public void testGenerics(){
		GenericList<Integer> lst = new GenericList<Integer>();
		try {
			lst.add(0,5);
			lst.add(1,4);
			assertTrue(lst.getval(0)==5);
			lst.setVal(0, 1);
			assertTrue(lst.getval(0)==1);
		} catch (FullSequenceException e) {
			System.out.println(e.error());
		} catch (InvalidPositionException e) {
			System.out.println(e.error());
		}
		
	}
	
	//test SafeZone.java
	@Test
	public void testsafe(){
		SafeZone zn = new SafeZone();
		//check if exception is thrown
		try {
			zn.add(0, region);
			zn.add(1, region);
			Assert.fail("Expected exception to be thrown");
		} catch (FullSequenceException e) {
			assertThat(e.error(),containsString("List is full"));
		} catch (InvalidPositionException e) {
			System.out.println(e.error());
			Assert.fail("Not correct exception thrown");
		}
	}
	
	//test PathCalculation.java
	@Test
	public void testPathCal(){
		//  Normal Cases
		//define a path to test
		//path test goes from (0,0) to (4,0) to (4,8)
		PathT test = new PathT();
		try {
			//add three points to the path test
			test.add(0, pt);
			test.add(1, pt2);
			test.add(2, pt3);
		} catch (FullSequenceException e) {
			System.out.println(e.error());
		} catch (InvalidPositionException e) {
			System.out.println(e.error());
		}
		
		//test totalDistance
		double result = PathCalculation.totalDistance(test);
		assertTrue(result == 12);
		
		//test totalTurns
		double turns = PathCalculation.totalTurns(test);
		assertTrue(turns == 1);
		
		//test estimatedTime
		double time = PathCalculation.estimatedTime(test);
		//linear time is 12/15 = 0.8
		//angular time is 1.5708/30 = 0.05234
		assertEquals(0.85234,time,0.0001);
	}
	
	//test for exceptions
	@Test
	public void testException(){
		PathT test = new PathT();
		try {
			//add three points to the path test
			test.add(0, pt);
			test.add(1, pt2);
			test.add(2, pt3);
		} catch (FullSequenceException e) {
			System.out.println(e.error());
		} catch (InvalidPositionException e) {
			System.out.println(e.error());
		}
		
		//test for InvalidPositionException for negative position
		try {
			test.getval(-1);
			Assert.fail();
		} catch (InvalidPositionException e) {
			assertThat(e.error(),containsString("Index does not"));
		}
		
		//test for InvalidPositionException for larger position
		try {
			test.getval(3);
			Assert.fail();
		} catch (InvalidPositionException e) {
			assertThat(e.error(),containsString("Index does not"));
		}
	}
	
	//test for path of zero length
	@Test
	public void testZero(){
		//define a pathT variable
		PathT zero = new PathT();
		
		//test totalDistance
		double result = PathCalculation.totalDistance(zero);
		assertTrue(result == 0);
		
		//test totalTurns
		double turns = PathCalculation.totalTurns(zero);
		assertTrue(turns == 0);
		
		//test estimatedTime
		double time = PathCalculation.estimatedTime(zero);
		//linear time is 0/15 = 0
		//angular time is 0/30 = 0
		assertEquals(0.0,time,0.0001);
	}
	
	//test for total length of path for two coincident points
	@Test
	public void testSame(){
		//define a pathT variable
		PathT same = new PathT();
		try {
			//add two identical points to the path
			same.add(0, pt);
			same.add(1, pt);
		} catch (FullSequenceException e) {
			System.out.println(e.error());
		} catch (InvalidPositionException e) {
			System.out.println(e.error());
		}
		
		//test totalDistance
		double result = PathCalculation.totalDistance(same);
		assertTrue(result == 0);
		
		//test totalTurns
		double turns = PathCalculation.totalTurns(same);
		assertTrue(turns == 0);
		
		//test estimatedTime
		double time = PathCalculation.estimatedTime(same);
		//linear time is 0/15 = 0
		//angular time is 0/30 = 0
		assertEquals(0.0,time,0.0001);
		
		//test for total length of path
		assertTrue(same.size() == 2);
	}
	
	//test case for length of complex path
	@Test
	public void testComplex(){
		//define a complex path
		PathT pth = new PathT();
		
		//define five more points to make it complex
		PointT pt4 = null;
		PointT pt5 = null;
		PointT pt6 = null;
		PointT pt7 = null;
		PointT pt8 = null;
		try {
			pt4 = new PointT(3,8);
			pt5 = new PointT(0,4);
			pt6 = new PointT(0,2);
			pt7 = new PointT(7,2);
			pt8 = new PointT(9,2);
		} catch (InvalidPointException e1) {
			System.out.println(e1.error());
		}
		
		//add eight points to the path
		try {
			//add point: (0,0)
			pth.add(0, pt);
			//add point: (4,0)
			pth.add(1, pt2);
			//add point: (4,8)
			pth.add(2, pt3);
			//add point: (3,8)
			pth.add(3, pt4);
			//add point: (0,4)
			pth.add(4, pt5);
			//add point: (0,2)
			pth.add(5, pt6);
			//add point: (7,2)
			pth.add(6, pt7);
			//add point: (9,2)
			pth.add(7, pt8);
		} catch (FullSequenceException e) {
			System.out.println(e.error());
		} catch (InvalidPositionException e) {
			System.out.println(e.error());
		}

		//test totalDistance
		double result = PathCalculation.totalDistance(pth);
		//straight line distance = 4+8+1+2+9 = 24
		//oblique lines distance = 5
		assertEquals(result,29,0.0001);
		
		//test totalTurns
		double turns = PathCalculation.totalTurns(pth);
		//pt->pt2, pt2->pt3, pt3->pt4, pt4->pt5, pt6->pt7
		//total 5 turns
		assertTrue(turns == 5);
		
		//test estimatedTime
		double time = PathCalculation.estimatedTime(pth);
		//linear time is 29/15 = 1.9333
		//angular time is 8.1378/30 = 0.2712
		assertEquals(2.20456,time,0.0001);
	}

}
