import { ComponentFixture, TestBed,async } from '@angular/core/testing';

import { AwsInstancesComponent } from './aws-instances.component';

describe('AwsInstancesComponent', () => {
  let component: AwsInstancesComponent;
  let fixture: ComponentFixture<AwsInstancesComponent>;

  beforeEach(async (() => {
    TestBed.configureTestingModule({
      declarations: [ AwsInstancesComponent ]
    })
    .compileComponents();

  beforeEach(()=>{
    fixture = TestBed.createComponent(AwsInstancesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
