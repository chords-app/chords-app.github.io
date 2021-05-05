import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CheckGLobalComponent } from './check-global.component';

describe('CheckGLobalComponent', () => {
  let component: CheckGLobalComponent;
  let fixture: ComponentFixture<CheckGLobalComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CheckGLobalComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CheckGLobalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
