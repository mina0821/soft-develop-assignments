package src;

public class InvalidPositionException extends Throwable{
	private String msg;
	
	public InvalidPositionException(String msg){
		this.msg = msg;
	}
	
	public String error(){
		return this.msg;
	}

}

