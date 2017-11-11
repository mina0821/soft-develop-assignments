package src;

public class InvalidRegionException extends Throwable{
	private String msg;
	
	public InvalidRegionException(String msg){
		this.msg = msg;
	}
	
	public String error(){
		return this.msg;
	}

}

