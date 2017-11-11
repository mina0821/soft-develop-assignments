package src;

public class SafeZone extends GenericList<RegionT>{
	private final static int MAX_SIZE = 1;
	
	public void add(int i, RegionT p) throws FullSequenceException, InvalidPositionException{
		//check for exceptions
		if (this.size() == MAX_SIZE){
			throw new FullSequenceException("List is full");
		}
		
		if (i<0 | i>this.size()){
			throw new InvalidPositionException("Index does not exist");
		}
		
		s.add(i, p);
	}

}
