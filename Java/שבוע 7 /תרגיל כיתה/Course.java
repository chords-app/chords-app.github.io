package zoom11042021;

public class Course {
	private int code;
	private String name;
	private double grade;
	private Worker lect;
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
	public double getGrade() {
		return grade;
	}
	public void setGrade(double grade) {
		if(grade>=0&&grade<=100)
			this.grade = grade;
	}
	public Worker getLect() {
		return lect;
	}
	public void setLect(Worker lect) {
		/*
		 * Worker w = new Worker(123,"Shadi",17);
		 * Course c=new Course();
		 * c.setLect(w);
		 */
		this.lect = lect;
	}
	public void setLect(int code, String name, int hours) {
		/*
		 * Course c=new Course();
		 * c.setLect(123,"shadi",17);
		 */
		this.lect = new Worker(code,name,hours);
	}
	public Course(){}
	public Course(int code, String name, Worker lect, double grade){
		this.setCode(code);
		this.name=name;
		this.lect=lect;
		this.setGrade(grade);
	}
	public void prtCourse(){
		System.out.println("The Course code is:" + code);
		System.out.println("The Course Name is:" + name);
		System.out.println("The Course Grade is:" + grade);
		this.lect.prtWorker();
	}
	
}
