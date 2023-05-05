import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AwsS3ObjectsComponent } from './aws-s3-objects.component';

describe('AwsS3ObjectsComponent', () => {
  let component: AwsS3ObjectsComponent;
  let fixture: ComponentFixture<AwsS3ObjectsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AwsS3ObjectsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AwsS3ObjectsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
