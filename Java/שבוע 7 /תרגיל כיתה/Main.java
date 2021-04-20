package zoom11042021;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Worker man = new Worker(111,"ABC",25);
		Dep ourDep = new Dep(234,"Software",man);
		Course[] ourCourses = new Course[5];
		Course[] ourCourses2 = new Course[5];
		Student s1,s2;
		/******************************/
		Worker lect1 = new Worker(222,"aaa",30);
		Worker lect2 = new Worker(333,"bbb",30);
		Worker lect3 = new Worker(444,"ccc",30);
		Worker lect4 = new Worker(555,"ddd",30);
		Worker lect5 = new Worker(666,"eee",30);
		ourCourses[0] = new Course(123,"Math",lect1,85);
		ourCourses[1] = new Course(234,"C",lect1,70);
		ourCourses[2] = new Course(345,"Java",lect1,60);
		ourCourses[3] = new Course(456,"Eng",lect1,48);
		ourCourses[4] = new Course(567,"SQL",lect1,89);
		
		ourDep.prtDep();
		System.out.println("**********************************");
		s1 = new Student(78945,"ttt",ourCourses);
		
		s1.prtStudent();
		System.out.println("**********************************");
		System.out.println("The average for " + s1.getName() + " is:" + s1.getAverage());
		System.out.println("**********************************");
		System.out.println();
		/********************************/
		ourCourses2[0] = new Course(123,"Math",lect1,55);
		ourCourses2[1] = new Course(234,"C",lect1,44);
		ourCourses2[2] = new Course(345,"Java",lect1,88);
		ourCourses2[3] = new Course(456,"Eng",lect1,17);
		ourCourses2[4] = new Course(567,"SQL",lect1,22);
		s2 = new Student(454545,"www",ourCourses2);
		s2.prtStudent();
		System.out.println("**********************************");
		System.out.println("The average for " + s2.getName() + " is:" + s2.getAverage());

	}

}
