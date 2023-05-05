import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AwsVolumesComponent } from './aws-volumes.component';

describe('AwsVolumesComponent', () => {
  let component: AwsVolumesComponent;
  let fixture: ComponentFixture<AwsVolumesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AwsVolumesComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AwsVolumesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
