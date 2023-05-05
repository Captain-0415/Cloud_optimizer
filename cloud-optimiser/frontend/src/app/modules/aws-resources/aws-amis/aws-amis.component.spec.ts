import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AwsAmisComponent } from './aws-amis.component';

describe('AwsAmisComponent', () => {
  let component: AwsAmisComponent;
  let fixture: ComponentFixture<AwsAmisComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AwsAmisComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AwsAmisComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
