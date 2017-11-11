package src;

import java.lang.Math;

public class PointT {
	private double xc;
	private double yc;
	
	public PointT(double x, double y) throws InvalidPointException{
		if ((0 <= x & x <= Constants.MAX_X) == false){
			throw new InvalidPointException("Invalid point");
		}else if((0 <= y & y <= Constants.MAX_Y) == false){
			throw new InvalidPointException("Invalid point");
		}
		this.xc = x;
		this.yc = y;
	}
	
	public double xcrd(){
		return this.xc;
	}
	
	public double ycrd(){
		return this.yc;
	}
	
	public double dist(PointT p){
		double xpart = this.xc - p.xcrd();
		double ypart = this.yc - p.ycrd();
		return Math.sqrt((xpart * xpart) + (ypart * ypart));
	}

}
