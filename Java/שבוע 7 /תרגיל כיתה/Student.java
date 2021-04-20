package zoom11042021;

public class Student {
	private int code;
	private String name;
	private Course[] courses;
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
	public Course[] getCourses() {
		return courses;
	}
	public void setCourses(Course[] courses) {
		this.courses = courses;
	}
	public Student(){}
	public Student(int code, String name, Course[] courses){
		this.setCode(code);
		this.name=name;
		this.courses=courses;
	}
	public void prtStudent(){
		System.out.println("The Student code is:" + code);
		System.out.println("The Student Name is:" + name);
		int i;
		System.out.println("The student's courses are:");
		for(i=0;i<this.courses.length;i++)
			courses[i].prtCourse();
	}
	public double getAverage(){
		int i;
		double avg=0;
		for(i=0;i<this.courses.length;i++){
			avg += courses[i].getGrade();
		}
		avg = (double)avg/this.courses.length;
		return avg;
	}
}
