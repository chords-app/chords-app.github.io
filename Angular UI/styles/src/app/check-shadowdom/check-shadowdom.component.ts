import { Component, OnInit, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'app-check-shadowdom',
  template: '<p>Using Emulator </p>',
  styles:['p{color:red}']

})
export class CheckShadowdomComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

}
