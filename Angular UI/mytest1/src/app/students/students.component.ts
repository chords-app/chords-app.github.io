import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-students',
  templateUrl: './students.component.html',
  styleUrls: ['./students.component.css']
})
export class StudentsComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }


  studentsList: any = [
    {Id:1, Name:'Idan Guy',Course:'Angular 2'},
    {Id:2, Name:'Sharon Tal', Course:'Angular 1'}, 
    {Id:3, Name:'Yuval Shir', Course:'Python'},
    {Id:4, Name:'Adam Gil', Course:'Angular 2'}, 
    {Id:5, Name:'Veronika Bruy', Course:'Angular 1'},
    {Id:6, Name:'Ori Dobosh', Course:'Angular 1'} 
  ]
}
