import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-courses',
  templateUrl: './courses.component.html',
  styleUrls: ['./courses.component.css']
})
export class CoursesComponent implements OnInit {
  constructor() { }

  ngOnInit(): void {
  }

 coursesInSemester: Number = 8;
 message: String = "Courses Information"
 isPythonActive: boolean = true;
 totalCourses: Number = 8;



  coursesList: any = [
    {number:1, name:'Java 1', semester:'A'},
    {number:2, name:'Java 2', semester:'B'}, 
    {number:3, name:'Python', semester:'A'},
    {number:4, name:'Angular 1', semester:'B'}, 
    {number:5, name:'Angular 2', semester:'A'}, 
    {number:6, name:'React', semester:'B'}, 
    {number:7, name:'MongoDB', semester:'B'},
    {number:8, name:'SQL', semester:'A'},  
  ]
getCoursesInSemester (){
this.coursesInSemester
}  

showMessage () {
console.log (this.message)
}

printCourses () {
var i;
for (i = 0; i < 9; i++) { 
console.log (this.coursesList [i])
}
}

checkPython () {
return this.isPythonActive; 
}

checkCourses () {
if (this.totalCourses > 3)
console.log (true)
else
console.log (false)

}
}


