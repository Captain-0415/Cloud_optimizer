import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AwsResourcesComponent } from './aws-resources.component';

describe('AwsResourcesComponent', () => {
  let component: AwsResourcesComponent;
  let fixture: ComponentFixture<AwsResourcesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AwsResourcesComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AwsResourcesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
