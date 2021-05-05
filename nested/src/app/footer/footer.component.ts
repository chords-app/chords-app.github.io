import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.css']
})
export class FooterComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }
  
collegeName: String = 'Ort Braude College'
address: String = 'Karmiel, Snunit 51'
tel: String = '04-9901973'

}

