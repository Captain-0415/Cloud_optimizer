import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardComponent } from './modules/dashboard/dashboard.component';
import { DefaultComponent } from './layout/default/default.component';
import { AwsInstancesComponent } from './modules/aws-resources/aws-instances/aws-instances.component';


const routes: Routes = [
{path : '', component : DefaultComponent,
children:[
{path:'dashboard',component: DashboardComponent},
{path:'aws-resources/instances',component: AwsInstancesComponent},
]},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
