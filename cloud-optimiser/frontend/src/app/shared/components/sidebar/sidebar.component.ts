import { Component,OnInit } from '@angular/core';
//import { MatDrawer } from '@angular/material/sidenav';

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.scss']
})
export class SidebarComponent implements OnInit {
	panelOpenState = false;
	
	constructor(){ }
	
	ngOnInit(): void {
	}

}
