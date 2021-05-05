import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { CheckGLobalComponent } from './check-global/check-global.component';
import { CheckShadowdomComponent } from './check-shadowdom/check-shadowdom.component';

@NgModule({
  declarations: [
    AppComponent,
    CheckGLobalComponent,
    CheckShadowdomComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
