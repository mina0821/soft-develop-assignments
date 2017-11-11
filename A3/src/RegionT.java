package src;

/**
 * This class defines an ADT for a region
 * 
 * @author Mingnan
 *
 */
public class RegionT {
	
	// state variables
	private PointT lower_left;
	private double width;
	private double height;
	
	/**
	 * Constructor for RegionT
	 * 
	 * @param pt lower left point of the region
	 * @param w the width of the rectangle
	 * @param h the height of the rectangle
	 */
	public RegionT(PointT pt, double w, double h) throws InvalidRegionException{
		//check for exceptions
		if (w <= 0 | h <= 0){
			throw new InvalidRegionException("Invalid region width and height");
		}else if ((pt.xcrd() + w) >= Constants.MAX_X){
			throw new InvalidRegionException("Invalid region in x-axis");
		}else if ((pt.ycrd() + h) >= Constants.MAX_Y){
			throw new InvalidRegionException("Invalid region in y-axis");
		}
		
		this.lower_left = pt;
		this.width = w;
		this.height = h;
	}
	
	/**
	 * Determine if a point is in region objects
	 * 
	 * @param p the point to test if is in the region (+tolerance)
	 * @return true if the point sit within the tolerance of the region
	 */
	public boolean pointInRegion(PointT p){
		//  1  2  3 
		//  4  5  6
		//  7  8  9
 		// Divide the region (+tolerance) into 9 parts
		// 1,3,7,9 is a quarter of a circle
		// 2,4,5,6,8 is a rectangle
		
		//rectangle data
		double x = this.lower_left.xcrd();
		double y = this.lower_left.ycrd();
		double w = this.width;
		double h = this.height;
		//input point data
		double px = p.xcrd();
		double py = p.ycrd();
		//tolerance
		double tol = Constants.TOLERANCE;
		//four vertex of the rectangle
		PointT top_left = null;
		PointT top_right = null;
		PointT lower_right = null;
		try {
			//top-left point of the rectangle
			top_left = new PointT(x,y+h);
			//top-right point of the rectangle
			top_right = new PointT(x+w,y+h);
			//lower-right point of the rectangle
			lower_right = new PointT(x+w,y);
		} catch (InvalidPointException e) {
			System.out.println(e.error());
			return false;
		}
		
		//check if the point is in 2,5,8
		if (px>=x & px<=x+w & py>=y-tol & py<=y+h+tol){
			return true;
		}
		//check if the point is in 4,5,6
		else if(px>=x-tol & px<=x+w+tol & py>=y & py<=y+h){
			return true;
		}
		//check if the point is in 1
		else if(p.dist(top_left)<=tol){
			return true;
		}
		//check if the point is in 3
		else if(p.dist(top_right)<=tol){
			return true;
		}
		//check if the point is in 7
		else if(p.dist(this.lower_left)<=tol){
			return true;
		}
		//check if the point is in 9
		else if(p.dist(lower_right)<=tol){
			return true;
		}
		return false;
	}

}
