import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-students-table',
  templateUrl: './students-table.component.html',
  styleUrls: ['./students-table.component.css']
})
export class StudentsTableComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
    console.log (this.selectedCourse)
  }
@Input() selectedCourse: String

studentsList: any = [
  {id:1, name:'Idan Guy', Course:'Angular'},
  {id:2, name:'Sharon Tal', Course:'Angular'},
  {id:3, name:'Yuval Shir', Course:'Python'},
  {id:4, name:'Adam Gil', Course:'Java'},
  {id:5, name:'Amir Ravve', Course:'Python'},
  {id:6, name:'Ravit Levy', Course:'MongoDB'},
  {id:7, name:'Liav Cohen', Course:'Java'},
  {id:8, name:'Yossi Ben', Course:'Angular'}
]}

