import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { SharedModule } from '../../shared/shared.module';
import { DefaultComponent } from './default.component';
import { AwsAnalysisRecommendationComponent } from 'src/app/modules/aws-analysis-recommendation/aws-analysis-recommendation.component';
import { DashboardComponent } from '../../modules/dashboard/dashboard.component';
import { AwsResourcesComponent } from 'src/app/modules/aws-resources/aws-resources.component';
import { AwsAmisComponent } from 'src/app/modules/aws-resources/aws-amis/aws-amis.component';
import { AwsClustersComponent } from 'src/app/modules/aws-resources/aws-clusters/aws-clusters.component';
import { AwsEipsComponent } from 'src/app/modules/aws-resources/aws-eips/aws-eips.component';
import { AwsEnisComponent } from 'src/app/modules/aws-resources/aws-enis/aws-enis.component';
import { AwsInstancesComponent } from 'src/app/modules/aws-resources/aws-instances/aws-instances.component';
import { AwsS3ObjectsComponent } from 'src/app/modules/aws-resources/aws-s3-objects/aws-s3-objects.component';
import { AwsSnapshotsComponent } from 'src/app/modules/aws-resources/aws-snapshots/aws-snapshots.component';
import { AwsUserReportsComponent } from 'src/app/modules/aws-resources/aws-user-reports/aws-user-reports.component';
import { AwsVolumesComponent } from 'src/app/modules/aws-resources/aws-volumes/aws-volumes.component';
import { DailyCostSavedComponent } from 'src/app/modules/daily-cost-saved/daily-cost-saved.component';
import { MatDividerModule } from '@angular/material/divider';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button'; 
import { FlexLayoutModule } from '@angular/flex-layout';
import { MatMenuModule } from '@angular/material/menu';
import { MatListModule } from '@angular/material/list';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatExpansionModule } from '@angular/material/expansion';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatCardModule } from '@angular/material/card';
import { MatInputModule } from '@angular/material/input';
import { MatTableModule } from '@angular/material/table';
import { MatTabsModule } from '@angular/material/tabs';
import { MatPaginatorModule } from '@angular/material/paginator';
import { MatSortModule } from '@angular/material/sort';
import { MatSelectModule } from '@angular/material/select';
import { MatSnackBarModule } from '@angular/material/snack-bar';
import { MatOptionModule } from '@angular/material/core';
import { MatCheckboxModule } from '@angular/material/checkbox';
import { MatProgressBarModule } from '@angular/material/progress-bar';

@NgModule({
  declarations: [
    DashboardComponent,
    DefaultComponent,
    AwsAnalysisRecommendationComponent,
    AwsResourcesComponent,
    AwsResourcesComponent,
    AwsAmisComponent,
    AwsClustersComponent,
    AwsEipsComponent,
    AwsEnisComponent,
    AwsInstancesComponent,
    AwsS3ObjectsComponent,
    AwsSnapshotsComponent,
    AwsUserReportsComponent,
    AwsVolumesComponent,
    DailyCostSavedComponent
    ],
  imports: [
    RouterModule,
    SharedModule,
    CommonModule,
    MatDividerModule,
    MatToolbarModule,
    MatIconModule,
    MatButtonModule,
    FlexLayoutModule,
    MatMenuModule,
    MatListModule,
    MatFormFieldModule,
    MatExpansionModule,
    MatSidenavModule,
    MatCardModule,
    MatInputModule,
    MatTableModule,
    MatTabsModule,
    MatPaginatorModule,
    MatSortModule,
    MatSelectModule,
    MatSnackBarModule,
    MatOptionModule,
    MatCheckboxModule,
    MatProgressBarModule
    ],
  exports: [
    MatSortModule
  ]
})
export class DefaultModule { }
