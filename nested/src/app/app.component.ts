import { Component, ViewChild } from '@angular/core';
import { CoursesListComponent } from './courses-list/courses-list.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  title = 'nested';
  @ViewChild (CoursesListComponent) coursesList?: CoursesListComponent;

 studentsFlag: boolean = false;
 coursesFlag: boolean = false;
 homeFlag: boolean = true;

 showHome() {
  this.coursesFlag = false;
  this.studentsFlag = false;
  this.homeFlag = true;
 }
 showStudents() {
    this.coursesFlag = false;
    this.studentsFlag = true;
    this.homeFlag = false;
    }

  showCourses() {
      this.coursesFlag = true
      this.studentsFlag = false
      this.homeFlag = false;
      }
  }



