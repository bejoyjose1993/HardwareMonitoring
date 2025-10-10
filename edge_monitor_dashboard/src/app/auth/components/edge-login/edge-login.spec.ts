import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EdgeLogin } from './edge-login';

describe('EdgeLogin', () => {
  let component: EdgeLogin;
  let fixture: ComponentFixture<EdgeLogin>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [EdgeLogin]
    })
    .compileComponents();

    fixture = TestBed.createComponent(EdgeLogin);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
