import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AwsEnisComponent } from './aws-enis.component';

describe('AwsEnisComponent', () => {
  let component: AwsEnisComponent;
  let fixture: ComponentFixture<AwsEnisComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AwsEnisComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AwsEnisComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
