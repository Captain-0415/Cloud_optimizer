import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AwsUserReportsComponent } from './aws-user-reports.component';

describe('AwsUserReportsComponent', () => {
  let component: AwsUserReportsComponent;
  let fixture: ComponentFixture<AwsUserReportsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AwsUserReportsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AwsUserReportsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
