package src;

public class InvalidPointException extends Throwable{
	private String msg;
	
	public InvalidPointException(String msg){
		this.msg = msg;
	}
	
	public String error(){
		return this.msg;
	}

}
