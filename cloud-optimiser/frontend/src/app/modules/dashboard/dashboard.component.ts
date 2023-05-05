import { Component,OnInit,ViewChild } from '@angular/core';
//import { DeletedResourcesService } from '
import { MatTableDataSource } from '@angular/material/table';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit{

//@ViewChild('instancesViolSort') instancesViolSort: MatSort;
//@ViewChild('unusedInstancesSort') unusedInstancesSort: MatSort;
//@ViewChild('vmsViolSort') vmsViolSort: MatSort;
//@ViewChild('unusedVmsSort') unusedVmsSort: MatSort;

//@ViewChild('instancesViolPaginator') instancesViolPaginator: MatPaginator;
//@ViewChild('unusedInstancesPaginator') unusedInstancesPaginator: MatPaginator;
//@ViewChild('vmsViolPaginator') vmsViolPaginator: MatPaginator;
//@ViewChild('unusedVmsPaginator') unusedVmsPaginator: MatPaginator;

constructor() {}
ngOnInit(): void{
}
}
