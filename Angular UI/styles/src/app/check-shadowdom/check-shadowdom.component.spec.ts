import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CheckShadowdomComponent } from './check-shadowdom.component';

describe('CheckShadowdomComponent', () => {
  let component: CheckShadowdomComponent;
  let fixture: ComponentFixture<CheckShadowdomComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CheckShadowdomComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CheckShadowdomComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
