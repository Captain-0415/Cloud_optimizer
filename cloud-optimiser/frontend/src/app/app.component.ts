import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'cloud-optimiser';
  sideBarOpen=true;
  
  sideBarToggler(event: any){
  this.sideBarOpen=!this.sideBarOpen;
}
}
