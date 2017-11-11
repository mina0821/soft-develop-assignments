package src;

public class FullSequenceException extends Throwable{
	private String msg;
	
	public FullSequenceException(String msg){
		this.msg = msg;
	}
	
	public String error(){
		return this.msg;
	}

}

