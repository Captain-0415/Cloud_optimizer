import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AwsEipsComponent } from './aws-eips.component';

describe('AwsEipsComponent', () => {
  let component: AwsEipsComponent;
  let fixture: ComponentFixture<AwsEipsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AwsEipsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AwsEipsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
