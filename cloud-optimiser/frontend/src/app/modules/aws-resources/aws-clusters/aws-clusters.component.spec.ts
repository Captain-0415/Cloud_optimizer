import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AwsClustersComponent } from './aws-clusters.component';

describe('AwsClustersComponent', () => {
  let component: AwsClustersComponent;
  let fixture: ComponentFixture<AwsClustersComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AwsClustersComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AwsClustersComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
