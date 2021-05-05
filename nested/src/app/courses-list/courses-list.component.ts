import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-courses-list',
  templateUrl: './courses-list.component.html',
  styleUrls: ['./courses-list.component.css']
})
export class CoursesListComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }
  coursesList: any = [
    {number:292100, name:'Angular'},
    {number:292101, name:'Python'}, 
    {number:292102, name:'Java'},
    {number:292103, name:'MongoDB'}
  ]

  selectedCourse: String = ' ';
  showStudentComponent: boolean = false;
  showAngular ()
  {
this.selectedCourse = 'Angular'
this.showStudentComponent = true
  }

  showPython ()
  {
this.selectedCourse = 'Python'
this.showStudentComponent = true
  }
  showJava ()
  {
this.selectedCourse = 'Java'
this.showStudentComponent = true
  }
  showMongo ()
  {
this.selectedCourse = 'MongoDB'
this.showStudentComponent = true
  }
}

