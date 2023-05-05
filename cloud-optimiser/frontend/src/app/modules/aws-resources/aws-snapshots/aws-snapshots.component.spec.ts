import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AwsSnapshotsComponent } from './aws-snapshots.component';

describe('AwsSnapshotsComponent', () => {
  let component: AwsSnapshotsComponent;
  let fixture: ComponentFixture<AwsSnapshotsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AwsSnapshotsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AwsSnapshotsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
