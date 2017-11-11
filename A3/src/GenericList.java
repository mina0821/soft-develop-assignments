package src;

import java.util.ArrayList;

/**
 * This class creates a list with random
 * type T.
 * 
 * @author Mingnan Su
 *
 * @param <T>
 */
public class GenericList<T> {
	protected ArrayList<T> s;
	public final static int MAX_SIZE = 100;
	
	/**
	 * Constructor for GenericList
	 */
	public GenericList(){
		s = new ArrayList<T>();
	}
	
	/**
	 * adding a element at given index
	 * (shift the elements after the index
	 * to to right by one. Sub the element
	 * in the list)
	 * 
	 * @param i the position of the element
	 * @param p the element itself
	 * @throws FullSequenceException when list is full
	 * @throws InvalidPositionException when index is not valid
	 */
	public void add(int i, T p) throws FullSequenceException, InvalidPositionException{
		//check for exceptions
		if (this.size() == MAX_SIZE){
			throw new FullSequenceException("List is full");
		}
		
		if (i<0 | i>this.size()){
			throw new InvalidPositionException("Index does not exist");
		}
		
		s.add(i, p);
	}
	
	/**
	 * delete a element from the list
	 * (shift the elements after the index 
	 * to the left by one)
	 * 
	 * @param i the position of the element want to delete
	 * @throws InvalidPositionException when index is not valid
	 */
	public void del(int i) throws InvalidPositionException{
		//check for exceptions
		if (i<0 | i>=this.size()){
			throw new InvalidPositionException("Index does not exist");
		}
		
		s.remove(i);
		
	}
	
	/**
	 * set the value of element with given index
	 * 
	 * @param i the index to replace value
	 * @param p the element to add
	 * @throws InvalidPositionException when index is not valid
	 */
	public void setVal(int i, T p) throws InvalidPositionException{
		//check for exceptions
		if (i<0 | i>=this.size()){
			throw new InvalidPositionException("Index does not exist");
		}
		
		s.set(i, p);
		
	}
	
	/**
	 * get the value of a given position
	 * 
	 * @param i the index of the element
	 * @return the value of the element
	 * @throws InvalidPositionException when index is not valid
	 */
	public T getval(int i) throws InvalidPositionException{
		//check for exceptions
		if (i<0 | i>=this.size()){
			throw new InvalidPositionException("Index does not exist");
		}
		
		return s.get(i);
	}
	
	/**
	 * determine the size of the list
	 * 
	 * @return the length of the list
	 */
	public int size(){
		return s.size();
	}

}
