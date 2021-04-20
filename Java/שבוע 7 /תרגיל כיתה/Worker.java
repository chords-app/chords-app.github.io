package zoom11042021;

public class Worker {
	private int code;
	private String name;
	private int hours;
	public int getCode() {
		return code;
	}
	public void setCode(int code) {
		if(code>0)
			this.code = code;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public int getHours() {
		return hours;
	}
	public void setHours(int hours) {
		if(hours>0)
			this.hours = hours;
	}
	public Worker(){}
	public Worker(int code, String name, int hours){
		this.setCode(code); // this.code = code;
		this.setName(name); //this.name=name;
		this.setHours(hours);//this.hours=hours
	}
	public void prtWorker(){
		System.out.println("The code is:" + code);
		System.out.println("The Name is:" + name);
		System.out.println("The hours is:" + hours);
	}
}
