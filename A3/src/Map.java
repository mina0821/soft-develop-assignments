package src;

public class Map {
	private Obstacles obstacles;
	private Destinations destinations;
	private SafeZone safeZone;
	
	public Map (Obstacles o,Destinations d, SafeZone s){
		this.obstacles = o;
		this.destinations = d;
		this.safeZone = s;
	}
	
	public Obstacles get_Obstacles(){
		return this.obstacles;
	}
	
	public Destinations get_destinations(){
		return this.destinations;
	}
	
	public SafeZone get_safeZone(){
		return this.safeZone;
	}

}
