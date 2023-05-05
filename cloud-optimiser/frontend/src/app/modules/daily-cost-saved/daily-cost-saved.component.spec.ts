import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DailyCostSavedComponent } from './daily-cost-saved.component';

describe('DailyCostSavedComponent', () => {
  let component: DailyCostSavedComponent;
  let fixture: ComponentFixture<DailyCostSavedComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DailyCostSavedComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DailyCostSavedComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
