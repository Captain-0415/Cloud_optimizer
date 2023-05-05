import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FooterComponent } from './components/footer/footer.component';
import { HeaderComponent } from './components/header/header.component';
import { SidebarComponent } from './components/sidebar/sidebar.component';
import { MatDividerModule } from '@angular/material/divider';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button'; 
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
import { FlexLayoutModule } from '@angular/flex-layout';
import { RouterModule } from '@angular/router';


@NgModule({
  declarations: [
    FooterComponent,
    HeaderComponent,
    SidebarComponent
  ],
  imports: [
	CommonModule,
	MatDividerModule,
	MatToolbarModule,
	MatIconModule,
	MatButtonModule,
	FlexLayoutModule,
	MatMenuModule,
	MatListModule,
	RouterModule,
	MatFormFieldModule,
	MatExpansionModule,
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
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
  exports: [
	HeaderComponent,
	SidebarComponent,
	FooterComponent
  ]
})
export class SharedModule { }
