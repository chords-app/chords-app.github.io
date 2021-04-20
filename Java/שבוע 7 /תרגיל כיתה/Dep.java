package zoom11042021;

public class Dep {
	private int code;
	private String name;
	private Worker man;
	
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
	public Worker getMan() {
		return man;
	}
	public void setMan(Worker man) {
		this.man = man;
	}
	public Dep(){}
	public Dep(int code, String name, Worker man){
		this.setCode(code);
		this.name=name;
		this.man=man;
	}
	public void prtDep(){
		System.out.println("The Dep code is:" + code);
		System.out.println("The Dep Name is:" + name);
		this.man.prtWorker();
		/*System.out.println("The man code is:" man.getCode());
		 * System.out.println("The man Name is:" man.getName());
		 * System.out.println("The man hours is:" man.getHours());
		 */
	}

}
