package src;

import java.lang.Math;

/**
 * This module calculates the attributes of a path
 * 
 * @author Mingnan
 *
 */
public class PathCalculation {
	
	/**
	 * calculates the total distance of the given path
	 * 
	 * @param p the path need to be calculated
	 * @return the distance of given path
	 */
	public static double totalDistance(PathT p){
		//define a variable to store the result
		double sum = 0;
		PointT pt1 = null;
		PointT pt2 = null;
		
		for (int i = 0; i < p.size()-1; i++) {
			try {
				
				//get the value of two points
				pt1 = p.getval(i);
				pt2 = p.getval(i+1);
				
			} catch (InvalidPositionException e) {
				System.out.println(e.error());
			}
			
			//add the distance into sum
			sum = sum + pt1.dist(pt2);
			
		}
		
		return sum;
	}
	
	/**
	 * calculates the total number of turns 
	 * in the given path
	 * 
	 * @param p the path need to calculated
	 * @return the number of turns existed in path
	 */
	public static double totalTurns(PathT p){
		//define a variable to store the result
		double sum = 0;
		PointT a = null;
		PointT b = null;
		PointT c = null;
		
		for (int i = 0; i < p.size()-2; i++) {
			try {
				
				//get the value of three points
				a = p.getval(i);
				b = p.getval(i+1);
				c = p.getval(i+2);
				
			} catch (InvalidPositionException e) {
				System.out.println(e.error());
			}
			
			double angl = angle(a,b,c);
			if (angl != 0){
				sum++;
			}
		}
		return sum;
	}
	
	/**
	 * calculate the time need for traversing the path
	 * 
	 * @param p the path need to be calculated
	 * @return the estimated time for traversing given path
	 */
	public static double estimatedTime(PathT p){
		//create a variable to store the result 
		double result = 0;
		double dist = 0;
		double angl = 0;
		
		//calculate linear time
		for (int i = 0; i < p.size()-1; i++) {
			try {
				//calculate the distance between adjacent points
				dist = p.getval(i).dist(p.getval(i+1));
			} catch (InvalidPositionException e) {
				System.out.println(e.error());
			}
			//divide the distance by velocity
			dist = dist / Constants.VELOCITY_LINEAR;
			result = result + dist;
		}
		
		//calculate the angular time
		for (int i = 0; i < p.size()-2; i++) {
			try {
				//calculate the angle between two vectors
				angl = angle(p.getval(i),p.getval(i+1),p.getval(i+2));
			} catch (InvalidPositionException e) {
				System.out.println(e.error());
			}
			//divide the angle by velocity
			angl = angl / Constants.VELOCITY_ANGULAR;
			result = result + angl;
		}
		return result;
	}
	
	/**
	 * Calculates the angle between two vectors
	 * two vectors could get from two of the three points
	 * 
	 * @param p1 the first point to determine first vector
	 * @param p2 the second point to determine first, second vector
	 * @param p3 the third point to determine second vector
	 * @return the angle in radiance between two vectors
	 */
	public static double angle(PointT p1,PointT p2, PointT p3){
		//initialize two point variable 
		PointT u = null;
		PointT v = null;
		
		//find the dot product of u and v
		double ux = p2.xcrd()-p1.xcrd();
		double uy = p2.ycrd()-p1.ycrd();
		double vx = p3.xcrd()-p2.xcrd();
		double vy = p3.ycrd()-p2.ycrd();
		double dot = ux*vx - uy*vy;
		
		//find ||u|| and ||v||
		double udist = p1.dist(p2);
		double vdist = p2.dist(p3);
		
		//combine all the components
		double overall = dot / (udist*vdist);
		
		return Math.acos(overall);
	}

}
