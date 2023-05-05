import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AwsAnalysisRecommendationComponent } from './aws-analysis-recommendation.component';

describe('AwsAnalysisRecommendationComponent', () => {
  let component: AwsAnalysisRecommendationComponent;
  let fixture: ComponentFixture<AwsAnalysisRecommendationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AwsAnalysisRecommendationComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AwsAnalysisRecommendationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
